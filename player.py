class Player:
    VERSION = "1.13"



    def betRequest(self, game_state):

        players = game_state["players"]
        actual_round = int(game_state["bet_index"])

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

        if len(community_ranks) != 0:
            if len(community_ranks) < 5:
                if self.check_for_pair(my_ranks, community_ranks):
                    return int(game_state["current_buy_in"]) + int(game_state["minimum_raise"]) * 4
                elif self.check_for_two_pair(my_ranks, community_ranks):
                    return int(game_state["current_buy_in"]) + int(game_state["minimum_raise"]) * 8
                else:
                    return int(game_state["current_buy_in"]) + int(game_state["minimum_raise"])
        else:
            if my_ranks[0] == my_ranks[1]:
                return int(game_state["current_buy_in"]) + int(game_state["minimum_raise"]) * 4
            else:
                return int(game_state["current_buy_in"]) - int(game_state["players"]["in_action"]["bet"]) + int(game_state["minimum_raise"])
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
                    if pairs.get('first', 0) != 0:
                        pairs['second'] = True
                    else:
                        pairs['first'] = True
                if pairs['first'] and pairs['second']:
                    return True
        return False

    def showdown(self, game_state):
        pass





