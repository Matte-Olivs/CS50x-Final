"""
This module contains fundamental constants for each file
 - screen informations
 - screen setup
 - assets loading: background, button image and cursor image
 - fonts
 - default RGB colors
 - Relative path to files using os (learned during the CS50AI course)
 - button dimensions based on the screen size (ui scaling learned and suggested by ChatGPT)
"""

import os
import pygame

pygame.init()


# Initial setup
# Gets desktop screen information for a dynamic fullscreen window.
screen_info = pygame.display.Info()
SCREEN_WIDTH = screen_info.current_w
SCREEN_HEIGHT = screen_info.current_h
HALF_WIDTH = SCREEN_WIDTH // 2
HALF_HEIGHT = SCREEN_HEIGHT // 2
SCREEN_DIMENSIONS = (SCREEN_WIDTH, SCREEN_HEIGHT)


# Pygame screen setup
screen_flags = screen_flags = pygame.NOFRAME | pygame.RESIZABLE
SCREEN = pygame.display.set_mode(SCREEN_DIMENSIONS, screen_flags)
pygame.display.set_caption("I Dont't Know!")


BASE_WIDTH = 1920
BASE_HEIGHT = 1080

def scaler_func(dimension):
    """This snippet of code was suggested by ChatGPT"""
    scale_factor = min(SCREEN_WIDTH / BASE_WIDTH, SCREEN_HEIGHT / BASE_HEIGHT)

    return int(dimension * scale_factor)


# Load menu's assets
ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")  # abspath suggested by ChatGPT

try:
    BUTTONS_DIR = os.path.join(ASSETS_DIR, "buttons")
    
    BUTTON_BACKGROUND = pygame.image.load(os.path.join(BUTTONS_DIR, "button1.png")).convert_alpha()
    ALT_BTN_BACKGROUND = pygame.image.load(os.path.join(BUTTONS_DIR, "button2.png")).convert_alpha()
    CURSOR_IMAGE = pygame.image.load(os.path.join(BUTTONS_DIR, "cursor.png")) 
    CURSOR_IMAGE.set_colorkey((255, 255, 255))
    TABLE_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_DIR, "backgrounds", "table.png")).convert_alpha(), SCREEN_DIMENSIONS)
    
    print("Menu assets loaded successfully")
except pygame.error as e:
    print(f"Error loading resources: {e}!")
    print("Make sure all of the required assets exist in the assets folder.")
    
    pygame.quit()
    exit()


# Load music and starts playing
MUSIC_DIR = os.path.join(ASSETS_DIR, "music")
pygame.mixer.music.load(os.path.join(MUSIC_DIR, "Let'sGo.wav"))
pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=0)  # loops=-1 makes the music play indefinitely


# Load sounds
sfx_on = [True]  # Keep track of the sfx on/off
SFX_DIR = os.path.join(ASSETS_DIR, "SFX")
CARD_SOUND = pygame.mixer.Sound(os.path.join(SFX_DIR, "card_sound.mp3"))
CLICK_SOUND = pygame.mixer.Sound(os.path.join(SFX_DIR, "btn_click.mp3"))


# Load game icons:
try:
    ICONS_DIR = os.path.join(ASSETS_DIR, "icons")

    scaled_dim = (scaler_func(40), scaler_func(40))

    HEART_IMG = pygame.image.load(os.path.join(ICONS_DIR, "heart.png")).convert_alpha() 
    HEART_IMG = pygame.transform.scale(HEART_IMG, scaled_dim)

    CALL_IMG = pygame.image.load(os.path.join(ICONS_DIR, "call.png")).convert_alpha()  
    CALL_IMG = pygame.transform.scale(CALL_IMG, scaled_dim)

    EYE_IMG = pygame.image.load(os.path.join(ICONS_DIR, "eye.png")).convert_alpha()  
    EYE_IMG = pygame.transform.scale(EYE_IMG, scaled_dim)

    STAR_IMG = pygame.image.load(os.path.join(ICONS_DIR, "star.png")).convert_alpha() 
    STAR_IMG = pygame.transform.scale(STAR_IMG, scaled_dim) 

    ICONS = {"lives": HEART_IMG, "cards": EYE_IMG, "call": CALL_IMG, "points": STAR_IMG}

    print("Icons loaded successfully")
except pygame.error as e:
    print(f"Error loading icon: {e}")


# Colors
DEFAULT_TEXT_COLOR = (0, 0, 0)
HOVER_TEXT_COLOR = (200, 200, 200)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Fonts
FONT_PATH = os.path.join(ASSETS_DIR, "fonts", "Catways.ttf")
LARGE_FONT = pygame.font.Font(FONT_PATH, scaler_func(100))
MEDIUM_FONT = pygame.font.Font(FONT_PATH, scaler_func(50))
NOT_SO_SMALL = pygame.font.Font(FONT_PATH, scaler_func(40))
SMALL_FONT = pygame.font.Font(FONT_PATH, scaler_func(25))


# Button dimensions
BUTTON_WIDTH = scaler_func(250)
BUTTON_HEIGHT = scaler_func(80)
BUTTON_TEXT_SIZE = scaler_func(40) 
CURSOR_WIDTH = 60
CURSOR_HEIGHT = 40
