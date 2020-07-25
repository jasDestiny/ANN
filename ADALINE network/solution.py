def activationFunction(value):
    if value>=0:
        return 1
    return -1
    
def adaline(inputs, weights, learning_rate, target, tolerance):
    y=[float("inf") for x in target]
    delW=[0 for i in weights]
    error=[float("inf") for i in target]
    epoch=0
    
    while (target!=y or sum(error)>tolerance): 
        epoch+=1
        print("Epoch #",epoch)
        for epochN in range(len(target)):
            Yin=0
            for i in range(len(weights)):
                Yin+=inputs[epochN][i]*weights[i]
            print("Yin: ", Yin)
            error[epochN]=(target[epochN]-Yin)**2
            y[epochN]=activationFunction(Yin)
                
            for i in range(len(delW)):
                delW[i]=learning_rate*(target[epochN]-Yin)*inputs[epochN][i]
                
            print("DelW: ",delW)
            
            for i in range(len(delW)):
                weights[i]+=delW[i]
            print("weights: ", weights)
        print("error: ",error)
            
        print("Y",y)
    
    return weights
                

adaline([[1,1,1],[1,-1,1],[-1,1,1],[-1,-1,1]],[0.1,0.1,0.1],0.1,[1,1,1,-1],1.4)

        
        
        
        
    
    
