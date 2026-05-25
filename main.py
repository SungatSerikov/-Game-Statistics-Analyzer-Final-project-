from services.file_manager import read_players_file
from ui.console_menu import menu


def main():
    players = read_players_file("data/input.json")

    if players is None:
        print("Failed to load players")
        return

    menu(players)


if __name__ == "__main__":
    main()