# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 23:29:49 2020

@author: saiteja pasunuti
"""

#pip install lifelines
#lifelines is a complete survival analysis library
import lifelines
from lifelines.datasets import load_waltons

import pandas as pd
#pandas is used for data manipulation

# Loading the the survival un-employment data
patient = pd.read_csv("D:/360digiTMG/unsupervised/mod25 survival analytics/Patient/Patient.csv")
patient.head()
patient.describe()


# followup is referring to time 
T = patient.Followup

# Importing the KaplanMeierFitter model to fit the survival analysis
from lifelines import KaplanMeierFitter

# Initiating the KaplanMeierFitter model
kmf = KaplanMeierFitter()

# Fitting KaplanMeierFitter model on Time and Events for death 
kmf.fit(T,event_observed=patient.Eventtype)

# Time-line estimations plot 
kmf.plot()

patient.Scenario.value_counts()


# Applying KaplanMeierFitter model on Time and Events for the Scenario "A"
kmf.fit(T[patient.Scenario=="A"], patient.Eventtype[patient.Scenario=="A"], label='A')
ax = kmf.plot()

##############################################################################

