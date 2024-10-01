import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("washing machine")
icon = pygame.image.load('img/washing-machine.jpg')
pygame.display.set_icon(icon)

square = pygame.Surface((50, 170))
square.fill("Blue")

washing_machine = pygame.image.load('img/washing-machine.jpg')

running = True
while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, "Red", (50, 50), 30)
    screen.blit(square, (275, 65))
    screen.blit(washing_machine, (0, 0))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

