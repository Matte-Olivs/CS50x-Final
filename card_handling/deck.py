"""
This module contains:
 - a Card class to manage each single card
 - a Deck class to create, shuffle and draw cards
 - an AnimatedCard class to create moving cards
"""

from common.constants import *
import os
import random
import time

CARD_SIZE = (scaler_func(90), scaler_func(120))
CARD_SPACING = scaler_func(50)  # Horizontal spacing between cards
HOVER_OFFSET = scaler_func(30)  # Hover offset


class Card:
    """Represents a single card with its image and a mask for precise mouse detection."""
    def __init__(self, value: str, suit: str):
        self.value = value
        self.suit = suit
        try:
            CARDS_DIR = "cards" 
            original_image = pygame.image.load(os.path.join(ASSETS_DIR, CARDS_DIR, f"{suit}_{value}.png"))  # Load the image of the card
            self.image = pygame.transform.scale(original_image, CARD_SIZE) 
            self.mask = pygame.mask.from_surface(self.image)  # Create its mask
        except pygame.error as e:
            self.image = None
            self.mask = None
            print(f"Error loading card image: {e}")

    def __repr__(self):
        return f"{self.value.capitalize()} of {self.suit.capitalize()}"

    def __str__(self):
        return self.__repr__()


class Deck:
    """Represents the complete deck of cards, manages shuffling and drawing cards."""
    
    try:
        back_image = pygame.image.load("assets/cards/card_back_03.png")  # Load the image of the back of the cards
        back_image = pygame.transform.scale(back_image, CARD_SIZE)
        back_mask = pygame.mask.from_surface(back_image)  # Create a mask for the back
    except pygame.error as e:
        back_image = None
        back_image = None
        back_mask = None
        print(f"Error loading the card's back image: {e}")


    def __init__(self):
        self.cards = []  # Create a lists of cards whith values and suits for build the deck
        self.suits = ["hearts", "diamonds", "clubs", "spades"]
        self.values = ["ace", "2", "3", "4", "5", "6", "7", "jack", "queen", "king"]
        self.create_deck()


    def create_deck(self):
        """Create all the deck using the lists of suits and values for add every card."""
        for suit in self.suits:
            for value in self.values:
                card = Card(value, suit)
                if card.image:
                    self.cards.append(card)
        self.shuffle()
        print("Deck created and shuffled.")


    def shuffle(self): 
        """Shuffle the deck."""
        random.shuffle(self.cards)

   
    def draw_card(self): 
        """Return the card on the top of the deck."""
        if self.cards:
            return self.cards.pop(0)
        return None


class AnimatedCard:
    """Manages the animation of a card, moving it from a start position to an end position."""
    def __init__(self, card: Card, start_pos: tuple[int, int], end_pos: tuple[int, int], duration: float, pl_num: int, len_players: int, is_face_up = False):
        self.card = card
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.duration = duration
        self.pl_num = pl_num
        self.len_players = len_players
        self.is_face_up = is_face_up
        
        self.start_time = time.time()
        self.elapsed_time = 0 
        

    def get_current_pos(self):
        """Moves the card's position based on the elapsed time."""
        self.elapsed_time = time.time() - self.start_time
        t = min(self.elapsed_time / self.duration, 1.0)
        
        current_x = self.start_pos[0] + t * (self.end_pos[0] - self.start_pos[0])
        current_y = self.start_pos[1] + t * (self.end_pos[1] - self.start_pos[1])

        return (current_x, current_y)
    