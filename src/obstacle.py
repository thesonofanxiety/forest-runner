from src.display import F_W, F_H
from pyray import WHITE, draw_rectangle_lines_ex, Rectangle, load_texture, unload_texture, draw_texture_ex, Vector2
from random import random
from src.debug import DEBUG

class Obstacle:
    def __init__(self,scene,width,height,kind):
        self.body = Rectangle(F_W+width, F_H-height-50, width, height)
        self.velocity = -scene.ground_vel
        self.type = kind
    def process(self,scene,dt):
        self.velocity = -scene.ground_vel
        self.body.x += self.velocity*dt
    def draw(self,scene):
        if DEBUG: draw_rectangle_lines_ex(self.body,1, WHITE)
        draw_texture_ex(scene.trees[self.type], Vector2(self.body.x, self.body.y), 0,1,WHITE)
        


def load_obstacles(self):
    self.trees = []
    for i in range(0,5):
        t = load_texture('res/imgs/trees/tr{}.png'.format(i+1))
        ts = load_texture('res/imgs/trees/trs{}.png'.format(i+1))
        self.trees.append(t)
        self.trees.append(ts)

def unload_obstacles(self):
    self.trees = []
    for i in self.trees:
        unload_texture(i)
    del self.trees