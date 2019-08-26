
class Player:
    VERSION = "1.0"

    def betRequest(self, game_state):

        players = game_state["players"]
        my_hand = {}
        for player in players:
            if player["name"] == "SteamBot":
                my_hand = player["hole_cards"]
        my_ranks = []
        for card in my_hand:
            my_ranks.append(card["rank"])
        if my_ranks[0] == my_ranks[1]:
            return game_state["minimum_raise"]
        return 0

    def showdown(self, game_state):
        pass

