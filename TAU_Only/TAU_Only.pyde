def setup():
  size(int(TAU)*int(TAU)*int(TAU),int(TAU)*int(TAU)*int(TAU))
  colorMode(HSB, int(TAU), int(TAU), int(TAU))

def draw():
  randomSeed(int(TAU))
  background(int(random(TAU)), int(random(TAU)), int(random(TAU)))
