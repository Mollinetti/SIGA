
import Gene, Parameters, random, math

#GAME ENGINE, SHOULD HAVE BEEN CALLED LIKE THIS, BUT OH WELL...
class GameEngine:

	#game parameters, the letters represents the utility function received by playing:
	#
	#	R: reward
	#	T: temptation
	#	P: punishment
	#	S: sucker
	#
	def __init__(self, param = Parameters):
		#discount factor
		self.beta = 0.9
		self.param = param
		#starting payment matrix (original Dillema)
		self.R = 3
		self.T = 5
		self.S = 1
		self.P = 0
		#maximum payoff
		self.maximum_payoff = (self.param.numRounds)* max(self.R, self.T, self.P, self.S)

	#change game behavior according to chosen number (I used a number notation in order to leave an easier implementation for stochastic games)
	def change(self, type):

		#Prisoner's Dillema
		if type == 1:
			self.R = 3
			self.T = 5
			self.S = 1
			self.P = 0
		#Stag Hunt
		elif type == 2:
			self.R = 5
			self.T = 3
			self.S = 1
			self.P = 0
		#Hawk Dove
		elif type == 3:
			self.R = 3
			self.T = 5
			self.S = 0
			self.P = 1
		#Harmonic Games
		elif type == 4:
			self.R = 5
			self.T = 3
			self.S = 0
			self.P = 1
		#update payoff
		self.maximum_payoff = (self.param.numRounds)* max(self.R, self.T, self.P, self.S)
	#standard game without any sthocasticity
	def socialGame(self, bestval, p1 = Gene, p2 = Gene):
		for k in range(0,self.param.numRounds):
			p1move = p1.play()
			p2move = p2.play()
			#model all possible moves (both C, both D, one D and one C)
			#both cooperate
			if(p1move == "C" and p2move == "C"):
				p1.socialFitness+= math.pow(self.beta,k+1) * self.R
				p2.socialFitness+= math.pow(self.beta,k+1) * self.R
			#player1 cooperate and player 2 defect
			elif(p1move == "C" and p2move == "D"):
				p1.socialFitness+= math.pow(self.beta,k+1) * self.S
				p2.socialFitness+= math.pow(self.beta,k+1) * self.T
			#player 1 defect and player 2 cooperate
			elif(p1move == "D" and p2move == "C"):
				p1.socialFitness+= math.pow(self.beta,k+1) * self.T
				p2.socialFitness+= math.pow(self.beta,k+1) * self.S
			#both defect
			elif(p1move == "D" and p2move == "D"):
				p1.socialFitness+= math.pow(self.beta,k+1) * self.P
				p2.socialFitness+= math.pow(self.beta,k+1) * self.P

		#calculate normalized fitness
		p1normfit = (p1.socialFitness / self.maximum_payoff) * bestval
		p2normfit = (p2.socialFitness / self.maximum_payoff) * bestval

		#return fitnesses as a list
		return p1normfit, p2normfit

               
     #whole social interaction process
	def socialInteraction(self, bestval, population):
    	
    	#initilize random list
		index = list(range(0, (int(self.param.popNum) - 1)))

		random.shuffle(index)

		for i in range(0, int(self.param.popNum)-2, 2):

			population[index[i]].socialFitness, population[index[i+1]].socialFitness =self.socialGame(bestval, population[index[i]], population[index[i+1]])
    	
