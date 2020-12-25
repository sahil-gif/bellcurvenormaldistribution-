import pandas as pd
import plotly.figure_factory as ff
import csv as ff

df=pd.read_csv("data.csv")
fig=ff.create_distplot{[Phone_Result],["Result"]}
fig.show()
