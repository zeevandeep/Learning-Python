import random
import math
class Roll:
        def __init__(self):
                self.allRolls = []
                self.nRolls = 100
                self.num = 0

        def rollDie(self,number):
                self.num = number
                for i in range(self.nRolls):
                        sum = 0
                        tempRoll = []
                        while sum < self.num:
                                tmp = random.randint(1,6)
                                tempRoll.append(tmp)
                                sum = sum + tmp
                        self.allRolls.append(tempRoll)
        
        def mean(self):
                nsum = 0
                for i in range(self.nRolls):
                        nsum = nsum + sum(self.allRolls[i])
                return (nsum/self.nRolls)

        def std(self,mean):
                st_dev = 0
                for i in range(self.nRolls):
                        st_dev = st_dev + (sum(self.allRolls[i])-mean)*(sum(self.allRolls[i])-mean)
                return math.sqrt(st_dev/self.nRolls)

        def numTrialMean(self):
                tmean = 0
                for i in range(self.nRolls):
                        tmean = tmean + len(self.allRolls[i])
                return (tmean/self.nRolls)
        
        def numTrialStd(self,mean):
                st_dev = 0
                for i in range(self.nRolls):
                        st_dev = st_dev + (len(self.allRolls[i])-mean)*(len(self.allRolls[i])-mean)
                return math.sqrt(st_dev/self.nRolls)

# Define object
c=Roll()

# Rolling the dice for M=20
c.rollDie(20)
print "M = 20"
print "Mean - M = " + str((c.mean() - c.num))
print "Standard Deviation - M = " + str((c.std(c.mean()) - c.num))
print ""

# Rolling the dice for M=10000
c.rollDie(10000)
print "M = 10000"
print "Mean - M = " + str((c.mean() - c.num))
print "Standard Deviation - M = " + str((c.std(c.mean()) - c.num))
print ""

# Rolling the dice for M=20 - number of Trials
c.rollDie(20)
print "M = 20"
print "Mean of number of Rolls = " + str((c.numTrialMean()))
print "Standard Deviation of Number of Rolls = " + str((c.numTrialStd(c.numTrialMean())))
print ""

# Rolling the dice for M=10000 - number of Trials
c.rollDie(10000)
print "M = 10000"
print "Mean of number of Rolls = " + str((c.numTrialMean()))
print "Standard Deviation of Number of Rolls =" + str((c.numTrialStd(c.numTrialMean())))
print ""
