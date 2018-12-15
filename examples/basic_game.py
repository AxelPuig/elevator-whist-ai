from elevatorwhist import ElevatorWhist

n_players = int(input("How many players? "))
game = ElevatorWhist(n_players)
n_cards = int(input("How many cards? "))
game.new_round(n_cards)

print("Suit led is %i" % game.suit_led)
while None in game.bids:
    print("Player %i hand : %s" % (game.current_player, game.get_hand()))
    game.bid(int(input("Bid? ")))

while True:
    print("Player %i your hand is %s" % (game.current_player, game.get_hand()))
    game.play_card(int(input("Play a card: ")))
    log = game.get_log()
    print(log)
    if "endround" in (l[0] for l in log):
        print("End ! Your points are: %s" % game.points)
        break
