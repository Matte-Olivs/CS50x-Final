"""
This module handles the draw phase for each player using a DrawPhase class. Moreover:
 - it animates the cards, using the deck module
 - it adds each drawn card to the player hand when the animation is complete
"""

from common.constants import *
from card_handling.card_manager import AnimatedCard
from common.text_handler import display_text


class DrawPhase:
        def __init__(self, gameplay):
            self.gameplay = gameplay
            
            self.drawn = None 
            self.full_hands = 0  # If all players have a full hand, move to the next phase


        def check_full_hands(self, to_draw):
            """If all players have a full hand, return the next phase"""
            if self.full_hands == len(self.gameplay.players):
                # Resets variables
                self.full_hands = 0
                self.gameplay.player_index = 0
                self.drawn = None
                self.gameplay.animating = False

                display_text(True, "Time to call!", MEDIUM_FONT, BLACK, (HALF_WIDTH, SCREEN_HEIGHT * 0.4)) 
                pygame.time.wait(2000)
                        
                if to_draw == 1:
                    return "single_call_phase"
                        
                return "call_phase"
                
            self.full_hands = 0  # Reset the full hands variable

            # Count the players who have a full hand
            for player in self.gameplay.players:   
                if len(player.hand) == to_draw: 
                    self.full_hands += 1 
            
            if to_draw != 1:
                self.gameplay.card_manager.draw_player_hands(self.gameplay.players, 0, self.gameplay.PLAYER_POS)  


        def execute(self, to_draw):    
            """Draws cards for each player based on the current turn."""
            current_player = self.gameplay.players[(self.gameplay.turn + self.gameplay.player_index) % len(self.gameplay.players)]  # Keep track of the current player
            self.gameplay.card_manager.draw_deck(self.gameplay.deck, self.gameplay.PLAYER_POS[current_player.pl_num][4])
            
            # Draw a card and create and animated card object   
            if len(self.gameplay.deck.cards) >= 1 and not self.gameplay.animating:  
                self.drawn = self.gameplay.deck.draw_card() # draws a card from the deck
                if sfx_on[0]:    
                    CARD_SOUND.play()
                    
                self.gameplay.anim_c = AnimatedCard(
                    self.drawn, 
                    (HALF_WIDTH, HALF_HEIGHT), 
                    (self.gameplay.PLAYER_POS[current_player.pl_num][0], self.gameplay.PLAYER_POS[current_player.pl_num][1]), 
                    self.gameplay.ANIMATION_DURATION, 
                    current_player.pl_num, 
                    self.gameplay.len_players, 
                    False
                )  # Create and animated card object
                self.gameplay.animating = True

            # Animate the card going from deck to hand 
            if self.gameplay.animating:
                self.gameplay.animating = self.gameplay.card_manager.animation(self.gameplay.anim_c, self.gameplay.PLAYER_POS[current_player.pl_num][4])     

                # If the animation is finished, give a card to the next player
                if not self.gameplay.animating:
                    
                    current_player.hand.append(self.drawn)
                    self.gameplay.player_index += 1
                    
            # If all players have a full hand, return the next phase
            next_phase = self.check_full_hands(to_draw)
            if next_phase == "call_phase":
                return "call_phase"
            elif next_phase == "single_call_phase":
                return "single_call_phase"
           
            return "draw_phase"