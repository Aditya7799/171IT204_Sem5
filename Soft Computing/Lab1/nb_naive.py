import csv
data=list(csv.reader(open("SPECT.csv")))
data=data[1:]
# print(data)

#APPLYING NAIVE BAYES ALGORITHM
dataset_size=len(data)
no_of_attr=len(data[0])

#1 yes 1
#0 no 
prob=[[0,0,0,0] for _ in range(no_of_attr)]
yes,no=0,0
for i in data:
	if(i[0]=="Yes"):
		yes+=1
	else:
		no+=1
count_one=[0]*(no_of_attr)
count_zero=[0]*(no_of_attr)
for row in data:
	for i in range(1,len(row)):
		if(row[0]=="Yes" and row[i]=="1"):
			prob[i][1]+=1
		elif(row[0]=="No" and row[i]=="1"):
			prob[i][0]+=1
for row in data:
	for i in range(1,len(row)):
		if(row[i]=="1"):
			count_one[i]+=1
		elif(row[i]=="0"):
			count_zero[i]+=1
print(count_one)
print(count_zero)

for i in range(1,len(prob)):
	for j in range(2):
		if(j==0):
			prob[i][j]/=count_one[i]
		elif(j==1):
			prob[i][j]/=count_one[i]


		
print(prob)
#TAKE INPUT HERE
inp=data[42]
total_yes=1
total_no=1

for i in range(1,no_of_attr):
	if(inp[i]=='1'):
		total_yes=total_yes*float(prob[i][1])
	elif(inp[i]=='0'):
		total_no=total_no*float(prob[i][0])

print(total_yes,total_no)
print(dataset_size)
print(yes,no)
a=total_yes*(yes/dataset_size)
b=total_no*(no/dataset_size)
print(a,b)
print(a/(a+b))






