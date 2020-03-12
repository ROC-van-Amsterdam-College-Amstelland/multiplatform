# Op3 - Multiplatform

## Les 1

### Leerdoelen

1. [ ] Ik kan Git downloaden en installeren op mijn laptop  
2. [ ] Ik kan een Assignment accepteren in Github Classroom
3. [ ] Ik kan een `clone` maken van een repository
4. [ ] Ik kan de laatste versie van Python downloaden en installeren op mijn laptop
5. [ ] Ik kan de Microsoft Python Extension installeren in VS Code
6. [ ] Ik kan in VS Code instellen welke Python interpreter gebruikt moet worden
7. [ ] Ik kan in VS Code een debugger instellen voor Python
8. [ ] Ik kan een `.py` bestand uitvoeren in de VS Code terminal
9. [ ] Ik kan een breakpunt zetten in een `.py` bestand
10. [ ] Ik kan de debugger opstarten in VS Code
11. [ ] Ik kan stapsgewijs door een `.py` bestand lopen met de debugger
12. [ ] Ik kan een `commit` maken met een duidelijke commit message
13. [ ] Ik kan mijn code `pushen` naar Github

### Uitleg

In deze les gaan we je ontwikkelomgeving instellen zodat je voor deze lessen kan werken met Python binnen VS Code. Ook leer je omgaan met Github Classroom om je code in te leveren. 

>We gebruiken VS Code als editor tijdens deze lessen. Als je gewend bent om met een andere editor te werken zie dit dan als een mooie kennismaking met wat in zeer korte tijd is uitgegroeid tot een van de meest populaire editors. Als je gewend bent aan de sneltoetsen van een bepaalde editor; er zijn in VS Code extensions te vinden die de keybindings van je oude editor instellen voor gebruik binnen VS Code.

### Opdracht

1. Installeer Python en stel VS Code in voor gebruik van Python, zie [hier](https://github.com/ROC-van-Amsterdam-College-Amstelland/Docs/blob/master/Python/Installatie-vscode-instellen/README.md) voor uitleg.
2. Open het `.py` bestand in deze repository in VS Code
3. Kies uit het rechtermuisknop menu de optie `Run Python File in Terminal`
4. Je ziet de output van het bestand verschijnen in je terminal
5. Onderstaand voorbeeld laat zien wat er in je terminal verschijnt:
```terminal
Lineare getallen reeks: 1,0,1,2,3,4,5,6,7,8,
Fibonacci getallen reeks: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
Fibonacci getallen reeks: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
Geometrische getallen reeks: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512,
Geometrische getallen reeks: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512,
````
> De bedoeling is dat er 3 getallenreeksen als output worden getoond in je terminal:
> 1. Een lineare reeks: elk volgend getal in de reeks is het voorgaande getal + 1
> 2. Een fibonacci reeks: elk volgend getal is de som van de twee voorgaande getallen
> 3. Een geometrische reek: elk volgend getal is het voorgaande getal keer 2  

6. Zorg er voor dat:  
    1. [ ] Elke reeks getallen maar één keer in de output verschijnt (fibonacci en geometrisch worden nu dubbel getoond)
    2. [ ] De Lineare getallen reeks er zo uit ziet: 0,1,2,3,4,5,6,7,8,9
    3. [ ] Dat de komma aan het eind van de output niet meer getoond wordt  
> Gebruik de mogelijkheid om te debuggen binnen VS Code om het programma te doorlopen:
> 1. Zet een breakpoint op regel 4 door op de kolom links van het regelnummer te klikken. Er verschijnt een rode stip. 
> 2. Ga naar de Debug tab in VS Code ( <kbd>CTRL</kbd><kbd>+</kbd><kbd>SHIFT</kbd><kbd>+</kbd><kbd>D</kbd> ).  
> 3. Druk op de groene play knop bovenaan links: de uitvoer van het programma stopt op regel 4.
> 4. Gebruik F11 om een enkele stap verder te gaan in de uitvoer. Terwijl je dit doet zie je links de waardes van de verschillende variabelen in het programma veranderen.
> 5. Boven en in het midden van je venster is er ook een debug controlle paneel verschenen, de play en stop knop spreken wellicht voor zich. Experimenteer met de andere opties tot je begrijpt wat elke knop doet. 
7. Opgelost? Sla het bestand op en ga naar de Source Control tab in VS Code ( <kbd>CTRL</kbd><kbd>+</kbd><kbd>SHIFT</kbd><kbd>+</kbd><kbd>G</kbd> ) 
8. Stage het bestand voor jet het commit > [uitleg](https://github.com/ROC-van-Amsterdam-College-Amstelland/Docs/blob/master/Git/fe-git-workflow.md#files-stagen-voor-een-commit)
9.  Commit het bestand > [uitleg](https://github.com/ROC-van-Amsterdam-College-Amstelland/Docs/blob/master/Git/fe-git-workflow.md#git-commit)
10. Lever je code in door je code te pushen naar Github > [uitleg](https://github.com/ROC-van-Amsterdam-College-Amstelland/Docs/blob/master/Git/fe-git-workflow.md#git-push)
