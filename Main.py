import random
import math
from Models.Tile import Tile
from helperFunctions import mapRelatedFun
from pprint import pprint

Main: any

def mapSpace(length: int, width: int) -> int:
  map = [];
  for i in range(length):
    map.append([]);
    for j in range(width):
          map[i].append(Tile.getTileType(Tile("")));
     
  return map;

def main():
  length = int(input("Enter the length of the map: "));
  width = int(input("Enter the width of the map: "));
  mapGen = mapSpace(length, width);
  pprint(mapGen);

if __name__ == "__main__":
    main();