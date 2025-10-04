import pygame
pygame.init()


RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Test")

fps = pygame.time.Clock()

area = pygame.Surface((200, 200))
hitbox = pygame.Rect(0, 0, 100, 200)

font = pygame.font.SysFont("Times New Roman", 48)
font.set_bold(True)
font.set_italic(True)

text = font.render("Text", True, BLUE)

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False


    window.fill(GREEN)
    area.fill(RED)

    window.blit(area,(100,0))

    pygame.display.flip()
    fps.tick(60)

pygame.quit()

