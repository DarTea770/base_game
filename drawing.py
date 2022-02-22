import pygame
import random


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = []
        self.left = 30
        self.top = 30
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)

    def get_cell(self, mp):
        cx = (mp[0] - self.left) // self.cell_size
        cy = (mp[1] - self.top) // self.cell_size
        if 0 <= cx < self.width and 0 <= cy < self.height:
            return cx, cy
        else:
            return None

    def render(self, screen, textures):
        for y in range(self.height):
            for x in range(self.width):
                coords = ((x * self.cell_size + self.left, y * self.cell_size + self.top,
                           self.cell_size, self.cell_size), (x * self.cell_size + self.left,
                                                             y * self.cell_size + self.top,
                                                             self.cell_size, self.cell_size))
                screen.blit(textures[self.board[y][x]], coords[0])


class Player:
    def __init__(self, size):
        self.pos = (1, 1)
        self.size = size
        self.left = 30
        self.top = 30

    def render(self, screen, textures):
        coords = ((self.pos[0] * self.size + self.left, self.pos[1] * self.size + self.top,
                   self.size, self.size), (self.pos[0] * self.size + self.left,
                                           self.pos[1] * self.size + self.top,
                                           self.size, self.size))
        screen.blit(textures['player'], coords[0])


def start_menu(scr, start_img):
    scr.blit(start_img, (0, 0))
