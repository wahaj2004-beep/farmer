import pgzrun
import pygame
import random

WIDTH = 600
HEIGHT = 600

farmer = Actor("farmer")
carrot = Actor("carrot")
carrot._surf = pygame.transform.scale(carrot._surf, (60, 60))
carrot._update_pos()

farmer.pos = (300,300)
carrot.pos = (random.randint(50,WIDTH-50), random.randint(50,HEIGHT-50))
score = 0

def draw():
    screen.fill((50, 200, 50))
    carrot.draw()
    farmer.draw()
    screen.draw.text(f"Score: {score}", (10,10), color="white", fontsize=30)

def update():
    global score
    if keyboard.left: farmer.x -= 5
    if keyboard.right: farmer.x += 5
    if keyboard.up: farmer.y -= 5
    if keyboard.down: farmer.y += 5

    if farmer.colliderect(carrot):
        score += 1
        if farmer.colliderect(carrot):
          carrot.x = random.randint(50,550)
          carrot.y = random.randint(50,550)



pgzrun.go()