import pandas as pd
import plotly.express as px
df=pd.read_csv("covid_1.csv")
#fig = px.scatter(df,x="date",y="cases",title="Covid Cases",color="country")
fig = px.scatter(df,x="date",y="cases",title="scatter",color="country")
fig.show()
