"""
This displays the credits on the screen.
Thanks to:
 - Francesco Vinci, for helping me with the card animations
 - ZentropyArt, for drawing the game background from scratch
 - SofuAssets, for the pixel-style cards (available on itch.io)
 - Zakiro, for the catchy music (available on itch.io)
 - Khurasan, for the catways font (available on 1001 Free Fonts)
 - SnowyPandas, for the game icons (available on itch.io)
"""

from common.constants import HALF_WIDTH, SCREEN_HEIGHT, NOT_SO_SMALL, BLACK
from common.text_handler import display_text


class Credits:
    def __init__(self):
        self.credits = {
            "Francesco Vinci": "Help with game animations", 
            "ZentropyArt": "Table background", 
            "SofuAssets": "Cards", 
            "Zakiro": "Music", 
            "Khurasan": "Font", 
            "SnowyPandas": "Game icons"
        }
        self.y_positions = [0.3, 0.38, 0.46, 0.54, 0.62, 0.7]
    
    
    def show_credits(self):
        for (name, asset), pos in zip(self.credits.items(), self.y_positions):
            display_text(False, f"{asset}: {name}", NOT_SO_SMALL, BLACK, (HALF_WIDTH, SCREEN_HEIGHT * pos))
            