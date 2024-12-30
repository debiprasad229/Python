class phone:
    def make_call(self):
        print("make a call")
    def play_game(self):
            print("play a game")
p1=phone()
p1.make_call()
p1.play_game()
# adding parameters to class
class phone:
     def set_color(self,color):
          self.color=color
     def set_cost(self,cost):
          self.cost=cost
     def show_color(self):
          return self.color
     def show_cost(self):
          return self.cost
     def play_game(self):
          print("playing a game")     
     def make_call(self):
        print("make a call")
p2=phone()
p2.set_color('blue')
p2.set_cost(500)
print(p2.show_color())
print(p2.show_cost())
print(p2.play_game())
