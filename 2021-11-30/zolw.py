import turtle

def kwadrat(zolw, bok):
    for i in range(4):
        zolw.forward(bok)
        zolw.left(90)
        # x, y = zolw.pos()
        # print(x, y)

def szesciokat(zolw, bok):
    for i in range(6):
        zolw.forward(bok)
        zolw.left(60)

def slupek(zolw, wys, szerokosc_slupka):
    pass

def wykres_slupkowy(zolw, lista):
    for elem in lista:
        wys = elem * 100
        slupek(zolw, wys, 100)

def pentagram(zolw):
    pass

def spirala(zolw):
    pass

def lamana(zolw, lista_punktow):
    pass

def wielokat(zolw, lista_punktow): # tak jak lamana(), ale na koniec wraca na pozycję początkową
    pass

andrzej = turtle.Turtle()
andrzej.shape("turtle")

# andrzej.forward(100)
# andrzej.fd(100)
# andrzej.left(90)
# andrzej.fd(100)
# andrzej.left(90)
kwadrat(andrzej, 100)
szesciokat(andrzej, 200)
# lamana(andrzej, [(1, 2), (3, 4)])

turtle.exitonclick()