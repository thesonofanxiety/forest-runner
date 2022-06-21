from src.display import F_W, F_H
from src.buttons import Button, load_btn, unload_btn
from src.scenes import Scene, next_scene
from src.background import SKY
from src.saves_and_settings import handle_settings, draw_highscore
from pyray import get_mouse_position, unload_font, Vector2, draw_text_ex, WHITE, clear_background, load_font, BLACK, load_texture, unload_texture, draw_texture_ex,\
                  is_key_released, KEY_BACKSPACE, measure_text_ex, draw_rectangle_rec, Rectangle, draw_rectangle_lines_ex

TITLE_H = F_H/2
BUTTONS_H = F_H - TITLE_H

def go_to_level(self):
  self.next = 'level'

def display_rules(self):
  self.current_layout = 1

def exit_game(self):
  self.exit = True

def init_menu(self):
  self.font = load_font("res/fonts/Romulus.ttf")
  self.title = load_texture("res/imgs/title.png")
  self.background = load_texture("res/imgs/background/static.png")
  self.high_score = handle_settings()
  self.rules_rect = Rectangle(F_W/2-700/2, F_H/2-300/2+20 ,700,300)
  self.exit = False
  load_btn(self)
  self.main_btns = [
      Button("Start",     Vector2(F_W/2-self.btn.width/2, F_H/2-self.btn.height//3+200),                self,lambda: go_to_level(self)),
      Button("Rules",     Vector2(F_W/2-self.btn.width/2, F_H/2-self.btn.height//3+265),                self,lambda: display_rules(self)),
      Button("Exit",      Vector2(F_W/2-self.btn.width/2, F_H/2-self.btn.height//3+330),                self,lambda: exit_game(self))
  ]
  self.current_layout = 0

def process_menu(self, dt):
  self.mouse_point = get_mouse_position()
  if self.current_layout == 0:
    for btn in self.main_btns:
      btn.process(self)
  if self.current_layout == 1:
    if is_key_released(KEY_BACKSPACE):
      self.current_layout = 0
  
def draw_menu(self):
  clear_background(SKY)
  draw_texture_ex(self.background,Vector2(0,-F_H/2),0,1,WHITE)
  if self.current_layout == 0:
    draw_texture_ex(self.title,Vector2(F_W/2-self.title.width/2, TITLE_H/2-self.title.height/2),0,1,WHITE)
    draw_text_ex(self.font, "by thesonofanxiety",Vector2(F_W/2+self.title.width/2-180, TITLE_H/2+self.title.height/2-20),20,1,BLACK)
    for btn in self.main_btns:
      btn.draw(self)
    draw_highscore(self)
  if self.current_layout == 1:
    draw_rectangle_rec(self.rules_rect, WHITE)
    draw_rectangle_lines_ex(self.rules_rect,3,BLACK)
    ts1 = measure_text_ex(self.font, "Avoid trees using arrows.",32,1)
    draw_text_ex(self.font, "Avoid trees using arrows.",Vector2(F_W/2-ts1.x/2,F_H/2-ts1.y/2-20),32,1,BLACK)
    ts2 = measure_text_ex(self.font, "To exit press ESC.",32,1)
    draw_text_ex(self.font,"To exit press ESC.",Vector2(F_W/2-ts2.x/2,F_H/2-ts2.y/2+20),32,1,BLACK)
    ts2 = measure_text_ex(self.font, "Press backspace to go back to menu.",32,1)
    draw_text_ex(self.font,"Press backspace to go back to menu.",Vector2(F_W/2-ts2.x/2,F_H/2-ts2.y/2+60),32,1,BLACK)
    
def unload_menu(self):
  unload_btn(self)

  unload_font(self.font)
  unload_texture(self.title)
  pass
  
Menu = Scene(init_menu, process_menu, draw_menu, unload_menu)