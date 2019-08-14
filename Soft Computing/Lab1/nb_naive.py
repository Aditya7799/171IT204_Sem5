import csv
data=list(csv.reader(open("SPECT.csv")))
data=data[1:]
# print(data)

#APPLYING NAIVE BAYES ALGORITHM
dataset_size=len(data)
no_of_attr=len(data[0])
#Second is YES First is NO
prob=[[0,0] for _ in range(no_of_attr)]
yes,no=0,0
for i in data:
	if(i[0]=="Yes"):
		yes+=1
	else:
		no+=1
for row in data:
	for i in range(1,len(row)):
		if(row[0]=="Yes" and row[i]=="1"):
			prob[i][1]+=1
		elif(row[0]=="No" and row[i]=="1"):
			prob[i][0]+=1
print(prob)
#TAKE INPUT HERE
inp=data[2]
total=1
for i in range(1,no_of_attr):
	if(inp[i]=="1"):
		total=total*(prob[i][1]*1.0/yes)
	# else:
	# # 	total=total*(prob[i][0]*1.0/no)
	# print(total)
den=1
for i in range(1,no_of_attr):
	if(inp[i]=="1"):
		den=den*((prob[i][0]+prob[i][1])/(yes+no))
	print(den)
print(total/den)






