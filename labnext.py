from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import math

win = Tk()
win.config(bg="blue")

win.geometry("700x320")

def syracuse():
    multiplicateur = 0
    multmoins1 = 0
    multmoins1_2 = 0
    listgraphy = []
    t2 = 0
    list_t2 = []
    func_listx = []
    func_listb = []
    volval_list = []
    croiselist = []
    s1 = 0
    s2 = 0
    a = 0
    b = 0
    t = -1
    diff = 0
    xsomme = 0
    xsomme2 = 0
    ysomme = 0
    ysomme2 = 0
    lissage = 0
    listxrond = []
    listxrond2 = []
    listyrond = []
    listyrond2 = []
    tbis = 0
    tbis2 = 0
    t_max = 0
    vol_max = 0
    volval_nmoins1 = 0
    croisement = 1
    croisementbis = 0
    volmax2 = 0
    passagemax = 0
    valeurfincroisement = 1
    s2bis = 0
    s1bis = 0
    volval = int(a2.get())
    valeurdefin = int(b2.get())
    back = str(c2.get())
    volvaldebut = volval
    volvaldebut2 = str(volvaldebut)
    while volval != valeurdefin:
        t = t + 1
        listgraphy.insert(t, volval)
        volval_nmoins1 = volval
        volval_list.insert(t, volval)
        if volval < valeurdefin:
            valeurfincroisement = valeurfincroisement + 2
        if volval % 2 == 0 or volval == 2:
            volval = volval / 2
        else:
            volval = volval * 3 + 1
        a = volval - volval_nmoins1
        b = volval_nmoins1 - a * t
        func_listx.insert(t, a)
        func_listb.insert(t, b)
        if volval < volvaldebut:
            if croisementbis != 1 and t > 0:
                s2 = s2 + (abs(volval - volvaldebut) * (1 - (((volvaldebut - b) / a) - t)) / 2)
                s1 = s1 + (abs(volvaldebut - volval_nmoins1) * (((volvaldebut - b) / a) - t)) / 2
                croisement = croisement + 1
                croisementbis = 1
            else:
                if t > 0:
                    s2 = s2 + (abs(volval_nmoins1 - volval) / 2) + (abs(volval - volvaldebut))
                else:
                    s2 = s2 + (abs(volval_nmoins1 - volval) / 2)
                croisementbis = 1
        if volval > volvaldebut:
            if croisementbis != 2 and t > 0:
                s1 = s1 + (abs(volval - volvaldebut) * (1 - (((volvaldebut - b) / a) - t)) / 2)
                s2 = s2 + (abs(volvaldebut - volval_nmoins1) * (((volvaldebut - b) / a) - t)) / 2
                croisement = croisement + 1
                croisementbis = 2
            else:
                if t > 0:
                    s1 = s1 + abs(volval_nmoins1 - volval) / 2 + (abs(volval - volvaldebut))
                else:
                    s1 = s1 + abs(volval_nmoins1 - volval) / 2
                croisementbis = 2
        while tbis < len(volval_list):
            if volval > volval_list[tbis]:
                tbis2 = tbis2 + 1
            tbis = tbis + 1
        if tbis2 == len(volval_list):
            passagemax = 1
            t_max = t
            vol_max = volval
        tbis = 0
        tbis2 = 0

    a = volval - volval_nmoins1
    b = volval_nmoins1 - a * t
    func_listx.insert(t, a)
    func_listb.insert(t, b)

    if passagemax == 0:
        t_max = 0
        vol_max = volvaldebut
    if t / vol_max <= 0:
        lissage = 1 / ((3 * (t / vol_max)) / 0.01)
    else:
        lissage = 1

    diff = 1 / (t_max + (0.25 * (t * lissage / vol_max)) - (t_max - (0.25 * (t / vol_max))))

    multiplicateur = diff * 4.5 * (t / 100)
    multmoins1 = multiplicateur - 1
    multmoins1_2 = multmoins1 / (t / 100) * lissage

    xsomme = t_max - ((t / 100) * (t / vol_max)) * (multmoins1_2 / 2) + passagemax
    ysomme = vol_max
    ysomme2 = vol_max

    fig = plt.figure()

    fig.patch.set_facecolor(back)

    ax = fig.add_subplot(111)
    ax.patch.set_facecolor(back)

    plt.grid()

    s2 = str(s2)

    t2 = 1
    t2bis = 1

    while t2 < 100:
        if t2 == 1:
            listxrond.insert(0, xsomme)
            listyrond.insert(0, ysomme)
        if t2 <= 50:
            ysomme = ysomme + (math.pi / 50) * (1 / t2) * multiplicateur
            listyrond.insert(t2, ysomme)
        else:
            ysomme = ysomme - (math.pi / 50) * (1 / t2bis) * multiplicateur
            listyrond.insert(t2, ysomme)
            t2bis = t2bis + 1
        xsomme = xsomme + (((t / 100) * (t / vol_max)) / 50) * (multmoins1_2 / 2)
        listxrond.insert(t2, xsomme)
        t2 = t2 + 1
    t2 = 0

    while t2 < 99:
        if t2 < 50:
            if t2 == 0:
                plt.plot([listxrond[t2 + 1], listxrond[t2 + 1]], [listyrond[t2 + 1], listyrond[50 + t2] - 0.25 *
                                                                  multiplicateur],
                         color="red")
            if t2 > 0:
                plt.plot([listxrond[t2], listxrond[t2 + 1]], [listyrond[49 + t2] - 0.25 * multiplicateur,
                                                              listyrond[50 + t2] - 0.25 * multiplicateur], color="red")
                plt.plot([listxrond[t2], listxrond[t2 + 1]], [listyrond[t2], listyrond[t2 + 1]], color="red")
        else:
            plt.plot([listxrond[t2], listxrond[t2 + 1]], [listyrond[99 - t2], listyrond[98 - t2]], color="red")
            if t2 == 98:
                plt.plot([listxrond[t2], listxrond[t2 + 1]], [listyrond[50 - t2] - 0.25 * multiplicateur,
                                                              listyrond[49 - t2] - 0.25 * multiplicateur],
                         color="red")
                plt.plot([listxrond[t2 + 1], listxrond[t2 + 1]], [listyrond[49 - t2] - 0.25 * multiplicateur, vol_max],
                         color="red")
            else:
                plt.plot([listxrond[t2], listxrond[t2 + 1]], [listyrond[50 - t2] - 0.25 * multiplicateur,
                                                              listyrond[49 - t2] - 0.25 * multiplicateur],
                         color="red")
        t2 = t2 + 1

    t2 = 0

    croisement = str(croisement)
    valeurfincroisement = str(valeurfincroisement)

    while t2 < t:
        list_t2.insert(t2, t2)
        list_t2.insert(t2 + 1, t2 + 1)
        plt.plot([list_t2[t2], list_t2[t2 + 1]], [[volvaldebut], [volvaldebut]], "r--")
        plt.plot([list_t2[t2], list_t2[t2 + 1]], [valeurdefin, valeurdefin], "k--")
        plt.plot([list_t2[t2], list_t2[t2 + 1]], [listgraphy[t2], listgraphy[t2 + 1]], "b", marker="*")
        if t2 == 0:
            plt.plot([list_t2[t2], list_t2[t2]], [listgraphy[t2], listgraphy[t2]], "m--", marker="*", label=croisement)
            plt.plot([list_t2[t2], list_t2[t2]], [valeurdefin, valeurdefin], "k--", marker="*",
                     label=valeurfincroisement)
        x = np.arange(t2, t2 + 1, 0.001)

        def f1(x):
            return volvaldebut

        def f2(x):
            return func_listx[t2] * x + func_listb[t2]

        y1 = f1(x)
        y2 = f2(x)
        plt.fill_between(x, y1, y2, where=y1 > y2, color=(0.1, 0.5, 0.8))
        plt.fill_between(x, y1, y2, where=y1 < y2, color='g')
        t2 = t2 + 1
    x = np.arange(t2, t2 + 1, 0.001)

    def f1(x):
        return 0 * x + volvaldebut

    def f2(x):
        return func_listx[t2 + 1] * x + func_listb[t2 + 1]

    y1 = f1(x)
    y2 = f2(x)
    plt.fill_between(x, y1, y2, where=y1 > y2, color=(0.1, 0.5, 0.8), label=s2)
    plt.fill_between(x, y1, y2, where=y1 < y2, color='g', label=s1)
    plt.plot([t, t + 1], [valeurdefin, valeurdefin], "k--", label="Valeur de fin choisie")
    plt.plot([t, t + 1], [[volvaldebut], [volvaldebut]], "r--", label="Valeur de départ")
    plt.plot([t, t + 1], [listgraphy[t2], valeurdefin], "b", marker="*", label="Valeurs de la suite")
    plt.title("Visualisation de la suite de Syracuse")
    plt.xlabel("Numéro d'opération")
    plt.ylabel("Valeur de la suite")
    plt.legend()
    plt.show()
    plt.close()

Label(win, text="Veuillez choisir un vol de départ (3 est le minimum)", font=('Calibri 20'), bg="blue",
      fg="white").pack()
a2 = Entry(win, width=5)
a2.pack()
Label(win, text="Choisissez votre valeur de fin entre 1 ; 2 ou 4", font=('Calibri 20'), bg="blue", fg="white").pack()
b2 = Entry(win, width=5)
b2.pack()
Label(win, text="Quelle couleur de fond?",
      font=('Calibri 20'), bg="blue", fg="white").pack()
c2 = Entry(win, width=5)
c2.pack()


Button(win, text="COMMENCER", command=syracuse, bg="yellow").pack()

n2 = Entry(win, width=5)

nom = Label(win, text="", font=('Calibri 15'), bg="blue", fg="#2F2B40")
nom.pack()

nom2 = Label(win, text="", font=('Calibri 15'), bg="blue", fg="#2F2B40")
nom2.pack()

win.mainloop()
