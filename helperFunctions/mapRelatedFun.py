import random
from Models import wander


def printMap(map: list, wPosX:int, wPosY:int) -> None: #using this instead of prettyPrint to add wander
  # wandPosX = wPosX; # doulbe think this, might need to go in wander instead
  # wandPosY = wPosY; # double think this, might need to go in wnader instead
  for i in range(len(map)):
    for j in range(len(map[i])):
      # if(token.Wanderer.exists):
      #   map[i][j] = "WANDER";
      print(map[i][j], end=" ");
    print();

def randStartPos(map: list) -> tuple:
  x = random.randint(0, len(map) - 1);
  y = random.randint(0, len(map[0]) - 1);
  return (x, y);