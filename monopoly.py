from random import randint
from random import shuffle

class Player:
	def __init__(self):
		self.pos = 0
		self.doubles_series = 0

class Board:
	def movePlayer(self, player):
		move = self.roll(player)
		# Three double, go to jail
		if move == -1:
			self.sendToJail(player)
			return

		# Normal movement
		player.pos += abs(move)
		player.pos %= 40
		self.positions[player.pos][1] += 1

		## Special positions
		# Chance
		if player.pos == 7 or player.pos == 22 or player.pos == 36:
			draw = self.drawChance()
			# Advance To Go
			if draw == 1:
				player.pos = 0
				self.positions[0][1] += 1
			# Go Directly To Jail
			elif draw == 2:
				self.sendToJail(player)
			# Go Back 3 Spaces
			elif draw == 3:
				player.pos -= 3
				self.positions[player.pos][1] += 1
			# Advance To Nearest Railroad
			elif draw == 4 or draw == 5:
				if player.pos == 7:
					player.pos = 15
					self.positions[15][1] += 1
				elif player.pos == 22:
					player.pos = 25
					self.positions[25][1] += 1
				else:
					player.pos = 35
					self.positions[35][1] += 1
			# Take A Ride On The Reading
			elif draw == 6:
				player.pos = 5
				self.positions[5][1] += 1
			# Advance To Nearest Utility
			elif draw == 7:
				if player.pos == 22:
					player.pos = 28
					self.positions[28][1] += 1
				else:
					player.pos = 12
					self.positions[12][1] += 1
			# Advance To St. Charles Place
			elif draw == 8:
				player.pos == 11
				self.positions[11][1] += 1
			# Advance To Illinois Avenue
			elif draw == 9:
				player.pos = 24
				self.positions[24][1] += 1
			elif draw == 10:
				player.pos = 39
				self.positions[39][1] += 1
			# Advance to Boardwalk

		# Community Chest
		if player.pos == 2 or player.pos == 17 or player.pos == 33:
			draw = self.drawChest()
			if draw == 1:
				player.pos = 0
				self.positions[0][1] += 1
			if draw == 2:
				self.sendToJail(player)

		# Go To Jail
		if player.pos == 30:
			self.sendToJail(player)
			return
		# Doubles, roll again
		if move < 0:
			self.movePlayer(player)

	def sendToJail(self, player):
		player.pos = 10
		self.positions[40][1] += 1

	def drawChest(self):
		if len(self.chest) == 0:
			self.shuffleChest()
		return self.chest.pop()

	def drawChance(self):
		if len(self.chance) == 0:
			self.shuffleChance()
		return self.chance.pop()

	def roll(self, player):
		die1 = randint(1,6)
		die2 = randint(1,6)

		if die1 == die2:
			player.doubles_series += 1
			die1 = die2 = die1 * -1
		else:
			player.doubles_series = 0

		if player.doubles_series == 3:
			return -1

		return die1 + die2

	def shuffleChest(self):
		self.chest = range(1, 17)
		shuffle(self.chest)

	def shuffleChance(self):
		self.chance = range(1, 17)
		shuffle(self.chance)

	def randList(a, b):
		sourceList = range(a, b + 1)
		newList = []
		while len(sourceList) != 0:
			newList.push(sourceList.pop(randint()))

	def __init__(self):
		self.shuffleChest()
		self.shuffleChance()
		self.positions = [['Go', 0],
						  ['Mediteranean Avenue', 0],
						  ['Community Chest 1', 0],
						  ['Baltic Avenue', 0],
						  ['Income Tax', 0],
						  ['Reading Railroad', 0],
						  ['Oriental Avenue', 0],
						  ['Chance 1', 0],
						  ['Vermont Avenue', 0],
						  ['Connecticut Avenue', 0],
						  ['Just Visiting Jail', 0],
						  ['St. Charles Place', 0],
						  ['Electric Company', 0],
						  ['States Avenue', 0],
						  ['Virginia Avenue', 0],
						  ['Pennsylvania Railroad', 0],
						  ['St. James Place', 0],
						  ['Community Chest 2', 0],
						  ['Tennessee Avenue', 0],
						  ['New York Avenue', 0],
						  ['Free Parking', 0],
						  ['Kentucky Avenue', 0],
						  ['Chance 2', 0],
						  ['Indiana Avenue', 0],
						  ['Illinois Avenue', 0],
						  ['B. & O. Railroad', 0],
						  ['Atlantic Avenue', 0],
						  ['Ventnor Avenue', 0],
						  ['Water Works', 0],
						  ['Marvin Gardens', 0],
						  ['Go To Jail', 0],
						  ['Pacific Avenue', 0],
						  ['North Carolina Avenue', 0],
						  ['Community Chest 3', 0],
						  ['Pennsylvania Avenue', 0],
						  ['Short Line', 0],
						  ['Chance 3', 0],
						  ['Park Place', 0],
						  ['Luxury Tax', 0],
						  ['Boardwalk', 0],
						  ['Jail', 0]]


def main():
	player = Player()
	board = Board()
	iterations = 100000

	for i in range(iterations):
		board.movePlayer(player)

	totalMoves = 0
	for p in board.positions:
		totalMoves += p[1]
	print totalMoves

	for p in board.positions:
		print "{:.2f}%: {!s}".format(p[1] / float(totalMoves) * 100, p[0])

if __name__ == "__main__":
	main()