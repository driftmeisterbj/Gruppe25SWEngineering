Programvare som må være installert for å kunne kjøre programmet:

- Python (3.7 - 3.12), det anbefales med 3.11 eller 3.12 --- https://www.python.org/
- pip , Brukes for å installere wxpython som er biblioteket vi har benyttet oss av for brukergrensesnitt --- https://pip.pypa.io/en/stable/installation/

Hvordan kjøre:
Applikasjonen startes ved å kjøre "app.py" som ligger på rotnivå i prosjektet.
"app.py" kan kjøres via et IDE, f.eks. pycharm. Eller via CMD.

NB! Fjern anførselstegnene på kommandoene ved kjøring i CMD

CMD-kommandoer:
Starte applikasjonen via CMD hvis du står i mappen "Gruppe25SWEngineering (rot); "python app.py"

For å kjøre alle testene på en gang kan du gi denne kommandoen i CMD:
"python -m unittest tests.test_Camera tests.test_Device tests.test_Fridge tests.test_Heater tests.test_JsonDatabase tests.test_Light tests.test_Lock tests.test_read_write"
