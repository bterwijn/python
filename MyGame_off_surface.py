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
        self.aliens = Aliens()

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
        self.aliens.generate_alien(self.surface)
        self.aliens.move(self.surface)
        self.draw_game()
        if self.aliens.has_collision(self.ship):
            self.running = False
            print("Game over! score:", self.step_count)
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
        self.ship.stay_on_surface(self.surface)

    def draw_game(self):
        """ Draws the state of the game to the drawing surface """
        self.surface.fill((0, 0, 0))
        self.ship.draw(self.surface)
        self.aliens.draw(self.surface)
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

    def stay_on_surface(self, surface):
        """ Moves the ship back on the surface when it goes off """
        if self.position.x < 0:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = 0
        size = surface.get_size()
        if self.position.x > size[0]:
            self.position.x = size[0]
        if self.position.y > size[1]:
            self.position.y = size[1]

    def draw(self, surface):
        """ Draws the ship on the 'surface' """
        pygame.draw.circle(surface, self.color, self.position, self.radius)

class Aliens:
    """ Holds all aliens in the game """

    def __init__(self):
        """ Initalizes an empty container of Aliens """
        self.aliens = []
        self.generation_chance = 0.2

    def generate_alien(self, surface):
        """ By chance generate an alien at a random position at the top of 'surface' """
        if random.random() < self.generation_chance:
            size = surface.get_size()
            position = pygame.Vector2(random.randint(0, size[0]), 0)
            self.aliens.append(Alien(position))

    def move(self,surface):
        """ Moves all Aliens in this container """
        for alien in self.aliens:
            alien.move()
            if alien.is_off_surface(surface):
                self.aliens.remove(alien)

    def draw(self, surface):
        """ Draw all Aliens in this container """
        for alien in self.aliens:
            alien.draw(surface)

    def has_collision(self, ship):
        """ Check if 'ship' is in collision with any of the Aliens in this container """
        for alien in self.aliens:
            if alien.has_collision(ship):
                return True
        return False

class Alien:
    """ An Alien the player has to avoid touching """

    def __init__(self, position):
        """ Initalizes an Alien on a 'position' (Vector2) """
        self.radius = 6
        self.speed = 1.5
        self.position = position
        self.color = pygame.colordict.THECOLORS['red']

    def move(self):
        """ Moves an Alien one step """
        self.position.y += self.speed

    def is_off_surface(self, surface):
        """ Returns True if an Alien is off the surface, False otherwise """
        if self.position.x < 0 or self.position.y < 0:
            return True
        size = surface.get_size()
        if self.position.x > size[0] or self.position.y > size[1]:
            return True
        return False

    def draw(self, surface):
        """ Draws an Alien on the 'surface' """
        pygame.draw.circle(surface, self.color, self.position, self.radius)

    def has_collision(self, ship):
        """ Returns True of 'ship' is in collision this alien, False otherwise """
        distance = (self.position - ship.position).length()
        return distance < self.radius + ship.radius


main()
