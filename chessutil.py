#  we need a couple of classes to hold the values in the game
#
#  We need a state variable for each board
#       The variable is keyed by the current state
#       In this variable, we show the possible next states for a black move
#       We show the possible next states for a white move
#       We show the value of each next move, where known
#       
#       Values can be +1 (or other positive numbers) for a guaranteed white win
#                   -1 (or other negative numbers) for a guaranteed black win
#                   0 for a draw or better
#                   None for unknown
#
'''
class State():
    def __init__(self,currentBoard):
        self.currentBoard=currentBoard
        
    def addBlackState(self,nextBlackState,nextStateValue):
        self.nextBlackState.append((nextBlackState,nextStateValue))
        
    def addWhiteState(self,nextWhiteState,nextStateValue):
        self.nextWhiteState.append((nextWhiteState,nextStateValue))

'''

class QueueFrontier():
    def __init__(self):
        self.frontier=[]
        
    def empty(self):
        return len(self.frontier)==0
    
    def add(self,fromTo):
        self.frontier.append(fromTo)
        
    def remove(self):
        if self.empty():
            return None
        else:
            retVal=self.frontier[0]
            self.frontier=self.frontier[1:]
            return retVal
        

        