def setup():
    size(400, 400)
    noiseSeed(50)
    
def draw():
    background(220)
    inc = 0.1
    r = 25
    xoff = 0 + frameCount * 0.01
    yoff = 1000 + frameCount * 0.01
    fill(255,0,0)
    strokeWeight(2)
    circle(noise(xoff) * width, noise(yoff) * height, r * 2)
    xoff += inc
    yoff += inc
    circle(noise(xoff) * width, noise(yoff) * height, r * 2)
    xoff += inc
    yoff += inc
    circle(noise(xoff) * width, noise(yoff) * height, r * 2)
    xoff += inc
    yoff += inc
    circle(noise(xoff) * width, noise(yoff) * height, r * 2)
    xoff += inc
    yoff += inc
    circle(noise(xoff) * width, noise(yoff) * height, r * 2)
    xoff += inc
    yoff += inc
    circle(noise(xoff) * width, noise(yoff) * height, r * 2)
    xoff += inc
    yoff += inc
    circle(noise(xoff) * width, noise(yoff) * height, r * 2)
    xoff += inc
    yoff += inc
    circle(noise(xoff) * width, noise(yoff) * height, r * 2)
    xoff += inc
    yoff += inc
    circle(noise(xoff) * width, noise(yoff) * height, r * 2)
    xoff += inc
    yoff += inc
    circle(noise(xoff) * width, noise(yoff) * height, r * 2)
    xoff += inc
    yoff += inc
