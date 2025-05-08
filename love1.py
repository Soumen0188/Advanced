import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animated Love Sign")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)

# Load images
heart_image = pygame.image.load("heart.png")  # Replace with your heart image path

# Set initial position and speed
heart_x = width // 2
heart_y = height // 2
speed_x = 5
speed_y = 3

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update heart position
    heart_x += speed_x
    heart_y += speed_y

    # Check boundaries
    if heart_x <= 0 or heart_x >= width:
        speed_x = -speed_x
    if heart_y <= 0 or heart_y >= height:
        speed_y = -speed_y

    # Clear the screen
    screen.fill(white)

    # Draw heart
    screen.blit(heart_image, (heart_x, heart_y))

    # Update the display
    pygame.display.flip()

    # Add a small delay
    pygame.time.delay(30)

# Clean up
pygame.quit()
sys.exit()

