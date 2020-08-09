import numpy as np

def activation(sstm):
    solution=[]
    for i in sstm:
        soln=[]
        for j in i:
            if j>0:
                soln.append(1)
            elif j<0:
                soln.append(-1)
            else:
                soln.append(0)
        solution.append(soln)
    return np.array(solution)

def activation2(sstm):
    solution=[]
    for i in sstm:
        soln=[]
        for j in i:
            if j>0:
                soln.append(1)
            else:
                soln.append(-1)
        solution.append(soln)
    return np.array(solution)
    
def heteroassoc(inputs, target, train,isBipolar=False):
    inp=np.array(inputs)
    t=np.array(target)
    
    inp=inp.transpose()
    
    
    weights=inp@t
    print("weights")
    print(weights)
    
    tr=np.array(train)
    print("train")
    print(tr)
    
    print("train*weights product results")
    tw=tr@weights
    print(tw)
    
    if isBipolar:
        res=activation2(tw)
    else:
        res=activation(tw)
        
    print("result")
    print(res)
    
    print("overall results")
    for i in range(len(res)):
        print(res[i]==t[i])
    
    
    
inputs=[[1,-1,-1,-1],[1,1,-1,-1],[-1,-1,-1,1],[-1,-1,1,1]]
targets=[[-1,1],[-1,1],[1,-1],[1,-1]]
train=inputs
print(heteroassoc(inputs,targets,train,False))
    
