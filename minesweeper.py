import tkinter, configparser, random, os, tkinter.messagebox, tkinter.simpledialog

window = tkinter.Tk()

window.title("Minesweeper")

#prepare default values

rows = 10
cols = 10
mines = 10

field = []
buttons = []

colors = ['#FFFFFF', '#0000FF', '#008200', '#FF0000', '#000084', '#840000', '#008284', '#840084', '#000000']

gameover = False
customsizes = []


def createMenu():
    menubar = tkinter.Menu(window)
    menusize = tkinter.Menu(window, tearoff=0)
    menusize.add_command(label="small (10x10 with 10 mines)", command=lambda: setSize(10, 10, 10))
    menusize.add_command(label="medium (20x20 with 40 mines)", command=lambda: setSize(20, 20, 40))
    menusize.add_command(label="big (35x35 with 120 mines)", command=lambda: setSize(35, 35, 120))
    menusize.add_command(label="custom", command=setCustomSize)
    menusize.add_separator()
    for x in range(0, len(customsizes)):
        menusize.add_command(label=str(customsizes[x][0])+"x"+str(customsizes[x][1])+" with "+str(customsizes[x][2])+" mines", command=lambda customsizes=customsizes: setSize(customsizes[x][0], customsizes[x][1], customsizes[x][2]))
    menubar.add_cascade(label="size", menu=menusize)
    menubar.add_command(label="exit", command=lambda: window.destroy())
    window.config(menu=menubar)


