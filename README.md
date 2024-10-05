# Washing_machine
## Washing_machine - це програма яка симулює роботу пральної машини. В основі цієї програми лежить бібліотека ```pygame```

```python~~
pygame.init() #ініціалізує всі внутрішні модулі Pygame
clock = pygame.time.Clock() #створюємо об'єкт який буде контролювати час у програмі
font = pygame.font.Font("fonts/Roboto-Regular.ttf", 15) #завантажуємо шрифт та його розміір
```

## Імпортуємо та налаштовуємо всі моделі для програми


Створюємо дві кнопки які зупиняють та запускають роботу пральної машини

```python~~
text_start = font.render('start', False, 'White') #створюємо тект
button_start = pygame.Surface((40, 15)) #створюємо кнопку
text_rect_start = text_start.get_rect(center=(button_start.get_width() /2,
            button_start.get_height()/2)) #визначаємо кординати центра кнопки щоб в них поставити текст
button_start_rect = pygame.Rect(192 + 75, 29 + 30, 40, 15) #створюємо прямокутник який буде на кнопці проте його не видно

text_stop = font.render('stop', False, 'White') #
button_stop = pygame.Surface((40, 15)) #
text_rect_stop = text_stop.get_rect(center=(button_stop.get_width() /2, 
            button_stop.get_height()/2)) #
button_stop_rect = pygame.Rect(192 + 120, 29 + 30, 40, 15) #
```

Створюємо кнопки які задають режими

```python~~
time = 0
text_time = font.render(f'{time}', False, 'White') #це текст який відоражається на пралній машині та показує скільки
  секуд залишилося до закінчення прання

#створення кнопок прицип той самий
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
```

Імпортуємо всі зобреження та звуки які потрібні для роботи

```python~~
sound_very_fast = pygame.mixer.Sound('sounds/sound_very_fast.mp3')
sound_intensely = pygame.mixer.Sound('sounds/sound_intensely.mp3')
sound_fast = pygame.mixer.Sound('sounds/sound_fast.mp3')
sound_water = pygame.mixer.Sound('sounds/sound_water.mp3')
sound_finish = pygame.mixer.Sound('sounds/finish.mp3')


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
```

Розміщаємо ці зображення на екрані 
```python~~
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
```

А далі іде функціонал пральної машини. Спершу думав зробити не по кількості обертів а по часу, проте ідея не увінчалася успіхом

Розберу на даній частині коду 
```python~~
        if event.type == pygame.MOUSEBUTTONDOWN: #відстежуємо подію натискання кнопки
            font = pygame.font.Font("fonts/Roboto-Regular.ttf", 15) #шрифт я вказав тут томущо в мене тоді задавався дуже малий шрифт на таймер
            if button_start_rect.collidepoint(pygame.mouse.get_pos()): #а тут іде перевірка чи натиск миші був в зоні кнопки
```

### Факт про мій код
ось є рядок коду ```button_start_rect = pygame.Rect(192 + 75, 29 + 30, 40, 15)``` 
цікавить тут саме оці два значення 192 + 75, 29 + 30 я зрозумів як працює ```pygame.Rect``` і я вже прописав код
ну і типу все повино працювати а воно не працює і в чому пробле хто його знає? А проблема була в тому що я прописав
не (192 + 75, 29 + 30, 40, 15) а ( 75, 30, 40, 15) і я до останього не розумів чому воно не працює почав експерементувати
ну і методом проб і помилок до мене дійшло що якщо ти розміщаєш елемент по іншому елементу то до x і y потрібно додати 
кординати того елемента по якму ти ставиш кнопку. Та я хотів викинути у вікно свій комп'ютер коли це зрозумів а моє бажання
закинути проек було дужк високе.
Те як я вирішува цю проблем було схоже на:
![Alt-текст](https://cs13.pikabu.ru/post_img/big/2023/07/12/5/1689144753284012617.png "Орк")
