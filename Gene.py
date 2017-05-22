'''
Created on 01/07/2015

@author: Mollinetti
'''
import random, Parameters

class Gene():
    
    population = 0
        
    def __init__(self, param = Parameters):
        self.genotype = []
        self.fitness = float("inf")
        self.violations = float("inf")
        self.socialFitness = float(0)
        self.totalFitness = float(0)
        self.restrictions = []
        
        #generating optimization parameters
        for i in range(0,param.dim):
            self.genotype.append(random.uniform(param.lowBound[i], param.uppBound[i]))
        
        #generating strategy profile
        num = random.uniform(0,1)
        if num >= 0 and num < param.allDRate:
            self.probC = 0.1
            self.probD = 0.9
        elif num >= param.allDRate and num < param.allDRate + param.allCRate:
            self.probC = 0.9
            self.probD = 0.1
        elif num >= param.allDRate + param.allCRate and num < param.allDRate + param.allCRate + param.TFTRate: 
            self.probC = 0.5
            self.probD = 0.5
        else:
            self.probC = random.random()
            self.probD = 1 - self.probC 

        Gene.population +=1

    #model what kind of move will the player do
    def play(self):
        #flip a coin
        coin = random.random()
        #C
        if (coin >= 0 and coin < self.probC):
            return "C"
        #D
        elif (coin >= self.probC and coin < 1):
            return "D"
                
    def traverse(self):
        print(self.genotype)
    
    @classmethod
    def howmany(cls):
        print ("currently {:d} genes".format(cls.population))
        
        
