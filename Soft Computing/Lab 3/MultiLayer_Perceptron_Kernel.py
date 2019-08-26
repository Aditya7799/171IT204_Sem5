from numpy import exp,array,random,dot,tanh

class Layer():
    def __init__(self,no_of_neurons,number_of_inputs_per_neuron):
        self.weights=random.random((number_of_inputs_per_neuron,no_of_neurons))
        #weights[i][j] = weight of synaptic link form node i in previous layer to node j in current layer

class NeuralNetwork():
    def __init__(self,no_of_input_nodes,no_of_hidden_layer_nodes,lrate,iter):
        self.lrate=lrate
        self.iterations=iter
        self.hidden=Layer(no_of_hidden_layer_nodes,no_of_input_nodes,)
        self.output=Layer(1,no_of_hidden_layer_nodes)
    
    def sig(self,x):
        return 1/(1+exp(-x))
    
    def th(self,x):
        return tanh([x])[0]
    
    def sig_der(self,x):
        return x*(1-x)
    
    
    def think(self,input):
        hiddenLayer_output=self.sig(dot(input, self.hidden.weights))
        outputLayer_output=self.sig(dot(hiddenLayer_output,self.output.weights))
        return (hiddenLayer_output,outputLayer_output)
        
    
    def train(self,train,train_outputs,test,test_outputs):
        A,P,R=0,0,0
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
        print(test_length,test_out_length)
        err=0
        hid,Y=self.think(test)
        for i in range(test_length):
            if(abs(test_outputs[i][0]-Y[i][0])>0.1):
                err+=1
        # print(err)    
        

        return (1-err/test_length)*100,P,R







