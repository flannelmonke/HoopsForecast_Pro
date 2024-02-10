import re
import pandas as pd
import urllib.request

links = open('links.txt', 'r')
links = links.readlines()


for link in links[100:200]:
    url = link.strip()

    fp = urllib.request.urlopen(url)
    mybytes = fp.read()

    webpage = mybytes.decode("utf8")
    fp.close()

    tables =  re.findall(r'(<div class=\"table__inner\">[\s\S]*?<\/table>)', webpage)

    team_1 = tables[0]
    team_2 = tables[1]

    team_headers = re.findall(r'(<th class=\".*\">.*<\/th>)', team_1)
    team_headers = [re.sub(r'(<th class=\".*\">|<\/th>)', '', header) for header in team_headers]

    # GET DATA FROM TEAM 1 TABLE
    team_1_data_raw = re.findall(r'(<td class=\".*\">[\s\S]*?<\/td>)', team_1)
    team_1_data_raw = [re.sub(r'(<td class=\".*\">|<\/td>|<a [\s\S]*?>\n|\n|<\/a>|<div [\s\S]*?>[\s\S]*?>[\s\S]*?<\/div>)','', data) for data in team_1_data_raw]

    # GET DATA FROM TEAM 2 TABLE
    team_2_data_raw = re.findall(r'(<td class=\".*\">[\s\S]*?<\/td>)', team_2)
    team_2_data_raw = [re.sub(r'(<td class=\".*\">|<\/td>|<a [\s\S]*?>\n|\n|<\/a>|<div [\s\S]*?>[\s\S]*?>[\s\S]*?<\/div>)','', data) for data in team_2_data_raw]

    print("Team 1 Data: ", len(team_1_data_raw))
    print("Team 2 Data: ", len(team_2_data_raw))
    # CREATE OBJECT TO INSERT INTO DATAFRAME
    team_1_data = {team_headers[i]: [] for i in range(len(team_headers))}
    team_2_data = {team_headers[i]: [] for i in range(len(team_headers))}

    # ITERATE THROUGH TEAM 1 DATA AND INSERT INTO OBJECT
    row_iterator = 0
    for i in range(len(team_1_data_raw)):
        if row_iterator == len(team_headers):
            row_iterator = 0
            team_1_data[team_headers[row_iterator]].append(team_1_data_raw[i])
            row_iterator += 1
        else:
            team_1_data[team_headers[row_iterator]].append(team_1_data_raw[i])
            row_iterator += 1

    # Iterate through team 2 data and insert into object
    row_iterator = 0
    for i in range(len(team_2_data_raw)):
        if row_iterator == len(team_headers):
            row_iterator = 0
            team_2_data[team_headers[row_iterator]].append(team_2_data_raw[i])
            row_iterator += 1
        else:
            team_2_data[team_headers[row_iterator]].append(team_2_data_raw[i])
            row_iterator += 1
    
    # Remove whitespace from player names
    team_1_data['PLAYER'] = [re.sub(r'(\s)', '', player) for player in team_1_data['PLAYER']]
    team_2_data['PLAYER'] = [re.sub(r'(\s)', '', player) for player in team_2_data['PLAYER']]        

    # Take every other element of the three duplicate columns
    # Pts
    team_1_data['Pts'] = team_1_data['Pts'][0:len(team_1_data['Pts']):2]
    team_2_data['Pts'] = team_2_data['Pts'][0:len(team_2_data['Pts']):2]
    # Reb
    team_1_data['Reb'] = team_1_data['Reb'][0:len(team_1_data['Reb']):2]
    team_2_data['Reb'] = team_2_data['Reb'][0:len(team_2_data['Reb']):2]
    # Ast
    team_1_data['Ast'] = team_1_data['Ast'][0:len(team_1_data['Ast']):2]
    team_2_data['Ast'] = team_2_data['Ast'][0:len(team_2_data['Ast']):2]


    # Insert into dataframe
    team_1_panda = pd.DataFrame(team_1_data)
    team_2_panda = pd.DataFrame(team_2_data)

    # Remove duplicate keys from team_1_panda and team_2_panda
    team_1_panda = team_1_panda.loc[:,~team_1_panda.columns.duplicated()]
    team_2_panda = team_2_panda.loc[:,~team_2_panda.columns.duplicated()]

    # Add team name to each player
    team_1_panda['Team'] = team_1_data['PLAYER'][len(team_1_data['PLAYER'])-1]
    team_2_panda['Team'] = team_2_data['PLAYER'][len(team_2_data['PLAYER'])-1]

    # Merge the two dataframes
    game_data = pd.concat([team_1_panda, team_2_panda], axis=0)

    # Export to csv
    file_name = url.split('/')[-1] + '.csv'
    game_data.to_csv("./datasets/"+file_name, index=False)
    print("Data frame exported to: " + file_name)