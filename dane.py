from RegonAPI import RegonAPI
from RegonAPI.exceptions import ApiAuthenticationError


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

    TEST_API_KEY = "a379ed7d123946f0a9b8"
    NIP = nip

    # Authentication
    api = RegonAPI(
        bir_version="bir1.1", is_production=True, timeout=10, operation_timeout=10
    )
    try:
        api.authenticate(key=TEST_API_KEY)
    except ApiAuthenticationError as e:
        print("[-]", e)
        exit(0)
    except Exception as e:
        raise

    # Search by NIP
    result = api.searchData(nip=NIP)
    return result[0]