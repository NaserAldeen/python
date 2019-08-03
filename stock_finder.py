from bs4 import BeautifulSoup
from urllib.request import urlopen

def findStockInformation(url):

    request = urlopen(url)
    html_page = request.read()
    request.close()

    page_soup = BeautifulSoup(html_page, "html.parser")

    block = page_soup.find("div", {"class":"stock-overview__text-and-value-items"})
    block2 = page_soup.find_all("div", {"class":"stock-overview__text-and-value-item"})


    for item in block2:
        title = item.find("span",{"class":"stock-overview__text"})
        value = item.find("span", {"class":"number number--aligned"})
        unit = item.find(class_=None)
        
        if not unit == None:
            print("{}: {} {}".format(title.text, value.text, unit.text))
        elif value == None:
            break;
        else:
            print("{}: {}".format(title.text, value.text))


choices = {
"1" :"https://english.mubasher.info/markets/BK/stocks/SULTAN",
"2" :"https://english.mubasher.info/markets/BK/stocks/NBK",
"3" :"https://english.mubasher.info/markets/BK/stocks/OOREDOO/",
"4" :"https://english.mubasher.info/markets/BK/stocks/ZAIN/",
"5" :"https://english.mubasher.info/markets/BK/stocks/BURG/"
    }

print("Welcome to the stock information finder!")

while True:
    print("\nChoose one of the listed companies:\n")
    print("""
    1- Sultan Center Food (SULTAN)
    2- National Bank of Kuwait (NBK)
    3- National Mobile Telecommunications (OOREDOO)
    4- Mobile Telecommunications (ZAIN)
    5- Burgan Bank
    """)
    user_choice = input("Your choice >> ")
    if user_choice == "6":
        break
    print("\nPlease wait a moment.. \n")
    
    findStockInformation(choices[user_choice])

    second_choice = input("\nDo you want to try again or exit? (1 to continue, or any key to leave) >> ")
    if second_choice == "1":
        continue
    else: break











