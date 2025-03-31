from boss import Boss

class Game:
    def __init__(self):
        self.score = 0
        self.player = None
        self.opponent = None
        self.is_running = False

    def start(self):
        self.is_running = True
        self.score = 0
        print("Game started!")

    def update(self):
        if self.is_running:
            print("Game is updating...")
            # Add game logic here
        else:
            print("Game is not running.")

    def end_game(self):
        self.is_running = False
        print("Game ended!")
        def convert_enemy_to_star(self):
            if self.is_running:
                self.score += 1
                print(f"Enemy converted to star! Current score: {self.score}")
            else:
                print("Game is not running. Cannot convert enemy.")
                class Player:
                    def __init__(self):
                        self.lives = 3

                    def lose_life(self):
                        if self.lives > 0:
                            self.lives -= 1
                            print(f"Player hit! Lives remaining: {self.lives}")
                        else:
                            print("No lives left.")

                    def is_alive(self):
                        return self.lives > 0

                # Integrate the Player class into the Game class
                def check_player_hit(self):
                    if self.player and self.player.is_alive():
                        self.player.lose_life()
                        if not self.player.is_alive():
                            self.end_game()
                            print("Game over! Player has no lives left.")
                    else:
                        print("Player is already out of lives.")

                        # Import the Boss class from boss.py

                        def spawn_boss(self):
                            if self.is_running:
                                print("Boss has appeared!")
                                self.opponent = Boss(speed=2)  # Boss moves twice as fast
                            else:
                                print("Game is not running. Cannot spawn boss.")

                        # Add logic to check if the boss should appear
                        def check_for_boss(self):
                            if self.score > 0 and self.score % 5 == 0:  # Example condition: every 5 enemies defeated
                                self.spawn_boss()
                                self.check_for_boss()