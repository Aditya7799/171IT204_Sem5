import csv
import numpy as np
import random
from random import shuffle
class Perceptron():
    def __init__(self,lrate=0.2,iterations=10):
        self.lrate=lrate
        self.iter=iterations
    
    def activationFunction(self,x):
        if(x>=0):
            return 1.0
        else:
            return -1.0
    

    def train(self,train,test,attr):
        self.weights=[random.random() for _ in range(attr)]
        # print(self.weights)
        # print("Original Weights:",self.weights)
        self.errors=[]
        # print(attr)
        for _ in range(self.iter):
            err=0
            for row in train:
                # print(row)
                Y=0
                for x in range(attr):
                    Y=Y+(self.weights[x]*row[x])
                Y=self.activationFunction(Y)                
                err=row[-1]-Y
                # print(err)
                if(err!=0.0):
                    for x in range(attr):
                        change=self.lrate*(err**row[x])
                        self.weights[x]+=change
        # print(self.weights)
                
        err=0
        tp=0
        tn=0
        fp=0
        fn=0
        prec,recall=0,0
        for row in test:
            Y=0
            for x in range(attr):
                Y=Y+(self.weights[x]*row[x])
            # print("Calculated Y:",Y,"Expected:",row[-1])
            Y=self.activationFunction(Y)
            Z=row[-1]
            # print("Calculated Y:",Y,"Expected:",Z)
            # print(Z," ",Y)
            if(Z==Y):
                if(Z==1.0):
                    tp+=1
                if(Z==-1.0):
                    tn+=1
            else:
                if(Y==1.0):
                    fp+=1
                if(Y==-1.0):
                    fn+=1
        # print(tp,tn,fp,fn)
        try:
            acc=(tp+tn)/(tp+tn+fp+fn)
            prec=(tp)/(tp+fp)
            recall=(tp)/(tp+fn)
        except:
            pass
        return(acc*100,prec*100,recall*100)
    
def preprocess(Dataset_path):
    f=open(Dataset_path)
    data=list(csv.reader(f))
    data=data[1:]
    shuffle(data)
    no_of_attr=len(data[0])-1
    
    for row in data:
        for c in range(no_of_attr):
            row[c]=float(row[c])
        if(row[-1]=="Yes"):
            row[-1]=1.0
        elif(row[-1]=="No"):
            row[-1]=-1.0
    # print(data)
    return (no_of_attr,data)

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

def main(lrate=0.2,iterations=500):
    no_of_attr,dataset=preprocess("Datasets/SPECTF.csv")
    num_folds=10
    Accuracy,Precision,Recall=[],[],[]

    for i in range(1,11):
        train,test=fold(dataset,i,num_folds)
        p=Perceptron(lrate,iterations)
        a,p,r=p.train(train,test,no_of_attr)
        Accuracy.append(a)
        Precision.append(p)
        Recall.append(r)
    Average=[sum(Accuracy)/len(Accuracy),sum(Precision)/len(Precision),sum(Recall)/len(Recall)]
    # print("Net Accuracy:",Average[0])
    # print("Net Precision:",Average[1])
    # print("Net Recall:",Average[2])
    return Average
    


if(__name__ =='__main__'):
    main()  