class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Shot(Entity):
    def __init__(self, x, y, speed):
        super().__init__(x, y)
        self.speed = speed

    def move(self):
        """Move the shot by its speed."""
        self.y += self.speed

    def hit_target(self, target):
        """
        Check if the shot hits a target.
        :param target: An object with x, y, width, and height attributes.
        :return: True if the shot hits the target, False otherwise.
        """
        return (self.x >= target.x and self.x <= target.x + target.width and
                self.y >= target.y and self.y <= target.y + target.height)