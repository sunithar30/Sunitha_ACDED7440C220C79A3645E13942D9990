#Implement a class called player that represents a criket player.
#The player class should havea method called play() which prints"The player is playing cricket.
#Derive two classes, Batsman and Bowler, from the player class. Override the play() method in each derived class to print "The batsman is batting" and "The bowler is bowling",respectively.
#Write a program to create objectes of both the Batsman and Bowler classes and call the play() method for each object.


#define the base class player
class player:
    def play(self):
        print("The player is playing cricket.")

#define the derived class Batsman
class Batsman(player):
    def play(self):
        print("The batsman is batting.")

#define the dervied class Bowler
class Bowler(player):
    def play(self):
        print("The blower is bowling.")

#create object of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

#call the play() method for each object
batsman.play()
bowler.play()