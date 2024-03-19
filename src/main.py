from games.game_simulator import GameSimulator
from games.tictactoe.players.human import HumanTicTacToePlayer
from games.tictactoe.players.greedy import GreedyTicTacToePlayer
from games.tictactoe.players.minimax import MinimaxTicTacToePlayer
from games.tictactoe.players.random import RandomTicTacToePlayer
from games.tictactoe.players.defensiveMinimax import DefensiveMinimaxTicTacToePlayer
from games.tictactoe.players.defensiveGreedy import DefensiveGreedyTicTacToePlayer
from games.tictactoe.players.offensiveMinimax import OffensiveMinimaxTicTacToePlayer
from games.tictactoe.players.offensiveGreedy import OffensiveGreedyTicTacToePlayer
from games.tictactoe.players.randomS import RandomDisplayTicTacToePlayer
from games.tictactoe.simulator import TicTacToeSimulator

def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()


def main():
    print("ESTG IA Games Simulator\n")

    print("Select an option:")
    print("1. Play 1vs1 against a bot")
    print("2. Run simulations")
    print("3. Run display simulation between randoms")
    choice = input("Enter your choice (1 or 3): ")

    num_iterations = 200
    num_iterations_display = 15

    ttt_simulations = [
        {
            "name": "Random VS Random",
            "player1": RandomTicTacToePlayer("Random 1"),
            "player2": RandomTicTacToePlayer("Random 2")
        },
        {
            "name": "Greedy VS Random",
            "player1": GreedyTicTacToePlayer("Greedy"),
            "player2": RandomTicTacToePlayer("Random")
        },
        {
            "name": "Minimax VS Random",
            "player1": MinimaxTicTacToePlayer("Minimax"),
            "player2": RandomTicTacToePlayer("Random")
        },
        {
            "name": "Minimax VS Greedy",
            "player1": MinimaxTicTacToePlayer("Minimax"),
            "player2": GreedyTicTacToePlayer("Greedy")
        },
        {
            "name": "Offensive Minimax VS Defensive Minimax",
            "player1": OffensiveMinimaxTicTacToePlayer("Offensive Minimax"),
            "player2": DefensiveMinimaxTicTacToePlayer("Defensive Minimax")
        },
        {
            "name": "Offensive Greedy VS Defensive Greedy",
            "player1": OffensiveGreedyTicTacToePlayer("Offensive Greedy"),
            "player2": DefensiveGreedyTicTacToePlayer("Defensive Greedy")
        },
        {
            "name": "Offensive Greedy VS Offensive Minimax",
            "player1": OffensiveGreedyTicTacToePlayer("Offensive Greedy"),
            "player2": OffensiveMinimaxTicTacToePlayer("Offensive Minimax")
        },
        {
            "name": "Defensive Greedy VS Defensive Minimax",
            "player1": DefensiveGreedyTicTacToePlayer("Defensive Greedy"),
            "player2": DefensiveMinimaxTicTacToePlayer("Defensive Minimax")
        }
        
    ]

    human_simulations = [
        {
            "name": "Human VS Random",
            "player1": HumanTicTacToePlayer("Human"),
            "player2": RandomTicTacToePlayer("Random")
        },
        {
            "name": "Human VS Greedy",
            "player1": HumanTicTacToePlayer("Human"),
            "player2": GreedyTicTacToePlayer("Greedy")
        },
        {
            "name": "Human VS Minimax",
            "player1": HumanTicTacToePlayer("Human"),
            "player2": MinimaxTicTacToePlayer("Minimax")
        },
        {
            "name": "Human VS Offensive Minimax",
            "player1": HumanTicTacToePlayer("Human"),
            "player2": OffensiveMinimaxTicTacToePlayer("Offensive Minimax")
        },
        {
            "name": "Human VS Defensive Minimax",
            "player1": HumanTicTacToePlayer("Human"),
            "player2": DefensiveMinimaxTicTacToePlayer("Defensive Minimax")
        },
        {
            "name": "Human VS Offensive Greedy",
            "player1": HumanTicTacToePlayer("Human"),
            "player2": OffensiveGreedyTicTacToePlayer("Offensive Greedy")
        },
        {
            "name": "Human VS Defensive Greedy",
            "player1": HumanTicTacToePlayer("Human"),
            "player2": DefensiveGreedyTicTacToePlayer("Defensive Greedy")
        }
    ]
    
    display_simulations = [
        {
            "name": "Random VS Random (Displayed)",
            "player1": RandomDisplayTicTacToePlayer("RandomDisplay 1"),
            "player2": RandomDisplayTicTacToePlayer("RandomDisplay 2")
        }
    ]


    if choice == '1':
        print("\nChoose your opponent:")
        for i, sim in enumerate(human_simulations, 1):
            print(f"{i}. {sim['name']}")

        bot_choice = 0
        while bot_choice < 1 or bot_choice > len(human_simulations):
            try:
                bot_choice = int(input("Enter the number of the bot you want to play against: "))
                if bot_choice < 1 or bot_choice > len(human_simulations):
                    print("Please enter a valid number from the list.")
            except ValueError:
                print("Please enter a numeric value.")

        selected_sim = human_simulations[bot_choice - 1]
        run_simulation(selected_sim["name"], TicTacToeSimulator(selected_sim["player1"], selected_sim["player2"]), 1)

    # Scenario for running simulations
    elif choice == '2':
        for sim in ttt_simulations:
            run_simulation(sim["name"], TicTacToeSimulator(sim["player1"], sim["player2"]), num_iterations)

    elif choice == '3':
        for sim in display_simulations:
            run_simulation(sim["name"], TicTacToeSimulator(sim["player1"], sim["player2"]), num_iterations_display)
    
    else:
        print("Invalid choice. Exiting...")


if __name__ == "__main__":
    main()