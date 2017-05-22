'''
Created on 01/07/2015

@author: Mollinetti
'''
import math

def fitnessFunc(function, arg):
    result = function(arg)
    return result


def GoldsteinPrice(x):
    result =  ( 1 + math.pow( x[0] + x[1] + 1, 2 ) * ( 19 - 14 * x[0] + 3 * math.pow( x[0], 2 ) - 14 * x[1] + 6 * x[0] * x[1] + 3 * pow( x[1], 2 ) ) )* ( 30 + math.pow( 2 * x[0] - 3 * x[1], 2 ) *( 18 - 32 * x[0] + 12 * math.pow( x[0], 2 ) + 48 * x[1] - 36 * x[0] * x[1] + 27 * pow( x[1], 2 ) ) )
    violations = 0
    return result, violations


#-----------------------------------------------------MWTCS-------------------------------------------------------------------------------------------------


def MWTCScalculateG1(x):
    return float(1 - ((pow(x[1], 3) * x[2]) / (7178 * pow(x[0], 4))))



def MWTCScalculateG2(x):
    return float(((4 * x[1] * x[1] - x[0] * x[1]) / (12566 * pow(x[0], 3) * x[1] - pow(x[0], 4))) + (1 / (5108.0 * x[0] * x[0])) - 1)


def MWTCScalculateG3(x):
    return float(1 - 140.45 * x[0] / (x[2] * x[1] * x[1]))


def MWTCScalculateG4(x):
    return float((x[0] + x[1]) / 1.5 - 1)
  


def MWTCScalculateFitness(x):
    return float((x[2] + 2.0) * x[1] * pow(x[0],2.0))




def MWTCS(x):

    violations = 0

    restrictions = list(range(4))

    restrictions[0] = MWTCScalculateG1(x)

    if restrictions[0] > 0:
        violations+=1
    

    restrictions[1] = MWTCScalculateG2(x)

    if restrictions[1] > 0:
        violations+=1
    

    restrictions[2] = MWTCScalculateG3(x)

    if restrictions[2] > 0:
        violations+=1
    

    restrictions[3] = MWTCScalculateG4(x)

    if restrictions[3] > 0:
        violations+=1
    

    fitness = MWTCScalculateFitness(x)
    
    return fitness, violations, restrictions


#------------------------------------------------------------------------------WBD-----------------------------------------------------------------------------------------




def WBDcalculateTauDois(pos):
    return (6000.0 / (math.sqrt(2.0) * pos[0] * pos[1]))
    

def WBDcalculateTauTres( pos, r, j):
    
    M1 = float(14) + (pos[0]/2)
    return (float(M1) * r) / j
    

def WBDcalculateJ(pos):
    
    return (2.0 * (math.sqrt(2.0) * pos[0] * pos[1] * ((pow(pos[2],2.0) / 12) + (pow(((pos[0]+pos[2]) / 2), 2.0)))))
    

def WBDcalculateR(pos):
    
    return (math.sqrt((pow(pos[2],2.0) / 4.0) + pow(((pos[0]+pos[2]) / 2), 2.0)))
    

def WBDcalculateSigma( pos):
    
    return (float) ((6.0 * 6000.0 * 14) / (pos[3] * pow(pos[2],2.0)))
    

def WBDcalculateDelta( pos):
    
    return (float) ((4.0 * 6000.0 * pow(14, 3)) / ((30 * pow(10,6)) * pos[3] * pow(pos[2], 3)))
    

def WBDcalculatePC( pos):
    
    return (float)(((4.013 * (30 * pow(10,6)) * math.sqrt((pos[2] * pos[2] * pow(pos[3], 6)) / 36)) / 196) * (1 - (pos[2] * math.sqrt((30 * pow(10,6)) / (4 * (12 * pow(10,6))))) / 28))


def WBDcalculateTauUm( pos):
    
    j = WBDcalculateJ(pos)
    r = WBDcalculateR(pos)

    t2 = WBDcalculateTauDois(pos)
    t3 = WBDcalculateTauTres(pos,r,j)

    return  float(math.sqrt(pow(t2,2.0) + 2 * t2 * t3 * (1 / 2.0 * r) + pow(t3,2.0)))
    

def WBDcalculateG1(t1):
    
    return (t1 - float(13600.0))
    

def WBDcalculateG2(sigma):
    
    return float (sigma - 30000)
    

def WBDcalculateG3(pos):
    
    return float(pos[0] - pos[3])
    

def WBDcalculateG4(pos):
    
    return float(((0.10471 * pow(pos[0],2.0)) + (0.04811 * pos[2] * pos[3] * (14.0 + pos[1]))) - 5.0)
    

def WBDcalculateG5(pos):
    
    return (0.125 - pos[0])
    

def WBDcalculateG6(delta):
    
    return delta - float(0.25)

def WBDcalculateG7(pc):
    
    return float(6000 - pc)
    

def WBDcalculateFitness(pos):
    
    return float((1.10471 * pow(pos[0],2.0) * pos[1]) + (0.04811 *  pos[2] * pos[3] * (14.0 + pos[1])))
    

def WBD(pos):
    
    violations = 0                         
    sigma = WBDcalculateSigma(pos)
    delta = WBDcalculateDelta(pos)
    pc    = WBDcalculatePC(pos)

    t1 = WBDcalculateTauUm(pos)

    restrictions = list(range(7))
        
        
    restrictions[0] = WBDcalculateG1(t1)

    if restrictions[0] > 0:
        
        violations+=1
        

    restrictions[1]   = WBDcalculateG2(sigma)

    if restrictions[1] > 0:
        
        violations+=1
        

    restrictions[2]   = WBDcalculateG3(pos)

    if restrictions[2] > 0:
        
        violations+=1
        

    restrictions[3] = WBDcalculateG4(pos)

    if restrictions[3] > 0:
        
        violations+=1
        

    restrictions[4]  = WBDcalculateG5(pos)

    if restrictions[4] > 0:
        
        violations+=1
        

    restrictions[5]   = WBDcalculateG6(delta)

    if restrictions[5] > 0:
        
        violations+=1
        

    restrictions[6]   = WBDcalculateG7(pc)

    if restrictions[6] > 0:
        
        violations+=1
        

    fitness = WBDcalculateFitness(pos)
        
    return fitness, violations, restrictions






#-----------------------------------------------------------------------------DPV-------------------------------------------------------------------

def DPVcalculateG1(pos):

    return float (-pos[0]+ (0.0193 * pos[2]))



def DPVcalculateG2(pos):

    return float (-pos[1]+ (0.00954 * pos[2]))


def DPVcalculateG3(pos):

    return float (-(3.141592 * pow(pos[2], 2.0) * pos[3]) - ((4.0 / 3.0) * 3.141592 * pow(pos[2], 3.0)) + 1296000)


def DPVcalculateG4(pos):

    return float (pos[3] - 240.0)


def DPVcalculateFitness(pos):

    return float (0.6224 * pos[0]* pos[2] * pos[3] + 1.7781 * pos[1]*pos[2] * pos[2] + 3.1661 * pos[0]* pos[0]* pos[3] + 19.84 * pos[0]* pos[0]* pos[2])


def DPV(pos):

    violations = 0

    restrictions = list(range(4))

    restrictions[0]     = DPVcalculateG1(pos)

    if(restrictions[0] > 0):
        
        violations+=1
    

    restrictions[1]   = DPVcalculateG2(pos)

    if(restrictions[1] > 0):
    
               
        violations+=1
    

    restrictions[2]   = DPVcalculateG3(pos)

    if(restrictions[2] > 0):
    
               
        violations+=1
    

    restrictions[3] = DPVcalculateG4(pos)

    if(restrictions[3] > 0):
    
            
        violations+=1
    

    fitness = DPVcalculateFitness(pos)
    
    return fitness, violations, restrictions


#-------------------------------------------------------------------------------------SRD11----------------------------------------------------------------------------------------------------


def SRDcalculateG1(pos):

    return float ((27 / (pos[0]* pos[1] * pos[1] * pos[2])) - 1)


def SRDcalculateG2(pos):

    return float ((397.5 / (pos[0] * pos[1] * pos[1] * pos[2] * pos[2])) - 1)


def SRDcalculateG3(pos):

    return float ((1.93 * (pos[3] * pos[3] * pos[3]) / (pos[1] * pos[2] * pow(pos[5], 4))) - 1)


def SRDcalculateG4(pos):

    return float (((1.93 * pow(pos[4], 3)) / (pos[1] * pos[2] * pow(pos[6], 4))) - 1)


def SRDcalculateG5(pos):

    return float ((1 / 110 * (pos[5] * pos[5] * pos[5])) * (math.sqrt((750.0 * pos[3] / pos[1] * pos[2]) * (750.0 * pos[3] / pos[1] * pos[2]) + 16900000)) - 1)
   
def SRDcalculateG6(pos):

    return float (((math.sqrt((((745.0 * pos[4]) / (pos[1] * pos[2])) * ((745.0 * pos[4]) / (pos[1] * pos[2])) + 157.5 * 1000000))) / (85.0 * pos[6] * pos[6] * pos[6])) - 1)


def SRDcalculateG7(pos):

    return float ((pos[1] * pos[2] / 40) - 1)


def SRDcalculateG8(pos):

    return float ((5 * pos[1] / pos[0]) - 1)


def SRDcalculateG9(pos):


    return float ((pos[0]/ 12 * pos[1]) - 1)


def SRDcalculateG10(pos):

    return float (((1.5 * pos[5] + 1.9) / pos[3]) - 1)


def SRDcalculateG11(pos):

    return float (((1.1 * pos[6] + 1.9) / pos[4]) - 1)


def SRDcalculateFitness(pos):
 
    return float (0.7854 * pos[0]* pos[1] * pos[1] * (3.3333 * pos[2] * pos[2] + 14.9334 * pos[2] - 43.0934)) - 1.508 * pos[0]* (pos[5] * pos[5] + pos[6] * pos[6]) + 7.4777 * (pos[5] * pos[5] * pos[5] + pos[6] * pos[6] * pos[6]) + 0.78054 * (pos[3] * pos[5] * pos[5] + pos[4] * pos[6] * pos[6])


def SRD11(pos):

    violations = 0

    restrictions = list(range(11))  

    restrictions[0]     = SRDcalculateG1(pos)
    
    if(restrictions[0] > 0):
    
        violations+=1
    
    
    restrictions[1]   = SRDcalculateG2(pos)

    if(restrictions[1] > 0):
    
        violations+=1
    
    
    restrictions[2]   = SRDcalculateG3(pos)

    if(restrictions[2] > 0):
    
        violations+=1
    
    
    restrictions[3] = SRDcalculateG4(pos)

    if(restrictions[3] > 0):
    
        violations+=1
    
    
    restrictions[4]  = SRDcalculateG5(pos)

    if(restrictions[4] > 0):
    
        violations+=1
    
    
    restrictions[5]   = SRDcalculateG6(pos)

    if(restrictions[5] > 0):
    
        violations+=1
     
        
    restrictions[6]   = SRDcalculateG7(pos)

    if(restrictions[6] > 0):
    
        violations+=1
    
    
    restrictions[7]   = SRDcalculateG8(pos)

    if(restrictions[7] > 0):
    
        violations+=1
    
    
    restrictions[8]  = SRDcalculateG9(pos)

    if(restrictions[8] > 0):
    
        violations+=1
    
    
    restrictions[9]  = SRDcalculateG10(pos)

    if(restrictions[9] > 0):
    
        violations+=1
   
    restrictions[10]  = SRDcalculateG11(pos)

    if(restrictions[10] > 0):
    
        violations+=1
    
    fitness = SRDcalculateFitness(pos)
    return fitness, violations, restrictions
