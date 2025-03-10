def setup():
    size(640, 480)

def draw():
    background(220)
    total = 10
    for layer in range(total):
        xoff = layer * 1000 + frameCount*0.01
        stroke(0)
        strokeWeight(4)
        fill(255,150)
        beginShape()
        for i in range(width):
            n = noise(xoff)
            y = map(n, 0, 1, -150, 150)
            cy = map(layer, 0, total, 0, height)
            vertex(i, cy + y)
            
            xoff += 0.01
        vertex(width, height)
        vertex(0, height)
        endShape(CLOSE)
    
