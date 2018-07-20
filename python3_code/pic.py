import csv
import numpy as np
import matplotlib.pyplot as plt
price, size = np.loadtxt('house.csv', delimiter='|', usecols=(1,2), unpack=True)
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
import csv
import numpy as np
import matplotlib.pyplot as plt
price, size = np.loadtxt('house.csv', delimiter='|', usecols=(1,2), unpack=True)
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
plt.show()