from bs4 import BeautifulSoup 
with open("index.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    rootelem = soup.find("html")
    try:
        assert rootelem["lang"] == "hu"
        print("1/1, siker!")
    except:
        print("A nyelvnek hu-nak kell lennie! 0/1")