import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)    
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                sys.exit()
                
            # Delete an asteroid if a bullet reach into an asteroid
            for shot in shots:
                if shot.check_collision(asteroid):
                    asteroid.split()

        pygame.display.flip()

        # 60 FPS
        dt = game_clock.tick(60) / 1000 
         

if __name__ == "__main__":
    main()