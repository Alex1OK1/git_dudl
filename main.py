import pygame
import pygame_gui
import Buttons
import enum
import sqlite3
from game import DoodleJump

pygame.init()
is_rabotaet = True
USERNAME = ""


def singIn():
    global is_rabotaet

    pygame.display.set_caption('Doodle Jump')
    window_surface = pygame.display.set_mode((500, 600))
    screen = pygame.Surface((500, 600)).convert()
    background = pygame.transform.scale(pygame.image.load("imgs/field.jpg"), (500, 600))
    screen.blit(background, (0, 0))
    font = pygame.font.SysFont('arial', 25)
    text1 = font.render('Username', True, (188, 93, 88))
    text2 = font.render('Password', True, (188, 93, 88))
    text3 = font.render('', True, (188, 93, 88))
    text_input_box = Buttons.TextInputBox(50, 50, 400, font)
    pass_input_box = Buttons.PasswordInputBox(50, 150, 400, font)
    manager = pygame_gui.UIManager((600, 600))
    clock = pygame.time.Clock()
    signinbutton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 220), (400, 50)),
                                                text='Войти',
                                                manager=manager, )
    regbutton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 300), (400, 50)),
                                             text='Зарегестрироваться',
                                             manager=manager, )

    def f():
        nonlocal text3, text_input_box, pass_input_box, is_running
        con = sqlite3.connect("Users.sqlite")
        cur = con.cursor()
        x = cur.execute(f"SELECT * FROM users WHERE Login =  '{text_input_box.returnText()}' ").fetchall()
        con.commit()
        if len(x) == 0:
            text3 = font.render('Пользователя с таким ником не существует', True, (188, 93, 88))
        else:
            x = cur.execute(f"SELECT Pass FROM users WHERE Login =  '{text_input_box.returnText()}' ").fetchall()
            con.commit()
            if x[0][0] == pass_input_box.returnText():
                pygame.mixer.music.load('music.wav')
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(0.02)
                global USERNAME
                USERNAME = text_input_box.returnText()
                is_running = False
                global whatIsHappening
                whatIsHappening = Windows.MENU

    def reg():
        nonlocal is_running
        is_running = False
        global whatIsHappening
        whatIsHappening = Windows.REGISTER

    group = pygame.sprite.Group(text_input_box)
    group2 = pygame.sprite.Group(pass_input_box)
    is_running = True
    while is_running:
        time_delta = clock.tick(60) / 1000.0
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                is_running = False
                is_rabotaet = False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == signinbutton:
                        f()
                        print(is_running, "123")
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == regbutton:
                        reg()
            manager.process_events(event)
        manager.update(time_delta)
        window_surface.blit(background, (0, 0))
        group.update(events)
        group2.update(events)
        window_surface.blit(text1, (50, 20))
        window_surface.blit(text2, (50, 120))
        window_surface.blit(text3, (50, 300))
        group.draw(window_surface)
        group2.draw(window_surface)
        manager.draw_ui(window_surface)
        pygame.display.update()
    pygame.display.quit()


def inMenu():
    global is_rabotaet, whatIsHappening
    pygame.display.set_caption('Doodle Jump')
    window_surface = pygame.display.set_mode((400, 600))
    screen = pygame.Surface((400, 600)).convert()
    background = pygame.transform.scale(pygame.image.load("imgs/bck.png"), (400, 600))
    screen.blit(background, (0, 0))

    manager = pygame_gui.UIManager((400, 600))

    play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 130), (200, 50)),
                                               text='Играть',
                                               manager=manager)
    res_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 205), (200, 50)),
                                              text='Результаты',
                                              manager=manager)

    options = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 280), (200, 50)),
                                           text='настройки',
                                           manager=manager)

    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                is_rabotaet = False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == play_button:
                        print(123)
                        whatIsHappening = Windows.PLAY
                        is_running = False
                    if event.ui_element == options:
                        whatIsHappening = Windows.OPTIONS
                        is_running = False
                    if event.ui_element == res_button:
                        whatIsHappening = Windows.PROFILE
                        is_running = False
            manager.process_events(event)
        manager.update(time_delta)
        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)
        pygame.display.update()
    pygame.display.quit()


def register():
    global is_rabotaet

    pygame.display.set_caption('Doodle Jump')
    window_surface = pygame.display.set_mode((500, 600))
    screen = pygame.Surface((500, 600)).convert()
    background = pygame.transform.scale(pygame.image.load("imgs/field.jpg"), (500, 600))
    screen.blit(background, (0, 0))
    font = pygame.font.SysFont('arial', 25)
    text1 = font.render('Username', True, (188, 93, 88))
    text2 = font.render('Password', True, (188, 93, 88))
    text3 = font.render('', True, (188, 93, 88))
    text_input_box = Buttons.TextInputBox(50, 50, 400, font)
    pass_input_box = Buttons.PasswordInputBox(50, 150, 400, font)
    manager = pygame_gui.UIManager((600, 600))
    clock = pygame.time.Clock()
    regutton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 220), (400, 50)),
                                            text='Зарегестрироватся',
                                            manager=manager, )
    signinbutton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 220), (400, 50)),
                                                text='Войти',
                                                manager=manager, )

    def sign():
        nonlocal is_running
        is_running = False
        global whatIsHappening
        whatIsHappening = Windows.SINGIN

    def f():
        nonlocal text3, text_input_box, pass_input_box, is_running
        con = sqlite3.connect("Users.sqlite")
        cur = con.cursor()
        x = cur.execute(f"SELECT * FROM users WHERE Login = '{text_input_box.returnText()}' ").fetchall()
        con.commit()
        if text_input_box.returnText() == '':
            text3 = font.render('Логин не может быть пустым', True, (188, 93, 88))
            return
        if len(pass_input_box.returnText()) < 4:
            text3 = font.render('Слишком короткий пароль', True, (188, 93, 88))
            return
        if (len(x) > 0):
            text3 = font.render('Пользователь с таким именем существует', True, (188, 93, 88))
        else:
            x = cur.execute(
                f"INSERT INTO users VALUES(NULL, '{text_input_box.returnText()}' ,'{pass_input_box.returnText()}', 0, 0,'') ").fetchall()
            con.commit()
            is_running = False
            global whatIsHappening
            whatIsHappening = Windows.SINGIN

    group = pygame.sprite.Group(text_input_box)
    group2 = pygame.sprite.Group(pass_input_box)
    is_running = True
    while is_running:
        time_delta = clock.tick(60) / 1000.0
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                is_running = False
                is_rabotaet = False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == signinbutton:
                        sign()
                    if event.ui_element == regutton:
                        f()


            manager.process_events(event)
        manager.update(time_delta)
        window_surface.blit(background, (0, 0))
        group.update(events)
        group2.update(events)
        window_surface.blit(text1, (50, 20))
        window_surface.blit(text2, (50, 120))
        window_surface.blit(text3, (50, 300))
        group.draw(window_surface)
        group2.draw(window_surface)
        manager.draw_ui(window_surface)
        pygame.display.update()
    pygame.display.quit()


def ortions():
    global is_rabotaet, whatIsHappening
    pygame.display.set_caption('Doodle Jump')
    window_surface = pygame.display.set_mode((400, 600))
    screen = pygame.Surface((400, 600)).convert()
    background = pygame.transform.scale(pygame.image.load("imgs/field.jpg"), (400, 600))
    screen.blit(background, (0, 0))

    manager = pygame_gui.UIManager((400, 600))

    stmusic = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 130), (200, 50)),
                                           text='Вкл Музыку',
                                           manager=manager)
    endmusic = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 205), (200, 50)),
                                            text='Выкл Музыку',
                                            manager=manager)
    back = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 280), (200, 50)),
                                        text='Назад',
                                        manager=manager)

    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                is_rabotaet = False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == back:
                        whatIsHappening = Windows.MENU
                        is_running = False
                    if event.ui_element == stmusic:
                        pygame.mixer.music.play()
                    if event.ui_element == endmusic:
                        pygame.mixer.music.stop()

            manager.process_events(event)
        manager.update(time_delta)
        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)
        pygame.display.update()
    pygame.display.quit()


def profile():
    global is_rabotaet, whatIsHappening, USERNAME
    pygame.display.set_caption('Doodle Jump')
    window_surface = pygame.display.set_mode((600, 600))
    screen = pygame.Surface((600, 600)).convert()
    background = pygame.transform.scale(pygame.image.load("imgs/field.jpg"), (600, 600))
    screen.blit(background, (0, 0))

    manager = pygame_gui.UIManager((600, 600))

    back = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 220), (500, 50)),
                                        text='Назад',
                                        manager=manager)
    font = pygame.font.SysFont('arial', 25)
    con = sqlite3.connect("Users.sqlite")
    cur = con.cursor()
    x = cur.execute(f"SELECT * FROM users WHERE Login = '{USERNAME}' ").fetchall()
    print(x, USERNAME)
    con.commit()
    text1 = font.render('Счет: ' + str(x[0][3]), True, (188, 93, 88))
    text2 = font.render('Наилучший результат: ' + str(x[0][4]), True, (188, 93, 88))
    text3 = font.render('Имя: ' + USERNAME, True, (188, 93, 88))
    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                is_rabotaet = False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == back:
                        whatIsHappening = Windows.MENU
                        is_running = False

            manager.process_events(event)
        manager.update(time_delta)
        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)
        window_surface.blit(text1, (50, 20))
        window_surface.blit(text2, (50, 80))
        window_surface.blit(text3, (50, 140))
        pygame.display.update()
    pygame.display.quit()


class Windows(enum.Enum):
    SINGIN = singIn
    REGISTER = register
    MENU = inMenu
    STORE = 4
    INVENT = 5
    PROFILE = profile
    OPTIONS = ortions
    PLAY = DoodleJump().run


is_running = True
whatIsHappening = Windows.SINGIN

while is_rabotaet:
    if whatIsHappening == Windows.PLAY:
        z = whatIsHappening()
        con = sqlite3.connect("Users.sqlite")
        cur = con.cursor()
        x = cur.execute(f"SELECT * FROM users WHERE Login = '{USERNAME}' ").fetchall()
        print(x, USERNAME)
        con.commit()
        x = cur.execute(
            f"UPDATE users SET rate='{x[0][3] + z}', best='{max(x[0][4], z)}'WHERE Login = '{USERNAME}' ").fetchall()
        con.commit()
        whatIsHappening = Windows.MENU
    else:
        whatIsHappening()
