import matplotlib.pyplot as plt

x=[i for i in range(1,46)]
fig, ax = plt.subplots(nrows=2)
f=open("output.txt","r")
y1,y2,speedup=[],[],[]
for i in range(45):
	l=f.readline().split(' ')
	y1.append(float(l[0]))
	y2.append(float(l[1]))
	speedup.append(float(l[2]))

print(speedup)

#Plotting values
ax[0].plot(x,y1,label="SERIAL")
ax[0].plot(x,y2,label="OPTIMIZED")
ax[1].plot(x,speedup,label="SPEED UP")

ax[0].legend()
ax[1].legend()
plt.xlabel("Nth FIbonacci Number")
plt.ylabel("Execution time")
plt.savefig("Plot.png")
