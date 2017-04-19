from database import Database as d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['toolbar'] = 'None'

class create_crime_graph:
    def __init__(self, jaar, soort):
        N = 10
        crime = []
        police = []
        for wijk in d.get_areas("criminaliteit"):
            a = wijk[0]
            result = d.get_crime_data(soort, jaar, ("'" + a + "'"))
            crime.append(result)
            bureaus = d.get_police_data(("'" + a + "'"))
            police.append(bureaus)
        tuple_result = tuple(crime)
        tuple_police = tuple(police)
        ind = np.arange(N)
        width = 0.35
        fig, ax = plt.subplots()
        rects1 = ax.bar(ind, tuple_result, width, color = "r")
        rects2 = ax.bar(ind + width, tuple_police, width, color = "b")
        ax.set_ylabel("% criminaliteit/het aantal politiebureaus")
        ax.set_title("Percentage " + str(soort) + " criminaliteit + aantal politiebureaus " + str(jaar))
        ax.set_xticks(ind + width / 2)
        maxheight = 0
        for rect in rects1:
            a = rect.get_height()
            if maxheight < a:
                maxheight = a
            else:
                maxheight = maxheight
        ax.set_ylim([0,(maxheight + 8)])
        volgorde = []
        for wijk in d.get_areas("criminaliteit"):
            if wijk[0] == "Noord":
                volgorde.append("Noord     ")
            elif len(wijk[0]) <= 10:
                volgorde.append(wijk[0])
            else:
                short = ""
                for c in wijk[0]:
                    if len(short) <= 10:
                        short += c
                    else:
                        short += "..." 
                        break
                volgorde.append(short)
               
        ax.set_xticklabels(tuple(volgorde), rotation = 25)
        ax.legend((rects1[0], rects2[0]), ("Percentage criminaliteit", "Aantal politiebureaus"))

        def autolabel(rects):
            for rect in rects:
                height = float(rect.get_height()) 
                ax.text(rect.get_x() + rect.get_width()/2., height, '%d' % float(height), ha='center', va='bottom')

        plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)
        autolabel(rects1)
        autolabel(rects2)
        plt.show()