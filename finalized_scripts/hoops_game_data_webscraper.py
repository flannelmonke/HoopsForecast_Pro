import re
import pandas as pd
import urllib.request

links = open('./GIT_NO/links/game_links.txt', 'r')
links = links.readlines()


def remodel(df: pd.DataFrame):
    _2M, _2A, _3M, _3A, _1M, _1A = [], [], [], [], [], []
    for index, row in df.iterrows():
        if '2M-2A' in row and isinstance(row['2M-2A'], str):
            _2M.append(int(row['2M-2A'].split('-')[0]))
            _2A.append(int(row['2M-2A'].split('-')[1]))
        if '3M-3A' in row and isinstance(row['3M-3A'], str):
            _3M.append(int(row['3M-3A'].split('-')[0]))
            _3A.append(int(row['3M-3A'].split('-')[1]))
        if '1M-1A' in row and isinstance(row['1M-1A'], str):
            _1M.append(int(row['1M-1A'].split('-')[0]))
            _1A.append(int(row['1M-1A'].split('-')[1]))
        try:
            if 'FG%' in row:
                df.at[index, 'FG%'] = float(row['FG%'].rstrip('%'))
            else:
                df.at[index, 'FG%'] = 0
        except:
            df.at[index, 'FG%'] = 0
        try:
            if '1%' in row:
                df.at[index, '1%'] = float(row['1%'].rstrip('%'))
            else:
                df.at[index, '1%'] = 0
        except:
            df.at[index, '1%'] = 0
    df.insert(3, '2M', _2M)
    df.insert(4, '2A', _2A)
    df.insert(5, '3M', _3M)
    df.insert(6, '3A', _3A)
    df.insert(7, '1M', _1M)
    df.insert(8, '1A', _1A) 


for link in links[301:400]:
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

    remodel(game_data)
    game_data = game_data.drop(columns=["1M-1A", "2M-2A", "3M-3A"], axis=1)

    # Export to csv
    file_name = url.split('/')[-1] + '.csv'
    game_data.to_csv("./finalized_scripts/datasets/game_data/"+file_name, index=False)
    print("Data frame exported to: " + file_name)