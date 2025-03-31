from Character import Character

class Opponent(Character):
    def __init__(self, name, health, is_star=False):
        super().__init__(name, health)
        self.is_star = is_star

    def move(self, direction):
        print(f"{self.name} moves {direction}.")

    def shoot(self):
        print(f"{self.name} shoots!")


    def collide(self, other_entity):
        if hasattr(other_entity, 'is_bullet') and other_entity.is_bullet:
            print(f"{self.name} was hit by a bullet!")
            if hasattr(other_entity, 'player'):
                other_entity.player.score += 1
                print(f"{other_entity.player.name}'s score increased to {other_entity.player.score}.")


    def update_health(self, damage):
        self.health -= damage
        print(f"{self.name}'s health updated to {self.health}.")


    def is_alive(self):
        return self.health > 0