import unittest
from models.player_models import Player, MatchRecord
from services.analyzer import get_average_scores,get_leaderboard,get_best_performance

class TestAnalyzer (unittest.TestCase):
    def setUp(self):
        self.p1 = Player("Alice")
        self.p1.add_match(MatchRecord(100, "2026-01-01"))
        self.p1.add_match(MatchRecord(200, "2026-01-02"))