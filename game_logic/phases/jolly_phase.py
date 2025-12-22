"""This module handles the ace of hearts being played using a JollyPhase class."""

from common.button import handle_buttons, jolly_btns  
from common.constants import *
from common.text_handler import display_text


class JollyPhase:
    def __init__(self, gameplay):
        self.gameplay = gameplay

        self.jolly_btns = jolly_btns(self.jolly_high, self.jolly_low)


    def jolly_high(self):
        """Confirms the player's win call."""
        self.gameplay.last_player.jolly_val = "high"
        self.gameplay.player_index += 1


    def jolly_low(self):
        """Confirms the player's lose call."""
        self.gameplay.last_player.jolly_val = "low"
        self.gameplay.player_index += 1


    def execute(self, events):
        """Handles the ace of hearts being played."""
        display_text(True, "Jolly! Low or high?", MEDIUM_FONT, BLACK, (HALF_WIDTH, SCREEN_HEIGHT * 0.4))
        self.gameplay.card_manager.draw_player_hands(self.gameplay.players, self.gameplay.last_player.pl_num, self.gameplay.PLAYER_POS)
        self.gameplay.card_manager.draw_played_cards(self.gameplay.players, self.gameplay.PLAYER_POS)
        handle_buttons(self.jolly_btns, events)

        if self.gameplay.last_player.jolly_val:
            return "play_phase"
        
        return "jolly_phase"
