import random
import sys
import copy
class Game:
	"Tic-tac-toe : a two player game"
	def __init__(self):
		self.board = [''] * 9
		self.player1 = ['']
		self.player2 = ['']
		self.player1_marker = ['']
		self.player2_marker = ['']
		self.winningcombos = (
		[6, 7, 8], [3, 4, 5], [0, 1, 2], [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6],
		)
		self.corners = [0, 2, 8, 6]
		self.sides = [1, 3, 5, 7]
		self.middle = [4]
		self.form = '''
		\t| %s | %s | %s |
		\t| %s | %s | %s |
		\t| %s | %s | %s |
		'''
	def print_board(self, board = None):
		"Display board on the screen"
		if board is None:
			print self.form % tuple(self.board[6:9] + self.board[3:6] + self.board[0:3])
		else:
			print self.form % tuple(self.board[6:9] + self.board[3:6] + self.board[0:3])
	def get_marker(self):
		marker = raw_input("What do you want to be as your marker in X or O").upper()
		while marker not in ["X","O"]:
			marker = raw_input("What do you want to be as your marker in X or O").upper()
		if maker == "X":
			return ('X', 'O')
		else:
			return ('O', 'X')
	def help(self):
		print '''
		\n\tThis is a Two player game 3X3 board game.
		\n\Play it with your best.
		'''
	def quit_game(self):
		"Exit the game"
		self.print_board
		print "\n\tThanks for playing.\n\tIts my pleasure you played this game"
		sys.exit()
	def is_winner(self, board, marker):
		for combo in self.winningcombos:
			if(board[combo[0]] == board[combo[1]] == board[combo[2]] == marker):
				return True
			else:
				return False
	
	def is_space_free (self, board, index):
		return board[index] == ' '
	
	def is_board_full(self):
		for i in range(1, 9):
			if is_space_free(self.board, i):
				return False
			else:
				return True
	def get_player1_name(self):
		return raw_input("Whats is player 1 name?")

	def get_player2_name(self):
		return raw_input("Whats is player 2 name?")

	def get_player1_move(self):
		move = int(input(" Pick a spot to move : (1-9) "))
		while move not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not sel.is_space_free(self.board, move-1):
			move = int(input(" Pick a spot to move : (1-9) "))
		return move - 1

	def get_player2_move(self):
		move = int(input(" Pick a spot to move : (1-9) "))
		while move not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not sel.is_space_free(self.board, move-1):
			move = int(input(" Pick a spot to move : (1-9) "))
		return move - 1

	def make_move(self,board,index,move):
		board[index] = move
	
	def start_game(self):
		self.print_board(range(1,10))
		self.help()
		self.player1 = self.get_player1_name
		self.player1_marker , self.player2_marker = self.get_marker
		if random.randint(0, 1) == 0:
			print "%s will go first"%player1
			self.enter_game_loop('1')
		else:
			print "%s will go first"%player2
			self.enter_game_loop('2')

	def enter_game_loop(self, turn):
		is_running = True
		player = turn
		while is_running:
			if player == 1:
				player1_input = self.get_player1_move()
				self.make_move(self.board, player1_input, self.player1_marker)
				if(is_winner(self.board, player1_marker)):
					self.print_board
					print "\n\tCONGRATULATIONS %s, YOU HAVE WON THE GAME!!! \\tn" % self.player1
					is_running = False
				else:
					if self.is_board_full():
	                      self.print_board()
	                      print "\n\t-- Match Draw --\t\n"
	                      is_running = False
	                       #break
                   else:
	                      self.print_board()
	                      player = '2'
						
            else:
            	player2_input = self.get_player2_move()
				self.make_move(self.board, player2_input, self.player2_marker)
				if(is_winner(self.board, player2_marker)):
					self.print_board
					print "\n\tCONGRATULATIONS %s, YOU HAVE WON THE GAME!!! \\tn" % self.player2
					is_running = False
				else:
					if is_board_full():
						self.print_board()
						print "\n\t-- Match Draw --\t\n"
                       	is_running = False
                    else:
                    	self.print_board()
                    	player = 2
        self.end_game()
    

    def end_game(self):
    	play_again = raw_input("would you like to play again y/n: ").lower()
    	if play_again == 'y':
    		self.__init__()
    		self.start_game()
    	else:
    		print "\n\t-- GAME OVER!!!--\n\t"
           	self.quit_game()


if __name__ == "__main__":   
     TicTacToe = Game()
TicTacToe.start_game()
    	


			



