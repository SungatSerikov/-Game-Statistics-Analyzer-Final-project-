from services.decorators import time_logger


def _calculate_average(player) -> float:
    matches = player.match_history
    if not matches:
        return 0.0
    total = sum(match.score for match in matches)
    return total / len(matches)


@time_logger
def get_average_scores(players: list) -> dict:
    averages = {}
    for player in players:
        averages[player.name] = _calculate_average(player)
    return averages


@time_logger
def get_leaderboard(players: list) -> list:
    leaderboard = sorted(
        players,
        key=lambda player: _calculate_average(player),
        reverse=True
    )
    return leaderboard


@time_logger
def get_best_performance(players: list) -> dict:
    best_score =None
    best_player=None
    best_date = None

    for player in players:
        matches = player.match_history
        if not matches:
            continue

        player_best =max(matches, key=lambda match: match.score)

        if best_score is None or player_best.score > best_score:
            best_score=player_best.score
            best_player=player.name
            best_date = player_best.date

    return {
        "player": best_player,
        "score": best_score,
        "date": best_date
    }


