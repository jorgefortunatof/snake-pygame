import random
import pygame
from pygame.locals import *

#INICIALIZA MODULOS
pygame.init()

#TAMANHO DA TELA
tela = pygame.display.set_mode((500,500))
pygame.display.set_caption('SNAKE')


#COBRA
snake = [(200,200), (210, 200), (220, 200)]
#CRIA SUPERFICIE CORPO DA COBRA
snake_skin = pygame.Surface((10,10))
#COR
snake_skin.fill((255,255,255))

UP = 0
RIGHT = 1
BOTTOM = 2
LEFT = 3

direction = RIGHT


def moving (direction, snake):
    if direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if direction == BOTTOM:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    
    for pos in range(len(snake) -1 , 0, -1):
        snake[pos] = (snake[pos-1][0], snake[pos-1][1])

def random_new_position():
    return (random.randint(10, 490)//10 *10,random.randint(10, 490)//10 *10 )

def collision (c1, c2):
    return c1[0] == c2[0] and c1[1] == c2[1]
    
def out_of_screen(obj):
    if obj[0] >= 500 or obj[0] < 0:
        return True
    if obj[1] >= 500 or obj[1] < 0:
        return True
    return False

def toutch_itself(snake):
    if len(snake) > 3:
        for i in range(len(snake)):
            if snake[0] == snake [i] and i > 3:
                return True
    return False

#MACA
apple = pygame.Surface((10,10))
apple.fill((255,0,0))
apple_possition = random_new_position()



#FPS
clock = pygame.time.Clock()

#LOPPING INFINITO 
while True:
    clock.tick(20)

    #PEGA OS EVENTOS 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP and direction != BOTTOM:
                direction = UP
            elif event.key == K_DOWN and direction != UP:
                direction = BOTTOM
            elif event.key == K_LEFT and direction != RIGHT:
                direction = LEFT
            elif event.key == K_RIGHT and direction != LEFT:
                direction = RIGHT

    if collision(apple_possition, snake[0]):
        apple_possition = random_new_position()
        snake.append((0,0))
    
    if out_of_screen(snake[0]) or toutch_itself(snake):
        pygame.quit()

    tela.fill((0,0,0))

    tela.blit(apple, apple_possition)
    moving(direction, snake)

    for pos in snake:
        tela.blit(snake_skin, pos)
    
    

    pygame.display.update()