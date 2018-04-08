import uuid
import json


class BD:
    def __init__(self, bd):
        self.bd_name = bd
        self.bd_in_dict = {}

    def bd_initializations(self, bd_name):
        with open(self.bd_name, 'r', encoding='utf-8') as f:
            try:
                self.bd_in_dict = json.load(f)
                for student_id in self.bd_in_dict:
            except ValueError:
                print("Bd structure error")

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