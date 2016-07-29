import rune
import random
import basic
import pygame

class Grid:
	def __init__(self, x, y):
		self._x = max(x, 3) # 3 lines minimun
		self._y = max(y, 3) # 3 columns minimun
		self._column = []
		
		self._rune_pos = (-1, -1)
		self._last_click_pos = (-1, -1)
		self._adjacent_list = []

		for j in range(self._y):
			_column = []
			for i in range(self._x):
				_column.append(self._get_rune())
			self._column.append(_column)			
			
		self._validate_grid()
	
	def _clean_states(self, c):
		self._column[c[0]][c[1]].change_state(rune.NO_HL)
		for cord in self._adjacent_list:
			self._column[cord[0]][cord[1]].change_state(rune.NO_HL)
		self._adjacent_list = []

	def change_state(self, j, i, p):
		print 'grid.change_state() j=' + str(j) + ' i=' + str(i)
		# checa se a nova posicao clicada e adjacente a anterior
		
		self._rune_pos = (j, i)
		print 'rune pos:'
		print self._rune_pos
		print self._adjacent_list

		for cord in self._adjacent_list:
			print 'for: ' + str(cord[0]) + '==' + str(self._rune_pos[0]) + ' and ' + str(cord[1]) + '==' + str(self._rune_pos[1])
			if cord[0] == self._rune_pos[0] and cord[1] == self._rune_pos[1]:
				print 'MOOOOVE'					
				self.move(self._last_click_pos, self._rune_pos, p)
				self._rune_pos = (-1, -1)
				self._clean_states(self._last_click_pos)
				self._last_click_pos = (-1, -1)
				return

		if self._last_click_pos[0] != -1 and self._last_click_pos[1] != -1:			
			self._clean_states(self._last_click_pos)

		self._last_click_pos = (j, i)
		
		self._column[j][i].change_state(rune.CLICKED)
		self._adjacent_list = []

		# checks up (if possible)
		if i > 0:
			self._column[j][i - 1].change_state(rune.ONLY_HL)
			print 'change_state ' + str(j) + ' ' + str(i - 1)
			self._adjacent_list.append((j, i - 1))
		# checks down (if possible)
		if i < self._x - 1:
			self._column[j][i + 1].change_state(rune.ONLY_HL)
			print 'change_state ' + str(j) + ' ' + str(i + 1)
			self._adjacent_list.append((j, i + 1))
		# checks left (if possible)
		if j > 0:
			self._column[j - 1][i].change_state(rune.ONLY_HL)
			print 'change_state ' + str(j - 1) + ' ' + str(i)
			self._adjacent_list.append((j - 1, i))
		# checks right (if possible)
		if j < self._y - 1:
			self._column[j + 1][i].change_state(rune.ONLY_HL)
			print 'change_state ' + str(j + 1) + ' ' + str(i)
			self._adjacent_list.append((j + 1, i))
		

	# the auto generate initial grid can't hold 3 runes in seq
	def _validate_grid(self):
		# vertical check
		for j in range(self._y):		
			for i in range(self._x - 2):
				if self._column[j][i].compare(self._column[j][i + 1]) == False:
					continue
				if self._column[j][i].compare(self._column[j][i + 2]) == False:
					continue
				else:
					self._change_rune(i + 2, j)
					i += 2
		# horizontal check
		for i in range(self._x):
			for j in range(self._y - 2):
				if self._column[j][i].compare(self._column[j + 1][i]) == False:
					continue
				if self._column[j][i].compare(self._column[j + 2][i]) == False:
					continue
				else:
					self._change_rune(i, j + 2)
					j += 2
	
	# todo: fazer de um jeito melhor!
	def _change_rune(self, i, j):
		#print 'i=' + str(i) + ' j=' + str(j)
		flags = [False, False, False, False, False]
		
		# checks up (if possible)
		if i > 0:
			flags[self._column[j][i - 1].get_type()] = True
			#print 'up ' + str(self._column[j][i - 1].get_type())
		# checks down (if possible)
		if i < self._x - 1:
			flags[self._column[j][i + 1].get_type()] = True
			#print 'down ' + str(self._column[j][i + 1].get_type())
		# checks left (if possible)
		if j > 0:
			flags[self._column[j - 1][i].get_type()] = True
			#print 'left ' + str(self._column[j - 1][i].get_type())
		# checks right (if possible)
		if j < self._y - 1:
			flags[self._column[j + 1][i].get_type()] = True
			#print 'right ' + str(self._column[j + 1][i].get_type())

		domain = []
		if flags[0] == False:
			domain.append(rune.RedRune())
		if flags[1] == False:
			domain.append(rune.WhiteRune())
		if flags[2] == False:
			domain.append(rune.BlueRune())
		if flags[3] == False:
			domain.append(rune.BlackRune())
		if flags[4] == False:
			domain.append(rune.SpecialRune())

		if domain == []:
			print 'domain empty i=' + str(i) + ' j=' + str(j)
			# gambiarra tirar isto depois			
			

		self._column[j][i] = random.choice(domain)
		
				

	def _get_rune(self):
		n = random.choice(range(9))
		if n == 0 or n == 1:
			return rune.RedRune()
		if n == 2 or n == 3:
			return rune.WhiteRune()
		if n == 4 or n == 5:
			return rune.BlueRune()
		if n == 6 or n==7:
			return rune.BlackRune()
		if n == 8:
			return rune.SpecialRune()

	# returns True if there is at least one possible move
	# returns False otherwise
	def search_move(self):
		# vertical check
		for j in range(self._y):		
			for i in range(self._x - 2):
				if self._column[j][i].compare(self._column[j][i + 1]) == False:
					continue
				if self._column[j][i].compare(self._column[j][i + 2]) == False:
					continue
				else:
					return True
					
		# horizontal check
		for i in range(self._x):
			for j in range(self._y - 2):
				if self._column[j][i].compare(self._column[j + 1][i]) == False:
					continue
				if self._column[j][i].compare(self._column[j + 2][i]) == False:
					continue
				else:
					return True
		# no possible move found		
		return False

	def search_up(self, i, j, rune):
		# checks up (if possible)
		if i > 0:
			if self._column[j][i - 1].compare(rune) == True:
				return True
		# checks left (if possible)
		if j > 0:
			if self._column[j - 1][i].compare(rune) == True:
				return True
		# checks right (if possible)
		if j < self._y - 1:
			if self._column[j + 1][i].compare(rune) == True:
				return True
		return False

	def search_down(self, i, j, rune):
		# checks down (if possible)
		if i < self._x - 1:
			if self._column[j][i + 1].compare(rune) == True:
				return True
		# checks left (if possible)
		if j > 0:
			if self._column[j - 1][i].compare(rune) == True:
				return True
		# checks right (if possible)
		if j < self._y - 1:
			if self._column[j + 1][i].compare(rune) == True:
				return True
		return False

	def search_left(self, i, j, rune):
		# checks up (if possible)
		if i > 0:
			if self._column[j][i - 1].compare(rune) == True:
				return True
		# checks down (if possible)
		if i < self._x - 1:
			if self._column[j][i + 1].compare(rune) == True:
				return True
		# checks left (if possible)
		if j > 0:
			if self._column[j - 1][i].compare(rune) == True:
				return True
		return False

	def search_right(self, i, j, rune):
		# checks up (if possible)
		if i > 0:
			if self._column[j][i - 1].compare(rune) == True:
				return True
		# checks down (if possible)
		if i < self._x - 1:
			if self._column[j][i + 1].compare(rune) == True:
				return True
		# checks right (if possible)
		if j < self._y - 1:
			if self._column[j + 1][i].compare(rune) == True:
				return True
		return False

	# procura e executa os matchs do turno
	def execute_match(self, player):
		blacklist = []
		# vertical check
		for j in range(self._y):
			i = 0
			while i < self._x - 2:
				if self._column[j][i].get_type() == -1:
					i += 1
					continue
				if self._column[j][i].compare(self._column[j][i + 1]) == False:
					i += 1
					continue
				if self._column[j][i].compare(self._column[j][i + 2]) == False:
					i += 1
					continue
				if i + 3 < self._x and self._column[j][i].compare(self._column[j][i + 3]) == True:
					if i + 4 < self._x and self._column[j][i].compare(self._column[j][i + 4]) == True:
						# 5-of-a-kind
						print '5-of-a-kind vertical i=' + str(i)
						player.increase_special_moves(2)
						self._column[j][i].action(player)
						blacklist.append((j, i))
						blacklist.append((j, i + 1))
						blacklist.append((j, i + 2))
						blacklist.append((j, i + 3))
						blacklist.append((j, i + 4))
						i += 4
					else:
						# 4-of-a-kind
						print '4-of-a-kind vertical i=' + str(i)
						player.increase_special_moves()
						self._column[j][i].action(player)
						blacklist.append((j, i))
						blacklist.append((j, i + 1))
						blacklist.append((j, i + 2))
						blacklist.append((j, i + 3))
						i += 3
				else:
					# 3-of-a-kind
					print '3-of-a-kind vertical i=' + str(i)
					self._column[j][i].action(player)
					blacklist.append((j, i))
					blacklist.append((j, i + 1))
					blacklist.append((j, i + 2))
					i += 2
					
		# horizontal check
		for i in range(self._x):
			j = 0
			while j < self._y - 2:
				if self._column[j][i].get_type() == -1:
					j += 1
					continue
				if self._column[j][i].compare(self._column[j + 1][i]) == False:
					j += 1
					continue
				if self._column[j][i].compare(self._column[j + 2][i]) == False:
					j += 1
					continue
				if j + 3 < self._y and self._column[j][i].compare(self._column[j + 3][i]) == True:
					if j + 4 < self._y and self._column[j][i].compare(self._column[j + 4][i]) == True:
						# 5-of-a-kind
						print '5-of-a-kind horizontal'
						player.increase_special_moves(2)
						self._column[j][i].action(player)
						self._column[j][i] = rune.Rune()
						self._column[j + 1][i] = rune.Rune()
						self._column[j + 2][i] = rune.Rune()
						self._column[j + 3][i] = rune.Rune()
						self._column[j + 4][i] = rune.Rune()
						j += 4
					else:
						# 4-of-a-kind
						print '4-of-a-kind horizontal'
						player.increase_special_moves()
						self._column[j][i].action(player)
						self._column[j][i] = rune.Rune()
						self._column[j + 1][i] = rune.Rune()
						self._column[j + 2][i] = rune.Rune()
						self._column[j + 3][i] = rune.Rune()
						j += 3
				else:
					# 3-of-a-kind
					print '3-of-a-kind horizontal'
					self._column[j][i].action(player)
					self._column[j][i] = rune.Rune()
					self._column[j + 1][i] = rune.Rune()
					self._column[j + 2][i] = rune.Rune()
					j += 2
		
		for cord in blacklist:
			self._column[cord[0]][cord[1]] = rune.Rune()


	# for tests
	def __str__(self):
		sOut = ''
		for i in range(self._x):
			sLine = ''			
			for j in self._column:
				sLine = sLine + ' ' + str(j[i])
			sOut = sOut + '\n' + sLine

		return sOut

	# returns True if the move is possible
	def move(self, cord1, cord2, p):
		print 'move ' + str(cord1) + ' -> ' + str(cord2)
		tmp = self._column[cord1[0]][cord1[1]]
		self._column[cord1[0]][cord1[1]] = self._column[cord2[0]][cord2[1]]
		self._column[cord2[0]][cord2[1]] = tmp
		self.execute_match(p)

	@staticmethod
	def test_case():

		# creates a grid
		g = Grid(4, 5)
		
		print str(g)
		

if __name__ == "__main__":
	Grid.test_case()
