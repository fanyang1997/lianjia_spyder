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
    for i in range(3):
        new_url = url + 'pg' + str(i+1)
        house_info_list.extend(get_house_info_list(new_url))
        if house_info_list:
            with open("./house.csv", "wb+") as f:
                writer = csv.writer(f, delimiter = "|")
                for house_info in house_info_list:
                    title = house_info.get("title")
                    price = house_info.get("price")
                    size = house_info.get("size")
                    block = house_info.get("block")
                    house_type = house_info.get("house_type")
                    writer.writerow([str(title), int(price), int(size), str(block), str(house_type)])