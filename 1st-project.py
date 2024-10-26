class Sneaker:
    def __init__(self, brand, size, price):
        self.brand = brand
        self.size = size
        self.price = price

class SneakerStore:
    def __init__(self):
        self.stock = []
    def add_sneaker(self, brand, size, price):
        sneaker = Sneaker(brand, size, price)
        self.stock.append(sneaker)
        print("Был добавлен :" + brand + ' ' + str(price) + ' ' + str(size))
    def display_stock(self):
        if self.stock == []:
            print("На складе нету ничего")
        else:
            print("Вот кроссы:")
            for sneaker in self.stock:
                print(sneaker.brand, sneaker.size, sneaker.price)
    def buy_sneaker(self, brand, size):
        for sneaker in self.stock:
            if sneaker.brand == brand and sneaker.size == size:
                self.stock.remove(sneaker)
            print("Ты купил:" + brand + ' ' + str(size))
            return
        print("Такого бренда нет в наличии")


store = SneakerStore()
store.add_sneaker('Nike', 27, 20000)
store.add_sneaker('Adidas', 42, 15000)
store.add_sneaker('Supreme', 35, 40000)

store.display_stock()

store.buy_sneaker('Nike', 42)
store.display_stock()

