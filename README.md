Door: Richard Neyhoff, Gerben Timmerman, Pauline Schomaker
Eindopdracht gevorderd programmeren: Battleships.

Gebruikershandleiding voor het battleships programma.

Het programma kan aangeroepen worden door 'python3 window.py' in de 
terminal aan te roepen. Of door het bestand window.py te starten.

Het openingsscherm opent zich nu, waar het spel gestart kan worden door op de
'Play' knop te drukken.

Vervolgens laadt het spel zich en dient de gebruiker zijn 5 schepen te plaatsen.
Als de gebruiker al zijn schepen geplaatst heeft, kan hij beginnen met het schieten
op de schepen van de computer. De gebruiker krijgt hierover meldingen tijdens het spelen.

De gebruiker heeft gewonnen wanneer deze alle schepen van de computer heeft laten
zinken, voordat de computer alle schepen van de gebruiker geraakt heeft.

Veel plezier tijdens het spelen!

=====================================================================================================

Documentatie voor Programmeurs:

Om het volledige programma uit te voeren heb je volgende bestanden nodig: window.py, board.py, gewonnen.py en verloren.py en alle bijbehoordende plaatjes.

Als je wilt beginnen moet je window.py uitvoeren. Je komt dan op het startscherm terecht. Wanneer je dan op play klikt verbind hij met de Board class en voert hij deze uit. Je krijgt dan eerst een melding op het scherm met daarin de speluitleg. 

Het is daarna dus de bedoeling dat je schepen gaat plaatsen. Je moet dan eerst de richting van het schip kiezen in de combobox(horizontaal of verticaal) deze text leest hij later in de functie schepenGebruiker() in om te bepalen welk coordinaat hij een stapje opzij moet doen en ook moet toevoegen aan de lijst. 

Als je de richting van het schip bepaald hebt, moet je op de button 'schipplaatsen' klikken. Nu komt er een inputvenster tevoorschijn waarin je het begincoordinaat van je schip moet invullen. Deze input neemt hij mee in de functie schepenGebruiker() waar het begincoordinaat dus is vastgesteld. Nu gaat hij voor dit coordinaat afhankelijk van de richting (horizontaal of verticaal) uit de combobox een stapje naar rechts of naar beneden. Een counter houdt bij hoevaak hij deze stapjes maakt. Als de counter gelijk is aan de lengte van het schip dan hoeft de functie geen coordinaten meer toe te voeren voor dat schip aan de lijst: self.lijstSchepenGebruiker.
Dit herhaal je 5x totdat de schepen geplaatst zijn. 

Als je de schepen geplaatst hebt kun je op de button 'start schieten' klikken. Als je hierop geklikt hebt gaat de computer begincoordinaten genereren, een randomrichting bepalen, deze telkens een stapje laten opschuiven en  deze coordinaten appenden aan de lijst: self.lijstSchepenComputer.

Vervolgens kom je in een while loop terecht die net zolang doorgaat totdat de lengte van de lijsten self.lijstSchepenGebruiker of self.lijstSchepenComputer gelijk is aan 0. Dit is omdat de lijst dan leeg is en dan dus alle coordinaten zijn geraakt en verwijderd zijn uit de lijst. In de while loop staat een functie  schietenGebruiker() en schietenComputer(). De functie schietenGebruiker() vraag om coordinaten als input gescheiden door een spatie en kijkt of dit coordinaat ook in de lijst self.lijstSchepenComputer staat. Als dit gekozen coordinaat in de lijst staat dan haalt hij het coordinaat uit de lijst en geeft hij in de  grid interface weer of hij een coordinaat geraakt heeft, deze is dan onderstreept en doorgekrast. Ook krijgt de gebruiker dan een melding dat hij geraakt heeft. Als het gekozen coordinaat niet in de lijst staat dan krijgt de gebruiker een melding dat hij gemist heeft. Het coordinaat word dan in de grid alleen doorgekrast en niet onderstreept. 

De functie shotComputer() genereert een random schot van de computer en kijkt of deze in de lijst met coordinaten van de gebruiker zit. Als het gegenereerde random schot in de lijst van de gebruiker zit haalt hij deze uit de lijst en krijgt de gebruiker een melding te zien dat de computer een schip heeft geraakt. Ook wordt het coordinaat in de interface doorgekrast. Als de computer zijn/haar schot niet inde lijstSchepenGebruiker zit, wordt alleen het schot doorgerkrast in de interface en krijgt de gebruiker een melding dat de computer gemist heeft.

Dit gaat dus net zolang door totdat de lengte van een van de lijsten gelijk is aan 0, want je zit in een while loop. Als de lengte van de  lijst van de gebruiker gelijk is aan 0 sluit hij de interface af en opent hij het verliezersscherm met de melding dat je gewonnen hebt. Als de lengte van de lijst van de computer gelijk is aan 0, sluit hij de interface af en opent hij het winnaarscherm met de melding dat je gewonnen hebt.

Notes:
We hebben geen oplossing kunnen bedenken om de schepen van de gebruiker binnen de grid te houden. Het is helaas dus mogelijk om 10 9 in te vullen als coordinaat en dus voegt de functie dan de coordinaten (10,9),(10,10),(10,11) aan de lijst. Dus kan de computer nooit (10,11) raken. Dus wijzen we de gebruiker erop dat hij moet proberen een coordinaat te kiezen zodat het schip coordinaten van de grid meekrijgt en niet van buiten. Anders is dit valsspelen. We hebben ons best gedaan dit op te lossen, maar door tijdnood kwamen we hier niet meer uit.

Daarbij kan het ook voorkomen dat er dubbele coordinaten in de lijst terrecht komen de schepen overlappen elkaar dan. Dit wilden we ook verhelpen, maar hier kwamen we ook niet meer uit in verband met tijdnood.

Hij laat tijdens het runnen de lijst met coordinaten van de computer in de terminal zien. Dit omdat het kan voorkomen dat er misschien een dubbele coordinaat kan voorkomen, maar op deze manier zie je waar de dubbele coordinaat zich bevindt. Als je dit niet wilt en gewoon wilt spelen zal je de print commandos uit board.py verwijderen. Dan kun je het spel spelen zonder dat je dingen worden voorgezegd in de terminal.


