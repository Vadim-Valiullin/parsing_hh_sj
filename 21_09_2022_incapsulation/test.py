from abc import ABC, abstractmethod


class Storage(ABC):

    @abstractmethod
    def __init__(self, items, capacity):
        self.items = items
        self.capacity = capacity
        pass

    @abstractmethod
    def add(self, product, quantity):
        pass

    @abstractmethod
    def remove(self, product, quantity):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self, items):
        self.items = items
        self.capacity = 0
        self._volume = 100

    def add(self, product, quantity):
        if self._volume - sum(list(self.items.values())) >= quantity:
            if product in self.items:
                self.items[product] += quantity
            else:
                self.items[product] = quantity
            return True
        return False

    def remove(self, product, quantity):
        if quantity <= self.items[product] and product in self.get_items():
            if quantity < self.items[product]:
                self.items[product] -= quantity
            else:
                del self.items[product]
            return True
        return False

    def get_free_space(self):
        self.capacity = self._volume - sum(list(self.items.values()))
        return self.capacity

    # @property
    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items)


class Shop(Storage):
    def __init__(self, items):
        self.items = items
        self.capacity = 0
        self._volume = 20

    def add(self, product: str, quantity: int):
        if self._volume - sum(list(self.items.values())) >= quantity and len(self.items) < 5:
            if product in self.items:
                self.items[product] += quantity
            else:
                self.items[product] = quantity
            return True
        return False

    def remove(self, product: str, quantity: int):
        if quantity <= self.items[product] and product in self.get_items():
            if quantity < self.items[product]:
                self.items[product] -= quantity
            else:
                del self.items[product]
            return True
        return False

    def get_free_space(self):
        self.capacity = self._volume - sum(list(self.items.values()))
        return self.capacity

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items)


class Request:
    def __init__(self, fromm: str, to: str, quantity: int, product: str):
        self.fromm = fromm
        self.to = to
        self.product = product
        self.quantity = quantity

    def __repr__(self):
        return f'Доставить {self.quantity} {self.product} из {self.fromm} в {self.to}'
