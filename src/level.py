from src.display import F_W, F_H
from src.scenes import Scene, next_scene
from src.background import init_background, draw_background, process_background, unload_background, SKY
from src.ground import init_ground, draw_ground, process_ground, unload_ground
from src.player import Player, STARTING_POS, load_player, unload_player
from src.obstacle import Obstacle, load_obstacles, unload_obstacles
from src.saves_and_settings import handle_settings, save_highscore, draw_highscore
from pyray import create_physics_body_rectangle, WHITE, load_font, unload_font, draw_text_ex, BLACK, Vector2, check_collision_recs, is_key_released, KEY_BACKSPACE, KEY_SPACE, measure_text_ex
from random import randint

GROUND_VEL = 92
MAX_GROUND_VEL = 450

def lvl_init(self):
  self.font = load_font("res/fonts/Romulus.ttf")
  self.background, self.scroll = init_background()
  self.dead = False
  self.ground_vel = 50
  self.timer  = 0
  self.player = Player(self)
  self.obstacles = []
  self.dead = False
  self.high_score = handle_settings()
  self.exit = False
  load_obstacles(self)
  load_player(self)
  init_ground(self)
  
def lvl_process(self, dt):
  if not self.dead:
    self.timer += 2*dt
    if self.ground_vel >= MAX_GROUND_VEL:
      self.ground_vel = MAX_GROUND_VEL
    else:
      self.ground_vel += 10*dt
    if round(self.timer*10)%3 == 0:
      if randint(0,1000) < 9:
        tp = randint(0, len(self.trees)-1)
        self.obstacles.append(Obstacle(self,self.trees[tp].width, self.trees[tp].height, tp))
    for ind, obst in enumerate(self.obstacles):
      obst.process(self,dt)
      if obst.body.x+obst.body.width <0:
        del self.obstacles[ind]
    self.player.handle_movement(self, dt)
    process_background(self.background, self.scroll, dt, v=self.ground_vel)
    process_ground(self, dt, v=self.ground_vel)
    if self.player.body.x > F_W or self.player.body.x < 0 - self.player.body.width:
      self.dead = True
    if any([check_collision_recs(self.player.body, obs.body) for obs in self.obstacles]):
      self.dead = True
  else:
    if is_key_released(KEY_SPACE):
      cs = round(self.timer,1)
      if cs > self.high_score:
        self.high_score = round(self.timer,1)
        save_highscore(self.high_score)
      self.obstacles = []
      self.ground_vel = GROUND_VEL
      self.timer = 0
      self.dead = False
      self.player.body.x = STARTING_POS[0]
      self.player.body.y = STARTING_POS[1]
    if is_key_released(KEY_BACKSPACE):
      cs = round(self.timer,1)
      if cs > self.high_score:
        self.high_score = round(self.timer,1)
        save_highscore(self.high_score)
      self.obstacles = []
      self.ground_vel = GROUND_VEL
      self.timer = 0
      self.dead = False
      self.player.body.x = STARTING_POS[0]
      self.player.body.y = STARTING_POS[1]
      self.next = 'menu'

  #if dead:
  #  self.next = Menu
  
def lvl_draw(self):
  draw_background(self.background, self.scroll)
  draw_text_ex(self.font, "Current score: {:.1f}".format(self.timer),Vector2(10,10),32,1,BLACK)
  self.player.draw(self)
  for i in self.obstacles:
    i.draw(self)
  if self.dead:
    t_w = measure_text_ex(self.font, "You died!",64,1)
    draw_text_ex(self.font, "You died!",Vector2(F_W/2-t_w.x/2,F_H/2-t_w.y/2),64,1,BLACK)
    t_w = measure_text_ex(self.font, "Press space to try again",32,1)
    draw_text_ex(self.font, "Press space to try again",Vector2(F_W/2-t_w.x/2,F_H/2-t_w.y/2+200),32,1,BLACK)
    t_w = measure_text_ex(self.font, "Press backspace to exit to menu",32,1)
    draw_text_ex(self.font, "Press backspace to exit to menu",Vector2(F_W/2-t_w.x/2,F_H/2-t_w.y/2+250),32,1,BLACK)
  draw_ground(self)
  draw_highscore(self)

  
def lvl_close(self):
  unload_background(self.background)
  unload_obstacles(self)
  unload_player(self)
    
Level = Scene(lvl_init, lvl_process, lvl_draw, lvl_close)
