import numpy as np
import matplotlib.pyplot as plt



# x=["sat","san","tues"]


# y=["math","physics","program"]

# plt.plot(x,y,"ro")
# plt.show()


#create sin function 
#  t=np.arange(0,10,0.1)
# y=np.sin(2*np.pi*t)
# plt.plot(t,y,"g--")
# plt.xlabel("time by sec")
# plt.ylabel("sin 2pt")
# plt.title("sequance of sin")
# plt.show() 

#CREATE BAR FIGURES

x1=np.arange(20)
# plt.figure(12)
# plt.bar(x1,x1**3,color="red",width=0.5,align='center')
# plt.show()

#create scatter fig by random number

# plt.figure("zalpars")

# plt.scatter(x1,x1+np.random.randn(len(x1)))
# plt.show()

#create step fig
# plt.figure(3)
# plt.step(x1,x1**3,lw=2,color='red')
# plt.title("step")
# plt.show()


#create pie plot

import pylab as pl
plt.figure(4,figsize=(6,6))
p1=[40,20,20,20]
pl.pie(p1,labels=["1","2","3","4"])
plt.title("scale")
plt.show()



