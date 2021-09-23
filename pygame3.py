import pygame
import random

pygame.init()  # initialize pygame
surface = pygame.display.set_mode((800, 600))  # create drawing surface

clock = pygame.time.Clock()
running = True
step_count = 0
while running:
    surface.fill((0, 0, 0))

    for event in pygame.event.get():  # handle events
        if event.type == pygame.QUIT:
            running = False

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        print("left")
    if keys_pressed[pygame.K_RIGHT]:
        print("right")
    if keys_pressed[pygame.K_DOWN]:
        print("down")
    if keys_pressed[pygame.K_UP]:
        print("up")

    max_color = 255
    color = pygame.Color(random.randint(0, max_color),  # red
                         random.randint(0, max_color),  # green
                         random.randint(0, max_color))  # blue

    size = surface.get_size()  # (800, 600)
    x1 = random.randint(0, size[0])
    y1 = random.randint(0, size[1])
    x2 = random.randint(0, size[0])
    y2 = random.randint(0, size[1])

    width = 4
    pygame.draw.line(surface, color, (x1, y1), (x2, y2), width)

    pygame.display.flip()  # update the surface
    clock.tick(60)  # run at max 60 frames per second
    step_count += 1
