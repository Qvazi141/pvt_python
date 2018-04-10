import uuid
import json


class BD:
    def __init__(self, bd, name):
        self._bd_path = bd
        self._bd_name = name
        self._bd_in_dict = {}
        self.obj_in_dict = {}

    def bd_initializations(self):
        with open(self._bd_path, 'r', encoding='utf-8') as f:
            try:
                self._bd_in_dict = json.load(f)
                for key in self._bd_in_dict:
                    self._create_object(key, self._bd_in_dict.get(key))
                self._bd_in_dict.clear()
            except ValueError:
                print("Bd structure error")

    def _create_object(self, object_id, data):
        if self._bd_name == "players":
            self.obj_in_dict[object_id] = Player(object_id, data)
        if self._bd_name == "teams":
            self.obj_in_dict[object_id] = Team(object_id, data, CONST_PLAYERS.obj_in_dict)


class Team:
    _structure_team = ['Name']

    def __init__(self, team_id, data, bd_players={}):
        self._team_id = team_id
        self.name = data[Team._structure_team[0]]
        self._bd_players = bd_players
        self._players = self.players

    @property
    def players(self):
        consist = {}
        for player in self._bd_players:
            if self._bd_players[player].team_id == self._team_id:
                consist[player] = (self._bd_players[player].name, self._bd_players[player].family)
        return consist


class Player:
    _structure_player = ('Name', 'Family', 'Team_id')

    def __init__(self, player_id, data):
        self._player_id = player_id
        self.name = data[Player._structure_player[0]]
        self.family = data[Player._structure_player[1]]
        self._team_id = data[Player._structure_player[2]]

    @property
    def team(self):
        for team_id in CONST_TEAMS.obj_in_dict:
            if self._team_id == team_id:
                team_name = team_id.name
        return team_name


class Match:
    def __init__(self, data):
        self.match_id = data[0]
        self.date = data[1]
        self.location = data[2]
        self.result = data[3]
        self.team1 = data[4]
        self.team2 = data[5]
        self.players = data[6]


if __name__ == "__main__":
    CONST_PLAYERS = BD('players.json', 'players')
    CONST_PLAYERS.bd_initializations()
    CONST_TEAMS = BD('teams.json', 'teams')
    CONST_TEAMS.bd_initializations()
    print(CONST_TEAMS.obj_in_dict['0'].players)