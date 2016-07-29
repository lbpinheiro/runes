import mana

class Player:
	def __init__(self, sName, iLifePoints):
		self._name = sName
		self._lifePoints = iLifePoints
		self._mana = mana.Mana()
		self._special_moves = 0

	def increase_special_moves(self, i=1):
		print 'player.increase_special_moves i=' + str(i)
		self._special_moves += i
	
	def decrease_special_moves(self, i=1):
		self._special_moves -= i

	def increase_life_points(self, i):
		self._lifePoints += i

	def decrease_life_points(self, iDamage):
		self._lifePoints -= iDamage

	def get_mana(self):
		return self._mana

	def get_name(self):
		return self._name

	def __str__(self):
		sOut = "Name:" + self._name
		sOut += "\nRed:" + str(self._mana.red)
		sOut += "\nWhite:" + str(self._mana.white)
		sOut += "\nBlue:" + str(self._mana.blue)
		sOut += "\nBlack:" + str(self._mana.black)
		sOut += "\nSpecial:" + str(self._special_moves)
		sOut += "\nHP:" + str(self._lifePoints)
		return sOut

	@staticmethod
	def test_case():
		import basic

		print 'Player class TestCase'

		# creates a simple player
		p = Player("Player 1", 10)
		basic.is_equal(1, "Player 1", p.get_name())
		basic.is_equal(2, True, p.get_mana().equal(mana.Mana()))

if __name__ == "__main__":
	Player.test_case()
