from pyray import init_window, set_target_fps

F_W, F_H = 1280, 720
FPS = 125

def init_disp(fps = FPS, width=F_W, height=F_H):
  init_window(F_W, F_H, b"Fly")
  set_target_fps(fps)
