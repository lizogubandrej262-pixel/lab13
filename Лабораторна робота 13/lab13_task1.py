class Table:
    def __init__(self, inventory_number, color, year, price):
        self.inventory_number = inventory_number
        self.color = color
        self.year = year
        self.price = price

    def set_inventory_number(self, new_number):
        self.inventory_number = new_number

    def set_price(self, new_price):
        self.price = new_price

    def show(self):
        print("Інвентарний номер:", self.inventory_number)
        print("Колір:", self.color)
        print("Рік виготовлення:", self.year)
        print("Ціна:", self.price)
        print("---")


tables = []

tables.append(Table("T001", "коричневий", 2018, 2500))
tables.append(Table("T002", "білий", 2020, 1800))
tables.append(Table("T003", "чорний", 2022, 3200))

print("Список столів:")
for t in tables:
    t.show()

print("Зміна інвентарного номера і ціни для першого стола:")
tables[0].set_inventory_number("T100")
tables[0].set_price(2800)
tables[0].show()

print("Пошук стола за інвентарним номером T002:")
for t in tables:
    if t.inventory_number == "T002":
        t.show()