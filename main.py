"""#### Fonctions secondaires
fonction permettant d'avoir le temps de vols, le temps de vol en altitude et le temps vol mximal 
puis afficher la liste syracuse grace un graphique
"""

# imports
from plotly.graph_objects import Scatter, Figure
### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """permet de metre en grphique la suite de syracuse"""
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )
    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')

#######################
def syracuse_l(n):
    """retourne la suite de Syracuse de source n
    Args:
        n (int): la source de la suite
    Returns:
        list: la suite de Syracuse de source n
    """
    # votre code ici
    tv = 0
    l = []
    l.append(n)
    while n != 1 :
        if n % 2 == 0:
            n= n/2
            l.append(n)
        else:
            n= n*3+1
            l.append(n)
        tv+=1
    return l
def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse
    Args:
        l (list): la suite de Syracuse
    Returns:
        int: le temps de vol
    """
    # votre code ici
    n = len(l)-1
    return n

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse
    Args:
        l (list): la suite de Syracuse
    Returns:
        int: le temps de vol en altitude
    """
    # votre code ici
    for i in range(len(l)-1):
        #print(l[i])
       # print( l[i] < l[0])
        if l[i] < l[0]:
            return i-1
    return 0

def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse
    Args:
        l (list): la suite de Syracuse
    Returns:
        int: l'altitude maximale
    """
    # votre code ici
    n = l[0]
    for i in range(len(l)-1):
        if l[i] > n:
            n=l[i]
    return n


#### Fonction principale


def main():
    """fonction principale pour appller les autre fonction secondaire"""
    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    print(lsyr)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
