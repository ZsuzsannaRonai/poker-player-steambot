class Player:
    VERSION = "1.5"


    def betRequest(self, game_state):

        players = game_state["players"]
        actual_round = game_state["round"]

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

        if actual_round == 0:
            if my_ranks[0] == my_ranks[1]:
                return game_state["minimum_raise"] * 1.5
            return game_state["minimum_raise"]

        if actual_round < 3:
            if my_ranks[0] == my_ranks[1]:
                if my_ranks[0] in community_ranks:
                    return game_state["minimum_raise"] * 3
                return game_state["minimum_raise"] * 1.5
            elif my_ranks[0] in community_ranks or my_ranks[1] in community_ranks:
                return game_state["minimum_raise"] * 1.5
            else:
                return game_state["minimum_raise"]

        return 0


    def showdown(self, game_state):
        pass





