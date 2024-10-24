
class ball:
    def __init__(self, mood):
        self.mood = mood
        self.size = 100

ball1 = ball("Great")
ball2 = ball("Not Great")

print (ball1.mood)
print (ball2.mood)