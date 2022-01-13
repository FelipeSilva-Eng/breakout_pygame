import pygame


class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def move_paddle_right(self, pixels):
        self.rect.x += pixels

        if self.rect.x >= 700:
            self.rect.x = 700

    def move_paddle_left(self, pixels):
        self.rect.x -= pixels

        if self.rect.x < 0:
            self.rect.x = 0
