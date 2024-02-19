import pygame
import sys
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Scrabble Game with Pygame")

# Couleurs
WHITE = (255, 255, 255)
LIGHTBLUE = (173, 216, 230)

# Distribution simplifiée des tuiles
tiles_distribution = {'A': 9, 'B': 2, 'C': 2}  # Exemple simplifié
tiles = []

font = pygame.font.Font(None, 36)

def create_tiles():
    for letter, count in tiles_distribution.items():
        for _ in range(count):
            tiles.append({'letter': letter, 'rect': pygame.Rect(random.randint(0, 800), random.randint(0, 600), 50, 50)})

create_tiles()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    for tile in tiles:
        pygame.draw.rect(screen, LIGHTBLUE, tile['rect'])
        text = font.render(tile['letter'], True, (0, 0, 0))
        screen.blit(text, (tile['rect'].x + 5, tile['rect'].y + 5))
    
    pygame.display.flip()

pygame.quit()
