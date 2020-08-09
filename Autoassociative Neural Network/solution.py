import numpy as np

def activation(sstm):
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
def autoassoc(inputMatrix, testMatrix, trainCheckList):
    im=np.array(inputMatrix)
    tm=np.array(testMatrix)
    
    im=im.transpose()
    stm=im@tm
    print(stm)
    
    sstm=trainCheckList@stm
    print(sstm)
    
    ssstm=activation(sstm)
    print(ssstm)
    
    for i in range(len(ssstm)):
        print(ssstm[i]==tm)
    
    
print(autoassoc([[-1,1,1,1]],[[-1,1,1,1]],[[-1,-1,1,1],[1,0,1,1]]))
    
