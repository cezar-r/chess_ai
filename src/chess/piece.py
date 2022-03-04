from .constants import *
import pygame


class Piece:

	def __init__(self, row, col, color):
		self.row = row
		self.col = col 
		self.color = color
		self.x = 0  
		self.y = 0 
		self.calc_pos()
		self.moved = False
		# self.img = None

	def calc_pos(self):
		self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
		self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
	

	def move(self, row, col):
		self.row = row
		self.col = col 
		self.calc_pos()
		self.moved = True

	def __str__(self):
		if self.color == WHITE:
			return f'W{self.rank}'
		else:
			return f'B{self.rank}'

	def __repr__(self):
		if self.color == WHITE:
			return f'W{self.rank}'
		else:
			return f'B{self.rank}'

	# def simulate_move(self, board_copy, piece_copy, ):
	# 	board_copy.move()




class Pawn(Piece):

	def __init__(self, row, col, color):
		super().__init__(row, col, color)
		self.rank = 1
		if color == WHITE:
			self.dir = -1
		else:
			self.dir = 1


	def valid_moves(self, board):

		# for row in board:
		# 	for piece in row:
		# 		if piece.rank == 100 and piece.color == self.color:
		# 			if self.checked():
		# 				return 

		valid_moves = {}
		left = self.col - 1 
		right = self.col + 1 
		up = self.row + self.dir

		# straight ahead

		if up < ROWS or up > 0:
			if board[up][self.col] == 0:
				valid_moves[(up, self.col)] = []

		if not self.moved:
			if board[up+self.dir][self.col] == 0 and board[up][self.col] == 0:
				valid_moves[(up+self.dir, self.col)] = []


		# capture up and left
		if left >= 0 and up < ROWS:
			if board[up][left] != 0:
				if board[up][left].color != self.color:
					valid_moves[(up, left)] = [board[up][left]]

		# capture up and right
		if right < COLS and up < ROWS:
			if board[up][right] != 0:
				if board[up][right].color != self.color:
					valid_moves[(up, right)] = [board[up][right]] 

		return valid_moves

	def draw(self, win):
		if self.color == WHITE:
			win.blit(W_PAWN, (self.x - W_PAWN.get_width()//2, self.y-W_PAWN.get_height()//2))
		else:
			win.blit(B_PAWN, (self.x - B_PAWN.get_width()//2, self.y-B_PAWN.get_height()//2))



class Knight(Piece):

	def __init__(self, row, col, color):
		super().__init__(row, col, color)
		self.rank = 3


	def valid_moves(self, board):
		valid_moves = {}
		dirs = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

		for _dir in dirs:
			x = self.col + _dir[0]
			y = self.row + _dir[1]

			if x >= 0 and x < ROWS and y >= 0 and y < COLS:
				piece = board[y][x]

				if piece != 0:
					if piece.color != self.color:
						valid_moves[(y, x)] = [piece]
				else:
					valid_moves[(y, x)] = []
		return valid_moves


	def draw(self, win):
		if self.color == WHITE:
			win.blit(W_KNIGHT, (self.x - W_KNIGHT.get_width()//2, self.y-W_KNIGHT.get_height()//2))
		else:
			win.blit(B_KNIGHT, (self.x - B_KNIGHT.get_width()//2, self.y-B_KNIGHT.get_height()//2))



class Rook(Piece):

	def __init__(self, row, col, color):
		super().__init__(row, col, color)
		self.rank = 5

	def valid_moves(self, board):

		valid_moves = {}
		dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

		for _dir in dirs:
			x = self.col + _dir[0]
			y = self.row + _dir[1]
			while x >= 0 and x < ROWS and y >= 0 and y < COLS:
				piece = board[y][x]

				if piece != 0:
					if piece.color == self.color:
						break
					else:
						valid_moves[(y, x)] = [piece]
						break
				else:
					valid_moves[(y, x)] = []
				x += _dir[0]
				y += _dir[1]
		return valid_moves


	def draw(self, win):
		if self.color == WHITE:
			win.blit(W_ROOK, (self.x - W_ROOK.get_width()//2, self.y-W_ROOK.get_height()//2))
		else:
			win.blit(B_ROOK, (self.x - B_ROOK.get_width()//2, self.y-B_ROOK.get_height()//2))





class Bishop(Piece):

	def __init__(self, row, col, color):
		super().__init__(row, col, color)
		self.rank = 3

	def valid_moves(self, board):

		valid_moves = {}
		dirs = [(-1, -1), (1, 1), (-1, 1), (1, -1)]

		for _dir in dirs:
			x = self.col + _dir[0]
			y = self.row + _dir[1]
			while x >= 0 and x < ROWS and y >= 0 and y < COLS:
				piece = board[y][x]

				if piece != 0:
					if piece.color == self.color:
						break
					else:
						valid_moves[(y, x)] = [piece]
						break
				else:
					valid_moves[(y, x)] = []
				x += _dir[0]
				y += _dir[1]
		return valid_moves

	def draw(self, win):
		if self.color == WHITE:
			win.blit(W_BISHOP, (self.x - W_BISHOP.get_width()//2, self.y-W_BISHOP.get_height()//2))
		else:
			win.blit(B_BISHOP, (self.x - B_BISHOP.get_width()//2, self.y-B_BISHOP.get_height()//2))


class Queen(Piece):

	def __init__(self, row, col, color):
		super().__init__(row, col, color)
		self.rank = 9

	def valid_moves(self, board):
		valid_moves = {}
		dirs = [(-1, -1), (1, 1), (-1, 1), (1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]

		for _dir in dirs:
			x = self.col + _dir[0]
			y = self.row + _dir[1]
			while x >= 0 and x < ROWS and y >= 0 and y < COLS:
				piece = board[y][x]

				if piece != 0:
					if piece.color == self.color:
						break
					else:
						valid_moves[(y, x)] = [piece]
						break
				else:
					valid_moves[(y, x)] = []
				x += _dir[0]
				y += _dir[1]
		return valid_moves

	def draw(self, win):
		if self.color == WHITE:
			win.blit(W_QUEEN, (self.x - W_QUEEN.get_width()//2, self.y-W_QUEEN.get_height()//2))
		else:
			win.blit(B_QUEEN, (self.x - B_QUEEN.get_width()//2, self.y-B_QUEEN.get_height()//2))


class King(Piece):

	def __init__(self, row, col, color):
		super().__init__(row, col, color)
		self.rank = 100

	def valid_moves(self, board):
		valid_moves = {}
		dirs = [(-1, -1), (1, 1), (-1, 1), (1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]

		for _dir in dirs:
			x = self.col + _dir[0]
			y = self.row + _dir[1]
			if x >= 0 and x < ROWS and y >= 0 and y < COLS:
				piece = board[y][x]

				if piece != 0:
					if piece.color != self.color:
						if not self.checked(board, y, x):
							valid_moves[(y, x)] = [piece]
				else:
					if not self.checked(board, y, x):
						valid_moves[(y, x)] = []
				x += _dir[0]
				y += _dir[1]

		valid_moves = self._check_castle(board, valid_moves)
		return valid_moves


	def draw(self, win):
		if self.color == WHITE:
			win.blit(W_KING, (self.x - W_KING.get_width()//2, self.y-W_KING.get_height()//2))
		else:
			win.blit(B_KING, (self.x - B_KING.get_width()//2, self.y-B_KING.get_height()//2))


	def checked(self, board, y, x):
		for row in board:
			for piece in row:
				if piece != 0:
					if piece.color != self.color and piece.rank < 100:
						valid_moves = piece.valid_moves(board)
						for (_y, _x) in valid_moves:
							if _y == y and _x == x:
								return True


	def _check_left_castle(self, board, valid_moves):
		left_rook = board[self.row][0]
		if left_rook != 0:
			for i in range(1, 4):
				if board[self.row][i] != 0:
					return valid_moves

			if left_rook.color == self.color and left_rook.rank == 5 and not left_rook.moved:
				if not self.checked(board, self.row, 2):
					valid_moves[(self.row, 1)] = [left_rook]
		return valid_moves



	def _check_right_castle(self, board, valid_moves):
		right_rook = board[self.row][7]
		if right_rook != 0:
			for i in range(5, 7):
				if board[self.row][i] != 0:
					return valid_moves

			if right_rook.color == self.color and right_rook.rank == 5 and not right_rook.moved:
				if not self.checked(board, self.row, 5):
					valid_moves[(self.row, 6)] = [right_rook]
		return valid_moves


	def _check_castle(self, board, valid_moves):
		if not self.moved:

			# check left rook
			valid_moves = self._check_left_castle(board, valid_moves)
			
			# check right rook
			valid_moves = self._check_right_castle(board, valid_moves)
		return valid_moves