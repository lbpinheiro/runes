import player
import mana
import pygame
import os
import basic

CLICKED = 1
ONLY_HL = 2
NO_HL = 3

class Rune:
	
	def __init__(self):
		self._state = NO_HL
		self._type = -1
		self._image_path = os.path.join(basic.IMAGES_DIR, "empty_space.bmp")
		self._image = pygame.image.load(self._image_path)
		self._image_hl = self._image

	def get_image(self):
		if self._state == NO_HL:
			#print 'get_image() returning NO_HL (state=' + str(self._state) + ')'
			return self._image
		else:
			#print 'get_image() returning HL (state=' + str(self._state) + ')'
			return self._image_hl

	def change_state(self, newState):
		print 'rune.change_state(' + str(newState) + ')'
		self._state = newState

	def compare(self, rune):
		return self._type == rune._type

	def action(self, trigger_player):
		pass

	def get_type(self):
		return self._type

	@staticmethod
	def test_case():
		RedRune.test_case()
		WhiteRune.test_case()
		BlueRune.test_case()
		BlackRune.test_case()

	# usado nos testes
	def __str__(self):
		return 'NON'

	def is_red(self):
		return 0 == self._type

	def is_white(self):
		return 1 == self._type

	def is_blue(self):
		return 2 == self._type

	def is_black(self):
		return 3 == self._type
	

class RedRune(Rune):
	def __init__(self):
		self._state = NO_HL
		self._type = 0
		self._image_path = os.path.join(basic.IMAGES_DIR, "red_rune.bmp")
		self._image_hl_path = os.path.join(basic.IMAGES_DIR, "red_rune_hl.bmp")
		self._image = pygame.image.load(self._image_path)
		self._image_hl = pygame.image.load(self._image_hl_path)

	def action(self, trigger_player):
		print 'RedRune.action'
		trigger_player.get_mana().add_red()

	def __str__(self):
		return 'RED'

	@staticmethod
	def test_case():
		print 'RedRune class TestCase'
		
		# creates a simple player
		p = player.Player("Player 1", 10)
		basic.is_equal(1, True, p.get_mana().equal(mana.Mana()))

		# this player trigger the action
		r = RedRune()
		r.action(p)
		basic.is_equal(2, True, p.get_mana().equal(mana.Mana(1)))

class WhiteRune(Rune):
	def __init__(self):
		self._state = NO_HL
		self._type = 1
		self._image_path = os.path.join(basic.IMAGES_DIR, "white_rune.bmp")
		self._image_hl_path = os.path.join(basic.IMAGES_DIR, "white_rune_hl.bmp")
		self._image = pygame.image.load(self._image_path)
		self._image_hl = pygame.image.load(self._image_hl_path)

	def action(self, trigger_player):
		print 'WhiteRune.action'
		trigger_player.get_mana().add_white()

	def __str__(self):
		return 'WHT'

	@staticmethod
	def test_case():
		import basic

		print 'WhiteRune class TestCase'
		
		# creates a simple player
		p = player.Player("Player 1", 10)
		basic.is_equal(1, True, p.get_mana().equal(mana.Mana()))

		# this player trigger the action
		r = WhiteRune()
		r.action(p)
		basic.is_equal(2, True, p.get_mana().equal(mana.Mana(0, 1)))

class BlueRune(Rune):
	def __init__(self):
		self._state = NO_HL
		self._type = 2
		self._image_path = os.path.join(basic.IMAGES_DIR, "blue_rune.bmp")
		self._image_hl_path = os.path.join(basic.IMAGES_DIR, "blue_rune_hl.bmp")
		self._image = pygame.image.load(self._image_path)
		self._image_hl = pygame.image.load(self._image_hl_path)

	def action(self, trigger_player):
		print 'BlueRune.action'
		trigger_player.get_mana().add_blue()

	def __str__(self):
		return 'BLU'

	@staticmethod
	def test_case():
		import basic

		print 'BlueRune class TestCase'
		
		# creates a simple player
		p = player.Player("Player 1", 10)
		basic.is_equal(1, True, p.get_mana().equal(mana.Mana()))

		# this player trigger the action
		r = BlueRune()
		r.action(p)
		basic.is_equal(2, True, p.get_mana().equal(mana.Mana(0, 0, 1)))

class BlackRune(Rune):
	def __init__(self):
		self._state = NO_HL
		self._type = 3
		self._image_path = os.path.join(basic.IMAGES_DIR, "black_rune.bmp")
		self._image_hl_path = os.path.join(basic.IMAGES_DIR, "black_rune_hl.bmp")
		self._image = pygame.image.load(self._image_path)
		self._image_hl = pygame.image.load(self._image_hl_path)

	def action(self, trigger_player):
		print 'BlackRune.action'
		trigger_player.get_mana().add_black()

	def __str__(self):
		return 'BLK'

	@staticmethod
	def test_case():
		import basic

		print 'BlackRune class TestCase'
		
		# creates a simple player
		p = player.Player("Player 1", 10)
		basic.is_equal(1, True, p.get_mana().equal(mana.Mana()))

		# this player trigger the action
		r = BlackRune()
		r.action(p)
		basic.is_equal(2, True, p.get_mana().equal(mana.Mana(0, 0, 0, 1)))

class SpecialRune(Rune):
	def __init__(self):
		self._state = NO_HL
		self._type = 4
		self._image_path = os.path.join(basic.IMAGES_DIR, "special_rune.bmp")
		self._image_hl_path = os.path.join(basic.IMAGES_DIR, "special_rune_hl.bmp")
		self._image = pygame.image.load(self._image_path)
		self._image_hl = pygame.image.load(self._image_hl_path)

	def action(self, trigger_player):
		print 'SpecialRune.action'
		trigger_player.increase_life_points(3)

	def __str__(self):
		return 'SPL'

	@staticmethod
	def test_case():
		import basic

		print 'BlackRune class TestCase'
		
		# creates a simple player
		p = player.Player("Player 1", 10)
		basic.is_equal(1, True, p.get_mana().equal(mana.Mana()))

		# this player trigger the action
		r = BlackRune()
		r.action(p)
		basic.is_equal(2, True, p.get_mana().equal(mana.Mana(0, 0, 0, 1)))

if __name__ == "__main__":
	Rune.test_case()
