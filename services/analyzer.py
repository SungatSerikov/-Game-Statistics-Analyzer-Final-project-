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


