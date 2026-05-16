import json
from datetime import datetime
from models.player_models import Player, MatchRecord
from services.decorators import time_logger

def player_generator(filename):
    with open(filename, "r") as file:
        data = json.load(file)

        for player_data in data:
            yield player_data


@time_logger
def read_players_file(filename):
    players = []
    player_map = {}
    try:
        for player_data in player_generator(filename):
            player_name = player_data.get("player")
            if not player_name or player_name.strip() == "":
                print("Player name is missing or empty. Skipping entry.")
                continue
            if player_name not in player_map:
                    players.append(Player(player_name))
                    player_map[player_name] = players[len(players)-1]
            try:
                score = int(player_data["score"])
                date = player_data["date"]
                datetime.strptime(date, "%Y-%m-%d")
            except (ValueError, KeyError):
                print(f"Failed to import {player_name}")
                continue
            player_map[player_name].add_match(MatchRecord(score, date))
        return players        
    except FileNotFoundError:
        print("Input does not exist!")
        return None
    except json.decoder.JSONDecodeError:
        print("Invalid JSON format!")
        return None
    
@time_logger
def save_report(players, filename):
    report = []
    for player in players:
        report.append(player.to_dict())

    with open(filename, "w") as file:
        json.dump(report, file, indent=4)
    print("Report saved successfully!")

@time_logger
def map_players_by_name(players):
    return {player.name: player for player in players}

@time_logger
def str2date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print(f"Invalid date format: {date_str}")
        return None

#players = read_players_file("data/input.json")
#for p in players:
    #print(p.display_info())
#save_report(players, "data/report.json")