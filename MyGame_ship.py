import pygame
import random

def main():
    game = MyGame()
    game.run()

class MyGame:

    def __init__(self):
        """ Initalizes the Game """
        pygame.init()  # initialize pygame
        self.surface = pygame.display.set_mode((800, 600))  # create drawing surface
        self.running = True
        self.step_count = 0
        self.ship = Ship(pygame.Vector2(self.surface.get_size()) / 2)
         # self.aliens = ...

    def run(self):
        """ Runs the Game until it ends """
        clock = pygame.time.Clock()
        while self.running:
            self.step()
            clock.tick(60)  # run at max 60 frames per second

    def step(self):
        """ Moves Game one step forward """
        self.handle_events()
        self.handle_keyboard_events()
        self.draw_game()
        self.step_count += 1

    def handle_events(self):
        """ Handles events """
        for event in pygame.event.get():  # handle events
            if event.type == pygame.QUIT:
                self.running = False

    def handle_keyboard_events(self):
        """ Handles keyboard events """
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            self.ship.move(pygame.Vector2(-1, 0))
        if keys_pressed[pygame.K_RIGHT]:
            self.ship.move(pygame.Vector2(1, 0))
        if keys_pressed[pygame.K_UP]:
            self.ship.move(pygame.Vector2(0, -1))
        if keys_pressed[pygame.K_DOWN]:
            self.ship.move(pygame.Vector2(0, 1))

    def draw_game(self):
        """ Draws the state of the game to the drawing surface """
        self.surface.fill((0, 0, 0))
        self.ship.draw(self.surface)
        pygame.display.flip()  # update the surface

class Ship:
    """ The Ship the player controls """

    def __init__(self, position):
        """ Initalizes a ship on a 'position' (Vector2) """
        self.radius = 10
        self.speed = 3
        self.position = position
        self.color = pygame.colordict.THECOLORS['white']

    def move(self, step):
        """ Moves the ship by 'step' (Vector2) """
        self.position += step * self.speed

    def draw(self, surface):
        """ Draws the ship on the 'surface' """
        pygame.draw.circle(surface, self.color, self.position, self.radius)

main()
