import pygame
import random


def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        x = 0
        y = 0

        clock = pygame.time.Clock()
        running = True


        while running:
            screen.fill("teal")
            for i in range(1, 33): pygame.draw.line(screen, ("dark gray"), (0, i * 32), (640, i * 32))
            for i in range(1, 33): pygame.draw.line(screen, ("dark gray"), (i * 32, 0), (i * 32, 512))
            position = screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))

            pygame.display.flip()
            clock.tick(60)

            for event in pygame.event.get():
                alea = random.randrange(0, 640)
                alea2 = random.randrange(0, 512)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    a, b = position.topleft
                    if a <= event.pos[0] <= a + 32 and b <= event.pos[1] <= b + 32:
                        while alea % 32 !=0:
                            alea = random.randrange(0, 640)
                        while alea2 % 32 != 0:
                            alea2 = random.randrange(0, 512)
                        x = alea
                        y = alea2
                if event.type == pygame.QUIT:
                    running = False
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
