import pygame
import sys
import random

pygame.init()

width, height = 1200, 700
FPS = 45

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Вар тандер, но бюджет булка с маком")
clock = pygame.time.Clock()
gold_img = pygame.image.load('gold (1).png')
samo_img = pygame.image.load('samo l.png')
samg = pygame.image.load('samo l.png')
phone_img = pygame.image.load('phone.png')
phoneglavmen_img = pygame.image.load('phoneglavmen.png')
phonetank_img = pygame.image.load('phonetank.png')
phoneboya_img = pygame.image.load('phoneboya.png')
porazhenie_img = pygame.image.load('porazhenie.png')
pobeda_img = pygame.image.load('pobeda.png')
samolet = pygame.image.load('samolet (1).png')
samolet_phone = pygame.image.load('phone_samaleti.png')
pygame.mixer.music.load('BABAH.mp3')
vistrel = pygame.mixer.Sound('BABAH.mp3')
pygame.mixer.music.load('explosion.mp3')
expl = pygame.mixer.Sound('explosion.mp3')
winning_sound = pygame.mixer.Sound('win.mp3')
losing_sound = pygame.mixer.Sound('lose.mp3')

font = pygame.font.Font(None, 36)

currency = 0
record = 0
n = 0

def main_menu():
    arise_great_country = pygame.mixer.Sound('Fonivaya_muzika.mp3')
    global currency
    music_playing = True
    while True:
        screen.blit(phoneglavmen_img, (0, 0))
        screen.blit(gold_img, (width - 100, 20))
        draw_text(str(currency), font, WHITE, screen, width - 50, 35)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(width // 2 - 100, 200, 200, 50)
        button_2 = pygame.Rect(width // 2 - 100, 300, 200, 50)
        button_3 = pygame.Rect(width // 2 - 100, 400, 200, 50)
        button_4 = pygame.Rect(width // 2 - 100, 500, 200, 50)

        pygame.draw.rect(screen, RED, button_1)
        pygame.draw.rect(screen, RED, button_2)
        pygame.draw.rect(screen, RED, button_3)
        pygame.draw.rect(screen, RED, button_4)

        draw_text('Танки', font, WHITE, screen, width // 2, 225)
        draw_text('Самолеты', font, WHITE, screen, width // 2, 325)
        draw_text('Купить самолет', font, WHITE, screen, width // 2, 425)
        draw_text('Вернуть самолет', font, WHITE, screen, width // 2, 525)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_1.collidepoint((mx, my)):
                    if music_playing:
                        arise_great_country.stop()
                        music_playing = False
                    tank_mode()
                if button_2.collidepoint((mx, my)):
                    if music_playing:
                        arise_great_country.stop()
                        music_playing = False
                    plane_mode()
                if button_3.collidepoint((mx, my)):
                    buy_airplane()
                if button_4.collidepoint((mx, my)):
                    change_airplane()

            # Воспроизведение музыки только в меню
        if music_playing:

            pygame.mixer.Sound.play(arise_great_country)

        pygame.display.update()
        clock.tick(FPS)



def change_airplane():
    global currency, samo_img
    if samo_img == samolet:
        samo_img = samg
        currency += 8000
def tank_mode():
    clock = pygame.time.Clock()

    # Загружаем музыку

    tankWidth = 40
    tankHeight = 20
    turretWidth = 5
    wheelWidth = 5
    groundHeight = 35

    def textObjects(text, color, size="small"):
        if size == "vsmall":
            font = pygame.font.SysFont("Calibre", 15)
            textSurf = font.render(text, True, color)
        if size == "small":
            font = pygame.font.SysFont("Calibre", 25)
            textSurf = font.render(text, True, color)
        if size == "medium":
            font = pygame.font.SysFont("Calibre", 35)
            textSurf = font.render(text, True, color)
        if size == "large":
            font = pygame.font.SysFont("Calibre", 50)
            textSurf = font.render(text, True, color)
        return textSurf, textSurf.get_rect()

    def show_message(msg, color, y_displace=0, size="small"):
        textSurf, textRect = textObjects(msg, color, size)
        textRect.center = (int(width / 2), int(height / 2) + y_displace)
        screen.blit(textSurf, textRect)

    class Button:

        def __init__(self, text, pos, font, bg="blue"):
            self.x, self.y = pos
            self.font = pygame.font.SysFont("Arial", font)
            self.text = text
            self.text = self.font.render(self.text, 1, pygame.Color("blue"))
            self.change_text(bg)

        def change_text(self, bg="blue"):
            self.size = self.text.get_size()
            self.surface = pygame.Surface(self.size)
            self.surface.fill(bg)
            self.surface.blit(self.text, (0, 0))
            self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

        def show(self):
            screen.blit(self.text, (self.x, self.y))

        def click(self, event, action):
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if self.rect.collidepoint(x, y):
                        if action == "quit":
                            main_menu()

                        if action == "controls":
                            controlsWin()

                        if action == "play":
                            mainGame()

                        if action == "main":
                            mainWindow()


    def mainWindow():
        music_tanki = pygame.mixer.Sound("tanki_music.mp3")
        pygame.mixer.Sound.play(music_tanki)
        button1 = Button("В БОЙ", (350, 350), font=30)
        button2 = Button("Управление", (350, 430), font=30)
        button3 = Button("выйти", (350, 510), font=30)

        while True:
            screen.blit(phonetank_img, (0, 0))
            show_message("РЕЖИМ ТАНКИ", '#000000', -200, size="large")
            show_message("Добро пожаловать в игру", 'black', -100, size="medium")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if button1.click(event, 'play'):
                    music_tanki.stop()  # Останавливаем музыку при выходе
                button2.click(event, 'controls')
                if button3.click(event, 'quit'):
                    music_tanki.stop()  # Останавливаем музыку при выходе
            button1.show()
            button2.show()
            button3.show()

            clock.tick(30)
            pygame.display.update()

    def controlsWin():
        music_tanki = pygame.mixer.Sound("tanki_music.mp3")
        pygame.mixer.Sound.play(music_tanki)
        button1 = Button("В БОЙ", (150, 500), font=30)

        button2 = Button("Главное меню", (350, 500), font=30)

        button3 = Button("Выйти", (550, 500), font=30)

        while True:
            screen.blit(phonetank_img, (0, 0))
            Green = (0, 255, 0)
            show_message("РЕЖИМ ТАНКИ", 'black', -200, size="large")
            show_message("Управление:", 'black', -100, size="medium")
            show_message("Задача, выстрелить и уничтожить врага, пока он это не сделал первым.", 'Black', -30)
            show_message("Чтобы стрелять нажмите ПРОБЕЛ", 'gray', 0)
            show_message("Чтобы поворачивать орудие нажимайте на стрелочку вверх и стрелочку низ", 'black', 30)
            show_message("Чтобы управлять танком используйте стрелочки вправо и влево", 'black', 60)
            show_message("Чтобы увеличивать/уменьшать разброс нажимайте на Ф и В", 'black', 90)
            show_message("Нажмите З, чтобы поставить игру на паузу", 'black', 120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if button1.click(event, 'play'):
                    music_tanki.stop()  # Останавливаем музыку при выходе
                button2.click(event, 'main')
                if button3.click(event, 'quit'):
                    music_tanki.stop()  # Останавливаем музыку при выходе
            button1.show()
            button2.show()
            button3.show()

            clock.tick(30)
            pygame.display.update()

    def tank(x, y, turPos, tank):
        # tank=1 if player's tank and -1 if computer's tank
        x = int(x)
        y = int(y)
        locs = [[27, 2], [26, 5], [25, 8], [23, 12], [20, 14], [18, 15], [15, 17], [13, 19], [11, 21]]
        possibleTurrets = []
        for i in locs:
            possibleTurrets.append((x - tank * i[0], y - i[1]))

        pygame.draw.circle(screen, '#000000', (x, y), int(tankHeight / 2))

        for i in range(-15, 16, 5):
            pygame.draw.circle(screen, '#000000', (x + i, y + 20), wheelWidth)

        return possibleTurrets[turPos]

    def explosion(x, y, size=50):
        explode = True

        while explode:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main_menu()

            startPoint = x, y

            colorChoices = ['red', 'brown2', 'yellow', 'gold1']

            magnitude = 1

            while magnitude < size:
                exploding_bit_x = x + random.randrange(-1 * magnitude, magnitude)
                exploding_bit_y = y + random.randrange(-1 * magnitude, magnitude)

                pygame.draw.circle(screen, colorChoices[random.randrange(0, 4)], (exploding_bit_x, exploding_bit_y),
                                   random.randrange(1, 5))
                magnitude += 1

                pygame.display.update()
                clock.tick(100)

            explode = False

    def show_health_bars(player_health, enemy_health):
        if player_health > 75:
            player_color = 'green'
        elif player_health > 50:
            player_color = 'yellow'
        else:
            player_color = 'red'

        if enemy_health > 75:
            enemy_color = 'green'
        elif enemy_health > 50:
            enemy_color = 'yellow'
        else:
            enemy_color = 'red'

        pygame.draw.rect(screen, player_color, (680, 25, player_health, 25))
        pygame.draw.rect(screen, enemy_color, (20, 25, enemy_health, 25))

    def fireShell(xy, tankx, tanky, turPos, gun_power, xlocation, barrier_width, randomHeight, enemyTankX, enemyTankY):
        pygame.mixer.Sound.play(vistrel)
        fire = True
        damage = 0

        startingShell = list(xy)

        while fire:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # print(startingShell[0],startingShell[1])
            pygame.draw.circle(screen, 'red', (startingShell[0], startingShell[1]), 5)

            startingShell[0] -= (12 - turPos) * 2

            # y = x**2
            startingShell[1] += int(
                (((startingShell[0] - xy[0]) * 0.015 / (gun_power / 50)) ** 2) - (turPos + turPos / (12 - turPos)))

            if startingShell[1] > height - groundHeight:
                hit_x = int((startingShell[0] * height - groundHeight) / startingShell[1])
                hit_y = int(height - groundHeight)

                if enemyTankX + 10 > hit_x > enemyTankX - 10:
                    damage = 25
                elif enemyTankX + 15 > hit_x > enemyTankX - 15:
                    damage = 18
                elif enemyTankX + 25 > hit_x > enemyTankX - 25:
                    damage = 10
                elif enemyTankX + 35 > hit_x > enemyTankX - 35:
                    damage = 5

                explosion(hit_x, hit_y)
                fire = False

            check_x_1 = startingShell[0] <= xlocation + barrier_width
            check_x_2 = startingShell[0] >= xlocation

            check_y_1 = startingShell[1] <= height
            check_y_2 = startingShell[1] >= height - randomHeight

            if check_x_1 and check_x_2 and check_y_1 and check_y_2:
                hit_x = int((startingShell[0]))
                hit_y = int(startingShell[1])
                explosion(hit_x, hit_y)
                fire = False

            pygame.display.update()
            clock.tick(60)
        return damage

    def compfireShell(xy, tankx, tanky, turPos, gun_power, xlocation, barrier_width, randomHeight, ptankx, ptanky):
        damage = 0
        currentPower = 1
        power_found = False

        while not power_found:
            currentPower += 1
            if currentPower > 100:
                power_found = True

            fire = True
            startingShell = list(xy)

            while fire:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                startingShell[0] += (12 - turPos) * 2
                startingShell[1] += int(
                    (((startingShell[0] - xy[0]) * 0.015 / (currentPower / 50)) ** 2) - (
                                turPos + turPos / (12 - turPos)))

                if startingShell[1] > height - height:
                    hit_x = int((startingShell[0] * height - height) / startingShell[1])
                    hit_y = int(height - height)
                    if ptankx + 15 > hit_x > ptankx - 15:
                        power_found = True
                    fire = False

                check_x_1 = startingShell[0] <= xlocation + barrier_width
                check_x_2 = startingShell[0] >= xlocation

                check_y_1 = startingShell[1] <= height
                check_y_2 = startingShell[1] >= height - randomHeight

                if check_x_1 and check_x_2 and check_y_1 and check_y_2:
                    hit_x = int((startingShell[0]))
                    hit_y = int(startingShell[1])
                    fire = False

        fire = True
        startingShell = list(xy)
        pygame.mixer.Sound.play(vistrel)
        while fire:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.draw.circle(screen, 'red', (startingShell[0], startingShell[1]), 5)

            startingShell[0] += (12 - turPos) * 2

            gun_power = random.randrange(int(currentPower * 0.90), int(currentPower * 1.10))

            startingShell[1] += int(
                (((startingShell[0] - xy[0]) * 0.015 / (gun_power / 50)) ** 2) - (turPos + turPos / (12 - turPos)))

            if startingShell[1] > height - groundHeight:
                hit_x = int((startingShell[0] * height - groundHeight) / startingShell[1])
                hit_y = int(height - groundHeight)

                if ptankx + 10 > hit_x > ptankx - 10:
                    damage = 25
                elif ptankx + 15 > hit_x > ptankx - 15:
                    damage = 18
                elif ptankx + 25 > hit_x > ptankx - 25:
                    damage = 10
                elif ptankx + 35 > hit_x > ptankx - 35:
                    damage = 5

                explosion(hit_x, hit_y)
                fire = False

            check_x_1 = startingShell[0] <= xlocation + barrier_width
            check_x_2 = startingShell[0] >= xlocation

            check_y_1 = startingShell[1] <= height
            check_y_2 = startingShell[1] >= height - randomHeight

            if check_x_1 and check_x_2 and check_y_1 and check_y_2:
                hit_x = int((startingShell[0]))
                hit_y = int(startingShell[1])
                explosion(hit_x, hit_y)
                fire = False

            pygame.display.update()
            clock.tick(60)
        return damage

    def game_over(winner):
        global currency
        button1 = Button("Играть снова", (350, 350), font=30)

        button2 = Button("Настройки", (350, 430), font=30)

        button3 = Button("Выйти", (350, 510), font=30)
        while True:
            Black = (0, 0, 0)
            text = ''
            color = ''
            if (winner == 1):
                screen.blit(pobeda_img, (0, 0))
                text = "Ура победа, ура победа!"
                color = Black
                pygame.mixer.Sound.play(winning_sound)
                currency += 500
            else:
                screen.blit(porazhenie_img, (0, 0))
                text = "Вы проиграли, увы и ах!"
                color = Black
                pygame.mixer.Sound.play(losing_sound)
                if currency > 550:
                    currency -= 550
            show_message("РЕЖИМ ТАНКИ", '#000000', -200, size="large")
            show_message(text, color, -100, size="medium")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                button1.click(event, 'play')
                button2.click(event, 'controls')
                button3.click(event, 'quit')
            button1.show()
            button2.show()
            button3.show()

            clock.tick(30)
            pygame.display.update()

    def pause():
        paused = True
        show_message("На паузе", 'white', -100, size="large")
        show_message("Нажмите С, чтобы продолжить или Й чтобы выйти", 'wheat', 25)
        pygame.display.update()
        while paused:
            # gameDisplay.fill(black)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
                    elif event.key == pygame.K_q:
                        main_menu()

            clock.tick(5)

    def mainGame():
        gameExit = False
        gameOver = False

        player_health = 100
        enemy_health = 100

        barrier_width = 50

        mainTankX = width * 0.9
        mainTankY = height * 0.9
        tankMove = 0
        currentTurPos = 0
        changeTur = 0

        enemyTankX = width * 0.1
        enemyTankY = height * 0.9

        fire_power = 50
        power_change = 0

        xlocation = (width / 2) + random.randint(int(-0.1 * width), int(0.1 * width))
        randomHeight = random.randint(int(height * 0.1), int(height * 0.6))

        while True:
            screen.blit(phoneboya_img, (0, 0))
            Green = (0, 255, 0)
            Red = (255, 0, 0)
            text = ''
            color = ''
            show_message("РЕЖИМ ТАНКИ", '#000000', -200, size="large")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        tankMove = -5

                    elif event.key == pygame.K_RIGHT:
                        tankMove = 5

                    elif event.key == pygame.K_UP:
                        changeTur = 1

                    elif event.key == pygame.K_DOWN:
                        changeTur = -1

                    elif event.key == pygame.K_p:
                        pause()
                    elif event.key == pygame.K_SPACE:
                        screen.blit(phoneboya_img, (0, 0))
                        show_message("РЕЖИМ ТАНКИ", '#000000', -200, size="large")
                        show_health_bars(player_health, enemy_health)
                        gun = tank(mainTankX, mainTankY, currentTurPos, 1)
                        enemy_gun = tank(enemyTankX, enemyTankY, 8, -1)
                        fire_power += power_change
                        font = pygame.font.SysFont("Calibre", 30)
                        text = font.render("Частота разброса: " + str(fire_power) + "%", True, 'black')
                        screen.blit(text, [width / 2, 0])
                        text = font.render("Высота: " + str(currentTurPos) + "м", True, 'black')
                        screen.blit(text, [width / 2, 20])
                        pygame.draw.rect(screen, 'brown',
                                         [xlocation, height - randomHeight, barrier_width, randomHeight])
                        screen.fill('brown',
                                     rect=[0, height - groundHeight, width, height])
                        pygame.display.update()

                        clock.tick(30)

                        damage = fireShell(gun, mainTankX, mainTankY, currentTurPos, fire_power, xlocation,
                                           barrier_width,
                                           randomHeight, enemyTankX, enemyTankY)
                        enemy_health -= damage

                        possibleMovement = ['f', 'r']
                        moveIndex = random.randrange(0, 2)

                        for x in range(random.randrange(0, 10)):

                            if width * 0.3 > enemyTankX > width * 0.03:
                                if possibleMovement[moveIndex] == "f":
                                    enemyTankX += 5
                                elif possibleMovement[moveIndex] == "r":
                                    enemyTankX -= 5

                                screen.blit(phoneboya_img, (0, 0))
                                show_message("РЕЖИМ ТАНКИ", '#000000', -200, size="large")
                                show_health_bars(player_health, enemy_health)
                                gun = tank(mainTankX, mainTankY, currentTurPos, 1)
                                enemy_gun = tank(enemyTankX, enemyTankY, 8, -1)
                                fire_power += power_change
                                font = pygame.font.SysFont("Calibre", 30)
                                text = font.render("Частота разброса: " + str(fire_power) + "%", True, 'black')
                                screen.blit(text, [width / 2, 0])
                                text = font.render("Высота: " + str(currentTurPos) + "м", True, 'black')
                                screen.blit(text, [width / 2, 20])
                                pygame.draw.rect(screen, 'brown',
                                                 [xlocation, height - randomHeight, barrier_width, randomHeight])
                                screen.fill('brown',
                                             rect=[0, height - groundHeight, width, height])
                                pygame.display.update()

                                clock.tick(30)

                        damage = compfireShell(enemy_gun, enemyTankX, enemyTankY, 8, 50, xlocation, barrier_width,
                                               randomHeight, mainTankX, mainTankY)
                        player_health -= damage

                    elif event.key == pygame.K_a:
                        power_change = -1
                    elif event.key == pygame.K_d:
                        power_change = 1

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        tankMove = 0

                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        changeTur = 0

                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        power_change = 0

            mainTankX += tankMove

            currentTurPos += changeTur

            if currentTurPos > 8:
                currentTurPos = 8
            elif currentTurPos < 0:
                currentTurPos = 0

            if mainTankX - (tankWidth / 2) < xlocation + barrier_width:
                mainTankX += 5

            show_health_bars(player_health, enemy_health)
            gun = tank(mainTankX, mainTankY, currentTurPos, 1)
            enemy_gun = tank(enemyTankX, enemyTankY, 8, -1)

            fire_power += power_change

            if fire_power > 100:
                fire_power = 100
            elif fire_power < 1:
                fire_power = 1

            font = pygame.font.SysFont("Calibre", 30)
            text = font.render("Частота разброса " + str(fire_power) + "%", True, 'black')
            screen.blit(text, [width / 2, 0])
            text = font.render("Высота " + str(currentTurPos) + "м", True, 'black')
            screen.blit(text, [width / 2, 20])
            pygame.draw.rect(screen, 'brown', [xlocation, height - randomHeight, barrier_width, randomHeight])
            screen.fill('brown', rect=[0, height - groundHeight, width, height])
            if player_health < 1:
                game_over(0)
                pygame.mixer.Sound.play(expl)
            elif enemy_health < 1:
                game_over(1)
                pygame.mixer.Sound.play(expl)

            pygame.display.update()
            clock.tick(FPS)

    mainWindow()


def plane_mode():
    samo_muz = pygame.mixer.Sound('fonovaya_muzika_plane.mp3')
    def main_winDow():
        global record
        music_playing = True
        while True:
            screen.blit(samolet_phone, (0, 0))
            draw_text(str(record), font, WHITE, screen, width - 50, 35)

            mx, my = pygame.mouse.get_pos()

            button_1 = pygame.Rect(width // 2 - 100, 200, 200, 50)
            button_2 = pygame.Rect(width // 2 - 100, 300, 200, 50)
            button_3 = pygame.Rect(width // 2 - 100, 400, 200, 50)

            pygame.draw.rect(screen, RED, button_1)
            pygame.draw.rect(screen, RED, button_2)
            pygame.draw.rect(screen, RED, button_3)

            draw_text('В БОЙ', font, WHITE, screen, width // 2, 225)
            draw_text('УПРАВЛЕНИЕ', font, WHITE, screen, width // 2, 325)
            draw_text('ВЫЙТИ', font, WHITE, screen, width // 2, 425)
            for event in pygame.event.get():
                if music_playing:
                    pygame.mixer.Sound.play(samo_muz)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_1.collidepoint((mx, my)):
                        game_da()
                    if button_2.collidepoint((mx, my)):
                        setting()
                    if button_3.collidepoint((mx, my)):
                        if music_playing:
                            samo_muz.stop()
                            music_playing = False
                        main_menu()

                # Воспроизведение музыки только в меню
            if music_playing:
                pygame.mixer.Sound.play(samo_muz, 6)

            pygame.display.update()
            clock.tick(FPS)

    def textObjects(text, color, size="small"):
        if size == "vsmall":
            font = pygame.font.SysFont("Calibre", 15)
            textSurf = font.render(text, True, color)
        if size == "small":
            font = pygame.font.SysFont("Calibre", 25)
            textSurf = font.render(text, True, color)
        if size == "medium":
            font = pygame.font.SysFont("Calibre", 35)
            textSurf = font.render(text, True, color)
        if size == "large":
            font = pygame.font.SysFont("Calibre", 50)
            textSurf = font.render(text, True, color)
        return textSurf, textSurf.get_rect()

    def show_message(msg, color, y_displace=0, size="small"):
        textSurf, textRect = textObjects(msg, color, size)
        textRect.center = (int(width / 2), int(height / 2) + y_displace)
        screen.blit(textSurf, textRect)


    class Button:

        def __init__(self, text, pos, font, bg="black"):
            self.x, self.y = pos
            self.font = pygame.font.SysFont("Arial", font)
            self.text = text
            self.text = self.font.render(self.text, 1, pygame.Color("black"))
            self.change_text(bg)

        def change_text(self, bg="black"):
            self.size = self.text.get_size()
            self.surface = pygame.Surface(self.size)
            self.surface.fill(bg)
            self.surface.blit(self.text, (0, 0))
            self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

        def show(self):
            screen.blit(self.text, (self.x, self.y))

        def click(self, event, action):
            global music_playing
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if self.rect.collidepoint(x, y):
                        if action == "quit":
                            main_winDow()

                        if action == "controls":
                            setting()

                        if action == "play":
                            game_da()

                        if action == "main":
                            main_winDow()

    def setting():
        button1 = Button("В БОЙ", (150, 500), font=30)

        button2 = Button("Главное меню", (350, 500), font=30)

        while True:
            screen.blit(samolet_phone, (0, 0))
            Green = (0, 255, 0)
            show_message("РЕЖИМ ТАНКИ", 'black', -200, size="large")
            show_message("Управление:", 'black', -100, size="medium")
            show_message("Задача, уклонятся от препядствий и пролететь в воздухе как можно дальше.", 'Black', -30)
            show_message("Чтобы набрать высоту нажмите ПРОБЕЛ", 'black', 0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                button1.click(event, 'play')
                button2.click(event, 'main')
            button1.show()
            button2.show()

            clock.tick(30)
            pygame.display.update()

    def game_da():
        global currency
        global record
        n = 0
        bird_x, bird_y = 100, height // 2
        bird_speed = 0
        gravity = 0.5
        obstacles = []
        obstacle_gap = 300

        running = True
        while running:
            screen.blit(phone_img, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird_speed = -10

            bird_speed += gravity
            bird_y += bird_speed

            # Изменяем размер самолета
            bird_rect = samo_img.get_rect(topleft=(bird_x, bird_y))
            samo_img_scaled = pygame.transform.scale(samo_img, (50, 50))  # Увеличиваем размер самолета
            if bird_rect.top <= 0 or bird_rect.bottom >= height:
                running = False

            for obstacle in obstacles:
                if bird_rect.colliderect(obstacle):
                    running = False

            if len(obstacles) == 0 or obstacles[-1].x < width - 400:  # Увеличиваем интервал появления препятствий
                h = random.randint(50, 400)
                obstacles.append(pygame.Rect(width, 0, 60, h))
                obstacles.append(pygame.Rect(width, h + obstacle_gap, 60, height - h - obstacle_gap))

            new_obstacles = []
            for obstacle in obstacles:
                obstacle.x -= 5
                if obstacle.x + 50 > 0:
                    new_obstacles.append(obstacle)
                else:
                    currency += 100
                    n += 1
                    if n > record:
                       record = n // 2
            obstacles = new_obstacles

            for obstacle in obstacles:
                pygame.draw.rect(screen, BLACK, obstacle)

            screen.blit(samo_img, (bird_x, bird_y))
            pygame.display.update()
            clock.tick(FPS)
    main_winDow()


def buy_airplane():
    global currency, samo_img
    if currency >= 10000:
        currency -= 10000
        samo_img = samolet


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

main_menu()

