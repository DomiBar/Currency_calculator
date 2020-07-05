import json
import requests
import csv

def export_to_csv(rates):
    file_csv='rates.csv'
    try:
        with open(file_csv,'w', newline='') as csvfile:
            fieldnames=['currency','code','bid','ask']
            writer=csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writerow({'currency':'Waluta','code':'Kod','bid':'Cena kupna','ask':'Cena sprzedaży'})
            writer.writerows(rates)    
    except:
        print(f"!!!!!!Nie udało się otworzyć pliku {file_csv} . Dane nie zostały zapisane.!!!!!!\nJeżeli plik jest otwarty w innym programie, zamknij go przed zapisem.")

rates=[]

response=requests.get('http://api.nbp.pl/api/exchangerates/tables/C?format=json')
data=response.json()

for key in data[0]['rates']:
    rates.append(key)

export_to_csv(rates)

