from math import *
import numpy as np
from operator import itemgetter, attrgetter                                                           

class NumberClass:
    def __init__(self):
        #Turn into dictionary of the form (word category, list of words within that category
        self.Feature = []
        self.weightVector = []
        self.count = 0
        for i in range(784):
            self.Feature.append(0)
            self.weightVector.append(1)
    
    def updateWeightVector(self, adder, positiony, positionx):
        temp = self.weightVector[positionx+positiony*28]
        self.weightVector[positionx+positiony*28] = temp*adder+temp
    
    def addToCount(self, adder):
        self.count += adder
        
    def getWeightVector(self, positiony, positionx):
        return self.weightVector[positionx+positiony*28]