import matplotlib.pyplot as plt

x=[i/100 for i in range(5,96,5)]
f=open("Outputs/output_Accuracy","r")
o=[[],[],[]]
o[0]=f.readline().split(' ')
o[1]=f.readline().split(' ')
o[2]=f.readline().split(' ')
o[0].remove('\n')
o[1].remove('\n')
o[2].remove('\n')
y1=[float(i) for i in o[0]]
y2=[float(i) for i in o[1]]
y3=[float(i) for i in o[2]]


#Plotting values
plt.plot(x,y1,label="IRIS")
plt.plot(x,y2,label="SPECT")
plt.plot(x,y3,label="SPECTF")
plt.legend()
plt.xlabel("Learning Rate")
plt.ylabel("Accuracy")
plt.savefig("Outputs/Plot.png")
