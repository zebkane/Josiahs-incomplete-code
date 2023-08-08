import math

import pygame
from pygame.locals import *

pygame.init()
surface = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True

grid_size = 10
grid_width = math.floor(surface.get_width() / grid_size)
grid_height = math.floor(surface.get_height() / grid_size)

play_x = grid_width / 2 - 1
play_y = grid_height / 2 + 1
play_color = "green"
colors = ["green", "red", "blue", "orange", "pink", "purple"]
color_number = 0
dir = "up"

def px_to_grid(px):
    return px * grid_size


class Player:
    def __init__(self, color, x, y):
        self.pos = {
            "x": x,
            "y": y
        }
        self.parts = [
            [x, y]
        ]
        self.color = color
        self.rect = pygame.Rect(px_to_grid(x), px_to_grid(x), grid_size,grid_size)

    def draw(self, x, y, color):
        self.parts[0][0] = x
        self.parts[0][1] = y
        self.color = color
        self.rect.update(x,y,grid_size,grid_size)
        for part in self.parts:
            pygame.draw.rect(surface, self.color,
                             pygame.Rect(px_to_grid(prev[0]), px_to_grid(part[1]), grid_size, grid_size))
            prev = part[]


class Food:
    def __init__(self, size, x, y, color):
        self.pos = {"x": x,
                    "y": y}
        self.color = color
        self.size = size
        self.rect =pygame.Rect(px_to_grid(self.pos["x"]), px_to_grid(self.pos["y"])
        , grid_size * self.size,grid_size * self.size)

    def draw(self):
        pygame.draw.rect(surface, self.color,pygame.Rect(px_to_grid(self.pos["x"]), px_to_grid(self.pos["y"]), grid_size * self.size,grid_size * self.size))


def draw_grid():
    for i in range(grid_width):
        pygame.draw.line(surface, "white", [grid_size * i, 0], [grid_size * i, surface.get_height()], width=1)

    for i in range(grid_height):
        pygame.draw.line(surface, "white", [0, grid_size * i], [surface.get_height(), grid_size * i], width=1)


player = Player(play_color, play_x, play_y)
foods = [Food(2, 10, 10, "green")]
obstacles = [Food(1, 5, 30, "blue")]
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                play_y -= 1
                dir = "up"
            elif event.key == K_DOWN:
                play_y += 1
                dir = 'down'
            elif event.key == K_RIGHT:
                play_x += 1
                dir = 'right'
            elif event.key == K_LEFT:
                play_x -= 1
                dir = 'left'
            elif event.key == K_GREATER:
                color_number += 1
            elif event.key == K_LESS:
                color_number -= 1

    surface.fill("black")

    draw_grid()
    for food in foods + obstacles:
        food.draw()
        if food.rect.colliderect(player.rect):
            foods.remove(food)
            player.parts.append(food)
    player.draw(play_x, play_y, play_color)
    color_number = color_number % len(colors)
    play_color = colors[color_number]
    for rock in obstacles:
        pass
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
