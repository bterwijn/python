import pygame

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
        # self.ship = ...
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
            print("left")
        # ...

    def draw_game(self):
        """ Draws the state of the game to the drawing surface """
        self.surface.fill((0, 0, 0))
        white = pygame.colordict.THECOLORS['white']
        size = pygame.Vector2(self.surface.get_size())
        pygame.draw.circle(self.surface, white, size / 2, 20, 2)
        pygame.display.flip()  # update the surface


main()
