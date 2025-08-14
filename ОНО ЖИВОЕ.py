N = int(input("Введите количество цифр: "))
num_list = list()


for i in range(1, N + 1):
    num = int(input(f"Число {i}: "))
    num_list.append(num)

if num_list == num_list[::-1]:
    print("Это палиндром")

else:
    count_num = 1
    new_num = []
    copy_num = num_list.copy()

    for i in range(len(num_list)):
        if copy_num != copy_num[::-1]:
            new_num.insert(0, num_list[i])
            copy_num.insert(len(num_list), num_list[i])

        else:
            print("СРАБОТАЛО")
            print(f"Нужно приписать чисел: {len(new_num)}")
            print(f"Сами числа: {new_num}")
            print(copy_num)
            quit()



