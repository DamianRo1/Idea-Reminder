#Physics conversion 6th and 7th advance
def menu1():
    print ("Selecciona la categoría relevante")
    print ("")
    listmenu1= ['1-Figuras Geométricas',
                '2-Dinámica',
                '3-Energía y Trabajo',
                '4-Poder e Impulso']
    print (listmenu1)
    
def mes1():
    print ("¿Qué necesita resolver?")
    print ("")
    


def mes2():
    print ("¿Qué valores tiene?")
    print ("")
    
def mes3():
    print ("Coming Soon")

def fullmenu(option):
    fullmenulist=[['1-Figuras Geométricas, 2-Dinámica, 3-Energía y Trabajo, 4-Poder e Impulso'],['1-Triangulo, 2-Circunferencia, 3-Elipse'],['Velocidad','Aceleración','Distancia','Tiempo','Fuerza','Masa'],[],[]]
    print (fullmenulist[option])



def main():
    start=str(input())
    if start=="S":
        fullmenulist=[['1-Figuras Geométricas, 2-Dinámica, 3-Energía y Trabajo, 4-Poder e Impulso'],['1-Triangulo, 2-Circunferencia, 3-Elipse'],['Velocidad','Aceleración','Distancia','Tiempo','Fuerza','Masa'],[],[]]
        print ("full menu?")
        fullmenuanswer=str(input("y/n?"))
        if (fullmenuanswer=="y"):
            print (fullmenulist[0])
            fmcat=int(input(""))
            fullmenu(fmcat)
        else:
            menu1()
            qs==False
            categ=int(input())
            if categ==1:
                print ("¿De cuál Figura?")
                print ("")
                listcateg1=["1-Triángulo", "2-Circunferencia", "3-Elipse","4-Cono", "5-Esfera"]
            elif categ==2:
                mes1()
                listcateg2=["1-Velocidad", "2-Aceleración", "3-Distancia", "4-Tiempo", "5-Fuerza", "6-Masa"]
                unkn=int(input())
                if unkn ==1:
                    mes2()
                elif unkn ==2:
                    mes2()
                elif unkn ==3:
                    mes2()
                    listunkn2_3=["1-Km", "2-Velocidad y Tiempo", "3-Velocidad Inicial, Aceleración y Tiempo", "4-Velocidad Final, Aceleración y Tiempo", "5-Trabajo y Fuerza"]
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