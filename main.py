import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    #stop game if turtle collided with car
    for cars in car_manager.all_cars:
      if cars.distance(player) < 20:
        game_is_on = False
        scoreboard.game_over()
      
      #make turtle to the startinf position if it cross the road
    if player.race_finished():
      player.start()
      #leveling up the scoreboard as well as speed of the car
      car_manager.level_up()
      scoreboard.increase_level()


    
