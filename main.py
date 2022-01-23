import pygame
import pygame_gui
import Buttons
import enum
import sqlite3
from game import  DoodleJump
is_rabotaet = True

def singIn():
    global is_rabotaet
    pygame.init()
    pygame.display.set_caption('Doodle Jump')
    window_surface = pygame.display.set_mode((500, 600))
    screen = pygame.Surface((500, 600)).convert()
    background = pygame.transform.scale(pygame.image.load("imgs/field.jpg"), (500, 600))
    screen.blit(background, (0, 0))
    font = pygame.font.SysFont('arial', 25)
    text1 = font.render('Login', True, (188, 93, 88))
    text2 = font.render('Password', True, (188, 93, 88))
    text3 = font.render('', True, (188, 93, 88))
    text_input_box = Buttons.TextInputBox(50, 50, 400, font)
    pass_input_box = Buttons.PasswordInputBox(50, 150, 400, font)
    manager = pygame_gui.UIManager((600, 600))
    clock = pygame.time.Clock()
    signinbutton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 220), (400, 50)),
                                               text='Войти',
                                               manager=manager,)
    def f():
        nonlocal text3, text_input_box, pass_input_box,is_running
        con = sqlite3.connect("Users.sqlite")
        cur = con.cursor()
        x = cur.execute(f"SELECT * FROM users WHERE Login =  '{text_input_box.returnText()}' ").fetchall()
        con.commit()
        if len(x) == 0:
            text3 = font.render('Пользователя с таким ником не существует', True, (188, 93, 88))
            print('qwe')
        else:
            x = cur.execute(f"SELECT Pass FROM users WHERE Login =  '{text_input_box.returnText()}' ").fetchall()
            con.commit()
            print(x)
            print('123123131313131313132313131231312321313123131313')
            if x[0][0] == pass_input_box.returnText():
                is_running = False
                global whatIsHappening
                whatIsHappening = Windows.MENU

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
                        print(is_running,"123")

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
    print('123')
    pygame.quit()

def inMenu():
    global  is_rabotaet,whatIsHappening
    pygame.init()
    pygame.display.set_caption('Doodle Jump')
    window_surface = pygame.display.set_mode((400, 600))
    screen = pygame.Surface((360, 600)).convert()
    background = pygame.transform.scale(pygame.image.load("imgs/bck.png"), (400, 600))
    screen.blit(background, (0, 0))

    manager = pygame_gui.UIManager((360, 655))

    play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 130), (200, 50)),
                                               text='Играть',
                                               manager=manager)
    res_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 205), (200, 50)),
                                              text='Результаты',
                                              manager=manager)
    store = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 280), (200, 50)),
                                         text='магазин',
                                         manager=manager)

    options = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 355), (200, 50)),
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
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == play_button:
                        whatIsHappening = Windows.PLAY
                        is_running = False
            if event.type == pygame.USEREVENT:
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == res_button:
                        print('Держи')

            manager.process_events(event)
        manager.update(time_delta)
        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)
        pygame.display.update()
    pygame.display.quit()

class Windows(enum.Enum):
    SINGIN = singIn
    LOGIN = 2
    MENU = inMenu
    STORE = 4
    INVENT = 5
    PROFILE = 7
    OPTIONS = 8
    PLAY = DoodleJump().run


is_running = True
whatIsHappening = Windows.SINGIN



while is_rabotaet:
    whatIsHappening()

