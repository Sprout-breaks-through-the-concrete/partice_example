class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random(-2, 2)
        self.vy = random(-2, 2)
        self.alpha = 255

    def finished(self):
        return self.alpha < 0

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.alpha -= 5

    def show(self):
        fill(255, self.alpha)
        ellipse(self.x, self.y, 16, 16)

# Particle list
particles = []

def setup():
    size(800, 600)
    noStroke()

def draw():
    background(0)
    particles.append(Particle(mouseX, mouseY))

    for p in particles[:]:
        p.update()
        p.show()
        if p.finished():
            particles.remove(p)
