import random

class Pig: # creates Pig class

    def __init__(self, player1_human = True, player2_human = False): # defines two players in the Pig class
        self.die = Die()
        self.p1 = Player('Player 1', player1_human)
        self.p2 = Player('Player 2', player2_human)

    def play(self): # defines the parameters of the game and how a player wins

        while(self.p1.score < 100 and self.p2.score < 100):
            self.p1.move()
            if self.p1.score < 100:
                self.p2.move()
        if (self.p1.score > self.p2.score):
            print('Player 1 wins!')
        else:
            print('Player 2 wins!')

class Player: # creates Player class

    def __init__(self, title, human_player = False):
        self.name = title
        self.is_human = human_player
        self.score = 0
        self.die = Die(6)

    def move(self):
        if self.is_human:
            self.player_roll()
        else:
            self.computer_roll()

    def player_roll(self):
        round_score = 0
        roll_again = 'y'

        while roll_again == 'y':
            self.die.roll()
            roll = self.die.face
            if roll == 1:
                print(f'{self.name} rolled a 1!')
                round_score = 0
                roll_again = 'n'
            else:
                print(f'{self.name} rolled a {roll}!')
                round_score += roll
                roll_again = input('Would you like to roll again? (y/n) ')
        self.score += round_score
        print(f'{self.name}\'s turn is over!')
        print(f'{self.name}\'s total score is {self.score}')


    def computer_roll(self):
        round_score = 0
        again = 'y'

        #establish a while loop for the computer's turn
        while again == 'y':
            self.die.roll()
            roll = self.die.face
            if roll == 1:
                print('{} rolled a 1'.format(self.name))
                round_score = 0
                again = 'n'
            else:
                print( '{} rolled a {}'.format(self.name,roll))
                round_score = round_score+roll
                if round_score < 20:
                    print('{} will roll again'.format(self.name))
                else:
                    again = 'n'
        self.score += round_score
        print( 'Turn is over')
        print( "{}'s round score is {}".format(self.name,round_score))
        print( "{}'s total score is {}\n\n".format(self.name,self.score))

class Die:

    def __init__(self, n = 6):
        self.sides = n
        self.roll()

    def roll(self):         #defines the die roll action
        self.face = int(random.random() * self.sides + 1)


if __name__ == "__main__":
    print('Welcome to Pig!')
    game = Pig()
    game.play()
    print('Thanks for playing!')