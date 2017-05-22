'''
Created on 01/07/2015

@author: Mollinetti
'''
import random, Gene, Parameters, GA, sys

if __name__ == "__main__":

    try:
        argfile = str(sys.argv[1])
        #init parameters by reading the txt
        p = Parameters.Params(argfile)
        #init mersenne twister seed
        random.seed(None,2)
        for i in range(0,int(sys.argv[2])):
            ga = GA.GA(str(i),p)
            
            ga.run()
    except IndexError:
        print("\nRight usage: python3 GA.py [Name of the function] [number of executions]\n")
    
    #g = []
   
    
    #for i in range(0, p.popNum):
        #g.append(Gene.Gene(lb, ub, 3))
        #ga.population[i].traverse()
        #ga.evaluate(ga.population[i])
        #print(ga.population[i].fitness)


    #print("\n\n SELECTION \n \n \n")
    #ga.selection()
    #for i in range(0, len(ga.tnPool)):
        #ga.tnPool[i].traverse()
        #print(ga.tnPool[i].fitness)

    #print("\n\nCROSSOVER\n\n\n")
    #ga.crossover()
    #for i in range(0, len(ga.tnPool)):
        #ga.tnPool[i].traverse()
        #print(i, ':', ga.tnPool[i].fitness)

    #print("\n\nUPDATES\n\n\n")
    #ga.update()
    #for i in range(0, p.popNum):
        #ga.population[i].traverse()
        #print(ga.population[i].fitness)

    #print("\n\nMUTATION\n\n\n")
    #ga.mutation()

    #print("\n\nFINAL POPULATION\n\n\n")
    #for i in range(0, p.popNum):
        #g.append(Gene.Gene(lb, ub, 3))
        #ga.population[i].traverse()
        #print(ga.population[i].fitness)

    #print("\n\nBEST:\n\n", ga.findBest().fitness)

    