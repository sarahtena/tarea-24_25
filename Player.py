from Character import Character

class Player(Character):
    def __init__(self, name, score=0, lives=3):
        super().__init__(name)
        self.score = score
        self.lives = lives

    def move(self, direction):
        # Implement movement logic here
        print(f"{self.name} moves {direction}")

    def shoot(self):
        # Implement shooting logic here
        print(f"{self.name} shoots!")

    def collide(self, other_entity):
        # Implement collision logic here
        print(f"{self.name} collides with {other_entity.name}")

    def update_score(self, points):
        self.score += points

        print(f"{self.name}'s score updated to {self.score}")

    def lose_life(self):
        if self.lives > 0:
            self.lives -= 1
            print(f"{self.name} loses a life. Lives left: {self.lives}")

            