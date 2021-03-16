import pygame
import random


def main(x, y):
    """This function is the main of the program"""
    pygame.init()
    pygame.display.set_caption('Practice with pygame "Dog on the lawn"')
    screen = pygame.display.set_mode([x, y])
    colors = {
        'sky_blue_1': [76, 167, 204],
        'sky_blue_2': [102, 192, 229],
        'sky_blue_3': [127, 218, 255],
        'grass_green_1': [47, 127, 0],
        'grass_green_2': [72, 153, 25],
        'grass_green_3': [98, 178, 51],
        'sun_yellow': [252, 212, 64],
        'cloud_grey_1': [234, 233, 233],
        'cloud_grey_2': [215, 213, 211],
        'dimgray': [105, 105, 105],
        'palevioletred': [219, 112, 147],
        'saddlebrown': [139, 69, 19],
        }
    # Set text
    font = pygame.font.Font(None, 32)
    text = font.render('Move the dog with the keyboard arrows!', True, colors['palevioletred'])
    flypos_x = x
    flypos_y = y / 2 - 150
    # Load plane png
    plane_image = pygame.transform.scale(pygame.image.load('plane.png').convert_alpha(), (200, 100))
    plane_image.set_colorkey((255, 255, 255))
    dog_size_x = 80
    dog_size_y = 120
    # Load dog png
    dog_image = pygame.transform.scale(pygame.image.load('dog.png').convert_alpha(), (dog_size_x, dog_size_y))
    dog_image.set_colorkey((255, 255, 255))
    dog_x = 200
    dog_y = 600
    # poop & pee
    poop = pygame.transform.scale(pygame.image.load('poop.png').convert_alpha(), (50, 50))
    poop_coordinates = []
    pee = pygame.transform.scale(pygame.image.load('pee.png').convert_alpha(), (100, 50))
    pee.set_colorkey((255, 255, 255))
    pee_coordinates = []
    # Set the number of clouds and random coordinates of their appearance
    cloud_coordinate_list = []
    for i in range(20):
        x_y_coordinates = random.randrange(0, x, 50), random.randrange(50, y * 0.25, 10)
        cloud_coordinate_list.append(x_y_coordinates)
    clock = pygame.time.Clock()
    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # making poop
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    poop_coordinates.append((dog_x + 15, dog_y + 60))
                if event.key == pygame.K_x:
                    pee_coordinates.append((dog_x + 15, dog_y + 60))
        # Dog control
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] == True:
            dog_x += 8
        if keys[pygame.K_LEFT] == True:
            dog_x -= 8
        if keys[pygame.K_UP] == True:
            dog_y -= 5
        if keys[pygame.K_DOWN] == True:
            dog_y += 5
        screen.fill(colors['sky_blue_3'])
        # Movement of text, banner and airplane
        fly_speed = 4
        if flypos_x > -800:
            flypos_x -= fly_speed
        else:
            flypos_x = x
        sky(x, y, screen, colors)
        grass(x, y, screen, colors)
        for i in range(30, x, 175):
            draw_tree(i, screen, colors)
        sun(x * 0.5, y * 0.1, 20, screen, colors)
        # Load the clouds and set them movement
        cloud_speed = 1
        for i in range(20):
            cloud(cloud_coordinate_list[i][0], cloud_coordinate_list[i][1], 20, screen, colors)
            if cloud_coordinate_list[i][0] < x + 15:
                x_save = cloud_coordinate_list[i][0]
                y_save = cloud_coordinate_list[i][1]
                cloud_coordinate_list.pop([i][0])
                cloud_coordinate_list.insert([i][0], (x_save + cloud_speed + i * 0.015, y_save))
            else:
                y_save = cloud_coordinate_list[i][1]
                cloud_coordinate_list.pop([i][0])
                cloud_coordinate_list.insert([i][0], (-75, y_save))
        banner(flypos_x, 200, screen, colors)
        screen.blit(text, (flypos_x + 260, 250))
        screen.blit(plane_image, (flypos_x, 200))
        for p_c in pee_coordinates:
            screen.blit(pee, p_c)
        for p_c in poop_coordinates:
            screen.blit(poop, p_c)
        screen.blit(dog_image, (dog_x, dog_y))
        # Borders for the dog where it can move
        if dog_y < y * 0.6 - 100:
            dog_y = y * 0.6 - 100
        elif dog_y > y - 120:
            dog_y = y - 120
        elif dog_x < 0:
            dog_x = 0
        elif dog_x > x - 80:
            dog_x = x - 80
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()


def sky(x, y, screen, colors):
    """This function draws the sky"""
    pygame.draw.rect(screen, colors['sky_blue_1'], ((0, 0), (x, y * 0.1)))
    pygame.draw.rect(screen, colors['sky_blue_2'], ((0, y * 0.1), (x, y * 0.15)))


def grass(x, y, screen, colors):
    """This function draws grass"""
    pygame.draw.rect(screen, colors['grass_green_1'], ((0, y * 0.6), (x, y * 0.08)))
    pygame.draw.rect(screen, colors['grass_green_2'], ((0, y * 0.675), (x, y * 0.15)))
    pygame.draw.rect(screen, colors['grass_green_3'], ((0, y * 0.8), (x, y * 0.2)))


def sun(x, y, r, screen, colors):
    """This function draws the sun"""
    color = colors['sun_yellow']
    pygame.draw.circle(screen, color, (x, y), r)  # Sun
    pygame.draw.line(screen, color, (x + r + 5, y), (x + r + 20, y), 1)  # →
    pygame.draw.line(screen, color, (x - r - 5, y), (x - r - 20, y), 1)  # ←
    pygame.draw.line(screen, color, (x, y + r + 5), (x, y + r + 20), 1)  # ↓
    pygame.draw.line(screen, color, (x, y - r - 5), (x, y - r - 20), 1)  # ↑
    pygame.draw.line(screen, color, (x - r, y - r), (x - r - 10, y - r - 10), 2)  # ↖
    pygame.draw.line(screen, color, (x + r, y - r), (x + r + 10, y - r - 10), 2)  # ↗
    pygame.draw.line(screen, color, (x + r, y + r), (x + r + 10, y + r + 10), 2)  # ↘
    pygame.draw.line(screen, color, (x - r, y + r), (x - r - 10, y + r + 10), 2)  # ↙


def cloud(x, y, r, screen, colors):
    """This function draws one cloud with a shadow"""
    color = colors['cloud_grey_1']
    color_shadow = colors['cloud_grey_2']
    pygame.draw.circle(screen, color_shadow, (x, y + 6), r * 0.8)  # Cloud shadow ↓
    pygame.draw.circle(screen, color_shadow, (x + 60, y + 6), r)
    pygame.draw.circle(screen, color_shadow, (x + 12, y + 8), r * 0.9)
    pygame.draw.circle(screen, color_shadow, (x + 38, y + 4), r * 1.3)
    pygame.draw.circle(screen, color, (x, y), r * 0.8)  # Cloud ↓
    pygame.draw.circle(screen, color, (x + 20, y - 5), r)
    pygame.draw.circle(screen, color, (x + 40, y - 10), r * 1.2)
    pygame.draw.circle(screen, color, (x + 60, y), r)
    pygame.draw.circle(screen, color, (x + 12, y + 2), r * 0.9)
    pygame.draw.circle(screen, color, (x + 38, y - 2), r * 1.3)


def banner(x, y, screen, colors):
    """This function draws a banner flying behind the plane"""
    color = colors['dimgray']
    pygame.draw.line(screen, color, (x + 180, y + 60), (x + 240, y + 60), 2)  # rope from the plane
    pygame.draw.line(screen, color, (x + 260, y + 40), (x + 720, y + 40), 2)  # —
    pygame.draw.line(screen, color, (x + 260, y + 80), (x + 720, y + 80), 2)  # —
    pygame.draw.line(screen, color, (x + 240, y + 60), (x + 260, y + 40), 3)  # /
    pygame.draw.line(screen, color, (x + 240, y + 60), (x + 260, y + 80), 3)  # \
    pygame.draw.line(screen, color, (x + 700, y + 60), (x + 720, y + 40), 3)  # /
    pygame.draw.line(screen, color, (x + 700, y + 60), (x + 720, y + 80), 3)  # \


def draw_tree(x, screen, colors):
    """This function draws trees"""
    pygame.draw.rect(screen, colors['saddlebrown'], [x + 44, 385, 15, 100])  # Tree trunk
    pygame.draw.polygon(screen, colors['grass_green_1'], [[x, 450], [x + 50, 350], [x + 100, 450]])  # Branches ↓
    pygame.draw.polygon(screen, colors['grass_green_2'], [[x + 5, 425], [x + 50, 325], [x + 95, 425]])
    pygame.draw.polygon(screen, colors['grass_green_2'], [[x + 10, 400], [x + 50, 325], [x + 90, 400]])
    pygame.draw.polygon(screen, colors['grass_green_3'], [[x + 15, 375], [x + 50, 325], [x + 85, 375]])


main(1024, 768)
