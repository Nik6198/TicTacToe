class TicTacToe:
    def __init__(self, board, sign):
        self.board = board
        self.player = sign
        self.minmaxarg = [0, 999 ]

    def printBoard(self):
        for i in range(3):
            for j in range(3):    
                print(self.board[i*3 + j],end=' ')
            print()
        print()

    def countInARow(self, start, end, inc, sign, count):
        localCount = 0
        possibleMove = -1
        for i in range(start,end,inc):
            if self.board[i] == sign:
                localCount += 1
            else:
                possibleMove = i
        if localCount == 3 and localCount == count:
            return 10
        if localCount == count and self.board[possibleMove] == '-':
            
            return possibleMove
        else:
            return -1
    
    def getOpponent(self):
        if self.player == 'x':
            return 'o'
        else:
            return 'x'
        
    def possibleWin(self,sign,count):
        ret = self.countInARow(0,3,1,sign,count)
        if ret != -1:
            return ret  
        ret = self.countInARow(3,6,1,sign,count)
        if ret != -1:
            return ret  
        ret = self.countInARow(6,9,1,sign,count)
        if ret != -1:
            return ret
        ret = self.countInARow(0,7,3,sign,count)
        if ret != -1:
            return ret
        ret = self.countInARow(1,8,3,sign,count)
        if ret != -1:
            return ret
        ret = self.countInARow(2,9,3,sign,count)
        if ret != -1:
            return ret
        ret = self.countInARow(0,9,4,sign,count)
        if ret != -1:
            return ret
        ret = self.countInARow(2,7,2,sign,count)
        if ret != -1:
            return ret
        else:
            return -1
    
    def findScore(self,flag,pos = None):
        
        score = 0
        if(not flag):
            self.player = self.getOpponent()
        sign = self.getOpponent()
        count = 2
        i = 10
        if pos != None:
            self.board[pos] = self.getOpponent()
        for i in [1,10]:
            ret = self.countInARow(0,3,1,sign,count)
            if ret != -1:
                score += i 
            ret = self.countInARow(3,6,1,sign,count)
            if ret != -1:
                score += i 
            ret = self.countInARow(6,9,1,sign,count)
            if ret != -1:
                score += i 
            ret = self.countInARow(0,7,3,sign,count)
            if ret != -1:
                score += i
            ret = self.countInARow(1,8,3,sign,count)
            if ret != -1:
                score += i 
            ret = self.countInARow(2,9,3,sign,count)
            if ret != -1:
                score += i 
            ret = self.countInARow(0,9,4,sign,count)
            if ret != -1:
                score += i 
            ret = self.countInARow(2,7,2,sign,count)
            if ret != -1:
                score += i 
            sign = self.player
            if pos != None:
                self.board[pos] = self.player
        if(not flag):
            self.player = self.getOpponent()
        return score
    

   

   
    def minMax(self,flag,depth):
        
        for pos in range(9):
            if self.board[pos] == '-':
                       
                #max player
                if maxTrue :
                    self.board[pos] = self.player
                    ret = self.possibleWin(self.player,3)
     
                    if(ret == 10):
                        self.minmaxarg[1] = 100
                        self.minmaxarg[0] = pos
                        self.board[pos]='-'
                        return

                    #maximizing the score
                    if depth == 1:
                        score = self.findScore(True)
                        if pos == 4 :
                            score += 4
                        if(self.minmaxarg[1] < score):
                            self.minmaxarg[1] = score
                            self.minmaxarg[0] = pos
                    else:
                        self.minMax(not maxTrue, depth -1 )
                #min player        
                else:
                    self.board[pos] = self.getOpponent()
                    ret = self.possibleWin(self.getOpponent(),3)

                    if(ret == 10 ):
                        self.minmaxarg[1] = -100
                        self.minmaxarg[0] = pos
                        self.board[pos]='-'
                        return
                    #minimizing the score
                    if depth == 1 :
                        score = -self.findScore(False) 
                        if pos == 4 :
                            score += -4   
                        if(self.minmaxarg[1] > score):
                            self.minmaxarg[1] = score
                            self.minmaxarg[0] = pos
                    else:
                        self.minMax(not maxTrue, depth -1 )

                self.board[pos] = '-'

        
def getInput():
    board = []
    for i in range(3):
        row = input().split(' ')
        board.extend(row)
    return board

sign = input()
print(sign)
game = TicTacToe(getInput(),sign)
game.printBoard()
game.minMax( True ,2)
game.board[game.minmaxarg[0]] = game.player
game.printBoard()