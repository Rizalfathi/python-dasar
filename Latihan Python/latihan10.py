username = input("Masukkan nama peserta: ")

email = input("\nMasukkan email peserta: ")

with open("data.txt", "w") as file:

    file.write(username)

    file.write(" ")

    file.write(email)

file.close()