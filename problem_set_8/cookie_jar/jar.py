class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        self.size = self.size + n

    def withdraw(self, n):
        self.size = self.size - n

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, new_capacity):
        if type(new_capacity) != int:
            raise ValueError

        if new_capacity < 0:
            raise ValueError

        self.__capacity = new_capacity

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, new_size):
        if type(new_size) != int:
            raise ValueError

        if new_size > self.__capacity:
            raise ValueError

        if new_size < 0:
            raise ValueError

        self.__size = new_size
