import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72

pygame.init()

background_image = pygame.transform.scale(pygame.image.load('123456.jpg'),
                                            (SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.Font(None, FONT_SIZE)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color('dodgerblue'))  # Background color of sprite
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        self.rect.x = max(
            min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(
            min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height), 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite collision")
all_sprites = pygame.sprite.Group()

sprite1 = Sprite(pygame.Color('white'), 30, 20)
sprite1.rect.x, sprite1.rect.y = random.randint(
    0, SCREEN_WIDTH - sprite1.rect.width), random.randint(
    0, SCREEN_HEIGHT - sprite1.rect.height)
all_sprites.add(sprite1)

sprite2 = Sprite(pygame.Color('red'), 30, 20)
sprite2.rect.x, sprite2.rect.y = random.randint(
    0, SCREEN_WIDTH - sprite2.rect.width), random.randint(
    0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite2)

sprite3 = Sprite(pygame.Color('blue'), 30, 20)
sprite3.rect.x, sprite3.rect.y = random.randint(
    0, SCREEN_WIDTH - sprite3.rect.width), random.randint(
    0, SCREEN_HEIGHT - sprite3.rect.height)
all_sprites.add(sprite3)

running = True
won = False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN
                                         and event.key == pygame.K_x):
            running = False

    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED
        sprite1.move(x_change, y_change)

        if sprite1.rect.colliderect(sprite2.rect) or sprite1.rect.colliderect(sprite3.rect):
            all_sprites.remove(sprite2)
            all_sprites.remove(sprite3)
            all_sprites.add(sprite1)
            won = True
#hello, this is a comment
    # Drawing
    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    # Display win message
    if won:
        win_text = font.render("You win!", True, pygame.Color('black'))
        screen.blit(win_text, ((SCREEN_WIDTH - win_text.get_width()) // 2,
                               (SCREEN_HEIGHT - win_text.get_height()) // 2))

    pygame.display.flip()
    clock.tick(90)

pygame.quit()
