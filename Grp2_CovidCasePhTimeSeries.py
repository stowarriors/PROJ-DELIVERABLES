import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates 

plt.style.use('seaborn')

data=pd.read_csv('data.csv')

data['country_code']=pd.to_datetime(data['country_code'])
data.sort_values('country_code', inplace=True)


case_active = data['active_cases']
country_date = data['country_code']

plt.plot_date(country_date, case_active,'k-')




plt.xlabel('Date')
plt.ylabel('Active Cases')


plt.tight_layout()
plt.savefig("PhilippinesActiveCases.pdf")
plt.show()