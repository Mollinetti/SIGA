'''
Created on 01/07/2015

@author: Mollinetti
'''


import random, Parameters, Gene

def getGeneResult(gene1, gene2, zeta):
    
    generesult = 0
    
    if gene1 > gene2:
        generesult = gene1 - gene2
    else:
        generesult = gene2 - gene1
        
    generesult*= zeta
    
    return generesult

def analyseFlow(parent1, parent2, param= Parameters):
    dir = [0] * param.dim
    
    for i in range(0,param.dim):
        if parent1[i] < parent2[i]:
            dir[i] = dir[i] + 1
        else:
            dir[i] = dir[i] - 1
    
    return dir

def Kcross(lowerBound, upperBound, dir, parent1=Gene, parent2=Gene,  param=Parameters):
    

    offspring1 = parent1.genotype 
    offspring2 = parent2.genotype

    resultoffspring1 = list(range(param.dim))
    resultoffspring2 = list(range(param.dim))


    for i in range(0, param.dim):
        gene1 = offspring1[i]
        gene2 = offspring2[i]

        if(random.uniform(0,1) <  param.getcRate()):
                
            result = getGeneResult(gene1, gene2, param.getZeta())

            if dir[i] > 0:
                resultoffspring1[i] = gene1 + result
                resultoffspring2[i] = gene2 + result
                
                #bounding the problem
                if resultoffspring1[i] > upperBound[i]:
                    resultoffspring1[i] = upperBound[i]
  
                if resultoffspring2[i] > upperBound[i]:
                    resultoffspring2[i] = upperBound[i]
                    
            else:
                resultoffspring1[i] = gene1 - result
                resultoffspring2[i] = gene2 - result
                
                #bounding the problem
                if resultoffspring1[i] < lowerBound[i]:
                    resultoffspring1[i] = lowerBound[i]
  
                if resultoffspring2[i] < lowerBound[i]:
                    resultoffspring2[i] = lowerBound[i]

            if  resultoffspring1[i] < 0:
                    resultoffspring1[i] = 0
                
            if  resultoffspring2[i] < 0:
                    resultoffspring2[i] = 0
                
                
            if random.uniform(0,1) < param.getdirCoeff():
                
                if dir[i] > 0:
                    resultoffspring1[i] = gene2 - result
                    resultoffspring2[i] = gene1 - result
                    
                    #bounding the problem
                    if resultoffspring1[i] < lowerBound[i]:
                        resultoffspring1[i] = lowerBound[i]
      
                    if resultoffspring2[i] < lowerBound[i]:
                        resultoffspring2[i] = lowerBound[i]
                        
                else:
                    
                    resultoffspring1[i] = gene2 + result
                    resultoffspring2[i] = gene1 + result
                    
                    #bounding the problem
                    if resultoffspring1[i] > upperBound[i]:
                        resultoffspring1[i] = upperBound[i]
      
                    if resultoffspring2[i] > upperBound[i]:
                        resultoffspring2[i] = upperBound[i]
                        
            else:
                
                if dir[i] > 0:

                    resultoffspring1[i] = gene2 + result
                    resultoffspring2[i] = gene1 + result
                    
                    #bounding the problem
                    if resultoffspring1[i] > upperBound[i]:
                        resultoffspring1[i] = upperBound[i]
      
                    if resultoffspring2[i] > upperBound[i]:
                        resultoffspring2[i] = upperBound[i]
                        
                else:
                    
                    resultoffspring1[i] = gene2 - result
                    resultoffspring2[i] = gene1 - result
                    
                    #bounding the problem
                    if resultoffspring1[i] < lowerBound[i]:
                        resultoffspring1[i] = lowerBound[i]
      
                    if resultoffspring2[i] < lowerBound[i]:
                        resultoffspring2[i] = lowerBound[i]
        else:
            resultoffspring1[i] = gene1
            resultoffspring2[i] = gene2

    child1 = Gene.Gene(param)

    child2 = Gene.Gene(param)

    child1.genotype = list(resultoffspring1)
    child2.genotype = list(resultoffspring2)

    return child1, child2

def KcrossSuperIndividual(lowerBound, upperBound, dir, parent1=Gene, parent2=Gene,  param=Parameters):
    

    offspring1 = list(parent1.genotype) 
    offspring2 = list(parent2.genotype)

    resultoffspring1 = list(range(param.dim))
    resultoffspring2 = list(range(param.dim))


    for i in range(0, param.dim):
        gene1 = offspring1[i]
        gene2 = offspring2[i]

        if(random.uniform(0,1) <  param.getcRate()):
                
            result = getGeneResult(gene1, gene2, param.getZeta())

            if dir[i] > 0:
                resultoffspring1[i] = gene1 + result
                resultoffspring2[i] = gene2 + result
                
                #bounding the problem
                if resultoffspring1[i] > upperBound[i]:
                    resultoffspring1[1] = upperBound[i]
  
                if resultoffspring2[i] > upperBound[i]:
                    resultoffspring2[1] = upperBound[i]
                    
            else:
                resultoffspring1[i] = gene1 - result
                resultoffspring2[i] = gene2 - result
                
                #bounding the problem
                if resultoffspring1[i] < lowerBound[i]:
                    resultoffspring1[1] = lowerBound[i]
  
                if resultoffspring2[i] < lowerBound[i]:
                    resultoffspring2[1] = lowerBound[i]

            if  resultoffspring1[i] < 0:
                    resultoffspring1[i] = 0
                
            if  resultoffspring2[i] < 0:
                    resultoffspring2[i] = 0
                
                
            if random.uniform(0,1) < param.getdirCoeff():
                
                if dir[i] > 0:
                    resultoffspring1[i] = gene2 - result
                    resultoffspring2[i] = gene1 - result
                    
                    #bounding the problem
                    if resultoffspring1[i] < lowerBound[i]:
                        resultoffspring1[1] = lowerBound[i]
      
                    if resultoffspring2[i] < lowerBound[i]:
                        resultoffspring2[1] = lowerBound[i]
                        
                else:
                    
                    resultoffspring1[i] = gene2 + result
                    resultoffspring2[i] = gene1 + result
                    
                    #bounding the problem
                    if resultoffspring1[i] > upperBound[i]:
                        resultoffspring1[1] = upperBound[i]
      
                    if resultoffspring2[i] > upperBound[i]:
                        resultoffspring2[1] = upperBound[i]
                        
            else:
                
                if dir[i] > 0:

                    resultoffspring1[i] = gene2 + result
                    resultoffspring2[i] = gene1 + result
                    
                    #bounding the problem
                    if resultoffspring1[i] > upperBound[i]:
                        resultoffspring1[1] = upperBound[i]
      
                    if resultoffspring2[i] > upperBound[i]:
                        resultoffspring2[1] = upperBound[i]
                        
                else:
                    
                    resultoffspring1[i] = gene2 - result
                    resultoffspring2[i] = gene1 - result
                    
                    #bounding the problem
                    if resultoffspring1[i] < lowerBound[i]:
                        resultoffspring1[1] = lowerBound[i]
      
                    if resultoffspring2[i] < lowerBound[i]:
                        resultoffspring2[1] = lowerBound[i]
        else:
            resultoffspring1[i] = gene1
            resultoffspring2[i] = gene2

    child1 = Gene.Gene(param)

    child2 = Gene.Gene(param)

    child1.genotype = list(resultoffspring1)
    child2.genotype = list(resultoffspring2)

    #return both childs and the superindividual
    return parent1, child1, child2 

def KCrossover(pool, param= Parameters):

    dir = []

    childs = []

    #fill a list with index numbers
    ind = list(range(len(pool)))

    #shuffle the indices list
    random.shuffle(ind)

    #loop over the pool in order to perform the crossovers (starting from individual 2, because individual 0 is te super individual)
    for i in range(0, int(len(pool)), 2):

        #print(i, i+1)

        #print(pool[ind[i]].fitness,pool[ind[i+1]].fitness)

        dir = analyseFlow(pool[ind[i]].genotype,pool[ind[i+1]].genotype, param)

        if ind[i] == 0:
            childs.extend(KcrossSuperIndividual(param.lowBound, param.uppBound, dir, pool[ind[i]], pool[ind[i+1]], param))

        elif ind[i+1] == 0:
            childs.extend(KcrossSuperIndividual(param.lowBound, param.uppBound, dir, pool[ind[i+1]], pool[ind[i]], param))

        else:
            childs.extend(Kcross(param.lowBound, param.uppBound, dir, pool[ind[i]], pool[ind[i+1]], param))

    #return the list with all childs
    return childs







                    


                
                
            