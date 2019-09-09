import csv
from random import shuffle
# import numpy as np
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
    return [(1-err/len(test))*100,prec*100,recall*100]

def preprocess(C,path):
    lines = csv.reader(open(path, 'r'))
    dataset = list(lines)
    dataset=dataset[1:]
    finaldataset=[]
    for i in range(len(dataset)):
        finaldataset.append([])
        for j in range(len(dataset[i])-1):
            if(C[j]==1):
                data=float(dataset[i][j])
                finaldataset[i].append(data)
        if(dataset[i][-1]=="Yes"):
            finaldataset[i].append(1.0)
        else:
            finaldataset[i].append(0.0)

        	
    return [len(finaldataset[0])-1,finaldataset]

def fold(dataset,fold_num,total_folds):
    l=len(dataset)
    start_index_test=l*(fold_num-1)//total_folds
    end_index_test=l*fold_num//total_folds
    #print(end_index_test)
    if start_index_test==0:
        start_index_train=end_index_test
        end_index_train=l
        return [dataset[start_index_train:end_index_train],dataset[start_index_test:end_index_test]]
    elif end_index_test==l:
        start_index_train=0
        end_index_train=start_index_test
        return [dataset[start_index_train:end_index_train],dataset[start_index_test:end_index_test]]
    else:
        new_dataset=[]
        for i in range(start_index_test):
            new_dataset.append(dataset[i])
        for j in range(end_index_test,l):
            new_dataset.append(dataset[j])
        return [new_dataset,dataset[start_index_test:end_index_test]]

def main(Chromosome,path="Datasets/SPECT.csv",cross_over=0.25,mutation=0.10):
    no_of_attr,dataset=preprocess(Chromosome,path)
    num_folds=10
    Accuracy,Precision,Recall=[],[],[]

    for i in range(1,num_folds+1):
        training,testing=fold(dataset,i,num_folds)
        # train_output,test_output=fold(output,i,num_folds)
        a,p,r=0,0,0

        # print(training)


        l=train(training, testing,no_of_attr)
        a=l[0]
        p=l[1]
        r=l[2]
        Accuracy.append(a)
        Precision.append(p)
        Recall.append(r)
    # print(Accuracy)
    Average=[sum(Accuracy)/len(Accuracy),sum(Precision)/len(Precision),sum(Recall)/len(Recall)]
    # print("Net Accuracy:",Average[0])
    # print("Net Precision:",Average[1])
    # print("Net Recall:",Average[2])
    return Average[0]

if(__name__ =="__main__"):
    main([1]*22,"Datasets/IRIS.csv",)
