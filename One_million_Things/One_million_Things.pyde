import math

# State of spiral
x = y = None
px = py = None
step = 1
state = 0
numSteps = 1
turnCounter = 1

# Scale / resolution
stepSize = 1
totalSteps = None

def isPrime(value):
    if value == 1: 
        return False
    for i in range(2,int(math.sqrt(value))+1):
        if (value % i) == 0:
            return False
    return True

def setup():
  size(1000,1000)

  global step, x, y, px, py, stepSize, totalSteps

  # set up spiral
  cols = width / stepSize
  rows = height / stepSize
  totalSteps = 1000000
  x = width / 2
  y = height / 2
  px = x
  py = y
  background(127)

def draw():
  for count in range(1000):
    global step, x, y, stepSize, px, py, state, turnCounter, numSteps, totalSteps
    if isPrime(step):
      fill(255)
      stroke(255)
      circle(x, y, stepSize * 0.5)
    else:
      fill(0)
      stroke(0)
      circle(x, y, stepSize * 0.5)
      
    # Connect current to previous with a line

    px = x
    py = y

    # Move according to state

    while(True):
      if (state==0):
        x = x + stepSize
        break
      elif (state==1):
        y = y - stepSize
        break
      elif (state==2):
        x = x - stepSize
        break
      elif (state==3):
        y = y + stepSize
        break 

    # change state
    if (step % numSteps) == 0:
      state = (state + 1) % 4
      turnCounter += 1
      if turnCounter % 2 == 0:
        numSteps += 1
    step += 1

    if (x < 0):
      print(step)

    # are we done?
    if (step > totalSteps):
      noLoop()
      break
  
  print(step)
