from math import *
import numpy as np
from operator import itemgetter, attrgetter                                                           

class NumberClass:
    def __init__(self):
        #Turn into dictionary of the form (word category, list of words within that category
        self.Feature = []
        self.weightVector = []
        self.count = 0
        self.changed  = 0
        for i in range(784):
            self.Feature.append(0)
            self.weightVector.append(0.5)
    
    def addToFeature(self, adder, positionx, positiony):
        self.Feature[positionx+28*positiony] += adder
    def updateWeightVector(self, adder, positiony, positionx):
        temp = self.Feature[positionx+positiony*28]
        self.weightVector[positionx+positiony*28] += temp*adder 
    
    def addToCount(self, adder):
        self.count += adder
        
    def getWeights(self):
        return self.weightVector
    
    def getFeature(self):
        return self.Feature
    
    def getWeightVector(self, positiony, positionx):
        return self.weightVector[positionx+positiony*28]
    
    def getStatus(self):
        return self.changed
    
    def changeStatus(self):
        self.changed = 1