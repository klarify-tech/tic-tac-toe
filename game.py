# creating the simplest implementation of tic-tac-toe for beginners
#It will store Game board
#It will run the game
import random
import functools

class Board:
    board_list =[]
    game_state = True
    value= " "
    def __init__(self,value):
        for x in range(9):
            self.board_list.append(value)
            

    def setBoard(self,index,value):
        self.board_list[index] = value

    def drawBoard(self):
        count=0
        while(count < 9):
            print(f" {self.board_list[count]} |",end="")
            count +=1
            if(count%3 == 0):
                print("")

                       
def start_game():
    newBoard = Board(" ")
    available_places = [0,1,2,3,4,5,6,7,8]
    game_state = True

    while len(available_places)>0 and game_state == True:
        computer_choice = random.choice(available_places)
        newBoard.setBoard(computer_choice,"O")
        available_places.remove(computer_choice)
        print("")
        newBoard.drawBoard()
        game_state = evaluate_board(newBoard.board_list)
        
        if (game_state == True and len(available_places)>0 ):
            player_choice = int(input(f"Input your position "))
            newBoard.setBoard(player_choice,"X")
            print("")
            newBoard.drawBoard()
            available_places.remove(player_choice)
            game_state = evaluate_board(newBoard.board_list)
            
            

    print("Game Over")


def evaluate_board(board):
    if(board[0] == board[1] and board[0] != " "):
        if(board[1]== board[2]):
            print(f"Game over {board[2]} wins")
            return False

    if(board[0] == board[3]and board[0] != " "):
        if(board[3]== board[6]):
            print(f"Game over {board[6]} wins")
            return False
    
    if(board[0] == board[4]and board[0] != " "):
        if(board[4]== board[8]):
            print(f"Game over {board[8]} wins")
            return False

    if(board[1] == board[4]and board[1] != " "):
        if(board[4]== board[7]):
            print(f"Game over {board[7]} wins")
            return False
    
    if(board[2] == board[5]and board[2] != " "):
        if(board[5]== board[8]):
            print(f"Game over {board[8]} wins")
            return False
    
    if(board[2] == board[4]and board[2] != " "):
        if(board[4]== board[6]):
            print(f"Game over {board[6]} wins")
            return False
    
    if(board[3] == board[4]and board[3] != " "):
        if(board[4]== board[5]):
            print(f"Game over {board[5]} wins")
            return False
    
    if(board[6] == board[7]and board[6] != " "):
        if(board[7]== board[8]):
            print(f"Game over {board[8]} wins")
            return False

    return True
    # 0 1 2 | 0 3 6 | 0 4 8
    # 1 4 7 | 2 5 8 | 3 4 5
    # 6 7 8 | 2 4 6
   


        
start_game()


