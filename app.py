import pygame
import time

pygame.init()
clock = pygame.time.Clock()

font = pygame.font.Font("fonts/Roboto-Regular.ttf", 24)
text = font.render('123456789', False, 'White')
button = pygame.Surface((50, 20))
text_rect = text.get_rect(center=(button.get_width() /2,
            button.get_height()/2))

pygame.init()
screen = pygame.display.set_mode((640, 360))
pygame.display.set_caption("washing machine")
icon = pygame.image.load('img/washing-machine.jpg')
pygame.display.set_icon(icon)

bg = pygame.image.load('img/background.jpg')
washing_machine = pygame.image.load('img/washing-machine.jpg')
clothing = pygame.image.load('img/clothing.png')



running = True
while running:
    screen.blit(bg, (0, 0))
    screen.blit(washing_machine, (192, 29))

    clothing = pygame.transform.rotate(clothing, -90)
    washing_machine.blit(clothing, (77, 100))
    washing_machine.blit(button, (0, 0))
    button.blit(text, text_rect)

    pygame.display.update()
    clock.tick(10)




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

