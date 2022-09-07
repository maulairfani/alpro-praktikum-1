angka1 = input('Masukkan angka pertama: ')
angka2 = input('Masukkan angka kedua: ')

def kalkulator(angka1, angka2):
    while True:
        operasi = input('Masukkan operasi (+, -, /, *) : ')
        
        try:
            angka1 = float(angka1)
            angka2 = float(angka2)
        except:
            return 'error'

        
        if operasi == '+':
            return angka1 + angka2
        elif operasi == '-':
            return angka1 - angka2
        elif operasi == '*':
            return angka1 * angka2
        elif operasi == '/':
            return angka1 / angka2
        else:
            print('error')
            continue
    
kalkulator(angka1, angka2)
# ppp