


import pygame
from .constants import *
from .piece import *
import copy

class Board:

	def __init__(self):
		self.board = []
		self.create_board()


	def _get_score(self, color):
		score = 0
		for row in self.board:
			for piece in row:
				if piece != 0:
					if piece.color == color:
						score += piece.rank
		return score


	def _has_king(self, color):
		for row in self.board:
			for piece in row:
				if piece != 0:
					if piece.color == color and piece.rank >= 100:
						return True
		return False


	def evaluate(self):
		return self._get_score(BLACK) - self._get_score(WHITE)


	def get_all_pieces(self, color):
		pieces = []
		for row in self.board:
			for piece in row:
				if piece != 0 and piece.color == color:
					pieces.append(piece)
		return pieces


	def draw_squares(self, win):
		win.fill(MOCHA)
		for row in range(ROWS):
			for col in range(row % 2, COLS, 2):
				pygame.draw.rect(win, CREAM, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


	def move(self, piece, row, col):
		# print(piece)
		if piece != 0:
			if piece.rank == 1 and (row == 0 or row == 7):
				piece = Queen(row, col, piece.color)
			self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
			piece.move(row, col)
		# print('in move func:')
		# self.print()
		# print()


	def get_piece(self, row, col):
		return self.board[row][col]


	def remove(self, pieces):
		for piece in pieces:
			# print(piece)
			# print(piece.color)
			# print(piece.row, piece.col)
			self.board[piece.row][piece.col] = 0
		# self.print()
		# exit()


	def create_board(self):
		board = []
		for row in range(ROWS):
			if row == 0:
				cur_row = [Rook(0, 0, BLACK), 
						Knight(0, 1, BLACK), 
						Bishop(0, 2, BLACK),
						Queen(0, 3, BLACK), 
						King(0, 4, BLACK),
						Bishop(0, 5, BLACK),
						Knight(0, 6, BLACK),
						Rook(0, 7, BLACK)]
			elif row == 1:
				cur_row = []
				for i in range(COLS):
					cur_row.append(Pawn(1, i, BLACK))
			elif row == ROWS - 1:
				cur_row = [Rook(ROWS - 1, 0, WHITE), 
						Knight(ROWS - 1, 1, WHITE), 
						Bishop(ROWS - 1, 2, WHITE),
						Queen(ROWS - 1, 3,  WHITE),
						King(ROWS - 1, 4, WHITE), 
						Bishop(ROWS - 1, 5,WHITE),
						Knight(ROWS - 1, 6, WHITE),
						Rook(ROWS - 1, 7, WHITE)]
			elif row == ROWS - 2:
				cur_row = []
				for i in range(COLS):
					cur_row.append(Pawn(ROWS - 2, i,  WHITE))
			else:
				cur_row = [0] * ROWS
			board.append(cur_row)
		self.board = board

	def draw(self, win):
		self.draw_squares(win)
		for row in range(ROWS):
			for col in range(COLS):
				piece = self.board[row][col]
				if piece != 0:
					piece.draw(win)

	def winner(self):
		if not self._has_king(WHITE):
			return BLACK
		elif not self._has_king(BLACK):
			return WHITE
		return None

	def get_valid_moves(self, piece):
		return piece.valid_moves(self.board)


	def add_piece(self, piece):
		self.board[piece.row][piece.col] = piece


	def get_board(self):
		return self.board

	def set_board(self, board):
		self.board = board

	def print(self):
		for row in self.board:
			print(row)
		print()

