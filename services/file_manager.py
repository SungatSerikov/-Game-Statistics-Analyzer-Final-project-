import json
import datetime
from models.player_models import Player, MatchRecord

def read_players_file(filename):
    players = []
    playerid = set()
    try:
        with open(filename, "r") as players_file:
            if len(str(players_file).strip()) == 0:
                print("File is empty!")
                return None
            data = json.load(players_file)
            for player_data in data:
                if player_data['player'] not in playerid:
                    playerid.add(player_data['player'])
                    p = Player(player_data['player'])
                    players.append(p)
                for player in players:
                    if player.name == player_data['player']:
                        try:
                            score = int(player_data['score'])
                            if player_data['date'] != None:
                                date = player_data['date']
                            player.add_match(MatchRecord(score, date))
                        except ValueError:
                            print("Failed to import", player_data['player'])
                            continue
        return players        
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print("Input does not exist!")
        return None
    
players = read_players_file("data/input.json")
for p in players:
    print(p.display_info())