'''
Przygotowujesz program dla sklepu z farbami. Klienci pytają czasami ile farby potrzeba do
pomalowania mieszkania.
Napisz funkcję calculate_paint, która:
- przyjmuje argument efficency_ltr_per_m2 - określającą ile farby trzeba
    do pomalowania metra kwadratowego
- przyjmuje dowolną ilość kolejnych argumentów odpowiadających
    za powierzchnie do pomalowania dla pokoi mieszkania, które ma być pomalowane
- funkcja ma zwracać informację o ilości potrzebnej farby

Przetestuj funkcję na dwa sposoby:
- przekazując powierzchnie do pomalowania w poszczególnych pokojach po prostu
    po przecinku wywołując funkcję
- definiując listę z powierzchniami, a następnie przekazując do funkcji tą listę
'''

def calculate_paint(efficency_lts_per_m2, *rooms):
    total_area = sum(rooms)
    paint = total_area * efficency_lts_per_m2
    return paint

print(calculate_paint(0.25, 42, 28, 30))

rooms = [42, 28, 30]
print(calculate_paint(0.25,*rooms))


'''
Piszesz funkcję log_it, która ma zapisać w pliku tekstowym np. 
c:\temp\log_it.txt przesłane do funkcji argumenty. Funkcja będzie 
wykorzystywana w innych miejscach programu, gdzie będzie wywoływana w 
strategicznych momentach, dokumentując działanie programu. Jeśli nie 
masz innych pomysłów to zadbaj o to aby:
- można było przesłać dowolną ilość argumentów
- podczas dopisywania informacji do pliku poszczególne argumenty rozdzielaj spacją
- na końcu w pliku zapisz ENTER, aby kolejne wywołanie funkcji dopisywało od nowej linijki

Przetestuj działanie funkcji wywołując ją np w taki sposób:
log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')
'''

def log_it(*args):
    path = r'/Users/wlasciciel/Desktop/ćwiczenia/log_it.txt'
    with open(path, 'a') as f:
        for line in args:
            f.write(line)
            f.write(' Sialalalala')

        f.write('\n')

log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')
