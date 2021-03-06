import pygame
import pygame.freetype
import random

pygame.init()

PED_IMAGES = ['Assets/DaPad.jpg', 'Assets/DaPad2.jpg', 'Assets/DaPad3.jpg', 'Assets/DaPad4.jpg', 'Assets/DaPad5.jpg',
              'Assets/DaPad6.jpg']

state = {

    "display_width": 1400,
    "display_height": 850,
    "car_position": [315, 425],
    'car_speed': 5,
    "enemy_position": [0, 0],
    "enemy_position2": [0, 0],
    "enemy_speed": 3,
    "enemy_speed2": 2,
    'car_image': pygame.image.load('Assets/Dababy.jpg'),
    'enemy_image': pygame.image.load(random.choice(PED_IMAGES)),
    'enemy_image2': pygame.image.load(random.choice(PED_IMAGES)),
    "crashed": False,
    "score": 0
}


#####


def draw_score():
    font_color = (0, 150, 250)
    font_obj = pygame.font.Font("Assets/arial.ttf", 50)

    # Render the objects
    text_obj = font_obj.render('Score: ' + str(state['score']), True, font_color)
    gameDisplay.blit(text_obj, (22, 0))


def move_enemy():
    enemy_position = state['enemy_position']
    enemy_position[1] += state['enemy_speed']
    if enemy_position[1] > state['display_height']:
        state['enemy_speed'] = 1 + 4 * random.random()
        enemy_position = [state['display_width'] * random.random(), 0]
        state['score'] += 1
        state['enemy_position'] = enemy_position
        state['enemy_image'] = pygame.image.load(random.choice(PED_IMAGES))
def move_enemy2():
    enemy_position2 = state['enemy_position2']
    enemy_position2[1] += state['enemy_speed2']
    if enemy_position2[1] > state['display_height']:
        state['enemy_speed2'] = 1 + 4 * random.random()
        enemy_position2 = [state['display_width'] * random.random(), 0]
        state['score'] += 1
        state['enemy_position2'] = enemy_position2
        state['enemy_image2'] = pygame.image.load(random.choice(PED_IMAGES))



def check_collision():
    x_diff = abs(state['enemy_position'][0] - state['car_position'][0])
    y_diff = abs(state['enemy_position'][1] - state['car_position'][1])
    if x_diff <= 180 and y_diff <= 180:
        state['crashed'] = True


def render_assets():
    gameDisplay.fill(white)
    pygame.display.set_caption('Lets GOOOO!')
    gameDisplay.blit(state['enemy_image'], tuple(state['enemy_position']))
    gameDisplay.blit(state['enemy_image2'], tuple(state['enemy_position2']))
    gameDisplay.blit(state['car_image'], tuple(state['car_position']))
    draw_score()
    pygame.display.update()


def process_game_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:

            ######added while loop
            if event.key == pygame.K_LEFT:
                pygame.key.set_repeat(10)
                state['car_position'][0] -= state['car_speed']

            if event.key == pygame.K_RIGHT:
                pygame.key.set_repeat(10)
                state['car_position'][0] += state['car_speed']
            if event.key == pygame.K_r:
                state["car_position"] = [315, 425]
                state['car_speed'] = 5
                state["enemy_position"] = [0, 0]
                state["enemy_speed"] = 3
                state["crashed"] = False
                state["score"] = 0
                state['car_image'] = pygame.image.load('Assets/Dababy.jpg')
                state["car_position2"] = [315, 425]
                state['car_speed2'] = 5
                state["enemy_position2"] = [0, 0]
                state["enemy_speed2"] = 2
                state["crashed"] = False
                state["score"] = 0


                ###

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pass


def check_crash():
    if state['crashed']:
        state['car_speed'] = 0
        state['enemy_speed'] = 0
        state['car_image'] = pygame.image.load('Assets/Badbaby.jpg')

        font_color_2 = (3, 150, 250)
        font_obj_2 = pygame.font.Font("Assets/arial.ttf", 75)
        text_obj_2 = font_obj_2.render(('OH NO YOUR A BAD BABY!'), True, font_color_2)
        gameDisplay.blit(text_obj_2, (400, 200))

        font_color_2 = (3, 150, 250)
        font_obj_2 = pygame.font.Font("Assets/arial.ttf", 75)
        text_obj_2 = font_obj_2.render(('Press R to Restart'), True, font_color_2)
        gameDisplay.blit(text_obj_2, (400, 300))

    pygame.display.update()


gameDisplay = pygame.display.set_mode((state['display_width'], state['display_height']))
black = (0, 0, 0)
white = (255, 255, 255)
clock = pygame.time.Clock()


def main_loop():
    while True:
        process_game_events()
        clock.tick(100)
        if not state['crashed']:
            move_enemy()
            move_enemy2()
            check_collision()
            render_assets()
            check_crash()


main_loop()

pygame.quit()
quit()
