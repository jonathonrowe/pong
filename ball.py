import pygame
from constants import BALL_LENGTH
from rectangleshape import RectangleShape

class Ball(RectangleShape):
    def __init__(self, x, y):
        super().__init__(x, y, BALL_LENGTH, BALL_LENGTH)
        