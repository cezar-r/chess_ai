import pygame
from .constants import *
from chess.board import Board
from chess.piece import *

class Game:
	"""
	This class represents the game state.
	It contains the board, as well as methods
	to retrieve info from the game, update the game, 
	and calls a bot to make moves

	Methods
	-------
	update()			-> None; 	updates the game state
	reset()				-> None; 	initializes the game
	select()			-> bool; 	called when a piece is clicked on the board
	draw_valid_moves() 	-> None; 	draws the circles onto the board
	change_turn()		-> None; 	changes turn
	winner()			-> (r,g,b); color of winner if there is one, otherwise None
	ai_move()			-> None; 	updates the board based on bot's move
	"""

	def __init__(self, win):
		self._init()
		self.win = win

	def _init(self):
		"""initializes the game"""
		self.selected = None
		self.board = Board()
		self.turn = WHITE
		self.valid_moves = {}

	def update(self):
		"""updates the game state"""
		self.board.draw(self.win)
		self.draw_valid_moves(self.valid_moves)
		pygame.display.update()

	def reset(self):
		"""initializes the game"""
		self._init()

	def select(self, row, col):
		"""Called when a piece is clicked on the board

		Parameters
		----------
		row: 	int
				index of row
		col: 	int
				index of col

		Returns
		-------
		bool:	true if piece selected is non-empty
		"""
		if self.selected:
			result = self._move(row, col)
			if not result:
				self.selected = None
				self.select(row, col)

		piece = self.board.get_piece(row, col)
		if piece != 0 and piece.color == self.turn:
			self.selected = piece 
			self.valid_moves = self.board.get_valid_moves(piece)
			return True
		return False

	def draw_valid_moves(self, moves):
		"""Draws all valid moves onto the screen

		Parameters
		----------
		moves:	dict
				dictionary of moves
		"""
		for move in moves:
			row, col = move
			pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

	def _move(self, row, col):
		"""Moves a piece to desired position

		Parameters
		----------
		row: 	int
				index of row
		col: 	int
				index of col

		Returns
		-------
		bool:	true if move is valid
		"""
		piece = self.board.get_piece(row, col)
		if self.selected and (row, col) in self.valid_moves:
			skipped = self.valid_moves[(row, col)]
			if skipped:
				piece = skipped[0]
				if piece.rank == 5 and piece.color == self.selected.color and self.selected.rank >= 100:
					if col == 1:
						next_col = 2
					else:
						next_col = 5
					self.board.move(piece, row, next_col)
					self.selected.rank += 50
				else:
					self.board.remove(skipped)
			self.board.move(self.selected, row, col)
			if self.selected.rank == 1:
				if self.selected.color == WHITE and row == 0:
					self.board.remove([self.selected])
					self.board.add_piece(Queen(row, col, WHITE))
				elif self.selected.color == BLACK and row == 7:
					self.board.remove([self.selected])
					self.board.add_piece(Queen(row, col, BLACK))
			self.change_turn()
		else:
			return False
		return True 


	def change_turn(self):
		"""changes turns"""
		self.valid_moves = {}
		if self.turn == WHITE:
			self.turn = BLACK
		else:
			self.turn = WHITE

	def winner(self):
		"""returns the rgb color of the winner as a tuple"""
		return self.board.winner()

	def get_board(self):
		"""returns the board"""
		return self.board

	def ai_move(self, board):
		"""chanegs board to board after ai move"""
		self.board = board
		self.change_turn()
		self.update()