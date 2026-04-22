
# 3
class Door:
    def __init__(self, is_open):
        self.is_open = is_open

    def check(self):
        if self.is_open:
            return "Eshik ochiq"
        else:
            return "Eshik yopiq"

d = Door(True)
print(d.check())

# 4
class GamePlayer:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def result(self):
        if self.score > 50:
            return f"{self.name} yutdi"
        else:
            return f"{self.name} yutqazdi"

p = GamePlayer("Ali", 60)
print(p.result())


# 5
class Temperature:
    def __init__(self, degree):
        self.degree = degree

    def check_weather(self):
        if self.degree == 25:
            return "Issiq"
        else:
            return "Sovuq"

t = Temperature(25)
print(t.check_weather())


# 6
class Password:
    def __init__(self, password):
        self.password = password

    def check(self):
        if len(self.password) < 6:
            return "Zaif parol"
        else:
            return "Kuchli parol"

pw = Password("12345")
print(pw.check())


# 7
class Speed:
    def __init__(self, speed):
        self.speed = speed

    def check(self):
        if self.speed > 100:
            return "Tezlik oshdi"
        else:
            return "Normal"
s = Speed(120)
print(s.check())



p = GamePlayer("Ali", 60)
print(p.result())



