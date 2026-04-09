from random import random


def printMap(map: list) -> None:
  for i in range(len(map)):
    for j in range(len(map[i])):
      print(map[i][j], end=" ");
    print();

def randStartPos(map: list) -> tuple:
  x = random.randint(0, len(map) - 1);
  y = random.randint(0, len(map[0]) - 1);
  return (x, y);