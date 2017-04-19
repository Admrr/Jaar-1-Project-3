from tkinter import *
import colors as c
from database import Database as d 
import grafieken as g
import matplotlib.pyplot as plt

tk = Tk()
tk.resizable(width=False, height=False)
tk.title("Data application")

width = 780
height = 720
canvas = Canvas(tk, width=width, height=height)
kaart = PhotoImage(file = "kaart4.gif")
canvas.create_image(405,355,image=kaart) #alles -500

class Standaard_Kaart:
    def __init__(self, area_color, text_color):
        self.Charlois =  Area(area_color,(341,409,359,428,419,411,415,463,407,465,407,480,445,515,471,549,425,547,377,565,377,579,328,581,274,559,301,549,312,533,301,528,299,509,331,437,317,431,318,413))
        self.charloisTxt = canvas.create_text(350,500,fill = text_color,text="Charlois")
        self.Delfshaven =  Area(area_color,(205,319,189,364,199,388,192,407,242,398,318,413,341,409,329,372,315,369,331,359,329,304))
        self.delfshavnTxt = canvas.create_text(250,360,fill = text_color,text="Delfshaven")
        self.Feijenoord =  Area(area_color,(431,333,417,337,381,383,341,409,359,428,419,411,415,463,407,465,407,480,445,515,469,490,491,490,497,465,467,403,479,395,469,348))
        self.feijenoordTxt = canvas.create_text(450,460,fill = text_color,text="Feijenoord")
        self.Hillegersberg_Schiebroek =  Area(area_color,(328,123,325,237,513,188,499,126,483,142,455,130,452,115,425,94,421,103,353,60))
        self.hillegersberg_schiebroekTxt = canvas.create_text(415,160,fill = text_color,text="Hillegersberg Schiebroek")
        self.Ijsselmonde =  Area(area_color,(548,396,493,411,479,395,467,403,497,465,491,490,469,490,445,515,471,549,516,554,549,542,605,511,611,519,621,513,641,404,583,389))
        self.ijsselmondeTxt = canvas.create_text(550,475,fill = text_color,text="Ijsselmonde")
        self.Kralingen_Crooswijk =  Area(area_color,(514,188,541,303,525,332,548,396,493,411,479,395,469,348,431,333,421,307,391,303,387,220))
        self.kralingen_crooswijkTxt = canvas.create_text(460,275,fill = text_color,text="Kralingen Crooswijk")
        self.Noord =  Area(area_color,(387,220,325,237,239,288,257,312,304,308,305,303,359,295,391,303))
        self.noordTxt = canvas.create_text(325,275,fill = text_color,text="Noord")
        self.Overschie =  Area(area_color, (103,129,131,122,137,137,237,73,284,133,315,109,328,123,325,237,239,288,259,314,205,319,178,269,206,233,200,230,169,244,143,215,133,228))
        self.overschieTxt = canvas.create_text(240,190,fill = text_color,text="Overschie")
        self.Prins_Alexander =  Area(area_color,(541,303,607,283,601,233,629,251,600,151,609,148,615,155,714,94,694,77,710,21,703,8,578,51,620,97,585,113,563,89,499,126))
        self.prins_alexanderTxt = canvas.create_text(560,170,fill = text_color,text="Prins Alexander")
        self.Centrum =  Area(area_color, (341,409,329,372,315,369,331,359,329,307,304,308,305,303,359,295,391,303,421,307,431,333,417,337,381,383))
        self.centrumTxt = canvas.create_text(360,350,fill = text_color,text="Centrum")
        self.button01 = Button(tk, text = "Criminaliteit 2009", command = create_average_crime_result_2009, bg = "white", fg = "black", width=24)
        self.button02 = Button(tk, text = "Criminaliteit 2011", command = create_average_crime_result_2011, bg = "white", fg = "black", width=24)
        self.button03 = Button(tk, text = "Diefstal 2009", command = create_diefstal_crime_result_2009, bg = "white", fg = "black", width=24)
        self.button04 = Button(tk, text = "Diefstal 2011", command = create_diefstal_crime_result_2011, bg = "white", fg = "black", width=24)
        self.button05 = Button(tk, text = "Drugsoverlast 2009", command = create_drugsoverlast_crime_result_2009, bg = "white", fg = "black", width=24)
        self.button06 = Button(tk, text = "Drugsoverlast 2011", command = create_drugsoverlast_crime_result_2011, bg = "white", fg = "black", width=24)
        self.button07 = Button(tk, text = "Geweld 2009", command = create_geweld_crime_result_2009, bg = "white", fg = "black", width=24)
        self.button08 = Button(tk, text = "Geweld 2011", command = create_geweld_crime_result_2011, bg = "white", fg = "black", width=24)
        self.button09 = Button(tk, text = "Inbraak 2009", command = create_inbraak_crime_result_2009, bg = "white", fg = "black", width=24)
        self.button10 = Button(tk, text = "Inbraak 2011", command = create_inbraak_crime_result_2011, bg = "white", fg = "black", width=24)
        self.button11 = Button(tk, text = "Vandalisme 2009", command = create_vandalisme_crime_result_2009, bg = "white", fg = "black", width=24)
        self.button12 = Button(tk, text = "Vandalisme 2011", command = create_vandalisme_crime_result_2011, bg = "white", fg = "black", width=24)
        self.button13 = Button(tk, text = "Overlast 2009", command = create_overlast_crime_result_2009, bg = "white", fg = "black", width=24)
        self.button14 = Button(tk, text = "Overlast 2011", command = create_overlast_crime_result_2011, bg = "white", fg = "black", width=24)
        self.button15 = Button(tk, text = "Vervuiling 2009", command = create_vervuiling_crime_result_2009, bg = "white", fg = "black", width=24)
        self.button16 = Button(tk, text = "Vervuiling 2011", command = create_vervuiling_crime_result_2011, bg = "white", fg = "black", width=24)
        self.button17 = Button(tk, text = "Verkeer 2009", command = create_verkeer_crime_result_2009, bg = "white", fg = "black", width=24)
        self.button18 = Button(tk, text = "Verkeer 2011", command = create_verkeer_crime_result_2011, bg = "white", fg = "black", width=24)
        self.button19 = Button(tk, text = "Marktparkeermogelijkheden", command = create_markt_result, bg = "white", fg = "black", width=24)
        self.button20 = Button(tk, text = "Concentratie metrostations", command = create_metro_result, bg = "white", fg = "black", width=24)
        self.button01.grid(row = 0, column = 0)
        self.button02.grid(row = 1, column = 0)
        self.button03.grid(row = 2, column = 0)
        self.button04.grid(row = 3, column = 0)
        self.button05.grid(row = 4, column = 0)
        self.button06.grid(row = 5, column = 0)
        self.button07.grid(row = 6, column = 0)
        self.button08.grid(row = 7, column = 0)
        self.button09.grid(row = 8, column = 0)
        self.button10.grid(row = 9, column = 0)
        self.button11.grid(row = 10, column = 0)
        self.button12.grid(row = 11, column = 0)
        self.button13.grid(row = 12, column = 0)
        self.button14.grid(row = 13, column = 0)
        self.button15.grid(row = 14, column = 0)
        self.button16.grid(row = 15, column = 0)
        self.button17.grid(row = 16, column = 0)
        self.button18.grid(row = 17, column = 0)
        self.button19.grid(row = 18, column = 0)
        self.button20.grid(row = 19, column = 0)

def numbers_crime_result(jaar, soort):
    resultaten = []
    for wijk in d.get_areas("criminaliteit"):
            a = wijk[0]
            result = d.get_crime_data(soort, jaar, ("'" + a + "'"))
            resultaten.append(result)
    
    global ch
    global fey
    global h_s
    global dlfs
    global kc
    global no
    global p_a
    global os
    global ij
    global ct

    ch = canvas.create_text(340,330, fill = "white",anchor = W, font = "Arial", text= str(resultaten[9]))
    fey = canvas.create_text(430,440, fill = "white",anchor = W, font = "Arial",text=str(resultaten[8]))
    h_s = canvas.create_text(395,140, fill = "white",anchor = W, font = "Arial",text=str(resultaten[7]))
    dlfs = canvas.create_text(230,340, fill = "white",anchor = W, font = "Arial",text=str(resultaten[6]))
    kc = canvas.create_text(440,255, fill = "white",anchor = W, font = "Arial",text=str(resultaten[5]))
    no = canvas.create_text(305,255, fill = "white",anchor = W, font = "Arial",text=str(resultaten[4]))
    p_a = canvas.create_text(520,150, fill = "white", anchor = W, font = "Arial",text= str(resultaten[3]))
    os = canvas.create_text(220,170, fill = "white",anchor = W, font = "Arial",text= str(resultaten[2]))
    ij = canvas.create_text(530,455, fill = "white",anchor = W, font = "Arial",text=str(resultaten[1]))
    ct = canvas.create_text(330,480, fill = "white",anchor = W, font = "Arial",text=str(resultaten[0]))

def numbers_metro_result():
    resultaten = []
    for wijk in d.get_areas("metro"):
            a = wijk[0]
            info = d.get_metro_info(("'" + a + "'"))[0]
            if info[1] != None:
                result = info[1]/info[0]
                result = result - (result % 0.01)                
            else:
                result = 0.00
            resultaten.append(result)

            #centrum, ijsselmonde, overschie, alex, noord, kralingen, delfs, hille, feije, charlois
    
    global ch
    global fey
    global h_s
    global dlfs
    global kc
    global no
    global p_a
    global os
    global ij
    global ct

    ch = canvas.create_text(340,330, fill = "white",anchor = W, font = "Arial", text= str(resultaten[0]))
    fey = canvas.create_text(430,440, fill = "white",anchor = W, font = "Arial",text=str(resultaten[8]))
    h_s = canvas.create_text(395,140, fill = "white",anchor = W, font = "Arial",text=str(resultaten[7]))
    dlfs = canvas.create_text(230,340, fill = "white",anchor = W, font = "Arial",text=str(resultaten[6]))
    kc = canvas.create_text(440,255, fill = "white",anchor = W, font = "Arial",text=str(resultaten[5]))
    no = canvas.create_text(305,255, fill = "white",anchor = W, font = "Arial",text=str(resultaten[4]))
    p_a = canvas.create_text(520,150, fill = "white", anchor = W, font = "Arial",text= str(resultaten[3]))
    os = canvas.create_text(220,170, fill = "white",anchor = W, font = "Arial",text= str(resultaten[2]))
    ij = canvas.create_text(530,455, fill = "white",anchor = W, font = "Arial",text=str(resultaten[1]))
    ct = canvas.create_text(330,480, fill = "white",anchor = W, font = "Arial",text=str(resultaten[9]))

def numbers_crime_result(jaar, soort):
    resultaten = []
    for wijk in d.get_areas("criminaliteit"):
            a = wijk[0]
            result = d.get_crime_data(soort, jaar, ("'" + a + "'"))
            resultaten.append(result)
    
    global ch
    global fey
    global h_s
    global dlfs
    global kc
    global no
    global p_a
    global os
    global ij
    global ct

    ch = canvas.create_text(340,330, fill = "white",anchor = W, font = "Arial", text= str(resultaten[0]))
    fey = canvas.create_text(430,420, fill = "white",anchor = W, font = "Arial",text=str(resultaten[8]))
    h_s = canvas.create_text(395,140, fill = "white",anchor = W, font = "Arial",text=str(resultaten[7]))
    dlfs = canvas.create_text(230,340, fill = "white",anchor = W, font = "Arial",text=str(resultaten[6]))
    kc = canvas.create_text(440,255, fill = "white",anchor = W, font = "Arial",text=str(resultaten[5]))
    no = canvas.create_text(305,255, fill = "white",anchor = W, font = "Arial",text=str(resultaten[4]))
    p_a = canvas.create_text(520,150, fill = "white", anchor = W, font = "Arial",text= str(resultaten[3]))
    os = canvas.create_text(220,170, fill = "white",anchor = W, font = "Arial",text= str(resultaten[2]))
    ij = canvas.create_text(530,455, fill = "white",anchor = W, font = "Arial",text=str(resultaten[1]))
    ct = canvas.create_text(330,480, fill = "white",anchor = W, font = "Arial",text=str(resultaten[9]))

def str_to_code(object, attr):
    return getattr(object, attr)

class crime_result:
    def __init__(self, main_screen, jaar, soort, cap):
        for wijk in d.get_areas("criminaliteit"):
            a = wijk[0]
            result = d.get_crime_data(soort, jaar, ("'" + a + "'"))
            canvas.itemconfig(str_to_code(main_screen, str(a)).shape, fill = c.rgb_to_hex(result, (255, 0 ,0), cap, False))

class markt_result:
    def __init__(self, main_screen):
        data = d.get_markt_data()
        for wijk in data:
            a = wijk[0]
            try:
                result = wijk[2]/wijk[1]
                canvas.itemconfig(str_to_code(main_screen, str(a)).shape, fill = c.rgb_to_hex(result, (0, 0, 255), 760, True))
            except(ZeroDivisionError):
                canvas.itemconfig(str_to_code(main_screen, str(a)).shape, fill = str_to_code(main_screen, str(a)).color)
            canvas.itemconfig(main_screen.Overschie.shape, fill = c.rgb_to_hex(1, (0, 0, 255), 1, False))


class metro_result:
    def __init__(self, main_screen):
        for wijk in d.get_areas("metro"):
            a = wijk[0]
            info = d.get_metro_info(("'" + a + "'"))[0]
            if info[1] != None:
                result = info[1]/info[0]
                canvas.itemconfig(str_to_code(main_screen, str(a)).shape, fill = c.rgb_to_hex(result, (0, 255, 0), 2, False))
            else:
                canvas.itemconfig(str_to_code(main_screen, str(a)).shape, fill = str_to_code(main_screen, str(a)).color)

def create_markt_result():
    remove_extra_images()
    markt_result(map)
    markten()

def create_average_crime_result_2009():
    remove_extra_images()
    tk.title("Criminaliteit Rotterdam")
    crime_result(map, "'2009'", "average", 20)
    politiebureau()
    numbers_crime_result("'2009'", "average")
    g.create_crime_graph("'2009'", "average")

def create_average_crime_result_2011():
    remove_extra_images()
    tk.title("Criminaliteit Rotterdam")
    crime_result(map, "'2011'", "average", 20)
    politiebureau()
    numbers_crime_result("'2011'", "average")
    g.create_crime_graph("'2011'", "average")

def create_diefstal_crime_result_2009():
    remove_extra_images()
    tk.title("Criminaliteit Rotterdam")
    crime_result(map, "'2009'", "diefstal", 25)
    politiebureau()
    numbers_crime_result("'2009'", "diefstal")
    g.create_crime_graph("'2009'", "diefstal")

def create_drugsoverlast_crime_result_2009():
    remove_extra_images()
    tk.title("Criminaliteit Rotterdam")
    crime_result(map, "'2009'", "drugsoverlast", 22)
    politiebureau()
    numbers_crime_result("'2009'", "drugsoverlast")
    g.create_crime_graph("'2009'", "drugsoverlast")

def create_geweld_crime_result_2009():
    remove_extra_images()
    tk.title("Criminaliteit Rotterdam")
    crime_result(map, "'2009'", "geweld", 9)
    politiebureau()
    numbers_crime_result("'2009'", "geweld")
    g.create_crime_graph("'2009'", "geweld")

def create_inbraak_crime_result_2009():
    remove_extra_images()
    tk.title("Criminaliteit Rotterdam")
    crime_result(map, "'2009'", "inbraak", 23)
    politiebureau()
    numbers_crime_result("'2009'", "inbraak")
    g.create_crime_graph("'2009'", "inbraak")

def create_vandalisme_crime_result_2009():
    remove_extra_images()
    tk.title("Criminaliteit Rotterdam")
    crime_result(map, "'2009'", "vandalisme", 22)
    politiebureau()
    numbers_crime_result("'2009'", "vandalisme")
    g.create_crime_graph("'2009'", "vandalisme")

def create_overlast_crime_result_2009():
    remove_extra_images()
    tk.title("Criminaliteit Rotterdam")
    crime_result(map, "'2009'", "overlast", 22)
    politiebureau()
    numbers_crime_result("'2009'", "overlast")
    g.create_crime_graph("'2009'", "overlast")

def create_vervuiling_crime_result_2009():
    remove_extra_images()
    tk.title("Criminaliteit Rotterdam")
    crime_result(map, "'2009'", "vervuiling", 35)
    politiebureau()
    numbers_crime_result("'2009'", "vervuiling")
    g.create_crime_graph("'2009'", "vervuiling")

def create_verkeer_crime_result_2009():
    remove_extra_images()
    tk.title("Criminaliteit Rotterdam")
    crime_result(map, "'2009'", "verkeer", 23)
    politiebureau()
    numbers_crime_result("'2009'", "verkeer")
    g.create_crime_graph("'2009'", "verkeer")

def create_diefstal_crime_result_2011():
    remove_extra_images()
    tk.title("Criminaliteit Rotterdam")
    crime_result(map, "'2011'", "diefstal", 25)
    politiebureau()
    numbers_crime_result("'2011'", "diefstal")
    g.create_crime_graph("'2011'", "diefstal")

def create_drugsoverlast_crime_result_2011():
    remove_extra_images()
    tk.title("Criminaliteit Rotterdam")
    crime_result(map, "'2011'", "drugsoverlast", 22)
    politiebureau()
    numbers_crime_result("'2011'", "drugsoverlast")
    g.create_crime_graph("'2011'", "drugsoverlast")

def create_geweld_crime_result_2011():
    remove_extra_images()
    tk.title("Criminaliteit Rotterdam")
    crime_result(map, "'2011'", "geweld", 9)
    politiebureau()
    numbers_crime_result("'2011'", "geweld")
    g.create_crime_graph("'2011'", "geweld")

def create_inbraak_crime_result_2011():
    remove_extra_images()
    tk.title("Criminaliteit Rotterdam")
    crime_result(map, "'2011'", "inbraak", 23)
    politiebureau()
    numbers_crime_result("'2011'", "inbraak")
    g.create_crime_graph("'2011'", "inbraak")

def create_vandalisme_crime_result_2011():
    remove_extra_images()
    tk.title("Criminaliteit Rotterdam")
    crime_result(map, "'2011'", "vandalisme", 22)
    politiebureau()
    numbers_crime_result("'2011'", "vandalisme")
    g.create_crime_graph("'2011'", "vandalisme")

def create_overlast_crime_result_2011():
    remove_extra_images()
    tk.title("Criminaliteit Rotterdam")
    crime_result(map, "'2011'", "overlast", 22)
    politiebureau()
    numbers_crime_result("'2011'", "overlast")
    g.create_crime_graph("'2011'", "overlast")

def create_vervuiling_crime_result_2011():
    remove_extra_images()
    tk.title("Criminaliteit Rotterdam")
    crime_result(map, "'2011'", "vervuiling", 35)
    politiebureau()
    numbers_crime_result("'2011'", "vervuiling")
    g.create_crime_graph("'2011'", "vervuiling")

def create_verkeer_crime_result_2011():
    remove_extra_images()
    tk.title("Criminaliteit Rotterdam")
    crime_result(map, "'2011'", "verkeer", 23)
    politiebureau()
    numbers_crime_result("'2011'", "verkeer")
    g.create_crime_graph("'2011'", "verkeer")

def create_metro_result():
    remove_extra_images()
    tk.title("Concentratie metrostations Rotterdam")
    metro_result(map)
    metro_stations()
    numbers_metro_result()

def metro_stations():
    global mimg
    mimg = PhotoImage(file = "metro.gif")
    global mlimg
    mlimg = PhotoImage(file = "Metro legenda.gif")
    for item in d.metro_coordinaten():
        canvas.create_image(item[0], item[1], image = mimg)
    canvas.create_image((width - (mlimg.width()/2)), (height - (mlimg.height()/2)), image = mlimg)

def politiebureau():
    global pimg 
    pimg = PhotoImage(file = "wouten.gif")
    global climg
    climg = PhotoImage(file = "Politiebureaus legenda.gif")
    for item in d.politie_coordinaten():
        canvas.create_image(item[0], item[1], image = pimg)
    canvas.create_image((width - (climg.width()/2)), (height - (climg.height()/2)), image = climg)
def markten():
    tk.title("Marktparkeermogelijkheden")
    global marimg
    marimg = PhotoImage(file = "Markt legenda.gif")
    global q2
    q2 = canvas.create_text(10, 680, anchor = W, font = "Arial", text = "Kans op gratis parkeren bij de markt")
    global maing
    maing = PhotoImage(file = "rsz_markt.gif")
    for item in d.markt_coordinaten():
        canvas.create_image(item[0], item[1], image = maing)
    canvas.create_image((width - (marimg.width()/2)), (height - (marimg.height()/2)), image = marimg)

def remove_extra_images():
    plt.close()
    try:
        pimg.__del__()
        climg.__del__()
        canvas.delete(q1)
    except(NameError):
        pass
    try:
        maing.__del__()
        marimg.__del__()
        canvas.delete(q2)
    except(NameError):
        pass
    try:
        mimg.__del__()
        mlimg.__del__()
        canvas.delete(q3)
    except(NameError):
        pass
    try:
        canvas.delete(ch)
        canvas.delete(p_a)
        canvas.delete(os)
        canvas.delete(no)
        canvas.delete(kc)
        canvas.delete(ij)
        canvas.delete(h_s)
        canvas.delete(fey)
        canvas.delete(dlfs)
        canvas.delete(ct)
    except(NameError):
        pass
        
class Area:
    def __init__(self,color,location):
        self.color = color 
        self.shape = canvas.create_polygon(location, fill=self.color, outline='black', width = 2)

map = Standaard_Kaart(c.grey(), "white")
def mainLoop():
    canvas.grid()
    canvas.grid(row=0, column=6,rowspan = 800)
    tk.mainloop() 

mainLoop()