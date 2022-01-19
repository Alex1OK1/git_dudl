import pygame
import pygame_widgets
from pygame_widgets.button import Button

is_running = True
pygame.init()

pygame.display.set_caption('Doodle Jump')
window_surface = pygame.display.set_mode((400, 600))
screen = pygame.Surface((360, 600)).convert()
background = pygame.transform.scale(pygame.image.load("imgs/bck.png"), (400, 600))
screen.blit(background, (0, 0))
play_button = Button(
    # Mandatory Parameters
    window_surface,  # Surface to place button on
    57,  # X-coordinate of top left corner
    181,  # Y-coordinate of top left corner
    150,  # Width
    59,  # Height
    image=pygame.image.load("imgs/btn.png"),
    onClick=lambda: print(type(pygame.image.load("imgs/buon.png")))  # Function to call when clicked on
)
toys = Button(
    # Mandatory Parameters
    window_surface,  # Surface to place button on
    103,  # X-coordinate of top left corner
    277,  # Y-coordinate of top left corner
    140,  # Width
    50,  # Height
    image=pygame.image.load("imgs/toys.png"),
    onClick=lambda: print(type(pygame.image.load("imgs/toys.png")))  # Function to call when clicked on
)


def bb():
    global is_running
    is_running = False
    print(is_running)


leave = Button(
    # Mandatory Parameters
    window_surface,  # Surface to place button on
    274,  # X-coordinate of top left corner
    301,  # Y-coordinate of top left corner
    91,  # Width
    80,  # Height
    image=pygame.image.load("imgs/exit.png"),
    onClick=lambda: bb()  # Function to call when clicked on
)
while is_running:
    events = pygame.event.get()
    for event in events:
        print(is_running)
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
    pygame_widgets.update(events)
    window_surface.blit(background, (0, 0))
    play_button.draw()
    toys.draw()
    leave.draw()
    pygame.display.update()
