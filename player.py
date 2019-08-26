class Player:
    VERSION = "1.6"


    def betRequest(self, game_state):

        players = game_state["players"]
        actual_round = int(game_state["round"])

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


    def frequency_in_community(self, community_ranks):
        # returns a dictionary with ranks as keys and duplication as value
        frequency = {}
        for rank in community_ranks:
            frequency[rank] = frequency.get(rank, 0) + 1
        return frequency

    def check_for_pair(self, my_ranks, community_ranks):
        # return a boolean if there is a pair between hand and community cards
        for my_rank in my_ranks:
            for com_rank in community_ranks:
                if my_rank == com_rank:
                    return True
        return False

    def check_for_two_pair(self, my_ranks, community_ranks):
        # return a boolean if there is two pair between hand and community cards
        pairs = {}
        for my_rank in my_ranks:
            for com_rank in community_ranks:
                if my_rank == com_rank:
                    if pairs['first']:
                        pairs['second'] = True
                    else:
                        pairs['first'] = True
                if pairs['first'] and pairs['second']:
                    return True
        return False

    def showdown(self, game_state):
        pass

