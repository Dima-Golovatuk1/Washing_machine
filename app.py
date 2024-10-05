import pygame

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.Font("fonts/Roboto-Regular.ttf", 15)

text_start = font.render('start', False, 'White')
button_start = pygame.Surface((40, 15))
text_rect_start = text_start.get_rect(center=(button_start.get_width() /2,
            button_start.get_height()/2))
button_start_rect = pygame.Rect(192 + 75, 29 + 30, 40, 15)

text_stop = font.render('stop', False, 'White')
button_stop = pygame.Surface((40, 15))
text_rect_stop = text_stop.get_rect(center=(button_stop.get_width() /2,
            button_stop.get_height()/2))
button_stop_rect = pygame.Rect(192 + 120, 29 + 30, 40, 15)

time = 0
text_time = font.render(f'{time}', False, 'White')

font = pygame.font.Font("fonts/Roboto-Regular.ttf", 10)
text_fast = font.render('fast', False, 'White')
button_fast = pygame.Surface((40, 15))
text_rect_fast = text_fast.get_rect(center=(button_fast.get_width() /2,
            button_fast.get_height()/2))
button_fast_rect = pygame.Rect(192 + 178, 29 + 0, 40, 15)

text_intensely = font.render('intensely', False, 'White')
button_intensely = pygame.Surface((40, 15))
text_rect_intensely = text_fast.get_rect(center=(8,
            button_intensely.get_height()/2))
button_intensely_rect = pygame.Rect(192 + 178, 29 + 30, 40, 15)

sound_very_fast = pygame.mixer.Sound('sounds/sound_very_fast.mp3')
sound_intensely = pygame.mixer.Sound('sounds/sound_intensely.mp3')
sound_fast = pygame.mixer.Sound('sounds/sound_fast.mp3')
sound_water = pygame.mixer.Sound('sounds/sound_water.mp3')
sound_finish = pygame.mixer.Sound('sounds/finish.mp3')

screen = pygame.display.set_mode((640, 360))
pygame.display.set_caption("washing machine")
icon = pygame.image.load('img/washing-machine.jpg')
pygame.display.set_icon(icon)

bg = pygame.image.load('img/background.jpg')
washing_machine = pygame.image.load('img/washing-machine.png')
clothing = pygame.image.load('img/clothing.png')
water = pygame.image.load('img/water.png')
water_height = 40
water = pygame.transform.scale(water, (100, water_height))
water.set_alpha(100)
water_y = 202


clock.tick(60)
running = True
water_level = False
sound_finish_work = False
num_rotate = 0
while running:

    screen.blit(bg, (0, 0))

    screen.blit(clothing, (255, 105))
    # 105
    screen.blit(water, (255, water_y))
    screen.blit(washing_machine, (192, 29))


    screen.blit(text_time, (290, 32))

    washing_machine.blit(button_start, (75, 30))
    button_start.blit(text_start, text_rect_start)

    washing_machine.blit(button_stop, (120, 30))
    button_stop.blit(text_stop, text_rect_stop)

    washing_machine.blit(button_intensely, (178, 30))
    button_intensely.blit(text_intensely, text_rect_intensely)
    washing_machine.blit(button_fast, (178, 0))
    button_fast.blit(text_fast, text_rect_fast)

    pygame.display.update()
    if num_rotate > 0 and working:
        if water_level and water_y >= 105:
            water_y -= 1
            water_height += 1
            water = pygame.transform.scale(water, (100, water_height))
            clock.tick(20)
            if sound_water_work == True:
                sound_water.play()
                sound_water_work = False
        else:
            if num_rotate < 120:
                sound_intensely.stop()
                sound_fast.stop()
                font = pygame.font.Font("fonts/Roboto-Regular.ttf", 15)
                clock.tick(20)
                time = int(num_rotate / 20)
                text_time = font.render(f'{time}', False, 'White')
                print(num_rotate)
                if sound_very_fast_work == True:
                    sound_very_fast.play()
                    sound_very_fast_work = False
            else:
                print(num_rotate)
                font = pygame.font.Font("fonts/Roboto-Regular.ttf", 15)
                clock.tick(5)
                time = int(((num_rotate-120)/5)+(120/20))
                text_time = font.render(f'{time}', False, 'White')
                if work == 'intensely' and sound == True:
                    sound_intensely.play()
                    sound = False
                elif work == "fast" and sound == True:
                    sound_fast.play()
                    sound = False

            clothing = pygame.transform.rotate(clothing, -90)
            num_rotate -= 1
    elif num_rotate <= 0 and water_y <= 202:
        water_y += 1
        water_height -= 1
        water = pygame.transform.scale(water, (100, water_height))
        clock.tick(20)
    else:
        if sound_finish_work:
            sound_finish.play()
            sound_finish_work = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            font = pygame.font.Font("fonts/Roboto-Regular.ttf", 15)
            if button_start_rect.collidepoint(pygame.mouse.get_pos()):
                working = True
                water_level = True
                sound_very_fast_work = True
                sound_water_work = True
                sound = True
                sound_finish_work = True
                water_y = 202
                water_height = 40
                print(water_y)
                print(True)
            elif button_stop_rect.collidepoint(pygame.mouse.get_pos()):
                print(False)
                sound_water.stop()
                sound_fast.stop()
                sound_intensely.stop()
                sound_very_fast.stop()
                working = False
            elif button_intensely_rect.collidepoint(pygame.mouse.get_pos()):
                num_rotate = 400
                work = 'intensely'
                working = False
                sound = True
                sound_water.stop()
                sound_fast.stop()
                sound_intensely.stop()
                sound_very_fast.stop()
                time = int(((num_rotate - 120) / 5) + (120 / 20))
                text_time = font.render(f'{time}', False, 'White')
            elif button_fast_rect.collidepoint(pygame.mouse.get_pos()):
                num_rotate = 200
                work = 'fast'
                sound = True
                working = False
                sound_water.stop()
                sound_fast.stop()
                sound_intensely.stop()
                sound_very_fast.stop()
                time = int(((num_rotate - 120) / 5) + (120 / 20))
                text_time = font.render(f'{time}', False, 'White')

