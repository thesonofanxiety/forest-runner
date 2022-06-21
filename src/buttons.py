from copy import deepcopy
from pyray import draw_texture_rec, check_collision_point_rec, is_mouse_button_released, is_mouse_button_down, MOUSE_BUTTON_LEFT, WHITE, Vector2, Rectangle,\
                  load_texture, draw_text_ex, load_sound, unload_sound, unload_texture, measure_text_ex, play_sound, wait_time, stop_sound, BLACK, begin_drawing, end_drawing

from src.level import Level



FRAME_H = (49,49,45)
FRAME_Y = (0, 49, 98)



class Button:
  def __init__(self,text: str, pos: Vector2, scene, func):
    self.text   = text
    self.pos    = pos
    self.state  = 0
    self.action = False
    self.func   = func
    self.bounds = Rectangle(pos.x, pos.y, scene.btn.width, 49)
    self.view   = Rectangle(0,0, scene.btn.width, FRAME_H[0])
    self.text_size = measure_text_ex(scene.font,self.text, 32, 1)
    
  def process(self,scene):
    if self.state == 2:
      self.pos.y -= 4
    self.action = False
    if check_collision_point_rec(scene.mouse_point, self.bounds):
      if is_mouse_button_down(MOUSE_BUTTON_LEFT):
        self.state = 2
        self.pos.y += 4
      else: 
        self.state = 1
      if is_mouse_button_released(MOUSE_BUTTON_LEFT):
        self.action = True
    else:
      self.state = 0
    self.view.y = FRAME_Y[self.state]
    self.view.height = FRAME_H[self.state]
    if self.action:
      play_sound(scene.btn_sfx)
      self.func()
      
  def draw(self,scene):
    draw_texture_rec(scene.btn, self.view, self.pos, WHITE)
    draw_text_ex(scene.font,self.text,Vector2(self.pos.x+scene.btn.width/2-self.text_size.x/2,
                                              self.pos.y+scene.btn.height/6-self.text_size.y/2),32,1,WHITE)
    
def load_btn(self):
  self.btn      = load_texture("res/imgs/button/btn.png")
  self.btn_sfx  = load_sound("res/sfx/button_sfx.mp3")
    
def unload_btn(self):
  begin_drawing()
  draw_text_ex(self.font, "Loading...", Vector2(10,10), 32, 1, BLACK)
  end_drawing()
  wait_time(1100)
  unload_texture(self.btn)
  unload_sound(self.btn_sfx)