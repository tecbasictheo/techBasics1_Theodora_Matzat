
# I hope I did the class right, I was a bit unsure if it was enough
# the glow function did not really work, so I wanted to submit a working code first before i add the bonus
# It needs a moment to load
import random
import pygame
import math

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 300
BACKGROUND_COLOR = ("light blue")
pegasus_group = pygame.sprite.Group()

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pegasus')


class PEGASUS(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        color = ["#FFC0CB", "#F8C8DC", "#FFB6C1", "#FF69B4", "#E37383", "#F33A6A", "#E30B5C", "#673147", "#FF10F0",
                 "#9F2B68"]
        color_choice = random.choice(color)

        self.image = pygame.image.load("pegasus.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = 1100
        self.rect.y = random.randrange(SCREEN_HEIGHT)
        self.image.fill((color_choice), special_flags=pygame.BLEND_ADD)
        self.speed = random.randint(1, 20)
        self.glow_time = 0

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > SCREEN_WIDTH:
            self.rect.x = -200
        '''self.glow_time += 0.05
        glow_intensity = int((math.sin(self.glow_time) + 1) * 75)
        self.image.fill((glow_intensity, glow_intensity, glow_intensity), special_flags=pygame.BLEND_ADD)
        self.image.fill((color_choice), special_flags=pygame.BLEND_ADD)'''


clock = pygame.time.Clock()
for i in range(5):
    new_pegasus = PEGASUS()
    pegasus_group.add(new_pegasus)

flag = True
while flag:
    clock.tick(90)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    pegasus_group.update()
    screen.fill(BACKGROUND_COLOR)

    pegasus_group.draw(screen)
    pygame.display.flip()

pygame.quit()
exit(0)
