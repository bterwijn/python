import pygame  # pip install pygame

pygame.init()  # initialize pygame
surface = pygame.display.set_mode((800, 600))  # create drawing surface (window)

surface_size = surface.get_size()
print(surface_size)  # (800, 600)

white = pygame.colordict.THECOLORS['white']
pygame.draw.line(surface, white, (100, 100), (700, 100), 4)

red = pygame.colordict.THECOLORS['red']
pygame.draw.line(surface, red, (700, 100), (700, 500), 20)

pygame.draw.circle(surface, red, (200, 400), 100, 10)

pygame.display.flip()  # update the surface

pygame.time.wait(100000)  # wait 100sec

