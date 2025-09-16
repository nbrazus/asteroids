import pygame
from constants import *
from player import *
from circleshape import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    dt = 0 
    asteroids = pygame.sprite.Group()
    updatable = pygame.spirte.Group()
    drawable = pygame.sprite.Group()
    player.containers = (drawable, updatable)
    asteroids.containers = (asteroids, drawable, updatable)
    while 1 == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(BLACK)
        for x in drawable:
            drawable.draw(x)
        updatable.update(dt)
        pygame.display.flip()
        
        clock.tick(60)
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
