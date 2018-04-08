import uuid
import json


class Team:
    def __init__(self, name, players):
        self.team_id = uuid.uuid4()
        self.name = name
        self.players = players


class Player:
    def __init__(self, name, team_id):
        self.player_id = uuid.uuid4()
        self.name = name
        self.team_id = team_id

    #@property
    #def team(self):



class Match:
    def __init__(self, date, location, result, team1, team2, players):
        self.match_id = uuid.uuid4()
        self.date = date
        self.location = location
        self.result = result
        self.team1 = team1
        self.team2 = team2
        self.players = players


if __name__ == "__main__":
    pass