from bs4 import BeautifulSoup 
with open("index.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    rootelem = soup.find("html")
    print(rootelem['lang'])