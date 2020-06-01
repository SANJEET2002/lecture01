import requests
import datetime 
from bs4 import BeautifulSoup





def get_seven_day_climate_report():
    name = input('Enter palce Here :- ')
    url  = 'https://www.weathercity.com/in/' + name

    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')

    print(soup.title.string)
    date = soup.find_all(class_='fc_summ_h1')
    temp = soup.find_all(class_ = 'fc_summ_hi')

    list_day = [item.get_text() for item in date]
    list_temp =[item.get_text() for item in temp]


    new_day = tuple(list_day)
    new_temp = tuple(list_temp)

    print(datetime.date.today())

    for num in range(0,len(new_day)):
        print(f'{new_day[num]} :- {new_temp[num]}')
        
        

if __name__ == "__main__":
    get_seven_day_climate_report()