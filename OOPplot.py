import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates 

class plot:
    def plotStyle(self,style):
        plt.style.use(style)
        
    def inFile(self,filename):
        self.data=pd.read_csv(filename)
        
    def dataSet(self):
        self.data['country_code']=pd.to_datetime(self.data['country_code'])
        self.data.sort_values('country_code', inplace=True)
        
    def dataLabel(self):
        self.case_active = self.data['active_cases']
        self.country_date = self.data['country_code']

    def plotParameters(self):
        plt.plot_date(self.country_date, self.case_active,'k-')
        
    def axisLabel(self,x,y):
        plt.xlabel(x)
        plt.ylabel(y)
        
    def plot(self,filename):
        plt.tight_layout()
        plt.savefig(filename)
        plt.show()
        
