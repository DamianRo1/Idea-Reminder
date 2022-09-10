#Physics conversion 2nd advance
def menu1():
    print ("Selecciona la categoría relevante")
    print ("")
    print ("1-Figuras Geométricas")
    print ("2-Dinámica")
    print ("3-Energía y Trabajo")
    print ("4-Poder e Impulso")
    
def mes1():
    print ("¿Qué necesita resolver?")
    print ("")
    


def mes2():
    print ("¿Qué valores tiene?")
    print ("")
    
def mes3():
    print ("Coming Soon")
    
def main():
    start=str(input())
    if start=="S":
        menu1()
        categ=int(input())
        if categ==1:
            print ("¿De cuál Figura?")
            print ("")
            print ("1-Triángulo")
            print ("2-Circunferencia")
            print ("3-Elipse")
            print ("4-Cono")
            print ("5-Esfera")
        elif categ==2:
            mes1()
            print ("1-Velocidad")
            print ("2-Aceleración")
            print ("3-Distancia")
            print ("4-Tiempo")
            print ("5-Fuerza")
            print ("6-Masa")
            unkn=int(input())
            if unkn ==1:
                mes2()
            elif unkn ==2:
                mes2()
            elif unkn ==3:
                mes2()
                print ("1-Km")
                print ("2-Velocidad y Tiempo")
                print ("3-Velocidad Inicial, Aceleración y Tiempo")
                print ("4-Velocidad Final, Aceleración y Tiempo")
                print ("5-Trabajo y Fuerza")
                fact=int(input())
                if fact==1:
                    for cont in range(1,10):
                        print (cont*1000)
                    
                elif fact==2:
                    mes3()
                elif fact==3:
                    mes3()
                elif fact==4:
                    mes3()
                elif fact==5:
                    mes3()
                else:
                    mes3()
            elif unkn ==4:
                mes2()
            elif unkn ==5:
                mes2()
            elif unkn ==6:
                mes2()
            else:
                mes3()
        elif categ==3:
            mes1()
        elif categ==4:
            mes1()
        else:
            mes3()
main()