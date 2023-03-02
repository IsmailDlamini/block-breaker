
# brick breaker Beta version
# This is a beta version so theres many bugs to be found in this code .. I'm working on it
# game play is also abit flawed

import pygame

pygame.init()

HEIGHT = 600
WIDTH = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("block breaker by ismail")

signature = pygame.transform.scale(pygame.image.load("signature.jpg"), (100, 100))


class Paddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        paddle = pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.width, self.height))

    def move(self):
        keys1 = pygame.key.get_pressed()

        if keys1[pygame.K_LEFT] and self.x > 5:
            self.x -= 7

        if keys1[pygame.K_RIGHT] and self.x + self.width < WIDTH - 5:
            self.x += 7


class Bricks:

    number = 20
    blocks = []

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 80, 30))


class Ball:
    def __init__(self, x, y, vel_x, vel_y):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def draw(self):
        pygame.draw.ellipse(screen, "yellow", (self.x, self.y, 25, 25))

    def move(self):
        self.y -= self.vel_y
        self.x -= self.vel_x


main_paddle = Paddle(WIDTH // 2 - 75, 530, 150, 30)
main_ball = Ball(WIDTH // 2 - 5, 505, 5, 5)

FPS = 60
clock = pygame.time.Clock()
bricks = []
clicks = []

started = False

space_taps = 0 

test = main_paddle.x + main_paddle.width // 2


def generate_bricks():

    row = 0
    column = 0

    if len(bricks) == 0:
        if len(clicks) == 0:
            for i in range(44):
                brick1 = Bricks(row, column, (0, 0, 0))
                row += 76
                if row > 800:
                    column += 32
                    row = 0

                bricks.append(brick1)

    for brick_build in bricks:
        pygame.draw.rect(screen, brick_build.color, (brick_build.x, brick_build.y, 75, 30))



def controll_ball_collisions():

    global started

    if main_ball.y > 600:
        main_ball.x = WIDTH // 2 - 5
        main_ball.y = 505
        main_paddle.x = WIDTH // 2 - 75 
        
        started = False


def start_screen():

    global started

    start_screen_font = pygame.font.Font("freesansbold.ttf", 30)
    start_screen_text1 = start_screen_font.render("This is a Beta version", False, "black")
    start_screen_text2 = start_screen_font.render("Has some bugs in code and gameplay flaws but enjoy", False, "black")
    start_screen_text3 = start_screen_font.render("Press _SPACE_BAR_ to start", False, "black")

    if not started:
        screen.blit(start_screen_text3, (WIDTH // 2 - start_screen_text3.get_width() // 2, 350))

    if not started and space_taps == 0:
        screen.blit(start_screen_text1, (WIDTH / 2 - start_screen_text1.get_width() // 2, 250))
        screen.blit(start_screen_text2, (WIDTH / 2 - start_screen_text2.get_width() // 2, 300))
        screen.blit(signature, (WIDTH / 2 - signature.get_width() // 2, 400))


    start_screen_text4 = start_screen_font.render("coded by Ismail", False, "black")
    screen.blit(start_screen_text4, (20, 570))

        


running = True

while running:

    clock.tick(FPS)

    screen.fill("white")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            """""
            for brick in bricks:
                if brick.x < mouse_pos[0] < brick.x + 75:
                    if brick.y < mouse_pos[1] < brick.y + 30:
                        clicks.append(brick)
                        if brick.color == (0, 0, 0):
                            brick.color = (255, 0, 0)

                        elif brick.color == (255, 0, 0):
                            bricks.remove(brick)
                            brick.x = 900
            print(f'{mouse_pos[0]}  {mouse_pos[1]}')
            
            """""

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        started = True
        clicks.append("1")
        space_taps += 1

    if keys[pygame.K_LEFT]:
        if not started:
            main_ball.x -= 7

    if keys[pygame.K_RIGHT]:
        if not started:
            main_ball.x += 7

    if started:
        Ball.move(main_ball)

    for brick in bricks:
        if brick.y + 30 > main_ball.y > brick.y:
            if brick.x < main_ball.x < brick.x + 75:

                if brick.color == (0, 0, 0):
                    brick.color = "red"
                    main_ball.vel_y *= -1

                elif brick.color == "red":
                    bricks.remove(brick)
                    main_ball.vel_y *= -1

    if main_ball.y + 10 > main_ball.y > main_paddle.y - 25:
        if main_paddle.x < main_ball.x < main_paddle.x + 150:
            main_ball.vel_y *= -1

    if main_ball.x < 5 or main_ball.x > 795:
        main_ball.vel_x *= -1

    Paddle.draw(main_paddle)
    Paddle.move(main_paddle)
    generate_bricks()
    Ball.draw(main_ball)
    start_screen()
    controll_ball_collisions()

    pygame.display.update()


pygame.quit()
