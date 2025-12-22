"""This module handles the last player's call if it's not valid using a RecallPhase class.""" 

from common.button import handle_buttons
from common.constants import *
from common.text_handler import display_text


class RecallPhase:
    def __init__(self, gameplay, call_phase):  # Requires the instance of CallPhase declared in core.py
        self.gameplay = gameplay

        self.call_phase = call_phase  # To use the recall phase variables and functions


    def execute(self, events):
        """
        Handles the last player's call if it's not valid.
        """ 
        recall_player = self.gameplay.last_player
        
        handle_buttons(self.call_phase.call_btns, events)

        if self.call_phase.temp_call == recall_player.prev_call:
            display_text(True, self.call_phase.temp_call, MEDIUM_FONT, RED, (HALF_WIDTH, SCREEN_HEIGHT * 0.65))     
        else:
            display_text(True, self.call_phase.temp_call, MEDIUM_FONT, BLACK, (HALF_WIDTH, SCREEN_HEIGHT * 0.65))

        self.gameplay.card_manager.draw_player_hands(self.gameplay.players, recall_player.pl_num, self.gameplay.PLAYER_POS)
           
        if recall_player.call != recall_player.prev_call:
            self.gameplay.player_index = self.gameplay.turn % len(self.gameplay.players)
            
            # Reset the variables
            self.call_phase.total_call = 0  
            self.call_phase.temp_call = 0
            self.call_phase.is_recall = False
            
            return "play_phase"
            
        if self.call_phase.temp_call == recall_player.prev_call:
            display_text(True, self.call_phase.temp_call, MEDIUM_FONT, RED, (HALF_WIDTH, SCREEN_HEIGHT * 0.65))          

        return "recall_phase"