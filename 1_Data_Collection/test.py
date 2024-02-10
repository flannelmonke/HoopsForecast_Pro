links = open('./GIT_NO/player_links.txt', 'r')

links = links.readlines()

i=0
for link in links[0:100]:
    url = link.strip()
    
    file_name = url.split('/')
    file_name = file_name[len(file_name)-2]
    file_name = file_name.split('-')
    file_name[0] = file_name[0].capitalize()
    file_name[1] = file_name[1].capitalize()
    file_name = file_name[0] + file_name[1] + '.csv'
    print(file_name)