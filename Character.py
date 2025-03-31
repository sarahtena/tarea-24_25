from Entity import Entity

class Character(Entity):
    def __init__(self, lives):
        super().__init__()
        self.lives = lives
        self.is_alive = lives > 0

    def move(self, direction):
        # Implement movement logic here
        pass

    def shoot(self):
        # Implement shooting logic here
        pass

    def collide(self, other_entity):
        # Implement collision logic here
        pass