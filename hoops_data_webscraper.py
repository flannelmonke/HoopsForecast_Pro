import re
import pandas as pd

# Open the webpage
webpage = open("./Denver Nuggets vs. Los Angeles Lakers - Oct 25, 2023 - Game recap Proballers.htm")
tables =  re.findall(r'(<div class=\"table__inner\">[\s\S]*?<\/table>)', webpage.read())

team_1 = tables[0]
team_2 = tables[1]

# GET HEADERS FROM TEAM 1 TABLE (Applicalbe to team 2 as well)
team_headers = re.findall(r'(<th class=\".*\">.*<\/th>)', team_1)
team_headers = [re.sub(r'(<th class=\".*\">|<\/th>)', '', header) for header in team_headers]

# Remove duplicate headers
team_headers = list(dict.fromkeys(team_headers))
team_headers

# GET DATA FROM TEAM 1 TABLE
team_1_data_raw = re.findall(r'(<td class=\".*\">[\s\S]*?<\/td>)', team_1)
team_1_data_raw = [re.sub(r'(<td class=\".*\">|<\/td>|<a [\s\S]*?>\n|\n|<\/a>|<div [\s\S]*?>[\s\S]*?>[\s\S]*?<\/div>)','', data) for data in team_1_data_raw]

# GET DATA FROM TEAM 2 TABLE
team_2_data_raw = re.findall(r'(<td class=\".*\">[\s\S]*?<\/td>)', team_2)
team_2_data_raw = [re.sub(r'(<td class=\".*\">|<\/td>|<a [\s\S]*?>\n|\n|<\/a>|<div [\s\S]*?>[\s\S]*?>[\s\S]*?<\/div>)','', data) for data in team_2_data_raw]


team_1_data = {team_headers[i]: [] for i in range(len(team_headers))}
team_2_data = {team_headers[i]: [] for i in range(len(team_headers))}

row_iterator = 0
for i in range(len(team_1_data_raw)):
    if row_iterator == len(team_headers):
        row_iterator = 0
        team_1_data[team_headers[row_iterator]].append(team_1_data_raw[i])
        team_2_data[team_headers[row_iterator]].append(team_2_data_raw[i])
        row_iterator += 1
    else:
        team_1_data[team_headers[row_iterator]].append(team_1_data_raw[i])
        team_2_data[team_headers[row_iterator]].append(team_2_data_raw[i])
        row_iterator += 1
        
team_1_data['PLAYER'] = [re.sub(r'(\s)', '', player) for player in team_1_data['PLAYER']]
team_2_data['PLAYER'] = [re.sub(r'(\s)', '', player) for player in team_2_data['PLAYER']]        

for i in range(len(team_headers)):
    print("HEADER: ",team_headers[i]," ",len(team_1_data[team_headers[i]]))
    print("\n")
    print("HEADER: ",team_headers[i]," ",len(team_2_data[team_headers[i]]))
    print("\n")
    
