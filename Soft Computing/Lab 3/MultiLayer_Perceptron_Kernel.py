from numpy import exp,array,random,dot,tanh
import numpy
class Layer():
    def __init__(self,no_of_neurons,number_of_inputs_per_neuron):
        self.weights=random.random((number_of_inputs_per_neuron,no_of_neurons))
        # self.weights=numpy.zeros([number_of_inputs_per_neuron,no_of_neurons], dtype = float)
        #weights[i][j] = weight of synaptic link form node i in previous layer to node j in current layer

class NeuralNetwork():
    def __init__(self,no_of_input_nodes,no_of_hidden_layer_nodes,lrate,iter):
        self.lrate=lrate
        self.iterations=iter
        self.hidden=Layer(no_of_hidden_layer_nodes,no_of_input_nodes,)
        self.output=Layer(1,no_of_hidden_layer_nodes)
    
    def sig(self,x):
        return 1/(1+exp(-x))
    
    def func(self,x):
        if(1-x<0.1):
            return 1.0
        else:
            return 0.0
    
    def sig_der(self,x):
        return x*(1-x)
    
    
    def think(self,input):
        hiddenLayer_output=self.sig(dot(input, self.hidden.weights))
        outputLayer_output=self.sig(dot(hiddenLayer_output,self.output.weights))
        return (hiddenLayer_output,outputLayer_output)
        
    
    def train(self,train,train_outputs,test,test_outputs):
        acc,prec,recall=0,0,0
        tp,tn,fp,fn=0,0,0,0
        for _ in range(self.iterations):
            hid,out=self.think(train)

            out_err=train_outputs-out
            # print(out_err)
            out_delta=out_err*self.sig_der(out)

            hid_err=out_delta.dot(self.output.weights.T)
            hid_delta=hid_err*(self.sig_der(hid))

            hidden_adjustment = array(train).T.dot(hid_delta)
            output_adjustment = hid.T.dot(out_delta)

            self.hidden.weights+=hidden_adjustment
            self.output.weights+=output_adjustment
        #checking test data
        test_length=test.shape[0]
        test_out_length=test_outputs.shape[0]
        
        err=0
        hid,y=self.think(test)
        for i in range(test_length):
            Z=test_outputs[i][0]
            Y=self.func(y[i][0])
            # print(Z,Y)
            if(Z==Y):
                if(Z==1.0):
                    tp+=1
                if(Z==0.0):
                    tn+=1
            elif(Z!=Y):
                err+=1
                if(Y==1.0):
                    fp+=1
                if(Y==0.0):
                    fn+=1
        try:
            acc=(tp+tn)/(tp+tn+fp+fn)
            prec=(tp)/(tp+fp)
            recall=(tp)/(tp+fn)
        except:
            pass
        return((1-err/test_length)*100,prec*100,recall*100)   
        
      







