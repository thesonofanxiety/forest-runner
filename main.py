from pyray import init_audio_device, get_frame_time, begin_drawing, end_drawing, window_should_close, draw_fps, close_window, close_audio_device, init_physics, set_config_flags, FLAG_MSAA_4X_HINT
from src.display import init_disp
from src.scenes import next_scene
from src.menus import Menu
from src.level import Level
from src.debug import DEBUG

set_config_flags(FLAG_MSAA_4X_HINT)
init_disp()                   # initialize graphics
init_audio_device()           # initialize audio

scenes = {
  'menu' : Menu,
  'level' : Level
}

current_scene = [scenes['menu']]# make scene variable behave like reference with help of python list mechanic
current_scene[0].init()         # initialize first scene

def main_loop(current_scene):
  dt = get_frame_time()         # time between frames
  current_scene[0].process(dt)  # game logic
  begin_drawing()               # drawing
  current_scene[0].draw()       # draw scene
  if DEBUG: draw_fps(10,50)     # draw fps counter
  end_drawing()                 # end of drawing
  if not current_scene[0].next == None: # scene changing mechanic
    current_scene[0] = next_scene(scenes,current_scene[0], scenes[current_scene[0].next])

def closing_events(current_scene):  # run when program should exit
  current_scene[0].close()
  close_audio_device()
  close_window()

while not window_should_close() and not current_scene[0].exit:
  main_loop(current_scene)

closing_events(current_scene)
