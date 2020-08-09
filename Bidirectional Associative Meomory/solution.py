import numpy as np

def activationfn(arr,bipolar):
    solution=[]
    for i in arr:
        soln=[]
        for j in i:
            if j==0:
                soln.append(0)
            elif j<0:
                soln.append(-1 if bipolar else 0)
            else:
                soln.append(1)
        solution.append(soln)
    
    return solution

def bam(inputs,initWeights,test,test2,bipolar):
    if bipolar:
        inp=np.array(inputs)
        inp=inp.transpose()
        print("Transpose of input matrix")
        print(inp)
        iw=np.array(initWeights)
        w=inp@iw
        weight=w
        print("Weight matrix")
        print(weight)

        
    else:
        inp=np.array(inputs)
        weight=np.array(initWeights)
        inp=2*inp
        weight=2*weight
        inp=inp-1
        weight=weight-1
        w=inp.transpose()@weight
        weight=w
        print("Transpose of input matrix")
        print(inp.transpose())
        print("Weight matrix")
        print(weight)
        
    t=np.array(test)
    print("Test array")
    print(t)

    solution=[]

    for i in test:
        solution.append(i@weight)
    print("solution of first test")
    print(solution)
    print("Solution of activ func")
    rsolution=activationfn(solution,bipolar)
    print(rsolution)
    
    print(rsolution==initWeights)

    weight=weight.transpose()
    print("Weight transpose")
    print(weight)

    t2=np.array(test2)
    solution2=[]

    for i in t2:
        solution2.append(i@w.transpose())
    print("solution of test2(backtesing?)")
    print(solution2)
    print("Solution of activ func")
    rsolution2=activationfn(solution2,bipolar)
    print(rsolution2)
    
    print(rsolution2==inputs)
    
inputs=[[1,1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,1],[1,1,1,1,1,1,1,-1,-1,1,-1,-1,1,-1,-1]]
initWeights=[[-1,1],[1,1]]
test=inputs.copy()
test2=[[-1,1],[1,1]]
bam(inputs,initWeights,test,test2,True)
