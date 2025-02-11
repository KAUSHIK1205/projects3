import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Epic Game Screen")

# Colors
light_blue = (135, 206, 235)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

# Font
font = pygame.font.SysFont(None, 55)

# Text
text = font.render("Welcome to the Game!", True, white)

# Circle settings
circle_x = 100
circle_y = 100
circle_radius = 30
circle_speed = 5

# Rectangle settings
rect_x = 150
rect_y = 150
rect_width = 200
rect_height = 100
rect_speed = 3

# Background music
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(-1)  # Loop the music

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move the circle
    circle_x += circle_speed
    if circle_x >= screen_width - circle_radius or circle_x <= circle_radius:
        circle_speed = -circle_speed
    
    # Move the rectangle
    rect_y += rect_speed
    if rect_y >= screen_height - rect_height or rect_y <= 0:
        rect_speed = -rect_speed
    
    # Dynamic background color
    bg_color = (circle_x % 256, circle_y % 256, rect_y % 256)
    screen.fill(bg_color)

    # Draw the rectangle
    pygame.draw.rect(screen, red, [rect_x, rect_y, rect_width, rect_height])

    # Draw the circle
    pygame.draw.circle(screen, green, (circle_x, circle_y), circle_radius)

    # Draw the text
    screen.blit(text, (screen_width//2 - text.get_width()//2, screen_height//2 - text.get_height()//2))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
