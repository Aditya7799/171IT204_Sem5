import NaiveBayes as P
import GA as G
#global variables
f=open("Outputs/output_Accuracy","w")
z=open("Outputs/output","w")
a=[]
p=[]
r=[]
cross_over=0.05
mutation=0.10
maxi=None


def display():
    print("*******************************************")

    print("SPECT.csv:")
    index=a[1].index(max(a[1]))
    print("Best Accuracy:",max(a[1]))
    print("Corresponding Recall:",r[1][index])
    print("Corresponding Precison:",p[1][index])
    print("Achieved for Lrate:",(index+1)*0.05)
    maxi=(index+1)*0.05

    print("*******************************************")

def write_to_file():
    for i in a:
        f.write(str(i)+" ")
    f.write("\n")
    for i in p:
        f.write(str(i)+" ")
    f.write("\n")
    for i in r:
        f.write(str(i)+" ")
    f.write("\n")
    f.write(str(maxi))

while cross_over<=0.05:
    # print(lrate)
    z.write("FOR CROSS_OVER RATE: "+str(cross_over)+"\n")
    z.write("SPECT:")
    temp=G.main(cross_over,mutation)
    a.append(temp[0])
    p.append(temp[1])
    r.append(temp[2])
    z.write(str(temp[0])+" "+str(temp[1])+" "+str(temp[2])+"\n")
    z.write("\n")
    cross_over+=0.05
    
display()
write_to_file()




