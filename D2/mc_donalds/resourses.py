director = 'DI'
admin = 'AD'
cook = 'CO'
cashier = 'CA'
cleaner = 'CL'

POSITIONS = [
    (director, 'Директор'),
    (admin, 'Администратор'),
    (cook, 'Повар'),
    (cashier, 'Кассир'),
    (cleaner, 'Уборщик')
]

cashier1 = Staff.objects.create(full_name = "Иванов Иван Иванович", position = Staff.cashier, labor_contract = 1754)
cashier2 = Staff.objects.create(full_name = "Петров Петр Петрович", position = Staff.cashier, labor_contract = 4355)