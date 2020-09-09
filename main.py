import pygame
import sys
import random


# General setup
pygame.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont("verdana", 20)
gameIcon = pygame.image.load('icon.ico')
pygame.display.set_icon(gameIcon)

# Main Window
screen_width = 720
screen_height = 660
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Colors
light_grey = (200, 200, 200)
bg_color = pygame.Color('grey12')

# Functions


def ball_animation():
    global ball_speed_x, ball_speed_y, p_score, o_score

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        ball_speed_x *= -1
        p_score += 1

    if ball.right >= screen_width:
        ball_speed_x *= -1
        o_score += 1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


def player_animation():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_ai():
    if opponent.top < ball.y:
        opponent.y += opponent_speed
    if opponent.bottom > ball.y:
        opponent.y -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x, y])


# Game Rectangles
ball = pygame.Rect(screen_width // 2 - 15, screen_height // 2 - 15, 20, 20)
player = pygame.Rect(screen_width - 20, screen_height // 2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height // 2 - 70, 10, 140)

# Game Variables
ball_speed_x = 5
ball_speed_y = 5
player_speed = 0
opponent_speed = 7
p_score = 0
o_score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -= 6
            if event.key == pygame.K_DOWN:
                player_speed += 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 6
            if event.key == pygame.K_DOWN:
                player_speed -= 6

    # Game Logic
    ball_animation()
    player_animation()
    opponent_ai()
    k = "Score: {}".format(p_score)
    l = "Score: {}".format(o_score)

    # Visuals
    screen.fill(bg_color)
    text_screen(l, light_grey, 30, 20)
    text_screen(k, light_grey, 590, 20)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width // 2,
                                            0), (screen_width // 2, screen_height))

    pygame.display.flip()
    clock.tick(60)
