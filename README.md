
# Discord Reaction Giveaway

Dieses kleine Python Skript gibt dir die Möglichkeit, das du Giveaways selbstständig hosten kannst.
Die Auswertung und die Gewinner wertet dir das Skript aus.

## Das Skript funktioniert derzeit nur unter Windows



## Token konfigurieren

# Es gibt zweit Varianten: 

### Varinate 1:
Du nutzt einen Bot [Bot erstellen](https://discord.com/developers/applications) welcher auf dem Discord Server bereits ist.



### Variante 2
 Du suchst dir dein persönlichen Token raus. (Nicht empfohlen)
 
 Wenn du damit erfahrung hast, musst du in der Main.py den Header (Line 13) zu \
 `header = {'authorization': f'{token}'}` verändern

 Den Token fügst du in config.py ein.

## Installation

Führe das Skript aus.

Es wird dich dann nach folgenden Daten fragen

- ChannelID (ID des Channels in welchem die Nachricht ist)
- MessageID (ID der Nachricht in dem Channel)
- Reaction (Die Reaction der Message)
- Name des Gewinnspieles
- Zeit wie lange der Gewinner Zeit hat sich zu melden
- Anzahl der Gewinner

Danach öffnet sich ein Editor Fenster mit den Copy - Paste Text welches den oder die Gewinner verkündet




## FAQ

#### Wie bekomme ich die Channel / Message ID?

- Geh in Discord unten links auf das Zahnrad neben deinen Namen
- Klicke unter dem Punkt "App-Einstellungen auf "Erweitert"
- Setze den Hacken bei "Entwicklungsmodus"

![alt text](https://img.max1021.de/Discord_UrBoaIdlJC.png "Screenshot 1")


#
#### Wie bekomm ich das React Emote zum kopieren?

- Füge das Emote ganz normal im Chat ein.
- Füge vor dem Emote dann  `\` ein um das Emote zu erhalten.
![alt text](https://img.max1021.de/Hg2l6LAxjk.gif "GIF1")

#
#### Wie funktioniert das bei Custom Emotes?
- Füge das Custom Emote von einem Server ein und füge wieder `\` davor ein.
- Nun wird dir das Emote als "Text" wiedergespiegelt.
- Kopier dir den Inhalt zwischen `< & >`` raus und füge es bei dem Skript ein
#### Beispiel -> 
Normale Ausgabe:
`<:ColorsGyroid:906472705665151006>`

Eingabe im Bot:
`:ColorsGyroid:906472705665151006`





