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

    def display_info(self) -> str: #полиморфизм
        return f"Player: {self.name} | Total matches: {len(self.__match_history)}"

    def to_dict(self) -> dict: #конвертация в словарь
        return {
            "player": self.name,
            "matches": [{"score": m.score, "date": m.date} for m in self.__match_history]
        }

# if __name__ == "__main__":
#     u = User("GenericUser")
#     p = Player("Alice")
#     p.add_match(MatchRecord(score=120, date="2026-01-01"))
#     p.add_match(MatchRecord(score=180, date="2026-01-02"))
    
#     print("--- Демонстрация полиморфизма ---")
#     users_list = [u, p]
#     for person in users_list:
#         print(person.display_info())

#     print("\n--- Демонстрация конвертации в словарь (to_dict) ---")
#     print(p.to_dict())

