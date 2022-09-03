angka1 = input('Masukkan angka pertama: ')
angka2 = input('Masukkan angka kedua: ')

def penjumlahan(angka1, angka2):
    hasil_penjumlahan = angka1 + angka2
    return hasil_penjumlahan

def pengurangan(angka1, angka2):
    hasil_pengurangan = angka1 - angka2
    return hasil_pengurangan

def perkalian(angka1, angka2):
    hasil_perkalian = angka1 * angka2
    return hasil_perkalian

def pembagian(angka1, angka2):
    hasil_pembagian = angka1 / angka2
    return hasil_pembagian

def kalkulator(angka1, angka2):
    while True:
        operasi = input('Masukkan operasi (+, -, /, *) : ')
        
        try:
            angka_1 = float(angka1)
            angka_2 = float(angka2)
        except:
            return 'error'

        
        if operasi == '+':
            return penjumlahan(angka_1, angka_2)
        elif operasi == '-':
            return pengurangan(angka_1, angka_2)
        elif operasi == '*':
            return perkalian(angka_1, angka_2)
        elif operasi == '/':
            return pembagian(angka_1, angka_2)
        else:
            print('error')
            continue
    
kalkulator(angka1, angka2)