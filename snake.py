import pygame
import random
import pygame.mixer


#To Initalize Game
pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title and BankGround
pygame.display.set_caption("Snakes")
pygame.display.update()
bgimage = pygame.image.load('bg.png')
bg = pygame.transform.scale(bgimage, (screen_width, screen_height))


# Game specific variables


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, white, [x, y, snake_size, snake_size])


def screen_text(text, color, x, y):
    text_screen = font.render(text, True, color)
    gameWindow.blit(text_screen, [x, y])


font = pygame.font.SysFont(None, 55)


def window():
    game_over = False
    exit_game = False
    gameWindow.fill(black)
    screen_text('Welcome To snake Game', white, 300, 250)
    screen_text('Press SpaceBar', white, 350, 300)
    pygame.display.update()
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()


# Game Loop
def gameloop():
    snk_list = []
    snk_length = 1
    exit_game = False
    game_over = False
    snake_x = random.randint(20, screen_width / 1.5)
    snake_y = random.randint(20, screen_height / 1.5)
    velocity_x = 0
    velocity_y = 0
    snake_size = 30
    food_x = random.randint(20, screen_width / 1.5)
    food_y = random.randint(20, screen_height / 1.5)
    score = 0
    clock = pygame.time.Clock()
    fps = 60
    velocity =10
    pause_ = False
    pause_x = 0
    pause_y = 0

    while not exit_game:
        #Screen Shown After Game Over
        if game_over:
            gameWindow.fill(black)
            screen_text('Game Over! Score: '+ str(score) , white, 300, 250)
            screen_text('Press Enter' , white, 300, 280)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        window()
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if not pause_:
                        if event.key == pygame.K_RIGHT:
                            if velocity_x != -velocity:
                                velocity_x = velocity
                                velocity_y = 0
                        if event.key == pygame.K_LEFT:
                            if velocity_x != velocity:
                                velocity_x = -velocity
                                velocity_y = 0
                        if event.key == pygame.K_UP:
                            if velocity_y != velocity:
                                velocity_y = -velocity
                                velocity_x = 0
                        if event.key == pygame.K_DOWN:
                            if velocity_y!= -velocity:
                                velocity_y = velocity
                                velocity_x = 0
                    if event.key == pygame.K_p:
                        #Pausing Mechanism
                        if not pause_:
                            pause_x = velocity_x
                            pause_y = velocity_y
                            velocity_x = velocity_y =0
                            pause_ = True
                        else:
                            velocity_x = pause_x
                            velocity_y = pause_y
                            pause_ = False

            #To Move Snake
            snake_x += velocity_x
            snake_y += velocity_y
            #To Check For Point 
            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 10
                snk_length += 5
                velocity +=1
         
                food_x = random.randint(20, screen_width / 1.5)
                food_y = random.randint(20, screen_height / 1.5)

            gameWindow.fill(black)
            gameWindow.blit(bg,(0,0))
            screen_text('Score:' +str(score), red, 5, 5)
           
            plot_snake(gameWindow, white, snk_list, snake_size)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
	    #Length Increment Logic
            head = []
            head.append(snake_x)
            head.append(snake_y)
            if not pause_:
                snk_list.append(head)
            if len(snk_list) > snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over = True
	    #To Avoid Game Over From Walls
            if snake_x < 0:
                snake_x = screen_width
            if snake_x > screen_width:
                snake_x = 0
            if snake_y < 0:
                snake_y = screen_height
            if snake_y > screen_height:
                snake_y = 0
                # game_over = True
	#To Update Game
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


window()
