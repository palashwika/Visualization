import matplotlib.pyplot as plt
x=[0,5,10,15,20,25,30]
y1=[0,25,100,225,400,625,900]
y2=[0,25,50,75,100,125,150]
plt.plot(x,y1,linestyle='dotted', marker='*')
plt.plot(x,y2,linestyle='solid', marker='o')
plt.title('velocity-Time Graph')
plt.xlabel('Velocity m/s')
plt.ylabel('Time(s)')
plt.xlim(0,40)
plt.ylim(0,1000)
plt.legend()
plt.show()