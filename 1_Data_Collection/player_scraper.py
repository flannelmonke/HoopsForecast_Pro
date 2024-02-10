import re
import pandas as pd
import urllib.request
import numpy as np

links = open('./GIT_NO/player_links.txt', 'r')
links = links.readlines()


for link in links[0:100]:
    url = link.strip()
    
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    
    webpage = mybytes.decode("utf8")
    fp.close()
    
    data = re.findall(r'(<div class="table__inner">[\s\S]*?</main>)', webpage)
    
    Nba = re.findall(r'(<table class="table">[\s\S]*?</table>)', data[0])
    Nba_stats = Nba[3]
    
    player_headers = re.findall(r'(<th class=".*">[\s\S]*?</th>)', Nba_stats)
    player_headers = list(map(lambda x: x.split('>')[1].split('<')[0], player_headers))

    player_data = re.findall(r'(<td class=".*">[\s\S]*?</td>)', Nba_stats)
    player_data = [re.sub(r'(<td class=\".*\">|<\/td>|<a [\s\S]*?>|<\/a>|<div [\s\S]*?>[\s\S]*?>[\s\S]*?<\/div>|\n)','', data) for data in player_data]
    player_data = [re.sub(r'[\s]+', '', data) for data in player_data]
    
    player_obj = {player_headers[i]: [] for i in range(len(player_headers))}

    row_iterator = 0
    for i in range(len(player_data)):
        if row_iterator == len(player_headers):
            row_iterator = 0
            player_obj[player_headers[row_iterator]].append(player_data[i])
            row_iterator += 1
        else:
            player_obj[player_headers[row_iterator]].append(player_data[i])
            row_iterator += 1
            
    player_obj['Pts'] = player_obj['Pts'][0:len(player_obj['Pts']):2]
    player_obj['Reb'] = player_obj['Reb'][0:len(player_obj['Reb']):2]
    player_obj['Ast'] = player_obj['Ast'][0:len(player_obj['Ast']):2]

    player_df = pd.DataFrame(player_obj)    
    
    
    for index, row in player_df.iterrows():
        player_df.at[index, 'W-L'] = np.array(player_df.at[index, 'W-L'].split('-'), dtype=int)
        player_df.at[index, '2P'] = (int(player_df.at[index, '2P'].split('/')[0]) / int(player_df.at[index, '2P'].split('/')[1])) 
        # repeat for 3P, FT, FG 
        player_df.at[index, '3P'] = (int(player_df.at[index, '3P'].split('/')[0]) / int(player_df.at[index, '3P'].split('/')[1]))
        player_df.at[index, 'FT'] = (int(player_df.at[index, 'FT'].split('/')[0]) / int(player_df.at[index, 'FT'].split('/')[1]))
        player_df.at[index, 'FG'] = (int(player_df.at[index, 'FG'].split('/')[0]) / int(player_df.at[index, 'FG'].split('/')[1]))

    file_name = url.split('/')
    file_name = file_name[len(file_name)-2]
    file_name = file_name.split('-')
    file_name[0] = file_name[0].capitalize()
    file_name[1] = file_name[1].capitalize()
    file_name = file_name[0] + file_name[1] + '.csv'
    file_name = './1_Data_Collection/datasets/player_stats/' + file_name + '.csv'
    player_df.to_csv(file_name, index=False)
    print("file written to: ", file_name)
    