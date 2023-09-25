import random
import math

class Team:
   def __init__(self, name, attack, midfield, defense, goalkeeper):
       self.name = name
       self.attack = attack
       self.midfield = midfield
       self.defense = defense
       self.goalkeeper = goalkeeper

   def get_score(self):
       # Calculate the number of goals using the logistic function
       x = self.attack / 10
       goals = round(random.gauss(x, 1))

       # We limit the number of goals in the range from 0 to 10
       goals = max(0, min(goals, 10))
       return goals

class Match:
   def __init__(self, team1, team2):
       self.team1 = team1
       self.team2 = team2
       self.score1 = 0
       self.score2 = 0

   def play(self):
       while True:
           # Generating the number of goals for each team
           self.score1 = self.team1.get_score()
           self.score2 = self.team2.get_score()

           # Checking if the result is logical
           if abs(self.score1 - self.score2) < 3:
               break

       return f"{self.team1.name} {self.score1} : {self.score2} {self.team2.name}"

# Creating Command Objects
team1 = Team("Chelsea", 1, 1, 99, 99)
team2 = Team("Liverpool", 99, 99, 1, 1)

# Create a match object and start the game
match = Match(team1, team2)
print(match.play())
print("gg")