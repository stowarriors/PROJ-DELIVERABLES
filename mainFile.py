from OOPbigquery import dataEx
from OOPplot import plot

def main():
    d = dataEx()
    d.query()
    d.queryId('Covid-2e75a41f090d.json')
    d.dataFrame()
    d.csvSave('datas.csv')
    
    p = plot()
    p.plotStyle('seaborn')
    p.inFile('datas.csv')
    p.dataSet()
    p.dataLabel()
    p.plotParameters()
    p.axisLabel('Date', 'Active Cases')
    p.plot('graph.pdf')

if __name__ == "__main__":
    main()
