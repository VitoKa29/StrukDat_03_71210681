input1 = input("Masukkan kalimat : ")
input2 = input("Masukkan kata : ")

input1 = input1.lower().split()
input2 = input2.lower()

jumlah = 0

for i in input1:
    if i == input2:
        jumlah += 1

print(jumlah)