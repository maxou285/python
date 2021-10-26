import turtle

t = turtle.Turtle()

def escalier(taille, nbmarche):
    for i in range(0, nbmarche):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
        taille = taille - 5
#escalier(50, 10)


nbcote = 4

turtle.pencolor("brown")                # Ne met pas la couleur du tracé à brown mais seulement la turtle elle meme
def carre(coté):
    for i in range(0, nbcote):
        t.forward(coté)
        t.left(90)

def carres(taille_de_depart, nbdecarres):
    for i in range(0,nbdecarres):
        carre(taille_de_depart * (i+1))

carres(10,10)
#carre(50)

turtle.fillcolor("violet") # Remplit la turtle pas le carré

turtle.done()

