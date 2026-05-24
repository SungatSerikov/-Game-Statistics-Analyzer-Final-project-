from services.decorators import time_logger


def _calculate_average(player) -> float:
    matches = player.match_history
    if not matches:
        return 0.0
    total = sum(match.score for match in matches)
    return total / len(matches)
