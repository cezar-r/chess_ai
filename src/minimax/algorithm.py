from copy import deepcopy
import pygame
import copy
from chess.board import Board
import pickle


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def minimax(position, depth, max_player, game):
	if depth == 0 or position.winner():
		return position.evaluate(), position

	if max_player:
		max_eval = float('-inf')
		best_move = None
		for move in get_all_moves(position, BLACK, game):
			evaluation = minimax(move, depth - 1, False, game)[0]
			max_eval = max(max_eval, evaluation)
			# alpha = max(alpha, max_eval)
			if max_eval == evaluation:
				best_move = move 
			# if beta <= alpha:
			# 	break

		return max_eval, best_move

	else:
		min_eval = float('inf')
		best_move = None
		for move in get_all_moves(position, WHITE, game):
			evaluation = minimax(move, depth - 1, True, game)[0]
			min_eval = min(min_eval, evaluation)
			# beta = min(beta, min_eval)
			if min_eval == evaluation:
				best_move = move 
			# if beta <= alpha:
			# 	break
		return min_eval, best_move


def simulate_move(piece, move, board, game, skip):
	if skip:
		board.remove(skip)
	# print("simulation:")
	# board.print()
	board.move(piece, move[0], move[1])
	return board


def get_all_moves(board, color, game):
	moves = []

	for piece in board.get_all_pieces(color):
		valid_moves = board.get_valid_moves(piece)
		for move, skip in valid_moves.items():
			temp_board = deepcopy(board)
			temp_piece = temp_board.get_piece(piece.row, piece.col)
			new_board = simulate_move(temp_piece, move, temp_board, game, skip)
			moves.append(new_board)
	return moves

