import random
class Tile:
  def __init__(self, tileType: str):
    self.tileType = tileType;
    self.tileValue = 0;
  def getTileType(self) -> str:
    randomNum = random.randint(0, 4);
    if randomNum == 0:
      self.tileType = "grass";
      self.tileValue = 0;
    elif randomNum == 1:
      self.tileType = "forest";
      self.tileValue = 1;
    elif randomNum == 2:
      self.tileType = "hill";
      self.tileValue = 2;
    elif randomNum == 3:
      self.tileType = "mountain";
      self.tileValue = 3;
    elif randomNum == 4:
      self.tileType = "road";
      self.tileValue = -1;
    return self.tileType;
