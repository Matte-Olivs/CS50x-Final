"""
This module handles the end of the turn, when each player has an empty hand, using an EndPhase class. Moreover:
- Removes players if they have no lives left
- Resets the deck
- Checks if the game has finished
"""

from common.constants import *
from card_handling.card_manager import Deck
from common.text_handler import display_text


class EndPhase:
    def __init__(self, gameplay):
        self.gameplay = gameplay


    def turn_reset(self):
        """Resets all the variables at the end of a turn."""
        self.gameplay.player_index = 0

        for player in self.gameplay.players:
            player.reset_variables()
           

    def is_draw_reset(self, players_lost):
        """If there's a draw, insert players back in the players list and move to the next round."""
        SCREEN.blit(TABLE_BACKGROUND, (0, 0))
        display_text(True, f"No winner, let's have another round!", MEDIUM_FONT, BLACK, (HALF_WIDTH, HALF_HEIGHT))   
        pygame.display.flip() 
        pygame.time.wait(2000)     
            
        SCREEN.blit(TABLE_BACKGROUND, (0, 0))  
        pygame.display.flip()
            
        for player in players_lost:
            player.lives += 1
            self.gameplay.players.append(player)


    def execute(self):
        self.gameplay.deck = Deck()
        players_lost = []  # Keep track of players who have 0 lives

        for player in self.gameplay.players:
            if player.call != player.points:
                player.life_lost()

            if player.lives == 0:
                players_lost.append(player)
        
        # Remove players who have 0 lives left
        for player in players_lost:
            self.gameplay.players.remove(player)

        if len(self.gameplay.players) == 0:  # If there's a draw, the players left have another round
           self.is_draw_reset(players_lost)
            
        self.turn_reset()
            
        return "draw_phase"