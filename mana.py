class Mana:
	def __init__(self, iRed=0, iWhite=0, iBlue=0, iBlack=0):
		self.red = iRed
		self.white = iWhite
		self.blue = iBlue
		self.black = iBlack

	def increase(self, mana):
		self.red += mana.red
		self.white += mana.white
		self.blue += mana.blue
		self.black += mana.black
	
	def decrease(self, mana):
		self.red = max(0, self.red - mana.red)
		self.white = max(0, self.white - mana.white)
		self.blue = max(0, self.blue - mana.blue)
		self.black = max(0, self.black - mana.black)

	def add_red(self, i=1):
		self.red += i

	def add_white(self, i=1):
		self.white += i

	def add_blue(self, i=1):
		self.blue += i

	def add_black(self, i=1):
		self.black += i

	def equal(self, mana):
		if self.red == mana.red and self.white == mana.white and self.blue == mana.blue and self.black == mana.black:
			return True
		else:
			return False

	@staticmethod
	def test_case():
		import basic

		print 'Mana class TestCase'

		# creates a simple Mana class, red=1, white=2, blue=3, black=0=default
		m = Mana(1, 2, 3)
		basic.is_equal(1, m.red, 1) 
		basic.is_equal(2, m.white, 2)
		basic.is_equal(3, m.blue, 3)
		basic.is_equal(4, m.black, 0)

		# adds 1 red mana
		m.increase(Mana(1))
		basic.is_equal(5, m.red, 2) 
		basic.is_equal(6, m.white, 2)
		basic.is_equal(7, m.blue, 3)
		basic.is_equal(8, m.black, 0)

		# adds 1 black mana
		m.increase(Mana(0, 0, 0, 1))
		basic.is_equal(9, m.red, 2) 
		basic.is_equal(10, m.white, 2)
		basic.is_equal(11, m.blue, 3)
		basic.is_equal(12, m.black, 1)

		# remove 4 red mana
		m.decrease(Mana(4))
		basic.is_equal(13, m.red, 0) 
		basic.is_equal(14, m.white, 2)
		basic.is_equal(15, m.blue, 3)
		basic.is_equal(16, m.black, 1)

		# remove 1 blue mana
		m.decrease(Mana(0, 0, 1))
		basic.is_equal(17, m.red, 0) 
		basic.is_equal(18, m.white, 2)
		basic.is_equal(19, m.blue, 2)
		basic.is_equal(20, m.black, 1)

if __name__ == "__main__":
	Mana.test_case()
