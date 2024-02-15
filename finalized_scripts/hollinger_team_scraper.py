import pandas as pd
import re
import urllib.request as ur

links = open('./GIT_NO/links/hollinger_teams.txt', 'r')
links = links.readlines()
master_df = pd.DataFrame()
print("links found: ", len(links))

for link in links:
    # For testing we will be using a local HTML saved from the source
    # webpage = open('../GIT_NO/PLAYER_STATS_2scrape/Page_1.htm', 'r').read()
    url = link.strip()
    fp = ur.urlopen(url).read().decode('utf-8')
    webpage = fp
    print("scraping: ",url, "\n")

    # Find the table
    table = re.findall(r'<table class="tablehead" cellspacing="1" cellpadding="3">[\s\S].*?</table>', webpage)[0]

    # Find the headers
    table_headers = re.findall(r'<tr class="colhead" align="right">([\s\S].*?)</tr>', table)[0]
    table_headers
    table_headers = re.findall(r'<td.*?>(.*?)</td>', table_headers)
    table_headers
    # webpage
    
    
    """
    Remove the HTML anchor tags from the headers
    """
    
    table_headers = [re.sub(r'(<a .*\">|<\/a>)', '', header) for header in table_headers]

    print("Table headers found: ", len(table_headers), "\n")

    """
        Find the player stats
    """
    # player_stats_raw = re.findall(r'(<td class=\".*\">[\s\S]*?<\/td>)', table)
    player_stats_raw = re.findall(r'<tr class="(oddrow team|evenrow team)-\d+-\d+" align="right">(.*?)</tr>', table)
    player_stats_raw = [re.findall(r'<td.*?>(.*?)</td>', player[1]) for player in player_stats_raw]
    player_stats_raw = [re.sub(r'(<a href=.*">|</a>|,.*|[\s])', '', stat) for player in player_stats_raw for stat in player]

    print("Player stats found: ", len(player_stats_raw), "\n")

    player_data = {table_headers[i]: player_stats_raw[i::len(table_headers)] for i in range(len(table_headers))}
    player_data
    df = pd.DataFrame(player_data)
    master_df = pd.concat([master_df, df], ignore_index=True)
    
master_df.to_csv('./finalized_scripts/datasets/player_stats/hollinger-team-stats.csv', index=False)
