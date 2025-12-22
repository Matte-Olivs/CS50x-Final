"""
This module handles settings. It allows to:
 - Change the music volume
 - Turn the SFX sounds on/off
"""

import pygame
from common.button import Button, handle_buttons
from common.constants import *
from common.text_handler import display_text


def load_settings_btns(increase_vol, decrease_vol, allow_sfx):
    buttons = [
        Button(
            (SCREEN_WIDTH * 0.53), SCREEN_HEIGHT * 0.6, BUTTON_WIDTH * 0.4, BUTTON_HEIGHT * 0.8,
            BUTTON_TEXT_SIZE, ALT_BTN_BACKGROUND, None, text="+",
            on_click_callback=increase_vol
        ),

        Button(
            (SCREEN_WIDTH * 0.47), SCREEN_HEIGHT * 0.6, BUTTON_WIDTH * 0.4, BUTTON_HEIGHT * 0.8,
            BUTTON_TEXT_SIZE, ALT_BTN_BACKGROUND, None, text="-", 
            on_click_callback=decrease_vol
        ),
        
        Button(
            HALF_WIDTH, (SCREEN_HEIGHT * 0.45), BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_TEXT_SIZE,
            BUTTON_BACKGROUND, CURSOR_IMAGE, text="SFX",
            on_click_callback=allow_sfx
        )
    ]

    return buttons


class Settings:
    def __init__(self):
        self.btns = load_settings_btns(self.increase_vol, self.decrease_vol, self.allow_sfx)
        self.volume = 1  # Keep track of the volume (it's a value between 0 and 1)


    def increase_vol(self):
        if self.volume < 1:
            self.volume += 0.1

        pygame.mixer.music.set_volume(round(self.volume, 1))

    def decrease_vol(self):
        if self.volume > 0.1:
            self.volume -= 0.1

        pygame.mixer.music.set_volume(round(self.volume, 1))


    def allow_sfx(self):
        if sfx_on[0]: 
            sfx_on[0] = False
        else:
            sfx_on[0] = True
    

    def run(self, events):
        display_text(False, f": {round(self.volume, 1) * 100} %", MEDIUM_FONT, BLACK, (SCREEN_WIDTH * 0.6, SCREEN_HEIGHT * 0.6))
        display_text(False, "Volume", MEDIUM_FONT, BLACK, (HALF_WIDTH, SCREEN_HEIGHT * 0.55)) 
        
        sfx = "on"
        if sfx_on[0]:
            sfx = "on"
        else:
            sfx= "off"
            
        display_text(False, f": {sfx}", MEDIUM_FONT, BLACK, (SCREEN_WIDTH * 0.6, (SCREEN_HEIGHT * 0.45)))

        handle_buttons(self.btns, events)
