"""This module handles the call phase for players using a CallPhase class."""

from common.button import handle_buttons, normal_round_btns
from common.constants import *
from common.text_handler import display_text


class CallPhase:
    def __init__(self, gameplay):
        self.gameplay = gameplay

        self.total_call = 0  # Keeps track of the sum of each call
        self.temp_call = 0  # The number to display if the player has not called yet
        self.call_btns = normal_round_btns(self.increase_call, self.decrease_call, self.confirm_call)  # Increase, decrease and confirm buttons

        self.is_recall = False

        self.call_surf = LARGE_FONT.render(str(self.temp_call), True, BLACK)  # To display the current selected call
        self.call_rect = self.call_surf.get_rect(center=((HALF_WIDTH, SCREEN_HEIGHT * 0.65)))
        

    def increase_call(self):
        """Increases the current player's call and the total call."""
        if self.temp_call < self.gameplay.cards_to_draw():
            self.temp_call += 1
            self.total_call += 1

    def decrease_call(self):
        """Decreases the current player's call and the total call."""
        if self.temp_call > 0:   
            self.temp_call -= 1
            self.total_call -= 1

    def confirm_call(self):        
        """Confirms the current player's call and moves the index to the next player."""
        if self.is_recall:
            self.gameplay.last_player.call = self.temp_call
        else:
            self.gameplay.card_manager.show_cards = False
            self.gameplay.players[(self.gameplay.turn + self.gameplay.player_index) % len(self.gameplay.players)].call = self.temp_call # Assign the call
            self.gameplay.player_index += 1  # Increase the player counter
            self.temp_call = 0  # Reset the temp call
            

    def execute(self, to_draw, events):
        """Handles the call phase for players by saving each call in player.call."""
        current_player = self.gameplay.players[(self.gameplay.turn + self.gameplay.player_index) % len(self.gameplay.players)]  # Keep track of the current player
        self.gameplay.card_manager.draw_player_hands(self.gameplay.players, current_player.pl_num, self.gameplay.PLAYER_POS) 

        display_text(True, f"Player {current_player.pl_num} is calling...", MEDIUM_FONT, BLACK, (HALF_WIDTH, SCREEN_HEIGHT * 0.4))    
        handle_buttons(self.call_btns, events)  # Draw and handle the call buttons
        display_text(True, self.temp_call, MEDIUM_FONT, BLACK, (HALF_WIDTH, SCREEN_HEIGHT * 0.65))  # If the player has not made a call, draw the current number on the screen
             
        # Check for calls
        if self.gameplay.player_index >= len(self.gameplay.players):
            # Recall phase if the last call is wrong
            if self.total_call == to_draw:
                self.is_recall = True
                self.gameplay.last_player = current_player
                current_player.prev_call = current_player.call
                display_text(True, f"Player {self.gameplay.player_index}, choose a different call", MEDIUM_FONT, BLACK, (HALF_WIDTH, SCREEN_HEIGHT * 0.6))
                pygame.time.wait(2000)      
                    
                return "recall_phase"
            else:
                self.gameplay.player_index = self.gameplay.turn % len(self.gameplay.players)
                self.total_call = 0
                self.temp_call = 0
                return "play_phase"
            
        return "call_phase"