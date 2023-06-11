"""
Math modülündeki hazır fonksiyonları kullanarak gelişmiş bir
hesap makinesi geliştirmeye çalışın.

Try to develop an advanced calculator
using ready-made functions in the Math module.
"""

import math


def collection(*args):
    result = sum(args)
    return result


def extraction(*args):
    result = args[0]
    for i in range(1, len(args)):
        result -= args[i]
    return result


def impact(*args):
    result = 1
    for num in args:
        result *= num
    return result


def divide(*args):
    result = args[0]
    for num in range(1, len(args)):
        if args[num] != 0:
            result /= args[num]
        else:
            return "Transaction Error"
    return result


def exponentiation(lower, exponent):
    return lower ** exponent


while True:
    print("Hesap Makinesi Programına Hoş Geldiniz!")
    print("Yapmak istediğiniz işlemi seçin:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Üs Alma")
    print("6. Karekök Alma")
    print("7. Logaritma")
    print("8. Faktöriyel")
    print("9. Çıkış")

    vote_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    vote = input("Seçiminizi yapın 1-9: ")
    try:
        vote = int(vote)
        if vote == 9:
            print("Çıkış yapılıyor.")
            break
        elif vote not in vote_number:
            print("Seçiminiz hatalı")
            continue
    except ValueError:
        print("Geçersiz giriş. Lütfen bir tam sayı girin.")
        continue


    numbers = []

    while True:
        number = input("Lütfen işlem yapacağınız sayıları giriniz: ")
        if number == 'q':
            break
        try:
            numbers.append(float(number))
        except ValueError:
            print("Lütfen sayı giriniz veya q ile çıkış yapınız.")
            continue

    if vote == 1:
        print("Sonuç ", collection(*numbers))
    elif vote == 2:
        print("Sonuç ", extraction(*numbers))
    elif vote == 3:
        print("Sonuç ", impact(*numbers))
    elif vote == 4:
        print("Sonuç ", divide(*numbers))
    elif vote == 5:
        if len(numbers) == 2:
            print("Sonuç ", exponentiation(*numbers))
        else:
            print("Fazla sayı girdiniz.")
    elif vote == 6:
        if len(numbers) == 1:
            if numbers[0] >= 0:
                print("Sonuç: ", math.sqrt(numbers[0]))
            else:
                print("Hata! Karekök alma işlemi için pozitif bir sayı gerekmektedir.")
        else:
            print("Hata! Karekök alma işlemi için 1 sayı gerekmektedir.")
    elif vote == 7:
        if len(numbers) == 1:
            print("Sonuç: ", math.log10(numbers[0]))
        else:
            print("Hata! Logaritma işlemi için 1 sayı gerekmektedir.")
    elif vote == 8:
        if len(numbers) == 1 and numbers[0] >= 0 and numbers[0] % 1 == 0:
            print("Sonuç: ", math.factorial(int(numbers[0])))
        else:
            print("Hata! Faktöriyel işlemi için doğal sayı girmelisiniz.")
    else:
        print("Geçersiz seçim!")



