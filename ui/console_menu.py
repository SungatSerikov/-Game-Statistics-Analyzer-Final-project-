from random import choice
from services.analyzer import get_leaderboard, get_average_scores,get_best_performance
from services.file_manager import save_report

def menu(players):
    while True:
        print("\n1. Show all players")
        print("2. Show leaderboard")
        print("3. Show average scores")
        print("4. Show best performance")
        print("5. Save report")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "0":
            break
        elif choice =="1":
            for player in players:
                print(player.display_info())
        elif choice == "2":
            for i, player in enumerate(get_leaderboard(players),1):
                print(f"{i}.{player.name }")
        elif choice == "3":
            for name,avg in get_average_scores(players).items():
                print(f"{name}:{avg:.2f}")
        elif choice == "4":
            best = get_best_performance(players)
            print(f"Player: {best['player']}, Score:{best['score']}, Date:{best['date']}")
        elif choice == "5":
            save_report(players,"output,json")
        else:
            print("Invalid option")