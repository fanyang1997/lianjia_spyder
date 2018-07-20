import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
import re
import csv
import urllib

def get_bsobj(url):
    page = urllib.request.urlopen(url)
    if page.getcode() == 200:
        html = page.read()
        bsobj = BeautifulSoup(html, "html5lib")
        return bsobj
    else:
        print("page error")
        sys.exit()
def get_house_info_list(url):
    house_info_list = []
    bsobj = get_bsobj(url)
    if not bsobj:
        return None
    house_list = bsobj.find_all("li", {"class":"clear"})
    for house in house_list:
        title = house.find("div", {"class":"title"}).get_text()
        info = house.find("div", {"class":"houseInfo"}).get_text().split("|")
        block = info[0].strip()
        house_type = info[1].strip()
        size_info = info[2].strip()
        size = re.findall(r"\d+", size_info)[0]
        price_info = house.find("div", {"class":"totalPrice"}).span.get_text()
        price = re.findall(r"\d+", price_info)[0]
        
        house_info_list.append({
            "title":title,
            "price":price,
            "size":int(size),
            "block":block,
            "house_type":house_type
        })
    return house_info_list
def house(url):
    house_info_list = []
    for i in range(20):
        new_url = url + 'pg' + str(i+1)
        house_info_list.extend(get_house_info_list(new_url))
        if house_info_list:
            with open("./house.csv", "w+", newline='') as f:
                writer = csv.writer(f, delimiter = "|")
                for house_info in house_info_list:
                    title = house_info.get("title")
                    price = house_info.get("price")
                    size = house_info.get("size")
                    block = house_info.get("block")
                    house_type = house_info.get("house_type")
                    #print(type(title))
                    writer.writerow([title, int(price), int(size), block, house_type])
def get_city_dict():
    city_dict = {}
    with open("C:\\Users\\11320\\code\\lianjia_spyder\\citys.csv", "r") as f:
        reader = csv.reader(f)
        for city in reader:
            print(city)
            city_dict[city[0]] = city[1]
    return city_dict
def get_district_dict(url):
    district_dict = {}
    html = urlopen(url).read()
    bsobj = BeautifulSoup(html, "html5lib")
    roles = bsobj.find("div", {"data-role":"ershoufang"}).findChildren("a")
    for role in roles:
        district_url = role.get("href")
        district_name = role.get_text()
        district_dict[district_name] = district_url
    return district_dict
def run():
    city_dict = get_city_dict()
    for city in city_dict.keys():
        print(city)
    input_city = input("Please input city name:")
    city_url = city_dict.get(input_city)
    if not city_url:
        print("input error")
        sys.exit()
    ershoufang_city_url = city_url + "ershoufang"
    district_dict = get_district_dict(ershoufang_city_url)
    for district in district_dict.keys():
        print(district)
    input_district = input("Please input area:")
    district_url = district_dict.get(input_district)
    if not district_url:
        print("input error")
        sys.exit()
    house_info_url = city_url + district_url[1:]
    #print(house_info_url)
    house(house_info_url)
if __name__ == "__main__":
    run()