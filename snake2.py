import pygame
import random

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
pygame.init()
screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption("Snake game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)
font2 = pygame.font.SysFont(None,60)

def text_screen(text, color, x, y):
    screen_text = font2.render(text, True, color)
    screen.blit(screen_text, [x,y])

def score_manager(score=None):
    hiscore = 0
    with open('hiscore.txt','r+') as f:
        try:
            hiscore= int(f.read())
        except:
            pass
    if score is None:
        return hiscore
    
    else:
        with open("hiscore.txt",'r+') as f:
            try:
                hiscore = int(f.read())
            except:
                hiscore = 0
            if score > hiscore:
                f.write(str(score))




def gameloop():
    exit_game = False
    game_over=False
    snake_x = 100
    snake_y = 100
    snake_size = 20
    speed = 300
    velocity_x = speed
    velocity_y = 0
    snake_list = []
    snake_len = 2

    #Food
    food_x = random.randint(20,screen.get_width())
    food_y = random.randint(20,screen.get_height())
    food_size = 8
    score = 0
    while not exit_game:
        keys = pygame.key.get_pressed()
        if game_over:
            screen.fill(white)
            screen.blit(font2.render("Game Over!!Press Space", True, red), (screen.get_width()/3, screen.get_height()/3))
            if keys[pygame.K_SPACE]: gameloop()
        else:
            dt = clock.get_time()/1000

            # Correct movement
            if keys[pygame.K_UP]:
                velocity_x = 0
                velocity_y = -speed
            if keys[pygame.K_DOWN]:
                velocity_x = 0
                velocity_y = speed
            if keys[pygame.K_LEFT]:
                velocity_x = -speed
                velocity_y = 0
            if keys[pygame.K_RIGHT]:
                velocity_x = speed
                velocity_y = 0
            
            if snake_x>screen.get_width():
                snake_x = 0
            if snake_y>screen.get_height():
                snake_y = 0 
            if snake_x<0:
                snake_x = screen.get_width()
            if snake_y<0:
                snake_y = screen.get_height()
            
            snake_x += velocity_x*dt
            snake_y+= velocity_y*dt
            
            
            screen.fill(black)
            text = font.render(f"Score {score}",True,white)
            screen.blit(font.render(f"Highest Score: {str(score_manager())}", True, white), (20, 50))

            screen.blit(text, (20,10, 55,55))
            
            head = (snake_x,snake_y)
            snake_rect = pygame.draw.rect(screen, white, (head[0], head[1], snake_size, snake_size))
            food = pygame.draw.circle(screen, red, center=(food_x,food_y), radius=food_size)
            
            for (x,y) in snake_list:
                pygame.draw.rect(screen, white, (x, y, snake_size, snake_size))
            
            if len(snake_list)>snake_len:
                del snake_list[0]
                
            if snake_rect.colliderect(food) :
                score += 1
                food_x = random.randint(20,screen.get_width())
                food_y = random.randint(20,screen.get_height())
                speed += 10
                snake_len+=5
                snake_list.append((snake_x,snake_y))
            
            snake_list.append(head)
            if head in snake_list[:-2]:
                score_manager(score)
                game_over=True
            

            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
        pygame.display.flip()
        clock.tick(60)  # FPS

def welcome():
    exit_game = False
    while not exit_game:
        screen.fill((0,0,0))
        text_screen("Welcome to Snakes", white, 420, 250)
        text_screen("Press Space Bar To Play", white, 390, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(60)

welcome()
pygame.quit()
quit()
