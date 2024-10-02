import pygame
import time

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.Font("fonts/Roboto-Regular.ttf", 15)

text_start = font.render('start', False, 'White')
button_start = pygame.Surface((40, 15))
text_rect_start = text_start.get_rect(center=(button_start.get_width() /2,
            button_start.get_height()/2))
button_start_rect = pygame.Rect(192 + 85, 29 + 30, 40, 15)



text_stop = font.render('stop', False, 'White')
button_stop = pygame.Surface((40, 15))
text_rect_stop = text_stop.get_rect(center=(button_stop.get_width() /2,
            button_stop.get_height()/2))
button_stop_rect = pygame.Rect(192 + 130, 29 + 30, 40, 15)

screen = pygame.display.set_mode((640, 360))
pygame.display.set_caption("washing machine")
icon = pygame.image.load('img/washing-machine.jpg')
pygame.display.set_icon(icon)

bg = pygame.image.load('img/background.jpg')
washing_machine = pygame.image.load('img/washing-machine.jpg')
clothing = pygame.image.load('img/clothing.png')


clock.tick(60)
running = True
num_rotate=0
while running:
    screen.blit(bg, (0, 0))
    screen.blit(washing_machine, (192, 29))


    washing_machine.blit(clothing, (77, 100))

    washing_machine.blit(button_start, (85, 30))
    button_start.blit(text_start, text_rect_start)

    washing_machine.blit(button_stop, (130, 30))
    button_stop.blit(text_stop, text_rect_stop)



    pygame.display.update()

    if num_rotate > 0 and working == True:
        if num_rotate < 120:
            clock.tick(60)
            print(int(num_rotate / 60))
        else:
            clock.tick(5)
            print(((num_rotate-120)/5)+(120/60))
        clothing = pygame.transform.rotate(clothing, -90)
        num_rotate -= 1



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_start_rect.collidepoint(pygame.mouse.get_pos()):
                num_rotate = 200
                working = True
            elif button_stop_rect.collidepoint(pygame.mouse.get_pos()):
                print(False)
                working = False

