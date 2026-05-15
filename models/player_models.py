from models.base import User

class MatchRecord:
    def __init__(self, score: int, date: str):
        self.score = score
        self.date = date

    def __repr__(self):
        return f"Match(score={self.score}, date='{self.date}')"

class Player(User):
    def __init__(self, name: str):
        super().__init__(name)
        self.__match_history = []
        self.__played_dates = set()

    def add_match(self, match: MatchRecord):
        self.__match_history.append(match)
        self.__played_dates.add(match.date)

    @property
    def match_history(self) -> list:
        return self.__match_history

    @property
    def played_dates(self) -> set:
        return self.__played_dates

# if __name__ == "__main__":
#     p = Player("Alice")
#     m1 = MatchRecord(score=120, date="2026-01-01")
#     p.add_match(m1)
    
#     print(f"Игрок: {p.name}")
#     print(f"История игр: {p.match_history}")
#     print(f"Игрок играл в эти даты: {p.played_dates}")

