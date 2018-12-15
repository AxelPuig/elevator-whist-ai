import numpy as np


class ElevatorWhist:
    """
    Class managing the game environment for AI and human players.
    """

    def __init__(self, n_players):
        self.n_players = n_players

        self.points = [0] * n_players

        self.log = [("gameinit", n_players)]

        print("Game created. Ready for new round.")

    def new_round(self, cards_per_hand):
        """ Creates a new round with cards_per_hand cards for each player """
        # Distribution
        pack = np.array([[value, color] for value in range(1, 14) for color in range(4)])
        np.random.shuffle(pack)

        self.hands = []
        for i in range(self.n_players):
            self.hands.append((pack[i * cards_per_hand:(i + 1) * cards_per_hand]).tolist())

        self.first_card = pack[-1].tolist()
        self.suit_led = pack[-1, 1]

        self.bids = [None] * self.n_players
        self.tricks = [0] * self.n_players
        self.pile = []
        self.current_player = 0
        self.log.append(("newround", cards_per_hand))

    def get_hand(self):
        """ Returns the hand of the current player """
        return self.hands[self.current_player]

    def get_pile(self):
        return self.pile

    def bid(self, bid):
        if self.bids[self.current_player] is not None:
            return
        self.bids[self.current_player] = bid
        self.log.append(("bid", self.current_player, bid))
        self.next_player()

    def next_player(self):
        self.current_player = (self.current_player + 1) % self.n_players

    def play_card(self, card_id):
        self.pile.append(self.hands[self.current_player].pop(card_id))
        self.log.append(("cardplayed", self.current_player, self.pile[-1]))
        self.next_player()

        # If round completed
        if len(self.pile) == self.n_players:
            best_card = max(enumerate(self.pile),
                            key=lambda card: (card[1][1] == self.suit_led, (card[1][0] - 2) % 13))[0]
            taker = (best_card + self.current_player) % self.n_players
            self.log.append(("taker", taker))
            self.tricks[taker] += 1
            self.pile = []

            if not len(self.hands[self.current_player]):
                self.count_points()

    def count_points(self):
        for player in range(self.n_players):
            if self.bids[player] == self.tricks[player]:
                self.points[player] += 2
            else:
                self.points[player] -= abs(self.bids[player] - self.tricks[player])
        self.log.append(("endround", self.points.copy()))

    def get_log(self):
        last_log = self.log
        self.log = []
        return last_log
