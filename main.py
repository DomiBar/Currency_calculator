import requests
import csv


class CurrencyCalculator:
    def __init__(self):
        self.rates = []

    def __str__(self):
        return str(self.rates)

    def get_rates(self):
        response = requests.get(
            'http://api.nbp.pl/api/exchangerates/tables/C?format=json')
        data = response.json()

        for key in data[0]['rates']:
            self.rates.append(key)

    def export_to_csv(self):
        file_csv = 'rates.csv'
        try:
            with open(file_csv, 'w', newline='') as csvfile:
                fieldnames = ['currency', 'code', 'bid', 'ask']
                writer = csv.DictWriter(
                    csvfile, fieldnames=fieldnames, delimiter=';')
                writer.writerow({'currency': 'Waluta', 'code': 'Kod',
                                 'bid': 'Cena kupna', 'ask': 'Cena sprzedaży'})
                writer.writerows(self.rates)
        except Exception:
            print(f"!!!!!!Nie udało się otworzyć pliku {file_csv}."
                  + "Dane nie zostały zapisane.!!!!!!")
            print("Jeżeli plik jest otwarty w innym programie,"
                  + "zamknij go przed zapisem.")
