import pandas as pd # helps in data analysis and manipulate
import plotly.express as px # visualize the data

#pandas reads the csv file and stores it as a 
df = pd.read_csv("line_chart.csv")
fig = px.line( df , x = "Year" , y = "Per capita income" , color = "Country" , title = "PER CAPITA INCOME" )
fig.show()