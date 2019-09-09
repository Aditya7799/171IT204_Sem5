import math

def train(train, test, no_of_attr):
    numberyes=0
    numberno=0
    for i in range(len(train)):
        if train[i][-1]==1.0:
            numberyes+=1
        if train[i][-1]==0.0:
            numberno+=1

    proYes=float(numberyes)/(numberyes+numberno)
    proNo=float(numberno)/(numberyes+numberno)

    p1yes=[0]*(no_of_attr)
    p1no=[0]*(no_of_attr)
    p0no=[0]*(no_of_attr)
    p0yes=[0]*(no_of_attr)
    for j in range(len(train)):
        for i in range(0,no_of_attr):
            if train[j][i]== 1 and train[j][-1]==1.0:
                p1yes[i]+=1
            if train[j][i]== 1 and train[j][-1]==0.0:
                p1no[i]+=1
            if train[j][i]== 0 and train[j][-1]==1.0:
                p0yes[i]+=1
            if train[j][i]== 0 and train[j][-1]==0.0:
                p0no[i]+=1
        
    for i in range(len(p1yes)):
        p1no[i]=p1no[i]/float(numberno)
        p1yes[i]=p1yes[i]/float(numberyes)
        p0no[i]=p0no[i]/float(numberno)
        p0yes[i]=p0yes[i]/float(numberyes)


    #finalYes=proYes
    #finalNo=proNo
    
    #print(test)
    for j in range(len(test)):
        yes_p=proYes
        no_p=proNo
        for i in range(0,no_of_attr):
            if test[j][i]== 0 :
                yes_p*=p0yes[i]
                no_p*=p0no[i]
            elif test[j][i]== 1 :
                yes_p*=p1yes[i]
                no_p*=p1no[i]
                #print(yes_p)
                #print(no_p)

        if yes_p>no_p:
            max_prob=1.0
        else:
            max_prob=0.0

        tp,tn,fp,fn,err=0,0,0,0,0
        prec,recall=0,0
        if(test[j][-1]==max_prob):
            if(max_prob==1.0):
                tp+=1
            else:
                tn+=1
        else:
            err+=1
            if(max_prob==1.0):
                fp+=1
            else:
                fn+=1

    try:
            acc=(tp+tn)/(tp+tn+fp+fn)
            prec=(tp)/(tp+fp)
            recall=(tp)/(tp+fn)
    except:
        pass
    return [acc*100,prec*100,recall*100]



        

# def main():
# 	filename="SPECT.csv"
# 	attributes=[]
# 	rows=[]
# 	with open(filename,'r') as csvfile:
# 		csvreader=csv.reader(csvfile)

# 		attributes=csvreader.next()
# 		for row in csvreader:
# 			rows.append(row)

# 	#print(len(rows),no_of_attr)
# 	k=10
# 	sum=0;
# 	print(attributes)
# 	for i in range(1,k+1):
# 		accuracy=[]
# 		after_fold=fold(rows,i,k)
# 		train_set=after_fold[0]
# 		test_set=after_fold[1]
# 		#print(len(train_set),"-----")
# def test():
#     acc=train(train_set,attributes,test_set)
# 		print("Fold",i,":",acc)
# 		sum=sum+acc
# 	print("Average:",sum/k)

# main()