import unittest
from models.player_models import Player, MatchRecord
from services.analyzer import get_average_scores,get_leaderboard,get_best_performance

class TestAnalyzer (unittest.TestCase):
    def setUp(self):
        self.p1 = Player("Maksat")
        self.p1.add_match(MatchRecord(100, "2026-01-01"))
        self.p1.add_match(MatchRecord(200, "2026-01-02"))

        self.p2 = Player("Adema")
        self.p2.add_match(MatchRecord(50,"2026-01-01"))

        self.players = [self.p1, self.p2]

        def test_average_scores(self):
            averages = get_average_scores(self.players)
            self.assertEqual(averages["Maksat"],150)
            self.assertEqual(averages["Addema"],50)

            def test_leaderboard(self):
                leaderboard = get_leaderboard(self.players)
                self.assertEqual(leaderboard[0].name,"Maksat")




