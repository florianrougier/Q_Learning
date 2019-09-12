#A Better Maze: Q-Learning - Training file

#Importing the libraries
import numpy as np
from environment import Environment

#Defining the parameters
gamma = 0.9 # Discount factor
alpha = 0.75 # Learning rate
nEpochs = 10000 # number of time we perform the q learning process

#Environment and Q-Table initialization
env = Environment()
rewards = env.rewardBoard
QTable = rewards.copy() # We can see the QTable in the variable explorer

#Preparing the Q-Learning process 1
possibleStates = list()
for i in range(rewards.shape[0]):
    if sum(abs(rewards[i])) != 0:
        possibleStates.append(i)
    
#Preparing the Q-Learning process 2
def maximum(qvalues):
    inx = 0
    maxQValue = -np.inf
    for i in range(len(qvalues)):
        if qvalues[i] > maxQValue and qvalues[i] != 0:
            maxQValue = qvalues[i]
            inx = i
            
    return inx, maxQValue

#Starting the Q Learning Process
for epoch in range(nEpochs):
    print('\rEpochs: ' + str(epoch + 1), end = '')
    
    startingPos = np.random.choice(possibleStates)
    
    #Getting all the playable actions
    possibleActions = list()
    for i in range(rewards.shape[1]):
        if rewards[startingPos][i] != 0:
            possibleActions.append(i)
            
    #Playing a random action
    action = np.random.choice(possibleActions)
    
    reward = rewards[startingPos][action]
    
    #Updating the Q-value
    _, maxQValue = maximum(QTable[action])
    
    TD = reward + gamma * maxQValue - QTable[startingPos][action]
   
    QTable[startingPos][action] = QTable[startingPos][action] + alpha * TD
    
#Displaying the results
currentPos = env.startingPos
while True:
    action, _ = maximum(QTable[currentPos])
    
    env.movePlayer(action)
    
    currentPos = action
    
    