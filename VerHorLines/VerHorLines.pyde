def setup ():
    size(400, 400)
    colorMode(HSB)

def draw():
    background(255)
    
    xinc = map(mouseY, 1, height, 1, 50)
    xinc = constrain(xinc, 10, float('inf'))

    for x in range(0, width, int(xinc)):
        h = (map(x, 0, width, 0, 360) + frameCount) % 360
        stroke(h, 255, 255)
        strokeWeight(4)
        line(x, 0 ,x, height)
        
    yinc = map(mouseX, 1, width, 1, 50)
    yinc = constrain(yinc, 10, float('inf'))
    
    for y in range(0, height, int(yinc)):
        h = (map(y, 0, height, 0, 360) + frameCount) % 360
        stroke(h, 255, 255)
        strokeWeight(4)
        line(0, y, width, y)
