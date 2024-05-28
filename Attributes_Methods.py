
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor

        if self.new_floor <= self.number_of_floors:
            for i in range(1, self.new_floor+1):
                print(i)
        else:
            print("Такого этажа не существует")

h1 = House("ЖК Эльбрус", 30)
print("ЖК Эльбрус")
h1.go_to(5)
print()

h2 = House("ЖК Бештау", 10)
print("ЖК Бештау")
h2.go_to(15)
