links = open('links.txt', 'r')

links = links.readlines()

i=0
for link in links[0:100]:
    url = link.strip()
    print(i, " " + url)
    i += 1
