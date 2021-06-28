import pandas as pd
import csv
import plotly.graph_objects as pg

data = pd.read_csv("data.csv")
sum = 0 

attempt = data["attempt"].tolist()
def Mean():
    for x in attempt:
        global sum
        sum = sum + int(x)
    
    mean = sum/len(attempt)
    print(mean)

#Mean()
#print(data.groupby("level")["attempt"].mean())

"""figure = pg.Figure(pg.Bar(
    x = data.groupby("level")["attempt"].mean(),
    y = ["Level 1","Level 2","Level 3","Level 4"],
    orientation = "h"
))
"""
#figure.show()

studentData = data.loc[data["student_id"] == "TRL_xsl"]

Graph = pg.Figure(pg.Bar(
    x = studentData.groupby("level")["attempt"].mean(),
    y = ["Level 1", "Level 2", "Level 3", "Level 4"],
    orientation = "h"
))

Graph.show()