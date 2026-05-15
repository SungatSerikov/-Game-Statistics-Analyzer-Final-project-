class User:
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    def display_info(self) -> str:
        return f"User: {self.name}"

