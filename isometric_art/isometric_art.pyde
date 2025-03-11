def setup():
  size(400, 400, P3D)
  ortho()

def draw():
  background(220)

  lights()
  fill(255)
  stroke(0)
  count = 1
  h = (10 *  25)/2
  for i in range(10):
    for j in range(count):
      push()
      w = (count * 25) / 2
      x = map(j, 0, count, -w, w) + 25/2
      translate(x+width/2, (h / 2 + i * 25))
      rotateX(-PI/4)
      rotateY(-PI/4)
      box(15)
      pop()
    count+= 1
    
  # helper line for centering object on screen
  # stroke(255, 0, 0)
  # line(width/2, 0, width/2, height)
  # line(0, height/2, width, height/2)
