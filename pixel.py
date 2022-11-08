import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import numpy as np
from math import floor

import sys



import pygame
pygame.init()

BLOCK = 10


class Generator:

    def __init__(self, x=106*BLOCK, y=17*BLOCK):
        self.x_screen = x
        self.y_screen = y
        self.screen = pygame.display.set_mode((self.x_screen, self.y_screen))
        pygame.display.set_caption('Generator')
        self.clock = pygame.time.Clock()
        self.screen.fill('#F0F0F0')
        self.arr = np.array([[0 for _ in range(106)]
                            for _ in range(17)])

    def generate(self, x_food, y_food, value):
        color = value*('#0A60AC') + (value != 1)*('#F0F0F0')
        pygame.draw.rect(self.screen, color, pygame.Rect(
            x_food*BLOCK, y_food*BLOCK, BLOCK, BLOCK), 6)
        return

    def arr_to_n(self):
        self.rot_arr = np.flip(np.rot90(self.arr, 1)[:, ::-1], 0)
        self.n = ''
        for y in self.rot_arr:
            for x in y:
                self.n += str(x)

        return self.n_to_decimal()

    def n_to_decimal(self):
        self.decimal = int(self.n, 2) * 17
        #print(f'k = {self.decimal}')
        return self.decimal

    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return self.arr_to_n()
                    sys.exit()

                if pygame.mouse.get_pressed()[0]:
                    try:
                        self.arr[floor(pygame.mouse.get_pos()[
                            1]/BLOCK)][floor(pygame.mouse.get_pos()[0]/BLOCK)] = 1
                        self.generate(floor(pygame.mouse.get_pos()[
                                      0]/BLOCK), floor(pygame.mouse.get_pos()[1]/BLOCK), 1)
                    except AttributeError:
                        pass
                if pygame.mouse.get_pressed()[2]:
                    try:
                        self.arr[floor(pygame.mouse.get_pos()[
                            1]/BLOCK)][floor(pygame.mouse.get_pos()[0]/BLOCK)] = 0
                        self.generate(floor(pygame.mouse.get_pos()[
                                      0]/BLOCK), floor(pygame.mouse.get_pos()[1]/BLOCK), 0)
                    except AttributeError:
                        pass
                pygame.display.update()


class Plotter:

    def __init__(self, arr, x=106*BLOCK, y=17*BLOCK):
        self.arr = arr
        self.x_screen = x
        self.y_screen = y
        self.screen = pygame.display.set_mode((self.x_screen, self.y_screen))
        pygame.display.set_caption('Plotter')
        self.screen.fill('#0A60AC')

    def plotter(self):

        for y_c, y in enumerate(self.arr):
            for x_c, value in enumerate(y):
                color = value*('black') + (value != 1)*('#F0F0F0')
                pygame.draw.rect(self.screen, color, pygame.Rect(
                    x_c*BLOCK, y_c*BLOCK, BLOCK, BLOCK), 6)

    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.plotter()
                pygame.display.update()


class Tupper:

    def __init__(self, k) -> None:
        self.k = k

    def tupper(self, x, y):
        return floor(((floor(self.k + y)//17) // 2**(17*x + (y)%17))%2) > 1/2

if __name__ == "__main__":
    generator = Generator()
    generator.main()
