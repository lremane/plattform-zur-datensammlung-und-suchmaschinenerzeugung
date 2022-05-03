# Plattform zur Datensammlung und Suchmaschinenerzeugung

## Members

- [Johannes Kindler](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/jkindler)
- [Philipp Semlinger](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/psemling)
- [Lukas Marche](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/lmarche)
- [Finn Mergenthal](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/fmergent)
- [David Deutschmann](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/ddeutsch)
- [Laurin Remane](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/mremane)
- [Abdul Rahman Alkedda](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/aalkedda)
- [Abdullah Al-hoty](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/aalhoty)
- [Moritz Meister](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/mmeister)
- [Lukas Ponicke](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/lponicke)
- [Tony Lenz](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/tlenz1)
- [Lukas Marche](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/lmarche)

## Design-Thinking-Process

Es soll eine Anwendung für Webseitenbetreiber, die RDF Daten bereitstellen, erstellet werden. In dieser Anwendung soll durch Eingabe einer URL diese Website nach RDF Daten gecrawlt, validiert, zwischengespeichert und an QAnswer.eu übergeben werden.

###Schritt 1: Verstehen
- Was soll neu entwickelt werden?
    - eine Anwendung welches einer Webseite die Anbindung an QAnswer ermöglicht
    - bereits existierende Toolchain zum (www -> rdf) einheitlich, dauerhaft und nutzer*innen-freundlich konfigurieren können
- Für wen soll entwickelt werden?
    - Nutzergruppen erkennen 
        - User Typ 1 (Edeka): Business Besitzer, der seine Daten auf QA zur Verfügung stellen/verarbeiten möchte
        - User Typ 2 (Theresa): Möchte Informationen aus spezifischen selbst ausgewählten Quellen durchsuchen können (automatisierte        Datenbeschaffung)
- Welche Rahmenbedingungen berücksichtigen?
    - robots.txt berücksichtigen
    - Zeitplan und Budget einhalten
    - nicht-funktionale Anforderungen notieren
        - ansprechendes Design
        - URL ähnlich zu QAnswer oder an QAnswer angegliedert
- Endzustand der Lösung?
    - User übergibt API Website per URL. Diese wird live gecrawlt an QAnswer übergeben, sodass der User Typ 1 direkt seine Daten zur Verfügung gestellt hat und User Typ 2 direkt seine Anfragen geben kann.

###Schritt 2: Beobachten
- Wie gehen Nutzer aktuell vor (in realer Umgebung)?
    - manuelles hochladen reiner RDF Dateien und dann Auswertung via QAnswer
- Welche Verbesserungen werden gewünscht?
    - Nutzeroberfläche soll geschaffen werden
    - Prozess soll automatisiert werden
    - Eingabe der URL
    - beständiges aktualisieren/updates des Datensatzes
    - persistente Konfiguration des Crawlingprozesses
- Welche Wünsche haben die Nutzer?
    - Einfaches (und schnelles) füttern von Daten aus Webseiten an QAnary
    - Updaten/Synchronisieren von RDF Daten aus anderen Quellen (Triplestores)
- Was würden sich die Nutzer (nicht die Devs!) als einen Idealzustand vorstellen?
    - Öffnen der Applikation, Einfügen des Links der Webseite, Bestätigen, (kurz!  Warten,) Anfragen eingeben, Antworten erhalten, Fertig
    - danach erfolgreiches Nutzen von QAnswer auf den neu gewonnenen Daten
    - Rückgabe von Statistiken (Menge der verwertbaren Daten, Häufigkeit der verwertbaren Daten in Gesamtdatensatz)
    - (Möglichkeit der direkten Nutzung einer QAnswer Suchzeile und Rückgabe der Antworten  innerhalb der Webseite)

### Issue Definition

### Design-Thinking-Prototypes

### Functional and Nonfunctional (User Stories)

#### Functional

#### Nonfunctional

### Product Vision

## Meetings 

- [Protocol](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/pdus/plattform-zur-datensammlung-und-suchmaschinenerzeugung/-/wikis/Board-Meetings)


