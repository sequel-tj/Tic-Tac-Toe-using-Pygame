import pygame
import sys
import time
from variables import *
from board import *

# initialising pygame
pygame.init()
screen = pygame.display.set_mode((width, height))

# pygame.draw.line(screen, line_color, (100, 100), (100, 500), 10)  # leftmost-vertical-boundary
# pygame.draw.line(screen, line_color, (500, 100), (500, 500), 10)  # rightmost-vertical-boundary
# pygame.draw.line(screen, line_color, (100, 100), (500, 100), 10)  # upper-horizontal-boundary
# pygame.draw.line(screen, line_color, (100, 500), (500, 500), 10)  # lower-horizontal-boundary


def draw_lines(x1, y1, x2, y2, color=line_color, w=10):
    pygame.draw.line(screen, color, (x1, y1), (x2, y2), w)


def draw_circle(x1, y1, color=o_color, w=circle_width, r=circle_radius):
    pygame.draw.circle(screen, color, (x1, y1), r, w)


def check_win(a, p):
    # rows
    for i in range(3):
        if a[i][0] == a[i][1] == a[i][2] == p:
            draw_lines(100, ls[i], 500, ls[i], ls_color[p])
            return p

    # cols
    for i in range(3):
        if a[0][i] == a[1][i] == a[2][i] == p:
            draw_lines(ls[i], 100, ls[i], 500, ls_color[p])
            return p

    # diagonals
    if a[0][0] == a[1][1] == a[2][2] == p:
        draw_lines(100, 100, 500, 500, ls_color[p], 15)
        return p
    if a[0][2] == a[1][1] == a[2][0] == p:
        draw_lines(500, 100, 100, 500, ls_color[p], 15)
        return p


def game_draw():
    s = pygame.Surface((620, 620))  # the size of your rect
    # s.set_alpha(225)  # alpha level
    s.fill(bg_color)  # this fills the entire surface
    screen.blit(s, (0, 0))  # (0,0) are the top-left coordinates

    draw_lines(185, 235, 295, 346, x_color, cross_width + 5)
    draw_lines(295, 235, 185, 346, x_color, cross_width + 5)
    pygame.draw.circle(screen, pygame.Color(o_color), (379, 292), 65, circle_width + 3)

    font = pygame.font.Font('freesansbold.ttf', 68)
    text = font.render('DRAW!', True, x_color)
    textRect = text.get_rect()
    textRect.center = (308, 410)
    screen.blit(text, textRect)

    pygame.display.update()
    time.sleep(1)
    game_restart()


def game_win(p):
    for i in range(3):
        for j in range(3):
            if Board[i][j] == 0:
                Board[i][j] = 3

    s = pygame.Surface((620, 620))  # the size of your rect
    # s.set_alpha(225)  # alpha level
    s.fill(bg_color)  # this fills the entire surface
    screen.blit(s, (0, 0))  # (0,0) are the top-left coordinates
    font = pygame.font.Font('freesansbold.ttf', 68)

    if p == 2:
        pygame.draw.circle(screen, pygame.Color(o_color), (300, 240), 120, circle_width + 15)
        text = font.render('WINNER!', True, x_color)
    else:
        draw_lines(175 + 25, 160, 374 + 25, 360, x_color, cross_width + 15)
        draw_lines(374 + 25, 160, 175 + 25, 360, x_color, cross_width + 15)
        text = font.render('WINNER!', True, o_color)

    textRect = text.get_rect()
    textRect.center = (300, 430)
    screen.blit(text, textRect)

    pygame.display.update()
    time.sleep(1)
    game_restart()


def game_restart():
    for i in range(3):
        for j in range(3):
            Board[i][j] = 0

    # screen color
    screen.fill(pygame.Color(bg_color))
    # boundaries
    draw_lines(100, 232, 500, 232)
    draw_lines(100, 369, 500, 369)
    draw_lines(232, 100, 232, 500)
    draw_lines(369, 100, 369, 500)

    return False


if __name__ == '__main__':
    player = 1
    ls = [167, 300, 434]
    ls_color = [line_color, o_color, x_color]

    win = game_restart()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                # centerX = 1000
                # centerY = 1000

                if (100 <= x < 500) and (100 <= y < 500):
                    if (100 <= x < 235) and (100 <= y < 235):
                        x = 0
                        y = 0
                        # centerX = 167
                        # centerY = 167
                    if (235 <= x < 369) and (100 <= y < 235):
                        x = 0
                        y = 1
                        # centerX = 302
                        # centerY = 167
                    if (369 <= x < 500) and (100 <= y < 235):
                        x = 0
                        y = 2
                        # centerX = 434
                        # centerY = 167
                    if (100 <= x < 235) and (235 <= y < 369):
                        x = 1
                        y = 0
                        # centerX = 167
                        # centerY = 302
                    if (235 <= x < 369) and (235 <= y < 369):
                        x = 1
                        y = 1
                        # centerX = 302
                        # centerY = 302
                    if (369 <= x < 500) and (235 <= y < 369):
                        x = 1
                        y = 2
                        # centerX = 434
                        # centerY = 302
                    if (100 <= x < 235) and (369 <= y < 500):
                        x = 2
                        y = 0
                        # centerX = 167
                        # centerY = 434
                    if (235 <= x < 369) and (369 <= y < 500):
                        x = 2
                        y = 1
                        # centerX = 302
                        # centerY = 434
                    if (369 <= x < 500) and (369 <= y < 500):
                        x = 2
                        y = 2
                        # centerX = 434
                        # centerY = 434

                    if is_available(x, y):
                        if player == 1:
                            draw_circle(ls[y], ls[x], o_color, circle_width, circle_radius)
                        else:
                            draw_lines(ls[y]-shift, ls[x]-shift, ls[y]+shift, ls[x]+shift, x_color, cross_width)
                            draw_lines(ls[y]+shift, ls[x]-shift, ls[y]-shift, ls[x]+shift, x_color, cross_width)

                        mark_board(x, y, player)

                        if check_win(Board, player):
                            win = True
                            # print(f"player {player} wins!")

                        pygame.display.update()
                        player = (player % 2)+1

                        if not win and is_full():
                            time.sleep(1.2)
                            win = False
                            game_draw()
                        if win:
                            time.sleep(1.2)
                            win = False
                            game_win(player)

        pygame.display.update()