class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor
    def __len__(self):
        return self.number_of_floor

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floor == other.number_of_floor
        raise NotImplemented

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor < other.number_of_floor
        raise NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floor <= other.number_of_floor
        raise NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor > other.number_of_floor
        raise NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floor >= other.number_of_floor
        raise NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floor != other.number_of_floor
        raise NotImplemented

    def __add__(self, other):
        if isinstance(other, House):
            return self.number_of_floor + other.number_of_floor
        if isinstance(other, int):
            return House(self.name, self.number_of_floor + other)
        raise NotImplemented

    def __iadd__(self, other):
        if isinstance(other, House):
            self.number_of_floor += other.number_of_floor
            return self
        if isinstance(other, int):
            self.number_of_floor += other
            return self
        raise NotImplemented

    def __radd__(self, other):
        return self + other

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floor}')


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__