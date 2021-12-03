import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv("dataset/Drinkstodisplay.csv")

df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

new_df = df.groupby(['Drink_Name']).agg(
    {'Unit_Price': 'sum', 'Case_Price': "sum"}).reset_index()

new_df = new_df.sort_values(by=['Unit_Price'], ascending=[False])

trace1 = go.Bar(x=new_df['Drink_Name'], y=new_df['Unit_Price'], name='Unit Price', marker={'color': '#CD7F32'})
trace2 = go.Bar(x=new_df['Drink_Name'], y=new_df['Case_Price'], name='Case Price', marker={'color': '#9EA0A1'})
data = [trace1, trace2]

layout = go.Layout(title='Prices of the most popular drinks in the United States', xaxis_title="Drink Names",
                   yaxis_title="Prices of Drinks in U.S. Dollars", barmode='stack')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='Price_Displayer.html')




