# solutions.py
# ------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

'''Implement the methods from the classes in inference.py here'''

import util
from util import raiseNotDefined
import random
import busters
import inference as inf

def normalize(self):
    """
    Normalize the distribution such that the total value of all keys sums
    to 1. The ratio of values for all keys will remain the same. In the case
    where the total value of the distribution is 0, do nothing.

    >>> dist = DiscreteDistribution()
    >>> dist['a'] = 1
    >>> dist['b'] = 2
    >>> dist['c'] = 2
    >>> dist['d'] = 0
    >>> dist.normalize()
    >>> list(sorted(dist.items()))
    [('a', 0.2), ('b', 0.4), ('c', 0.4), ('d', 0.0)]
    >>> dist['e'] = 4
    >>> list(sorted(dist.items()))
    [('a', 0.2), ('b', 0.4), ('c', 0.4), ('d', 0.0), ('e', 4)]
    >>> empty = DiscreteDistribution()
    >>> empty.normalize()
    >>> empty
    {}
    """
    total = self.total()
    for key, value in self.items():
        if total != 0:
                self[key] = value/total


def sample(self):
    """
    Draw a random sample from the distribution and return the key, weighted
    by the values associated with each key.

    >>> dist = DiscreteDistribution()
    >>> dist['a'] = 1
    >>> dist['b'] = 2
    >>> dist['c'] = 2
    >>> dist['d'] = 0
    >>> N = 100000.0
    >>> samples = [dist.sample() for _ in range(int(N))]
    >>> round(samples.count('a') * 1.0/N, 1)  # proportion of 'a'
    0.2
    >>> round(samples.count('b') * 1.0/N, 1)
    0.4
    >>> round(samples.count('c') * 1.0/N, 1)
    0.4
    >>> round(samples.count('d') * 1.0/N, 1)
    0.0
    """
    #getting random value
    randomValue = random.random()

    #normalizing the distribution
    normalize(self)

    totalProb=0

    for key, value in self.items():
        prob = totalProb+value #get probability
        if prob > randomValue: #if probability is greater than our random value
            return key #return key of that value


def getObservationProb(self, noisyDistance, pacmanPosition, ghostPosition, jailPosition):
    """
    Return the probability P(noisyDistance | pacmanPosition, ghostPosition).
    """
    #special cases
    if ghostPosition == jailPosition and noisyDistance != None:
        return 0
    if ghostPosition == jailPosition and noisyDistance == None:
        return 1
    if noisyDistance == None:
        return 0

    #calculating true distance.
    distance = util.manhattanDistance(pacmanPosition, ghostPosition)

    #returning P(noisyDistance | trueDistance)
    return busters.getObservationProbability(noisyDistance, distance)



def observeUpdate(self, observation, gameState):
    """
    Update beliefs based on the distance observation and Pacman's position.

    The observation is the noisy Manhattan distance to the ghost you are
    tracking.

    self.allPositions is a list of the possible ghost positions, including
    the jail position. You should only consider positions that are in
    self.allPositions.

    The update model is not entirely stationary: it may depend on Pacman's
    current position. However, this is not a problem, as Pacman's current
    position is known.
    """
    #getting initial locations
    currPacLoc = gameState.getPacmanPosition()
    jailLoc = self.getJailPosition()

    #iterating through the list of all possible positions
    for element in self.allPositions:

        #using getobservation prob to calculate P(noisyDistance | pacmanPosition, ghostPosition)
        #then multiplying it with the current belief to update our self.beliefs.
        self.beliefs[element] = self.beliefs[element] * \
        self.getObservationProb(observation, currPacLoc, element, jailLoc)

    self.beliefs.normalize()


def elapseTime(self, gameState):
    """
    Predict beliefs in response to a time step passing from the current
    state.

    The transition model is not entirely stationary: it may depend on
    Pacman's current position. However, this is not a problem, as Pacman's
    current position is known.
    """
    pacPos = gameState.getPacmanPosition()

    #creating a discrete dist object
    distObj = inf.DiscreteDistribution()

    #iterating through all the positions
    for position in self.allPositions:
        #getting the distribution for the current location
        currDistribution = self.getPositionDistribution(gameState, position)

        #using the items in currentdistribution we update beliefs
        for pos, prob in currDistribution.items():

            #beliefs are updated with the new probabilities
            distObj[pos] += self.beliefs[position] * prob

    #changing our current beliefs to the updated beliefs
    self.beliefs = distObj

