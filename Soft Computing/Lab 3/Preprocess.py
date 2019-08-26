from MultiLayer_Perceptron_Kernel import NeuralNetwork 
import csv
from random import shuffle
import numpy as np
def preprocess(path):
    f=open(path,"r")
    data=list(csv.reader(f))
    data=data[1:]
    shuffle(data)
    no_of_attr=len(data[0])-1
    
    
    for row in data:
        for c in range(no_of_attr):
            row[c]=float(row[c])
        if(row[-1]=="Iris-versicolor" or row[-1]=="Yes"):
            row[-1]=1.0
        elif(row[-1]=="Iris-setosa" or row[-1]=="No"):
            row[-1]=0.0
    
    output=[[i[-1]] for i in data]
    data=[np.array(i[0:len(i)-1]) for i in data]
    return (no_of_attr,np.array(data),np.array(output))

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

def main(path,lrate=0.5,iterations=500,num_hidden_nodes=20):
    no_of_attr,dataset,output=preprocess(path)
    num_folds=10
    Accuracy,Precision,Recall=[],[],[]

    for i in range(1,num_folds+1):
        train,test=fold(dataset,i,num_folds)
        train_output,test_output=fold(output,i,num_folds)
        n=NeuralNetwork(no_of_attr,num_hidden_nodes,lrate,iterations)
        a,p,r=n.train(train,train_output,test,test_output)
        Accuracy.append(a)
        Precision.append(p)
        Recall.append(r)
    # print(Accuracy)
    Average=[sum(Accuracy)/len(Accuracy),sum(Precision)/len(Precision),sum(Recall)/len(Recall)]
    print("Net Accuracy:",Average[0])
    print("Net Precision:",Average[1])
    print("Net Recall:",Average[2])
    return Average

if(__name__ =="__main__"):
    main("Datasets/IRIS.csv",)
