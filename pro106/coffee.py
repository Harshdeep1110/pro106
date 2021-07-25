import csv 
import plotly.express as px
import numpy as np

def getDataSource(path):
    x =[]
    y =[]

    with open(path) as f:
        reader = csv.DictReader(f)

        for i in reader:
            x.append(float(i['Coffee in ml']))
            y.append(float(i['sleep in hours']))

    return {'x':x,'y':y}

def findCorrelation(data):
    correlation = np.corrcoef(data['x'],data['y'])
    print("The correlation is",correlation[0][1])

def main():
    path = 'csv/coffee.csv'
    data = getDataSource(path)
    findCorrelation(data)

main()