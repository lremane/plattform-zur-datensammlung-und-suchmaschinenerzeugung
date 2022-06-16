# Sprint 2 - Abgabe

## 1. Name des Projektes

QEnable

## 2. Aktive Teammitglieder 

- [Johannes Kindler](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/jkindler)
- [Philipp Semlinger](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/psemling)
- [Finn Mergenthal](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/fmergent)
- [David Deutschmann](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/ddeutsch)
- [Laurin Remane](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/mremane)
- [Abdul Rahman Alkedda](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/aalkedda)
- [Abdullah Al-hoty](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/aalhoty)
- [Moritz Meister](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/mmeister)
- [Lukas Ponicke](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/lponicke)
- [Tony Lenz](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/tlenz1)
- [Lukas Marche](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/lmarche)

## 3.1 Link zum Piloten & "Tutorial"

[QEnable-Pilot](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/pdus/plattform-zur-datensammlung-und-suchmaschinenerzeugung/-/tree/developement)

[Tutorial](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/pdus/plattform-zur-datensammlung-und-suchmaschinenerzeugung/-/blob/developement/README.md)

## 3.2 Docker

[Dockerfile](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/pdus/plattform-zur-datensammlung-und-suchmaschinenerzeugung/-/blob/developement/Dockerfile)

Verwendung:

    sudo docker build -t flask-image .
    sudo docker run --rm -p 5000:5000 flask-image

## 3.3 Gitlab Action

## 4.1 Problemdefinition & Produktvison

Problemdefinition:

> Unser Kunde hat zu wenig eingebettete Webseiten aus denen QA Daten bezieht, keine Automatisierter Ablauf zur Indexierung.

Produktvision: 
> Es soll eine Anwendung für Webseitenbetreiber und Privatpersonen, die RDF Daten in Webseiten bereitstellen oder verarbeiten wollen, erstellt werden. In dieser Anwendung soll durch Eingabe einer URL diese Webseite nach RDF Daten gecrawlt, validiert, zwischengespeichert, analysiert und an QAnswer.eu übergeben werden.
Darauf folgend ist eine Suchanfrage auf den Daten über QAnswer möglich und die heraushezogenen RDF-, sowie die Analysedaten stehen dem Nutzer zur Verfügung.

## 4.2 Design-Thinking-Prototyp

[Prototyp](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/pdus/plattform-zur-datensammlung-und-suchmaschinenerzeugung#problemdef)

## 4.3 Erfüllte funktionale und nicht funktionale Anforderungeen

## 5. Beiträge der Teammitglieder