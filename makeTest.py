import pandas as pd
from collections import defaultdict
from openpyxl import load_workbook
import random 

egypt = ['Port Said', 'Sohag', 'Suez', 'Red Sea', 'Luxor', 'Beni Suef', 'Kafr El Sheikh', 'Dakahlia', 'Helwan', 'Aswan', 'Faiyum', 'Gharbia', 'South Sinai', 'Monufia', 'Matrouh', 'Qalyubia', 'Sharqia', 'Qena', 'Beheira', 'Alexandria', 'Damietta', 'Cairo', 'Giza', 'Asyut', 'North Sinai', 'New Valley', 'Ismailia', 'Minya']
cities_costs = dict()
try:
    dataset = pd.read_excel('Costs.xlsx')
    for f, t, c in zip(dataset['From'], dataset['To'], dataset['Cost']):
        cities_costs[f'{f}-{t}'] = c
except:
    cities_costs = None