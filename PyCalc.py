print("Prosty kalkulator")

try:
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))
except ValueError:
    print("Błąd: Nieprawidłowy format liczby!")
    exit()

dzialanie = input("Wybierz działanie (+, -, *, /): ")

if dzialanie == '+':
    wynik = liczba1 + liczba2
elif dzialanie == '-':
    wynik = liczba1 - liczba2
elif dzialanie == '*':
    wynik = liczba1 * liczba2
elif dzialanie == '/':
    if liczba2 == 0:
        print("Błąd: Nie można dzielić przez zero!")
        exit()
    wynik = liczba1 / liczba2
else:
    print("Nieprawidłowe działanie!")
    exit()
print(f"Wynik: {wynik}")