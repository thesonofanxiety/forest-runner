from pyray import load_texture, clear_background, draw_texture_ex, Color, Vector2, WHITE, unload_texture
from src.display import F_H, F_W

SKY = Color( 221, 243, 248 )

def init_ground(self):
  self.ground = load_texture("res/imgs/ground.png")
  self.gr_scrl = 0

def process_ground(self, dt, v=20):
    self.gr_scrl -= dt*v
    if self.gr_scrl <= -self.ground.width:
      self.gr_scrl = 0

def draw_ground(self):
    draw_texture_ex(self.ground, Vector2(self.gr_scrl, -F_H/2+55), 0, 1, WHITE)
    draw_texture_ex(self.ground, Vector2(self.ground.width + self.gr_scrl, -F_H/2+55), 0, 1, WHITE)

def unload_ground(background):
    unload_texture(self.ground)
