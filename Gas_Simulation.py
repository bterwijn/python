import pygame
import random
import copy

def main():
    gas_simulation = Gas_Simulation()
    gas_simulation.run()

class Gas_Simulation:
    """ Gas_Simulation that simulates molecules moving and colliding """
    
    def __init__(self):
        """ Initalizes the Simulation """
        pygame.init()  # initialize pygame
        self.surface = pygame.display.set_mode((800, 600))  # create drawing surface
        nr_molecules = 50
        self.molecules = Molecules(nr_molecules, self.surface.get_size())

    def run(self):
        """ Runs the simulation until the program ends """
        clock = pygame.time.Clock()
        running = True
        while running:
            self.surface.fill((0, 0, 0))
            for event in pygame.event.get():  # handle events
                if event.type == pygame.QUIT:
                    running = False
            self.molecules.move(self.surface.get_size())
            self.molecules.draw(self.surface)
            pygame.display.flip()  # update the drawing surface
            clock.tick(60)  # run at max 60 frames per second

class Molecules:
    """ Container of all the Molecules in the gas """

    def __init__(self, nr_molecules, surface_size):
        """ Tries to add 'nr_molecules' to the an area given by 'surface_size' """
        self.molecules = []
        for i in range(nr_molecules):
            self.try_add_molecule(100, surface_size)
        print("nr_molecules:", len(self.molecules))

    def try_add_molecule(self, tries, surface_size):
        """ Tries 'tries' times to add a Molecule that doesn't collide and then give up """
        for i in range(tries): 
            molecule = Molecule(surface_size)  # initialize a random molecule
            collision_molecule = self.is_in_collision_with_other_molecule(molecule)  # test for collision
            if collision_molecule is None:  # if no collision add the molecule to this container
                self.molecules.append(molecule)
                break

    def move(self, surface_size):
        """ Moves each molecule in the container thereby handeling collisions with the
            border and other molecules """
        for molecule in self.molecules:
            old_position = copy.copy(molecule.get_position())  # remember old position by shallow copy
            molecule.move()
            if molecule.handle_collide_with_borders(surface_size): # if it has a collision with border
                molecule.set_position(old_position)  # restore old position
            collision_molecule = self.is_in_collision_with_other_molecule(molecule)
            if not collision_molecule is None:  # if it has a collision with a molecule
                molecule.handle_collision_with_molecule(collision_molecule)  # handle the collision
                molecule.set_position(old_position)  # restore old position

    def is_in_collision_with_other_molecule(self, molecule):
        """ Checks if 'molecule' is in collision with an other molecule.
        Return the molecule it is in collision with or return 'None'
        if no collision """
        for m in self.molecules:
            if molecule.is_in_collision(m):
                return m
        return None

    def draw(self, surface):
        """ Draws all Molecules to the 'surface' """
        for molecule in self.molecules:
            molecule.draw(surface)

class Molecule:
    """ A Molecule within the gas """
    radius = 8

    def __init__(self, surface_size):
        """ Initalizes a Molecule at a random position and random speed """
        random_x = random.uniform(Molecule.radius, surface_size[0] - Molecule.radius)
        random_y = random.uniform(Molecule.radius, surface_size[1] - Molecule.radius)
        self.position = pygame.Vector2(random_x, random_y)
        max_speed = 3
        random_sx = random.uniform(-max_speed, max_speed)
        random_sy = random.uniform(-max_speed, max_speed)
        self.speed = pygame.Vector2(random_sx, random_sy)

    def move(self):
        """ Moves the Molecule by its speed """
        self.position += self.speed

    def get_position(self):
        """ Returns the position of the Molecule """
        return self.position

    def set_position(self, position):
        """ Sets the position of the Molecule to 'position' """
        self.position = position

    def handle_collide_with_borders(self, surface_size):
        """Handles collision with the surface of size 'surface_size', returns
        True when there is a collision, False otherwise """
        if self.position[0] < Molecule.radius or self.position[0] > surface_size[0] - Molecule.radius:
            self.speed[0] = -self.speed[0]
            return True
        if self.position[1] < Molecule.radius or self.position[1] > surface_size[1] - Molecule.radius:
            self.speed[1] = -self.speed[1]
            return True
        return False

    def handle_collision_with_molecule(self, molecule):
        """ Handles collision with another 'molecule' by swaps the speed of the two molecules """
        temp = self.speed
        self.speed = molecule.speed
        molecule.speed = temp

    def is_in_collision(self, molecule):
        """ Returns True if Ship is in collision with 'molecule', False otherwise """
        if self is molecule:  # a molecule can't collide with itself
            return False
        return (self.position - molecule.position).length() < 2 * Molecule.radius

    def draw(self, surface):
        """ Draws Molecule to the 'surface' """
        color = pygame.Color(255, 255, 255)
        pygame.draw.circle(surface, color, self.position, Molecule.radius, 2)

    def get_grid_coordinate(self):
        """ Returns the grid coordinate of the molecule as a tuple  """
        return (int(self.position[0] // (2 * Molecule.radius)),
                int(self.position[1] // (2 * Molecule.radius)))

main()
