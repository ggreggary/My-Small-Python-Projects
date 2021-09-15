import pygame, sys, random


def t_ball():
    global x_speed_x, y_speed_y, users_score, rivals_score

    ball.x += x_speed_x
    ball.y += y_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        y_speed_y *= -1

    if ball.left <= 0:
        moving_ball()
        users_score += 1

    if ball.right >= screen_width:
        moving_ball()
        rivals_score += 1

    if ball.colliderect(user) or ball.colliderect(rival):
        x_speed_x *= -1


def player1():
    user.y += users_speed

    if user.top <= 0:
        user.top = 0
    if user.bottom >= screen_height:
        user.bottom = screen_height


def my_rival():
    if rival.top < ball.y:
        rival.y += rivals_speed
    if rival.bottom > ball.y:
        rival.y -= rivals_speed

    if rival.top <= 0:
        rival.top = 0
    if rival.bottom >= screen_height:
        rival.bottom = screen_height


def moving_ball():
    global x_speed_x, y_speed_y

    ball.center = (screen_width / 2, screen_height / 2)
    y_speed_y *= random.choice((1, -1))
    x_speed_x *= random.choice((1, -1))


pygame.init()
clock = pygame.time.Clock()

screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('My Pong Game')

bby_blue = (200, 255, 255)
color_bkgd = pygame.Color('brown1')

users_score = 0
rivals_score = 0
basic_font = pygame.font.SysFont("Verdana", 40)

ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
user = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
rival = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

x_speed_x = 8 * random.choice((1, -1))
y_speed_y = 8 * random.choice((1, -1))
users_speed = 0
rivals_speed = 8

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                users_speed -= 8
            if event.key == pygame.K_DOWN:
                users_speed += 8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                users_speed += 8
            if event.key == pygame.K_DOWN:
                users_speed -= 8

    player1()
    my_rival()
    t_ball()

    screen.fill(color_bkgd)
    pygame.draw.rect(screen, bby_blue, user)
    pygame.draw.rect(screen, bby_blue, rival)
    pygame.draw.ellipse(screen, bby_blue, ball)
    pygame.draw.aaline(screen, bby_blue, (screen_width / 2, 0), (screen_width / 2, screen_height))

    user_scorecard = basic_font.render(f'{users_score}', False, bby_blue)
    screen.blit(user_scorecard, (418, 280))

    rival_scorecard = basic_font.render(f'{rivals_score}', False, bby_blue)
    screen.blit(rival_scorecard, (460, 280))

    pygame.display.flip()
    clock.tick(60)
