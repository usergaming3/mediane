while True:
    gh=input("bonjour, avez-vous un code premium?")
    if gh=="oui":
        a=int(input("quel est votre code d'accès?"))
        if a !=12345:
            import time
            delai =10
            print("Nous vérifions le code saisit,veuillez patienter")
            print("loading...")
            for i in range(delai, 0, -1):
                time.sleep(1)  
            print("ACCES DENIED")
        else:
            ascii_art = '''
                   .___.__                             
  _____   ____   __| _/|__|____    ____   ____   ____  
 /     \_/ __ \ / __ | |  \__  \  /    \ /    \_/ __ \ 
|  Y Y  \  ___// /_/ | |  |/ __ \|   |  \   |  \  ___/ 
|__|_|  /\___  >____ | |__(____  /___|  /___|  /\___  >
      \/     \/     \/         \/     \/     \/     \/ 
'''

        print(ascii_art)
        print("Nous somme Tres fières des vous présanter la version ALPHA de Médianne")
        print("voici les différantes options que Médianne propose actuellement:")
        print("=====> Médiamaths(1)")
        while True:
            choice0=int(input("quel option avez-vous choisit?:"))
            if choice0==(1):
                print("bienveunue dans Médiamaths Alpha")
                print("multiplications uniquement(1)")
                print("divisions uniquement(2)")
                print("aditions uniquement(3)")
                print("soustractions uniquement(4)")
                print("toutes les opérations comprises(5)")
                print("théorème de Pythagore(6)")
                print("réciproque du théorème de Pythagore(7)")
                choice1=int(input("quel opion avez-vous choisit?"))
                if choice1==(1):
                    print("veuillez inserer un premier nombre")
                    jh=int(input("=====>"))
                    print("veuillez inserer un autre nombre")
                    ja=int(input("=====>"))
                    result=ja*jh
                    print(result)
                    while True:
                        print("veuillez inserer un autre nombre")
                        jb=int(input("=====>"))
                        result=result*jb
                        print(result)
                elif choice1==(2):
                    print("veuillez inserer une valeure de base")
                    aaa=int(input("====>"))
                    print("un nombre par le quelle vous voulez le diviser")
                    aba=int(input("=====>"))
                    result=aaa/aba
                    print(result)
                    while True:
                        print("veuillez entrer une valeure au quel le tout va etre divisé")
                        aca=int(input("====>"))
                        result=result/aca
                        print(result)
            
                elif choice1==(3):
                    value=0
                    while True:
                        print("veuillez inserer une valeur qui va s'ajouter au total de tous les chiffres entrés")
                        l=int(input("====>"))
                        value=value+l
                        print(value)
                elif choice1==(4):
                    print("veuillez inserer une premiere valeur:")
                    ag=int(input("=====>"))
                    print("veuillez inserer une valeure qui va etre enlevé a l'égalitée précédante:")
                    ah=int(input("=====>"))
                    result=ag-ah
                    print(result)
                    while True:
                        print("veuillez inserer une valeure qui va etre enlevé a l'égalitée précédante:")
                        ab=int(input("=====>"))
                        result=result-ab
                        print(result)
                elif choice1==(5):
                    print("veuillez inserer une valeure de base")
                    base=int(input("=====>"))
                    print("que voulez vous faire a ce nombre?")
                    while True:
                        print("multiplier(* ou x)")
                        print("diviser(/)")
                        print("additionner(+)")
                        print("soustraire(-)")
                        print("pour la version sans rappel des fontions:000")
                        choice=input("opération:")
                        if choice==("*") or choice ==("x"):
                            print("par quel nombre voulez vous multiplier",base,"?")
                            multiple=int(input("====>"))
                            base=base*multiple
                            print(base)
                        elif choice==("/"):
                            print("par quel nombre voulez-vous diviser",base,"?")
                            div=int(input("====>"))
                            base=base/div
                            print(base)
                        elif choice==("+"):
                            print("quel nombre voulez-vous ajouter a",base,"?")
                            add=int(input("=====>"))
                            base=base+add
                            print(base)
                        elif choice==("-"):
                            print("quel valeur voulez-vous soustraire a",base,"?")
                            soust=int(input("=====>"))
                            base=base-soust
                            print(base)
                        elif choice ==("000"):
                            while True:
                                choice=input("opération:")
                                if choice==("*"):
                                    print("par quel nombre voulez vous multiplier",base,"?")
                                    multiple=int(input("====>"))
                                    base=base*multiple
                                    print(base)
                                elif choice==("/"):
                                    print("par quel nombre voulez-vous diviser",base,"?")
                                    div=int(input("====>"))
                                    base=base/div
                                    print(base)
                                elif choice==("+"):
                                    print("quel nombre voulez-vous ajouter a",base,"?")
                                    add=int(input("=====>"))
                                    base=base+add
                                    print(base)
                                elif choice==("-"):
                                    print("quel valeur voulez-vous soustraire a",base,"?")
                                    soust=int(input("=====>"))
                                    base=base-soust
                                    print(base)
                elif choice1==(6):
                    while True:
                        aa=input("comment se nomme votre trangle?")
                        print("dans votre triangle",aa,",quel est l'hypoténus?")
                        ab=(input("=====>"))
            
                        print("dans",aa,"comment s'apelle le deuxieme coté dont vous connaissez la valeure?? ")
                        ad=input("=====>")
                        print("hypotenus==",ab)
                        print(" coté=",ad)
                        ba=input("est-ce correct?(oui:non)")
                        if ba=="oui":
                            print("quel est la longueur de",ab,"?")
                            ae=int(input("=====>"))
                            print("quel est la longueur de",ad,"?")
                            af=int(input("=====>"))
                            res=(ae*ae)+(af*af)
                            import math
                            fg=math.sqrt(res)
                            print(" la valeure manquante est",fg)
                
                



                        elif ba =="non":
                            print("vous allez etre redirigé...")
                        else:
                            print("nous n'avons pas compris votre demmande, vous allez etre redirigé...")
                elif choice1==(7):
                    while True:
                        aa = input("Comment s'appelle votre triangle ? ")
                        print("Dans votre triangle", aa, ", quel est la valeur du point n°1 ?")
                        ab = float(input("=====> "))
                        print("Dans votre triangle", aa, ", quel est la valeur du point n°2 ?")
                        ac = float(input("=====> "))
                        print("Dans votre triangle", aa, ", quel est la valeur du dernier point ?")
                        ad = float(input("=====> "))

                        print("Côté n°1 =", ab)
                        print("Côté n°2 =", ac)
                        print("Côté n°3 =", ad)

                        ba = input("Est-ce correct ? (oui/non) ")
                        if ba == "non":
                            print("Vous allez être redirigé...")
                        elif ba == "oui":
                            za = ab * ab
                            zb = ac * ac
                            zc = ad * ad
                            ez = ab * ab + ac * ac
                            if ez == zc:
                                print("La réciproque du théorème de Pythagore est validée. Le triangle", aa, "est bien rectangle.")
                        else:   
                            print("Le triangle", aa, "n'est pas rectangle.")
                    else:
                        print("Votre demande n'a pas été comprise.")

                        print("Loading...")
                elif choice1==(8):
                    print("désolé,la fonction est actuellement indisponnible")
            else:print("désolé, votre demmande n'a pas été comprise...")

    else:
        print("bienvennue dans Médianne")
        print("Nous somme Tres fières des vous présanter la version ALPHA de Médianne")
        print("voici les différantes options que Médianne propose actuellement:")
        print("=====> Médiamaths(1)")
        while True:
            choice0=int(input("quel option avez-vous choisit?:"))
            if choice0==(1):
                print("bienveunue dans Médiamaths Alpha")
                print("multiplications uniquement(1)")
                print("divisions uniquement(2)")
                print("aditions uniquement(3)")
                print("soustractions uniquement(4)")
                print("toutes les opérations comprises(5)")
                print("théorème de Pythagore(6)")
                print("réciproque du théorème de Pythagore(7)")
                choice1=int(input("quel opion avez-vous choisit?"))
                if choice1==(1):
                    print("veuillez inserer un premier nombre")
                    jh=int(input("=====>"))
                    print("veuillez inserer un autre nombre")
                    ja=int(input("=====>"))
                    result=ja*jh
                    print(result)
                    while True:
                        print("veuillez inserer un autre nombre")
                        jb=int(input("=====>"))
                        result=result*jb
                        print(result)
                elif choice1==(2):
                    print("veuillez inserer une valeure de base")
                    aaa=int(input("====>"))
                    print("un nombre par le quelle vous voulez le diviser")
                    aba=int(input("=====>"))
                    result=aaa/aba
                    print(result)
                    while True:
                        print("veuillez entrer une valeure au quel le tout va etre divisé")
                        aca=int(input("====>"))
                        result=result/aca
                        print(result)
            
                elif choice1==(3):
                    value=0
                    while True:
                        print("veuillez inserer une valeur qui va s'ajouter au total de tous les chiffres entrés")
                        l=int(input("====>"))
                        value=value+l
                        print(value)
                elif choice1==(4):
                    print("veuillez inserer une premiere valeur:")
                    ag=int(input("=====>"))
                    print("veuillez inserer une valeure qui va etre enlevé a l'égalitée précédante:")
                    ah=int(input("=====>"))
                    result=ag-ah
                    print(result)
                    while True:
                        print("veuillez inserer une valeure qui va etre enlevé a l'égalitée précédante:")
                        ab=int(input("=====>"))
                        result=result-ab
                        print(result)
                elif choice1==(5):
                    print("veuillez inserer une valeure de base")
                    base=int(input("=====>"))
                    print("que voulez vous faire a ce nombre?")
                    while True:
                        print("multiplier(* ou x)")
                        print("diviser(/)")
                        print("additionner(+)")
                        print("soustraire(-)")
                        print("pour la version sans rappel des fontions:000")
                        choice=input("opération:")
                        if choice==("*") or choice ==("x"):
                            print("par quel nombre voulez vous multiplier",base,"?")
                            multiple=int(input("====>"))
                            base=base*multiple
                            print(base)
                        elif choice==("/"):
                            print("par quel nombre voulez-vous diviser",base,"?")
                            div=int(input("====>"))
                            base=base/div
                            print(base)
                        elif choice==("+"):
                            print("quel nombre voulez-vous ajouter a",base,"?")
                            add=int(input("=====>"))
                            base=base+add
                            print(base)
                        elif choice==("-"):
                            print("quel valeur voulez-vous soustraire a",base,"?")
                            soust=int(input("=====>"))
                            base=base-soust
                            print(base)
                        elif choice ==("000"):
                            while True:
                                choice=input("opération:")
                                if choice==("*"):
                                    print("par quel nombre voulez vous multiplier",base,"?")
                                    multiple=int(input("====>"))
                                    base=base*multiple
                                    print(base)
                                elif choice==("/"):
                                    print("par quel nombre voulez-vous diviser",base,"?")
                                    div=int(input("====>"))
                                    base=base/div
                                    print(base)
                                elif choice==("+"):
                                    print("quel nombre voulez-vous ajouter a",base,"?")
                                    add=int(input("=====>"))
                                    base=base+add
                                    print(base)
                                elif choice==("-"):
                                    print("quel valeur voulez-vous soustraire a",base,"?")
                                    soust=int(input("=====>"))
                                    base=base-soust
                                    print(base)
                elif choice1==(6):
                    while True:
                        aa=input("comment se nomme votre trangle?")
                        print("dans votre triangle",aa,",quel est l'hypoténus?")
                        ab=(input("=====>"))
            
                        print("dans",aa,"comment s'apelle le deuxieme coté dont vous connaissez la valeure?? ")
                        ad=input("=====>")
                        print("hypotenus==",ab)
                        print(" coté=",ad)
                        ba=input("est-ce correct?(oui:non)")
                        if ba=="oui":
                            print("quel est la longueur de",ab,"?")
                            ae=int(input("=====>"))
                            print("quel est la longueur de",ad,"?")
                            af=int(input("=====>"))
                            res=(ae*ae)+(af*af)
                            import math
                            fg=math.sqrt(res)
                            print(" la valeure manquante est",fg)
                
                



                        elif ba =="non":
                            print("vous allez etre redirigé...")
                        else:
                            print("nous n'avons pas compris votre demmande, vous allez etre redirigé...")
                elif choice1==(7):
                    while True:
                        aa = input("Comment s'appelle votre triangle ? ")
                        print("Dans votre triangle", aa, ", quel est la valeur du point n°1 ?")
                        ab = float(input("=====> "))
                        print("Dans votre triangle", aa, ", quel est la valeur du point n°2 ?")
                        ac = float(input("=====> "))
                        print("Dans votre triangle", aa, ", quel est la valeur du dernier point ?")
                        ad = float(input("=====> "))

                        print("Côté n°1 =", ab)
                        print("Côté n°2 =", ac)
                        print("Côté n°3 =", ad)

                        ba = input("Est-ce correct ? (oui/non) ")
                        if ba == "non":
                            print("Vous allez être redirigé...")
                        elif ba == "oui":
                            za = ab * ab
                            zb = ac * ac
                            zc = ad * ad
                            ez = ab * ab + ac * ac
                            if ez == zc:
                                print("La réciproque du théorème de Pythagore est validée. Le triangle", aa, "est bien rectangle.")
                        else:   
                            print("Le triangle", aa, "n'est pas rectangle.")
                    else:
                        print("Votre demande n'a pas été comprise.")

                        print("Loading...")
                elif choice1==(8):
                    print("désolé,la fonction est actuellement indisponnible")
            else:print("désolé, votre demmande n'a pas été comprise...")
         
  
         
        
        