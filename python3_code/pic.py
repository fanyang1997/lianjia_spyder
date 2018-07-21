#%%
import csv
import numpy as np
import matplotlib.pyplot as plt
price, size = np.loadtxt('C:\\Users\\11320\\code\\lianjia_spyder\\python3_code\\house.csv', delimiter='|', usecols=(1,2), unpack=True)
print(price)
print(size)
price_mean = np.mean(price)
size_mean = np.mean(size)
print("平均价格:", price_mean)
print("平均面积:", size_mean)
price_var = np.var(price)
size_var = np.var(size)
print("价格的方差：", price_var)
print("面积的方差：", size_var)
#%%
plt.figure()
plt.subplot(211)
plt.title("/ 10000RMB")
plt.hist(price, bins=20)
plt.subplot(212)
plt.xlabel("/ m**2")
plt.hist(size, bins=20)
plt.figure(2)
plt.title("price")
plt.plot(price)
plt.plot(size, price)
plt.show()
#%%
plt.plot(size, price)
plt.show()

#%%
def text_strip_split(text):
    
    list = [ '!' , ',' , '.' , '?' , ':' , '/' , '*' , '#' , '%' , '\\' , '_' , '-' , '=' , '+' , '&' ,';']

    for i in list:
        text = text.replace( i  , ' ').strip()
    text = text.split()

    print()

    while True:
        x = int(input('Enter number word that i should print on console:\n')) - 1
        if x > len(list) or x < 0:
            print('Enter other number!')
        else:
            break

    print(text[x])


word = input('Write the something text with special symbols: \n')
print(text_strip_split(word))