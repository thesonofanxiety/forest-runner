from pyray import Vector2, is_key_down, KEY_RIGHT, KEY_LEFT, KEY_UP, BLACK, draw_rectangle_lines_ex, Rectangle, WHITE, get_fps, load_texture, unload_texture,draw_texture_rec
from itertools import chain, cycle, count
from src.display import F_W, F_H
from src.debug import DEBUG
#from src.level import 

VEL = 475
STARTING_POS = (300,101)

class Player:
    def __init__(self, scene):
        self.body = Rectangle(float(300), float(101), float(30), float(30))
        self.velocity = Vector2(0,50)
        self.frame_ctr = 0
        self.current = 0
        self.draw_rec = Rectangle(0,0,80,80)
        self.state = 0
    def handle_movement(self,scene,dt):
        if self.is_on_ground(scene):
            self.body.y = F_H-84
            self.velocity.y = 0
            self.state = 0
        else:
            self.velocity.y += 125*15*dt
        if is_key_down(KEY_RIGHT):
            self.velocity.x = VEL
            self.state = 1
        elif is_key_down(KEY_LEFT):
            self.velocity.x = -VEL
            self.state = 1
        else:
            self.velocity.x = 0
        if is_key_down(KEY_UP) and self.is_on_ground(scene):
            self.velocity.y = -900
            self.state = 2
        self.velocity.x -= scene.ground_vel
        self.body.x += self.velocity.x*dt
        self.body.y += self.velocity.y*dt
        self.frame_ctr += 1

        if (self.frame_ctr >= get_fps()/15):
            self.frame_ctr = 0
            self.current += 1

            idd = scene.player_tex[self.state].width/80

            if (self.current > idd - 1):
                self.current = 0

            self.draw_rec.x = self.current*80
        

    def is_on_ground(self, scene):
        return self.body.y >= F_H-85
    def draw(self,scene):
        global DEBUG
        if DEBUG: draw_rectangle_lines_ex(self.body,1, WHITE)
        draw_texture_rec(scene.player_tex[self.state],self.draw_rec, Vector2(self.body.x-25/2, self.body.y-25), WHITE)
   
def load_player(self):
    self.player_tex = [load_texture('res/imgs/player/idle.png'),load_texture('res/imgs/player/run.png'), load_texture('res/imgs/player/jump.png')]

def unload_player(self):
    for i in self.player_tex:
        unload_texture(i)

