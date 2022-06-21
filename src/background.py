from pyray import load_texture, clear_background, draw_texture_ex, Color, Vector2, WHITE, unload_texture
from src.display import F_H, F_W

SKY = Color( 221, 243, 248 )

def init_background():
  tr1 = load_texture("res/imgs/background/00_trees.png")
  tr2 = load_texture("res/imgs/background/01_trees.png")
  tr3 = load_texture("res/imgs/background/02_trees.png")
  mnt = load_texture("res/imgs/background/03_mountain.png")
  cld = load_texture("res/imgs/background/04_clouds.png")

  return ((cld,mnt,tr3,tr2,tr1), [0]*5)

def process_background(background, scroll, dt, v=20):
  for i in range(len(scroll)):
    scroll[i] -= (i-0.1)*dt*v/len(background)
    if scroll[i] <= -background[i].width:
      scroll[i] = 0

def draw_background(background, scroll):
  clear_background(SKY)
  for i in range(len(scroll)):
   draw_texture_ex(background[i], Vector2(scroll[i], -F_H/2), 0, 1, WHITE)
   draw_texture_ex(background[i], Vector2(background[i].width + scroll[i], -F_H/2), 0, 1, WHITE)

def unload_background(background):
  for i in background:
    unload_texture(i)
