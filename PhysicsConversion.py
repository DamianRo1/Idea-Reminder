#Physics conversion 2nd advance



print ("What do I need to convert from?")
print ("1-meters  2-kilometers")
ogunit=int(input())
print ("How many?")
if ogunit==1:
    amnt=int(input())
    print (amnt/1000 ,"kilometers")
elif ogunit ==2:
    amnt=int(input())
    print (amnt*1000 ,"meters")