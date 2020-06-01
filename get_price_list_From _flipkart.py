import requests
import datetime 
from bs4 import BeautifulSoup

def get_price_list():

    url = input("paste the url herer :- ")
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')

    item_name = soup.find(class_= '_35KyD6').get_text()
    item_price = soup.find(class_='_1vC4OE _3qQ9m1').get_text()
    dicount_percentage = soup.find(class_='VGWI6T _1iCvwn').get_text()
    original_price =soup.find(class_= '_3auQ3N _1POkHg').get_text()

    print(datetime.date.today())
    print("item name  :-  " + item_name)
    print('item price :-  ' +item_price)
    print('original Price :-  ' + original_price)
    print('dicount % :-  ' + dicount_percentage)


if __name__ == '__main__':
    get_price_list()