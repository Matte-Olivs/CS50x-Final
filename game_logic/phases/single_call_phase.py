"""This handles the round where there's only a single card to draw using a SingleCallPhase class."""

from common.button import handle_buttons, one_card_btns
from common.constants import *
from common.text_handler import display_text


class SingleCallPhase:
    def __init__(self, gameplay):
        self.gameplay = gameplay

        self.one_card_btns = one_card_btns(self.win_call, self.lose_call)


    def win_call(self):
        """Confirms the player's win call."""
        self.gameplay.players[(self.gameplay.turn + self.gameplay.player_index) % len(self.gameplay.players)].call = 1
        self.gameplay.player_index += 1


    def lose_call(self):
        """Confirms the player's lose call."""
        self.gameplay.players[(self.gameplay.turn + self.gameplay.player_index) % len(self.gameplay.players)].call = 0
        self.gameplay.player_index += 1


    def execute(self, events):
        """Handles the round where there's only a single card to draw."""
        current_player = self.gameplay.players[(self.gameplay.turn + self.gameplay.player_index) % len(self.gameplay.players)]  # Keep track of the current player 
        display_text(True, f"Player {current_player.pl_num}, will you win or lose?", MEDIUM_FONT, BLACK, (HALF_WIDTH, SCREEN_HEIGHT * 0.4))
        
        other_players = self.gameplay.players.copy()  # Create a copy of the players list
        other_players.remove(current_player)  # Remove the current player
            
        handle_buttons(self.one_card_btns, events)  # Draw and handle the single round buttons
        self.gameplay.card_manager.single_card_round(other_players, self.gameplay.PLAYER_POS, current_player)  # Draw other player's cards
            
        # Check for calls
        if self.gameplay.player_index >= len(self.gameplay.players):
            return "play_phase"
        
        return "single_call_phase"