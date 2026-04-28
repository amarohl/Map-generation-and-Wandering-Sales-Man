# from Tile import Tile
from helperFunctions import mapRelatedFun
class Wanderer:
  def __init__(self,posX: int, posY: int):
    self.posX = posX;
    self.posY = posY;
    # self.sight = sight;
    # Tile.tileType = "WANDER";
    # self.tile.tileType = "Wanderer";
    # self.tile.tileValue = 0;
  # def __getpos__(self): 
  def exists(self):
    if(mapRelatedFun.printMap(map, self.pos) == self.pos):
      return True;

  def move(self):
    self.pos = map[0] + 1;
    return self.pos;