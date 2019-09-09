import matplotlib.pyplot as plt

x=[i for i in range(1,21)]
f=open("Outputs/output.txt","r")
o=[]
o=f.readline().split(' ')
o.remove('')
print(o)

y1=[float(i) for i in o]



#Plotting values
plt.plot(x,y1,label="SPECT")
plt.legend()
plt.xlabel("EPOCH")
plt.ylabel("Accuracy")
plt.savefig("Outputs/Plot.png")
