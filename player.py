class Player:
    VERSION = "1.1"

    def betRequest(self, game_state):

        players = game_state["players"]

        my_cards = {}
        for player in players:
            if player["name"] == "SteamBot":
                my_cards = player["hole_cards"]

        community_ranks = []
        for card in game_state["community_cards"]:
            community_ranks.append(card["rank"])

        my_ranks = []
        for card in my_cards:
            my_ranks.append(card["rank"])
        if my_ranks[0] == my_ranks[1]:
            return game_state["minimum_raise"]

        return 0

    def showdown(self, game_state):
        pass
