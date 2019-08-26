
class Player:
    VERSION = "1.0"

    def betRequest(self, game_state):
        players = game_state["players"]
        my_hand = {}
        for player in players:
            if player["name"] == "SteamBot":
                my_hand = player["hole_cards"]


        return 0

    def showdown(self, game_state):
        pass

