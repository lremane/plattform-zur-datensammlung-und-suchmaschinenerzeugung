# Sprint 3 - Abgabe

## 1. Name des Projektes

QEnable

## 2. Aktive Teammitglieder 

   - [Abdullah Al-hoty](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/users/aalhoty/activity)
   - [Abdul Rahman Alkedda](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/users/aalkedda/activity) [Backend, Frontend, Docker]
   - [David Deutschmann](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/users/users/ddeutsch/activity)
   - [Johannes Kindler](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/users/jkindler/activity) [CI/CD Pipeline, Docker, production deployment server support]
   - [Tony Lenz](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/users/tlenz1/activity)[Ausarbeitung Projektposter, Ausarbeitung Projektpräsentation]
   - [Lukas Marche](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/users/lmarche/activity)[Ausarbeitung Projektposter, Ausarbeitung Projektpräsentation, Vortrag]
   - [Moritz Meister](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/users/mmeister/activity)[Ausarbeitung Projektposter, Ausarbeitung Projektpräsentation, Domain Crawler, Reviewing]
   - [Finn Mergenthal](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/users/users/fmergent/activity) [Restrukturierung des Clients, Code reviews]
   - [Lukas Ponicke](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/users/lponicke/activity) [Scrum master, Ausarbeitung und Vortragen der Praesentation, Protokollieren der Meetings, Crawler, Reviewing]
   - [Laurin Remane](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/users/users/mremane/activity) [Austausch Client]
   - [Philipp Semlinger](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/users/users/psemling/activity) [Scrum master, organization, communication product owner]

## 3.1 Link zum Piloten & "Tutorial"

[QEnable-Pilot](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/pdus/plattform-zur-datensammlung-und-suchmaschinenerzeugung/-/tree/developement)

[Tutorial](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/pdus/plattform-zur-datensammlung-und-suchmaschinenerzeugung/-/blob/developement/README.md)

## 3.2 Docker

[Dockerfile](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/pdus/plattform-zur-datensammlung-und-suchmaschinenerzeugung/-/blob/developement/Dockerfile)

### 3.3.1 Quick-Start-Guide

    sudo docker build -t flask-image .
    sudo docker run --rm -p 5000:5000 flask-image

Weiter geht´s [hier](#ip).

### 3.3.2 Ausführliches Tutorial

Überprüfe, ob die Gruppe "docker" bereits existiert.

    groups 
    
Sollte die Gruppe nicht exitieren, muss diese erstellt werden.

    sudo groupadd docker


Der Nutzer muss der Gruppe "docker" hinzugefügt werden.

    usermod -aG docker $USER

Dockerstart:

    systemctl start docker

Es muss nun zu dem Verzeichnis des Dockerfiles navigiert und das Docker-Image gebaut werden.

    docker build -t <docker image name> .

Dabei muss `<docker image name>` mit einem Namen für das Docker-Image ersetzt werden. 

Der nächste Schritt ist die Ausführung des Docker-Images.

    docker run --rm -p 5000:5000 <docker image name>


`--rm`: Der Docker-Container wird nach dem Verlassen gelöscht, um Platz zu sparen.

`-p`: Gibt die Spezifikation des Ports an.

<a name="ip" ></a>Die Webseite ist nun unter `http://172.17.0.2:5000` erreichbar.


Optional, wenn man einen Container bauen möchte: 

    docker container create flask-image
    docker container list -a 
    docker start <docker container id>
    docker exec -it <docker container id> /bin/bash

Dabei muss `<docker container id>` mit der ID des Docker-Containers ersetzt werden. 

Dummy-Login-Daten:
Username: qenable@fyii.de
Password: password123
(https://qanswer-frontend.univ-st-etienne.fr/)

## 3.3 Gitlab Action

[.gitlab-ci.yml](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/pdus/plattform-zur-datensammlung-und-suchmaschinenerzeugung/-/blob/developement/.gitlab-ci.yml)

## 4.1 Problemdefinition & Produktvison

Problemdefinition:
> Es soll eine einfache Möglichkeit geschaffen werden, RDA-Daten aus schema.org-Webseiten zu ertrahieren, zu mappen und auf QAnswer hochgeladen werden

Produktvision: 
> Die Anwendung soll ein Web-Interface darstellen, in dem es zunächst möglich ist, sich auf QAnswer anzumelden. Der Erfolg soll mit einer Meldung bestätigt werden. Nun soll in einem Textfeld eine URL eingegeben werden und in einem zweiten Textfeld ein Name. Nun soll es zum einen einen Crawl-Button geben, welcher aus der URL die RDA-Daten entsprechend der schema.org-Darstellung extrahiert und als nt-File zum Download bereitstellt. Der Download soll erst mit einem erneuten Klick auf den entsprechenden Button starten. Gleichzeitig sollen die gecrawlten Daten automtisch auf QAnswer hochgeladen werden und dort mit dem Namen aus dem zweiten Textfeld benannt werden.
Nun können die Daten auf qanswer.fr entsprechend verwaltet und durchsucht werden.

  
## 4.2 Design-Thinking-Prototyp

Webapplikation - GUI

![image](https://www.imn.htwk-leipzig.de/~jkindler/PDuS/img-2.png)


## 4.3 Erfüllte funktionale und nicht funktionale Anforderungen

- Interface mit Anmeldeprozess
- Reaktion bei Anmeldung (Erfolgs- oder Misserfolgsmeldung)
- Möglichkeit URLs und Bezeichnungen in 2 Textfeldern einzugeben
- Crawl-Button, der die URL nach RDA-Daten durchsucht
- Reaktion bei Crawling (Erfolgs- oder Misserfolgsmeldung)
- Download-Button
- Korrektes Mapping der Daten entsprechend schema.org-Syntax
- Upload an QAnswer

## 5. Beiträge der Teammitglieder


Die ungleiche Anzahl der Commits und Lines per Person ist sehr ungleich verteilt, weil es unterschiedliche Grundvoraussetzungen der Teammitglieder gibt. Viele administrative Tätigkeiten, Führen und Auswerden von Protokollen, Kommunikation untereinander, mit dem Projektsponsor, Erstellen und Verteilen von Issues, Reviewing, Leiten der Meetings, Organisation des Gits, Halten und Erstellen von Präsentationen, Abgaben und Plakaten sind alles Tätigkeiten, die nicht direkt an Code-Lines absehbar sind. Dies erklärt die unterschiedliche Nachvollziehbarkeit der Aufgaben, die sich keinesfalls in unterschiedlichem zeitlichen Aufwand wiederspiegelt.

## 6. Intendierte Softwarearchitektur(UML-Diagramm)
 - markieren, welche Komponenten bereits implementiert sind
 - Geben Sie zu allen nicht-funktionalen Anforderungen (vgl. 4.3) an, ob diese in der Architektur repräsentiert sind und wenn ja, durch welche Komponente(n)
