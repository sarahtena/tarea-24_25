from Opponent import Opponent
class FinalBoss(Opponent):
    def __init__(self, base_speed):
        super().__init__(base_speed * 2)  # El jefe final se mueve al doble de velocidad

    def move(self):
        print(f"Jefe Final se mueve a una velocidad de {self.speed}")


# Ejemplo de uso
def on_enemy_defeated():
    print("¡Enemigo derrotado! ¡Aparece el Jefe Final!")
    boss = FinalBoss(base_speed=5)
    boss.move()


# Simular la derrota de un enemigo
on_enemy_defeated()
