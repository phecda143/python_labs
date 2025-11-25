name = input("ФИО:").upper().split()
print(f"Инициалы: {name[0][0]}{name[1][0]}{name[2][0]}")
print(f"Длина (символов): {sum(map(len, name))+2}")
