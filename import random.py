import random
def russian_roulette():
  game = input("lets play shall we... casual or extreme")
  if game == "extreme":
    print("2 bullets")
    trigger = random.choice("click", "click", "click", "boom", "click" "boom",)
    if trigger == "boom":
      print("game over")
      return game 
  elif game == "casual":
    print("1 bullets")
    trigger == random.choice("click", "click", "click", "click", "click" "boom",)
    if trigger == "boom":
      print("game over")
      return game 
  else:
    return game
  
russian_roulette()