import numpy as np


class ElevatorWhist:
    """
    Class managing the game environment for AI and human players.
    """

    def __init__(self, n_players):
        self.n_players = n_players

        self.current_player = 0
        self.distribute()

    def distribute(self):
        """ Creates players' hands """
        self.pack = np.array([[value, color] for value in range(1, 14) for color in range(4)])
        np.random.shuffle(self.pack)

        hands = []
        cards_per_hand = 52 // self.n_players
        for i in range(self.n_players):
            hands.append(self.pack[i * cards_per_hand:(i + 1) * cards_per_hand])
        self.hands = np.array(hands)  # Maybe numpy array useless here...
