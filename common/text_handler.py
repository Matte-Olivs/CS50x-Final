"""
This module contains a function to easily display a given string of text on the screen.
"""

import pygame
from common.constants import SCREEN


def display_text(to_update: bool, text: str, font: pygame.font, color: tuple, position: tuple):
    """Display a given text string on the screen"""
    
    text_surf = font.render(str(text), True, color)
    text_rect = text_surf.get_rect(center=position)
    SCREEN.blit(text_surf, text_rect)
    
    if to_update:
        pygame.display.update(text_rect)