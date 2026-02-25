print("Ketik 'a' untuk tambah, 'b' untuk kurang, 'c' untuk kali, 'd' untuk bagi")

while True:  # Initiate a continuous loop
    operator = input('Masukkan operator: ')

    if operator == 'a':
        num1 = int(input("Masukkan angka pertama: "))
        num2 = int(input("Masukkan angka kedua: "))
        print(num1 + num2)

    elif operator == 'b':
        num1 = int(input("Masukkan angka pertama: "))
        num2 = int(input("Masukkan angka kedua: "))
        print(num1 - num2)

    elif operator == 'c':
        num1 = int(input("Masukkan angka pertama: "))
        num2 = int(input("Masukkan angka kedua: "))
        print(num1 * num2)

    elif operator == 'd':
        num1 = int(input("Masukkan angka pertama: "))
        num2 = int(input("Masukkan angka kedua: "))
        if num2 == 0:  # Handle division by zero error
            print("Divisi dengan nol tidak diizinkan!")
        else:
            print(num1 / num2)

    else:
        print("Masukkan operator yang valid (a, b, c, atau d)")

    # Prompt the user to continue or exit
    again = input("Apakah Anda ingin melakukan operasi lagi? (y/n): ")
    if again.lower() != 'y':  # Check for 'y' or 'Y'
        break  # Exit the loop if the user enters 'n' or anything else
