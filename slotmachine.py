

import random

def main():
	#pygame.init()
	
	slot_machine = SlotMachine()
	slot_machine.startGame()


class SlotMachine:
	def __init__(self):
		# Make the starting information like possible bets icons jackpot etc.
		self.icons = []
		self.createIcons()

	def startGame(self):
		self.setStartingValues()
		gameisGoing = True
		while(gameisGoing):
			print("The Game is starting")
			print("1: Set Bet")
			print("2: Spin")
			print("3: Quit")
			selection = raw_input(">>> ")

			if (selection == "1"):
				self.setBet()
			elif (selection == "2"):
				self.spin()
			elif (selection == "3"):
				gameisGoing = False
			else:
				print("Invalid Value entered")

	def setStartingValues(self):
		self.bet = 0
		self.money = 1000
		self.JackPot = 1000000
		self.numberOfWheels = 10
		self.numberOfIcons = 10

	def setBet(self):
		# setting a bet with 6 options
		# Take money out of account
		# Keep track of the amount for bet in game state?
		betSelected = False;
		betOptions = [1 , 10, 25, 50, 100, 200]

		print("What would you like to bet?")
		for i in range(len(betOptions)):
			print(str(betOptions[i]))

		selection = raw_input(">>> ")

		for i in range(len(betOptions)):
			if (selection == str(betOptions[i])):
				self.bet = selection
				betSelected = True

		if(betSelected == False):
			print("Invalid Value entered")

	def spin(self):
		
		# pay
		# change the jackpot
		# spin for things
		self.pay()
		self.increasePot()
		spinResults = []
		payouts = {}
		for i in range(self.numberOfWheels):
			val = random.randint(1, self.numberOfIcons)
			spinResults.append(val)
			if(val in payouts):
				payouts[val] = payouts[val] + 1
			else:
				payouts[val] = 0

		total = 0
		for m in payouts:
			total += payouts[m]

		self.money += total*int(self.bet)

		# For now, if any values match each other then it is 1 buck times thier bet
		
        
	def pay(self):
		self.money = self.money - int(self.bet)

	def increasePot(self):
		self.JackPot = self.JackPot + random.randint(100, 1000)

	def createIcons(self):
		self.icons.append(Icon("Bob","blue")) # make the icon with an icon object
		self.icons.append(Icon("Sam","red")) # make the icon with an icon object
		self.icons.append(Icon("Kim","yellow")) # make the icon with an icon object

class Icon:
	def __init__(self, name, color):
		self.name = name
		self.color = color
		

if __name__ == "__main__": main()