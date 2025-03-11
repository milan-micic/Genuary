def setup():
    size(400,400,P3D)
    noiseSeed(50)
    
def draw():
    background(0)
    fill(0)
    # translate(-width / 2, -height / 2)
    lightSpecular(255, 255, 255)
    directionalLight(204, 204, 204, 0, 0, -1)
    specular(204, 102, 0)
    shininess(50)
    inc = 0.01
    r = 60
    xoff = 0 + frameCount * 0.01
    yoff = 1000 + frameCount * 0.01
    for i in range(100):
        circle(noise(xoff) * width, noise(yoff) * height, r * 2)
        xoff += inc
        yoff += inc
