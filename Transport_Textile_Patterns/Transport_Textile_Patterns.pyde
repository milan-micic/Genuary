x , y, sp = 0, 0, 40

def setup():
  size(400,400)
  background(50, 100, 75)

def draw():
  global x, y, sp
  stroke(255)
  r = random(1)
  if (r < 0.33):
    fill(255, 0, 255, 100)
    arc(x + sp, y + sp, sp * 2, sp * 2, radians(90), radians(180))
  elif (r < 0.67):
    fill(0, 255, 255, 100)
    arc(x, y, sp * 2, sp * 2, radians(0), radians(90))
  else:
    fill(255, 255, 0, 100)
    arc(x, y, sp * 2, sp * 2, radians(180), radians(270))
  x = x + sp
  if (x > width):
    x = 0
    y = y + sp