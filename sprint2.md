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

Nachdem Sie sich auf unserer Webseite befinden, müssen Sie sich rechts in ihrer Instanz von QAnswer einloggen (Nutzername Passwort)
-> Falls Account nicht vorhanden, schlägt Login fehl.

Nach dem erfolgreichen Login, verschwindet das „login-Panel“ .

Nun können Sie einen Link im Rechten Fenster „Quelle“ eingeben und mit einem Namen für das Dataset in QAnswer versehen.
Ein anschließendes betätigen des „start process!“ Buttons, wird der Crawl Vorgang gestartet und die gecrawlt rdf´s direkt an die eingeloggte Instanz von QAnswer übergeben.

Nun können (abhängig von der Strukturierung des RDF) in der QA Instanz fragen auf die Webseiten beantwortet werden.

## 3.2 Docker

[Dockerfile](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/pdus/plattform-zur-datensammlung-und-suchmaschinenerzeugung/-/blob/developement/Dockerfile)

Verwendung:

    docker build -t flask-image .
    docker run --rm -p 5000:5000 flask-image

## 3.3 Gitlab Action

[.gitlab-ci.yml](https://gitlab-softwareprojekt.fim.htwk-leipzig.de/pdus/plattform-zur-datensammlung-und-suchmaschinenerzeugung/-/blob/developement/.gitlab-ci.yml)

## 4.1 Problemdefinition & Produktvison

Problemdefinition:

> Unser Kunde hat zu wenig eingebettete Webseiten aus denen QA Daten bezieht, keine Automatisierter Ablauf zur Indexierung.

Produktvision: 
> Es soll eine Anwendung für Webseitenbetreiber und Privatpersonen, die RDF Daten in Webseiten bereitstellen oder verarbeiten wollen, erstellt werden. In dieser Anwendung soll durch Eingabe einer URL diese Webseite nach RDF Daten gecrawlt, validiert, zwischengespeichert, analysiert und an QAnswer.eu übergeben werden.
Darauf folgend ist eine Suchanfrage auf den Daten über QAnswer möglich und die heraushezogenen RDF-, sowie die Analysedaten stehen dem Nutzer zur Verfügung.

## 4.2 Design-Thinking-Prototyp

Webapplikation - GUI

![image](https://www.imn.htwk-leipzig.de/~jkindler/PDuS/img-2.png)


## 4.3 Erfüllte funktionale und nicht funktionale Anforderungen

> Als IT-Mitarbeiter eines Unternehmens kann ich RDF-Daten aus beliegen Websiten crawlen und diese an eine konkrete QAnswer instanz hochladen, damit ich auf diesen Daten natürlich sprachliche Fragen auf QAnswer stellen kann. (Die RDF-Daten der gecrawlten Website müssen das Alphabet von Schema.org verwenden, damit Fragen gestellt werden können)

> Als IT-Mitarbeiter eines Unternehmens kann ich RDF-Daten aus einer beliebigen Website crawlen und im N-Triples Format herunterladen.

## 5. Beiträge der Teammitglieder
