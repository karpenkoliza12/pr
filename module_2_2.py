first, second, third = (int(input("Введите 1 число: ")),
                        int(input("Введите 2 число: ")),
                        int(input("Введите 3 число: ")))

if first == second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)