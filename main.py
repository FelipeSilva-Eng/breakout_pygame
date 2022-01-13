import pygame
from paddle import Paddle
from ball import Ball
from brick import Brick


pygame.init()

# color to paint the briks
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)

score = 0
lives = 3

size = (800, 600)
screen = pygame.display.set_mode(size, vsync=1)
pygame.display.set_caption('Breakout')



paddle = Paddle(LIGHTBLUE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

all_sprites_list = pygame.sprite.Group()

all_bricks = pygame.sprite.Group()
for i in range(7):
    brick = Brick(RED, 80, 30)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)

for i in range(7):
    brick = Brick(ORANGE, 80, 30)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)

for i in range(7):
    brick = Brick(YELLOW, 80, 30)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)

all_sprites_list.add(paddle)
all_sprites_list.add(ball)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        paddle.move_paddle_right(5)
    if keys[pygame.K_LEFT]:
        paddle.move_paddle_left(5)

    if ball.rect.x >= 790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 590:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            # display game over for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render('GAME OVER', 1, WHITE)
            screen.blit(text, (250, 300))
            pygame.display.update()
            pygame.time.wait(3000)

            pygame.quit()
    if ball.rect.y < 40:
        ball.velocity[1] = -ball.velocity[1]

    # detect colision
    if pygame.sprite.collide_mask(ball, paddle):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.bounce()

    # check if the ball collides with any of the bricks
    brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
    for brick in brick_collision_list:
        ball.bounce()
        score += 1
        brick.kill()

        if len(all_bricks) == 0:
            # display the messa level complete for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render('LEVEL COMPLETE', 1, WHITE)
            screen.blit(text, (200, 300))
            pygame.display.flip()
            pygame.time.wait(3000)

            pygame.quit()

    screen.fill(DARKBLUE)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38],2 )

    all_sprites_list.draw(screen)
    all_sprites_list.update()

    # display the score and number of lives at top of the screen
    font = pygame.font.Font(None, 34)
    text = font.render('Score: ' + str(score), 1, WHITE)
    screen.blit(text, (20, 10))
    text = font.render('Lives: ' + str(lives), 1, WHITE)
    screen.blit(text, (650, 10))
    
    pygame.display.update()

    clock.tick(60)


