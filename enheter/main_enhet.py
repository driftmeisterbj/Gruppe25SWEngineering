from smart_kjoleskap import SmartKjøleskap
from smart_lys import SmartLys
from smart_varmeovn import SmartVarmeovn

kjøleskap = SmartKjøleskap("Kjøleskap")
lys = SmartLys("Stue Lys")
varmeovn = SmartVarmeovn("Stue Varmeovn")

def kjøleskap_meny():
    print("\n--- Kjøleskap ---")
    print("1. Skru på kjøleskap")
    print("2. Skru av kjøleskap")
    print("3. Sett temperatur")
    print("4. Sjekk status")
    valg = input("Velg et alternativ (1-4): ")
    
    if valg == '1':
        kjøleskap.skru_på()
    elif valg == '2':
        kjøleskap.skru_av()
    elif valg == '3':
        ny_temperatur = input("Skriv inn ny temperatur: ")
        kjøleskap.sett_temperatur(ny_temperatur)
    elif valg == '4':
        kjøleskap.status()
    else:
        print("Ugyldig valg, prøv igjen.")

def lys_meny():
    print("\n--- Lys ---")
    print("1. Skru på lys")
    print("2. Skru av lys")
    print("3. Sett lysstyrke")
    print("4. Sjekk status")
    valg = input("Velg et alternativ (1-4): ")

    if valg == '1':
        lys.skru_på()
    elif valg == '2':
        lys.skru_av()
    elif valg == '3':
        ny_lysstyrke = input("Skriv inn ny lysstyrke (1-10): ")
        lys.sett_lysstyrke(ny_lysstyrke)
    elif valg == '4':
        lys.status()
    else:
        print("Ugyldig valg, prøv igjen.")

def varmeovn_meny():
    print("\n--- Varmeovn ---")
    print("1. Skru på varmeovn")
    print("2. Skru av varmeovn")
    print("3. Sett temperatur")
    print("4. Sjekk status")
    valg = input("Velg et alternativ (1-4): ")

    if valg == '1':
        varmeovn.skru_på()
    elif valg == '2':
        varmeovn.skru_av()
    elif valg == '3':
        ny_temperatur = input("Skriv inn ny temperatur (15-30 grader): ")
        varmeovn.sett_temperatur(ny_temperatur)
    elif valg == '4':
        varmeovn.status()
    else:
        print("Ugyldig valg, prøv igjen.")

def main_menu():
    while True:
        print("\n--- Hovedmeny ---")
        print("1. Kjøleskap")
        print("2. Lys")
        print("3. Varmeovn")
        print("4. Avslutt")

        valg = input("Velg en enhet (1-4): ")

        if valg == '1':
            kjøleskap_meny()
        elif valg == '2':
            lys_meny()
        elif valg == '3':
            varmeovn_meny()
        elif valg == '4':
            print("Avslutter programmet.")
            break
        else:
            print("Ugyldig valg, prøv igjen.")

if __name__ == "__main__":
    main_menu()
