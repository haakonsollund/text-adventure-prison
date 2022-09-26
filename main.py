tau = 0
kniv = 0
bedøvelse_pistol = 0
usynlighetsdrikke = 0
skuddsikkervest = 0


def room_valg1():
    print("du sitter i en selle i et fengsel")
    print()
    print("du vil flykte fra fengslet og plutselig får du en pakke")
    print("du opner pakken og finner i kaken og denne kaken inneholder en ting")
    print()
    print("hva inneholder kaken du kan bruke for og rømme")
    print()

    valg1 = input("A: stål fil B: teleporterer C: bazooka D: drill ->")

    if valg1 == "A":
        room_valg2A()
    
    if valg1 == "B":
        print("du teleporterer deg ut")
        print()
        print("men havner på en skyte bane og blir skutt")
        print()
        restart7 = input("skriv A for å restarte -> ")
        if restart7 == "A":
            room_valg1()
    if valg1 == "C":
        print("du tar bazookaen og skyter og skudde går i mellom celle stangene og treffet veggen og sprenger og du er død nå")
        print()
        restart8 = input("skriv A for å restarte -> ")
        if restart8 == "A":
            room_valg1()
    if valg1 == "D":
        room_sti2()

def room_valg2A():
    print("du finner en stål fil men hva skal du bruken den på?")
    print()
    
    valg2A = input("A: Vinduet B: Døren")
   
    if valg2A == "A":
        print("du filer opp vinduet og hopper ut")
        print()
        print("men det er 8 etasjer og du dør")
        print()
        restart = input("skriv A for restart -> ")
        
        if restart == "A":
            room_valg2A()
    if valg2A == "B":
        room_valg3B()

def room_valg3B():
    print()
    print("du filer en stang fra selle døren og går ut")
    print()
    print("du står og ser på vaktene og de springer mot deg")
    print()
    print("du bruker metal stangen og slår de bevist løs")
    print()
    print("du ser 2 vakter kommer ut av heise du hopper in i rommet ved siden av deg og lukker døren men de så deg")
    print()
    print("du ser ett ventelasjonsanlegg og du ser ett granat belte og en stol hva vil du bruke")
    print()
    valg3B = input("A:granat belte B:stol -> ")

    if valg3B == "A":
        print()
        print("du plukker opp en granat fra belte og oppner døren og kaster den ut")
        print()
        print("men den spretter i vegen og inn i rommet ditt igjen og sprenger")
        restart2 = input("skriv A for å restarte")
        
        if restart2 == "A":
            room_valg3B()
    if valg3B == "B":
        print("du tar stolen og klatrer inn")
        print()
        print("men vil du gå høyre eller venstre")
        print()

        valg3B2 = input("A:venstre B:høyre ->")

        if valg3B2 == "A":
            print("du beveger deg mot venstre og går ei lang stund")
            print()
            print("du finner bare en opening under deg og faller ned")
            print()
            print("du faller i pause rommet til vaktene og blir tatt")
            restart3 = input("skriv A for å restarte ->")
            
            if restart3 == "A":
                room_valg3B()

        if valg3B2 == "B":
            room_tak()

def room_tak():
    print("du klatrer til høyre og befinner deg på take nå og skal ned")
    print()
    print("hva vil du bruke")
    print()

    valg_tak = input("A:harpune tau B:sugekopper C:fallskjerm D:jettpack ->")

    if valg_tak == "A":
        print("du skyter taue og tar tak og sklir")
        print()
        print("men det brenner på hendene og faller")
        print()
        print("due våkner og ser du er ikke i fengsle lenger men du datt på en vei og ble påkjørt")
        restart4 = input("skriv A for å restarte")
        if restart4 == "A":
            room_tak()

    if valg_tak == "B":
        print("du klatrer ned og springer bort")
        print()
        print("DU ER NÅ FRI")

    if valg_tak == "C":
        print("du tar fallskjermen og hopper")
        print()
        print("men det er ikke falskjermer i fengsler og det er en vanlig sekk og du dør")
        restart5 = input("skriv A for å restarte ->")
        if restart5 == "A":
            room_tak()
    
    if valg_tak == "D":
        print("du skrur jettpacken på men klarer ikke å kontrolere den")
        print()
        print("du flyr vekk fra fengsle men så rett tilbake og krasjer igjenom veggen og havner i cellen din")
        restart6 = input("skriv A for å restarte")
        if restart6 == "A":
            room_tak()

def room_sti2():
    print()
    print("du starter drillen og driller rett ned og faller ned i en forlatt do med planker spikrett fast døren og ett komlokk")
    print()
    print("du ser ett brekkjern og og en opasitator og plukker opp ett tau")
    print()
    print("en opasitator vil gjøre som att du kan gå igjennom vegger")
    print()
    print("hva vil du gjøre")
    tau =+ 1
    valg_sti2D = input("A:bruke opasitatoren B:Bruke brekkhjerne -> ")

    if valg_sti2D == "A":
        print("du bruker opasitatoren og og kan nå gå igjennom vegger")
        print()
        print("og så faller du igjennom golvet og tilslutt er på bunnen av fengslet og faller igjennom bakken og dør for jordens kjerne er for varm")
        print()
        restart9 = input("skriv A for å restarte")
        if restart9 == "A":
            room_sti2()
    
    if valg_sti2D == "B":
        print("du velger brekkhjerne på komlokket")
        print()
        print("og hopper ned og beffiner deg med 2 vakter som ser forvirret ut")
        print()
        print("du springer og må gå venstre eller høyre ")
        print()
        valg_sti2D2 = input("A:venstre B:høyre -> ")

        if valg_sti2D2 == "A":
            print("du løper til venstre og kaster deg inn døren og låser")
            print()
            print("du snur deg og ser 9 vakter og ser en sjangse for inger har våpen og tror du har en liten sjangse og slåss")
            valg_sjangse = input("A:bli tatt B:ta sjangse å slås -> ")

            if valg_sjangse == "A":
                print("du blir tatt ")
                restart10 = input(" skriv A for å restarte -> ")
                if restart10 == "A":
                    room_sti2()
        
            if valg_sjangse == "B":
                print("du tar en sjangse og prøver og slåss og blir banket opp")
                print()
                restart11 = input("skriv A får å restarte -> ")
                if restart11 == "A":
                    room_valg1()
                    
        if valg_sti2D2 == "B":
            room_tingrom()


def room_tingrom():
     print()
     print("du springer til høyre og går inn ett rom og låser døren og finner bedøvelses pistoler med 3 skudd")
     print()
     bedøvelse_pistol =+ 1
     print("du finner og en usynlig hets drikk og en skuddsikker vest og tar den på")
     usynlighetsdrikke =+ 1
     skuddsikkervest =+ 1
     print("du ser to dører till en som står topp secret på og en som leder til en utgang med 6 vakter med")
     print()
     print("vilken dør tar du?")
     print()
    
     valg_door = input("A:top secret B:utgang med vaktene -> ")

     if valg_door == "B":
        print("du går mot untganngen med vaktene hva vil du bruke for å kumme deg ut")
        print()
         
        utstyr = input("A:Usynlighetsdrikken B:tau -> ")

        if utstyr == "A":
            print("du drikker usynlighets drikken og går inn")
            print()
            usynlighetsdrikke =- 0
            print("vaktene stirrer på døren som opnet seg av seg selv og får panikk og skyter")
            print()
            print("de treffer deg i skudsikre vesten din og usynlig hets drikken din forsvinner fordi du ble skudt")
            print()
            restart12 = input("skriv A for å restarte")
            if restart12 == "A":
                room_tingrom()

     if valg_door == "A":
        print("du opner top secret døren og ser 3 vakter du husker du har 3 bedøvelses skudd for pistolen")
        print()
        print("du skyter de og de sover nå")
        bedøvelse_pistol =- 0
        print("du finner masse rare ting men oppe på vegen ser du lyd dempene sko du kan bruke taue ditt for å nå de så du gjør det")
        print()
        tau =- 0
        print("du knyter taue til en lasso og tasten opp og klatrer og henter de")
        print()
        print("du tar de på og går mot den andre døren igjen og drikker usynlighets drikken på nytt og de ser forvirret mot døren skyter du springer vekk og de kanke høre deg nå når du springer")
        print()
        print("du går ut utgangen og du er nå ute")
        usynlighetsdrikke =- 0
        print("DU ER NÅ FRI!")

        room_valg1()


        