import pygame
from pygame.locals import *
import sys
import random


class DoodleJump:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.green = pygame.image.load("imgs/green.png")
        pygame.font.init()
        self.score = 1
        self.g = 0
        self.font = pygame.font.SysFont("Arial", 50)
        self.blue = pygame.image.load("imgs/blue.png")
        self.red = pygame.image.load("imgs/red.png")
        self.red_1 = pygame.image.load("imgs/red_1.png")
        self.playerRight = pygame.image.load("imgs/right.png")
        self.playerRight_1 = pygame.image.load("imgs/right_1.png")
        self.playerLeft = pygame.image.load("imgs/left.png")
        self.playerLeft_1 = pygame.image.load("imgs/left_1.png")
        self.spring = pygame.image.load("imgs/spring.png")
        self.go = pygame.image.load("imgs/gameover.png")
        self.spring_1 = pygame.image.load("imgs/spring_1.png")
        self.direction = 0
        self.playerx = 400
        self.playery = 400
        self.platforms = [[400, 500, 0, 0]]
        self.springs = []
        self.cameray = 0
        self.jump = 0
        self.gravity = 0
        self.xmovement = 0

    def updatePlayer(self):
        if not self.jump:
            self.playery += self.gravity
            self.gravity += 1
        elif self.jump:
            self.playery -= self.jump
            self.jump -= 1
        key = pygame.key.get_pressed()
        if key[K_RIGHT]:
            if self.xmovement < 10:
                self.xmovement += 1
            self.direction = 0

        elif key[K_LEFT]:
            if self.xmovement > -10:
                self.xmovement -= 1
            self.direction = 1
        else:
            if self.xmovement > 0:
                self.xmovement -= 1
            elif self.xmovement < 0:
                self.xmovement += 1
        if self.playerx > 850:
            self.playerx = -50
        elif self.playerx < -50:
            self.playerx = 850
        self.playerx += self.xmovement
        if self.playery - self.cameray <= 200:
            self.cameray -= 10
        if not self.direction:
            if self.jump:
                self.screen.blit(self.playerRight_1, (self.playerx, self.playery - self.cameray))
            else:
                self.screen.blit(self.playerRight, (self.playerx, self.playery - self.cameray))
        else:
            if self.jump:
                self.screen.blit(self.playerLeft_1, (self.playerx, self.playery - self.cameray))
            else:
                self.screen.blit(self.playerLeft, (self.playerx, self.playery - self.cameray))

    def updatePlatforms(self):
        for p in self.platforms:
            rect = pygame.Rect(p[0], p[1], self.green.get_width() - 10, self.green.get_height())
            player = pygame.Rect(self.playerx, self.playery, self.playerRight.get_width() - 10,
                                 self.playerRight.get_height())
            if rect.colliderect(player) and self.gravity and self.playery < (p[1] - self.cameray):
                if p[2] != 2:
                    self.jump = 15
                    self.gravity = 0
                else:
                    p[-1] = 1
            if p[2] == 1:
                if p[-1] == 1:
                    p[0] += 5
                    if p[0] > 550:
                        p[-1] = 0
                else:
                    p[0] -= 5
                    if p[0] <= 0:
                        p[-1] = 1

    def drawPlatforms(self):
        for p in self.platforms:
            check = self.platforms[1][1] - self.cameray
            if check > 600:
                platform = random.randint(0, 1000)
                if platform < 800:
                    platform = 0
                elif platform < 900:
                    platform = 1
                else:
                    platform = 2

                self.platforms.append([random.randint(0, 700), self.platforms[-1][1] - 50, platform, 0])
                coords = self.platforms[-1]
                check = random.randint(0, 1000)
                if check > 900 and platform == 0:
                    self.springs.append([coords[0], coords[1] - 25, 0])
                self.platforms.pop(0)
                self.score += 100
            if p[2] == 0:
                self.screen.blit(self.green, (p[0], p[1] - self.cameray))
            elif p[2] == 1:
                self.screen.blit(self.blue, (p[0], p[1] - self.cameray))
            elif p[2] == 2:
                if not p[3]:
                    self.screen.blit(self.red, (p[0], p[1] - self.cameray))
                else:
                    self.screen.blit(self.red_1, (p[0], p[1] - self.cameray))

        for spring in self.springs:
            if spring[-1]:
                self.screen.blit(self.spring_1, (spring[0], spring[1] - self.cameray))
            else:
                self.screen.blit(self.spring, (spring[0], spring[1] - self.cameray))
            if pygame.Rect(spring[0], spring[1], self.spring.get_width(), self.spring.get_height()).colliderect(
                    pygame.Rect(self.playerx, self.playery, self.playerRight.get_width(),
                                self.playerRight.get_height())):
                self.jump = 50
                self.cameray -= 50

    def generatePlatforms(self):
        on = 600
        while on > -100:
            x = random.randint(0, 700)
            platform = random.randint(0, 1000)
            if platform < 800:
                platform = 0
            elif platform < 900:
                platform = 1
            else:
                platform = 2
            self.platforms.append([x, on, platform, 0])
            on -= 50

    def drawGrid(self):
        for x in range(80):
            pygame.draw.line(self.screen, (222, 222, 222), (x * 12, 0), (x * 12, 600))
            pygame.draw.line(self.screen, (222, 222, 222), (0, x * 12), (800, x * 12))

    def run(self):
        clock = pygame.time.Clock()
        self.generatePlatforms()
        running = True
        while running:
            self.screen.fill((255, 255, 255))
            clock.tick(70)
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            if self.playery - self.cameray > 700:
                self.cameray = 0
                self.score = 0
                self.springs = []
                self.platforms = [[400,400, 0, 0]]
                self.generatePlatforms()
                self.playerx = 400
                self.playery = 400
            self.drawGrid()
            self.drawPlatforms()
            self.updatePlayer()
            self.updatePlatforms()
            self.screen.blit(self.font.render(str(self.score - 1), -1, (0, 0, 0)), (25, 25))
            pygame.display.flip()
            if self.score == 0:
                running = False
                


