from RegonAPI import RegonAPI
from RegonAPI.exceptions import ApiAuthenticationError
import pandas as pd

from secure.gus_api_key import GUS_API_KEY

K_FILE = "dane\k_file.csv"
F_file = "f_file.csv"
POLA_DO_ZAPISU_KONT = ['Nazwa', 'Nip', 'Regon','Gmina' , 'Miejscowosc', 'KodPocztowy', 'Ulica', 'NrNieruchomosci', 'data_dodania']

def pobierz_kontr():
    dane = pd.read_csv(K_FILE, sep=";")
    return dane.values 

def dodaj_kon(dane):
    try:
        f = open(K_FILE, "r")
    except:
        f = open(K_FILE, "w")
        f.write(';'.join(POLA_DO_ZAPISU_KONT)+"\n")
    f.close()
    f = open(K_FILE, "a", encoding="UTF-8")
    line = ';'.join(dane)
    f.write(line)
    f.write("\n")
    f.close()

def pobierz_nazwy():
    dane = pd.read_csv(K_FILE, sep=";") 
    return dane['Nazwa'].values 

def pobierz_dane(nip):
    # Available reports
    REPORTS = [
        "BIR11OsFizycznaDaneOgolne",
        "BIR11OsFizycznaDzialalnoscCeidg",
        "BIR11OsFizycznaDzialalnoscRolnicza",
        "BIR11OsFizycznaDzialalnoscPozostala",
        "BIR11OsFizycznaDzialalnoscSkreslonaDo20141108",
        "BIR11OsFizycznaPkd",
        "BIR11OsFizycznaListaJednLokalnych",
        "BIR11JednLokalnaOsFizycznej",
        "BIR11JednLokalnaOsFizycznejPkd",
        "BIR11OsPrawna",
        "BIR11OsPrawnaPkd",
        "BIR11OsPrawnaListaJednLokalnych",
        "BIR11JednLokalnaOsPrawnej",
        "BIR11JednLokalnaOsPrawnejPkd",
        "BIR11OsPrawnaSpCywilnaWspolnicy",
        "BIR11TypPodmiotu",
    ]

    NIP = nip

    # Authentication
    api = RegonAPI(
        bir_version="bir1.1", is_production=True, timeout=10, operation_timeout=10
    )
    try:
        api.authenticate(key=GUS_API_KEY)
    except ApiAuthenticationError as e:
        print("[-]", e)
        exit(0)
    except Exception as e:
        raise

    # Search by NIP
    result = api.searchData(nip=NIP)
    print(type(result[0]))
    return result[0]