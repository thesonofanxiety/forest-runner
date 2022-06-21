import csv
from os.path import exists
from src.display import F_W, F_H
from pyray import measure_text_ex, draw_text_ex, Vector2, BLACK

DEFAULT_HIGHSCORE = 15

def load_highscore(path: str = "./user_data/high_score.dat"):
  with open(path,'r') as f:
    s = f.read()
    return float(s)

def save_highscore(highscore, path: str = "./user_data/high_score.dat"):
  with open(path,'w') as f:
    s = f.write(str(highscore))

def handle_settings(path: str = "./user_data/high_score.dat"):
  if exists(path):
    return load_highscore(path)
  else:
    save_highscore(DEFAULT_HIGHSCORE)
    return DEFAULT_HIGHSCORE

def draw_highscore(self):
  s = f"High score: {self.high_score}"
  ts = measure_text_ex(self.font, s,32,1)
  draw_text_ex(self.font, s,Vector2(F_W-10-ts.x, 10),32,1,BLACK)

