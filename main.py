from pygame import *

window_width, window_heigth = 400, 200
pygame.init()
def main():
    global SCREEN, CLOCK
    
    SCREEN = pygame.display.set_mode((window_width, window_heigth))
    CLOCK = pygame.time.clock()
    SCREEN.fil(0,0,0)

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()

def drawGrid():
    blockSize = 20
    for x in range(0, window_width, blockSize):
        for y in range(0, window_heigth, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, (200, 200, 200), rect, 1)


if __name__ == '__main__':
    main()