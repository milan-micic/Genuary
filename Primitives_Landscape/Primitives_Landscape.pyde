def setup():
  size(400,400)


def draw():
  background(100, 200, 255)

  randomSeed(50)

  fill(100, 50, 0)
  triangle(50, 320, 550, 320, 300, 50)
  triangle(-150, 320, 250, 320, 100, 175)

  clouds(100, 100)
  clouds(300, 125)
  
  fill(0, 100, 0)
  rect(0, 300, width, 350)

def clouds(xx, yy):
  for i in range(50):
    noStroke()
    fill(255, 150)
    x = random(-50, 50)
    y = random(-25, 25)
    circle(xx + x, yy + y, 50)
