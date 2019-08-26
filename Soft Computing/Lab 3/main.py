import Preprocess as P

#global variables
f=open("Outputs/output_Accuracy","w")
z=open("Outputs/output","w")
a=[[],[],[]]
p=[[],[],[]]
r=[[],[],[]]
lrate=0.05
maxi=[]


def display():
    print("*******************************************")
    print("IRIS.csv:")
    index=a[0].index(max(a[0]))
    print("Best Accuracy:",max(a[0]))
    print("Corresponding Recall:",r[0][index])
    print("Corresponding Precison:",p[0][index])
    print("Achieved for Lrate:",(index+1)*0.05)
    maxi.append((index+1)*0.05)

    print("SPECT.csv:")
    index=a[1].index(max(a[1]))
    print("Best Accuracy:",max(a[1]))
    print("Corresponding Recall:",r[1][index])
    print("Corresponding Precison:",p[1][index])
    print("Achieved for Lrate:",(index+1)*0.05)
    maxi.append((index+1)*0.05)

    print("SPECTF.csv:")
    index=a[2].index(max(a[2]))
    print("Best Accuracy:",max(a[2]))
    print("Corresponding Recall:",r[2][index])
    print("Corresponding Precison:",p[2][index])
    print("Achieved for Lrate:",(index+1)*0.05)
    maxi.append((index+1)*0.05)

    print("*******************************************")

def write_to_file():
    for row in a:
        for j in row:
            f.write(str(j)+" ")
        f.write("\n")
    f.write("\n")
    for row in p:
        for j in row:
            f.write(str(j)+" ")
        f.write("\n")
    f.write('\n')
    for row in r:
        for j in row:
            f.write(str(j)+" ")
        f.write("\n")
    f.write("\n")
    f.write(str(maxi))

while lrate<1.0:
    print(lrate)
    z.write("FOR LRATE: "+str(lrate)+"\n")
    z.write("IRIS:")
    temp=P.main("Datasets/IRIS.csv",lrate)
    a[0].append(temp[0])
    p[0].append(temp[1])
    r[0].append(temp[2])
    z.write(str(temp[0])+" "+str(temp[1])+" "+str(temp[2])+"\n")
    z.write("SPECT:")
    temp=P.main("Datasets/SPECT.csv",lrate)
    a[1].append(temp[0])
    p[1].append(temp[1])
    r[1].append(temp[2])
    z.write(str(temp[0])+" "+str(temp[1])+" "+str(temp[2])+"\n")
    z.write("SPECTF:")
    temp=P.main("Datasets/SPECTF.csv",lrate)
    a[2].append(temp[0])
    p[2].append(temp[1])
    r[2].append(temp[2])
    z.write(str(temp[0])+" "+str(temp[1])+" "+str(temp[2])+"\n")
    z.write("\n")
    lrate+=0.05
    
display()
write_to_file()




