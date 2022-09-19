

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
        pass
    if valg1 == "C":
        pass
    if valg1 == "D":
        pass

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
        print("du velger stolen og bruker dnen og klater inn i ventelasjons anlegge")
        print()
        print("")


        