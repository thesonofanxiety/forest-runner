from typing import Optional

class Scene:
  def __init__(self,init,proc,draw,close):
    self._init     = init
    self._process  = proc
    self._draw     = draw
    self._close    = close
    self.next      = None
  def init(self):
    self._init(self)
  def process(self, dt = None):
    self._process(self,dt)
  def draw(self):
    self._draw(self)
  def close(self):
    self._close(self)
  #def nextone(self):
  #  self.next.init()
  #  self.next.next = None
  #  self.close()
  #  return self.next
    
def next_scene(scenes,current: Optional[Scene] = None, n: Optional[Scene] = None):
  if current is None and n is None:
    raise ValueError(\
                    "At least one argument should be Scene object")
  if not current is None:
    current.close()
    current.next = None
  if not n is None:
    n.init()
    n.next = None
  return n
