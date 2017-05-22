'''
Created on 01/07/2015

@author: Mollinetti
'''

import util

class Params:
    
    def __init__(self, filename):
        with open(filename) as f:
            data = f.read().splitlines()
        self.dim      = int(data[0])
        self.popNum   = int(data[1])  
        self.cRate    = float(data[5])
        self.tn_size  = int(data[6])
        self.mRate    = float(data[7])
        self.hasConst = util.str_to_bool(data[3])
        self.restrictions = int(data[4])
        self.isMin    = util.str_to_bool(data[2])
        self.zeta     = float(data[8])
        self.dirCoeff = float(data[9])
        self.generations  = int(data[len(data)-1])
        line = data[len(data)-4]
        self.lowBound = line.split()
        self.lowBound = list(map(float, self.lowBound))
        line = data[len(data)-3]
        self.uppBound = line.split()
        self.uppBound = list(map(float, self.uppBound))
        self.funcName = data[len(data)-2]


        #GAME RELATED PARAMETERS
        self.allDRate =  float(data[10])
        self.allCRate =  float(data[11])
        self.TFTRate =   float(data[12])
        self.numGames =  int(data[13])
        self.numRounds = int(data[14])
        self.alpha =     float(data[15])
        self.beta =     float(data[16])

# def __init__(self, dimension, population, isMin, hasConstraint, crossoverRate, tn_size, mutationRate, zeta, dirCoeff, minimum, maximum):
 #       self.dim      = dimension
  #      self.popNum   = population 
   #     self.cRate    = crossoverRate
    #    self.tn_size  = tn_size
     #   self.mRate    = mutationRate
      #  self.hasConst = hasConstraint
       # self.isMin    = isMin
        #self.zeta     = zeta
        #self.dirCoeff = dirCoeff
        #self.lowBound = minimum
        #self.uppBound = maximum
      

    def getZeta(self):
        return self.zeta
    
    def getcRate(self):
        return self.cRate
    
    def getmRate(self):
        return self.mRate
    
    def getisMin(self):
        return self.isMin
    
    
    def getdirCoeff(self):
        return self.dirCoeff

