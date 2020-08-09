def activationFunction(value,theta=1):
    if value>=(1*theta):
        return 1
    elif value<=(-1*theta):
        return -1
    else:
        return 0
    
def perceptron(inputs, learning_rate, target,theta=1):
    weights=[0 for i in inputs[0]]
    outputs=[]
    delW=[]
    y=[float("inf") for x in target]
    epoch=0
    while target!=y:
        epoch+=1
        print("Epoch #",epoch)
        for i in range(len(inputs)):
            yin=0

            for j in range(len(inputs[i])):
                yin+=inputs[i][j]*weights[j]
            y[i]=activationFunction(yin)
            outputs.append(y[i])
            thisDelW=[]

            print("yin :",yin,"y :",y[i])
            for j in range(len(inputs[0])):
                thisDelW.append(learning_rate*inputs[i][j]*target[i])
            delW.append(thisDelW)


            if y[i]!=target[i]:
                for i in range(len(weights)):
                    weights[i]+=thisDelW[i]
    print("Final weights")
    return weights
                

perceptron([[1,1,1,1,1],[-1,1,-1,-1,1],[1,1,1,-1,1],[1,-1,-1,1,1]],1,[1,1,-1,-1])

#inputs+bias
#learning rate
#target
#add theta if wanted

        
        
        
        
    
    
