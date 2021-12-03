import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# first must CLEANSE the data
df = pd.read_csv("dataset/monthly_alpha_price_list_c.csv")

df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

new_df = df.groupby(['Drink_Name']).agg(
    {'Unit_Price': 'sum', 'Case_Price': "sum"}).reset_index()

new_df = new_df.sort_values(by=['Unit_Price'], ascending=[False]).tail(25).reset_index()

trace1 = go.Bar(x=new_df['Drink_Name'], y=new_df['Unit_Price'], name='Unit Price', marker={'color': '#CD7F32'})
trace2 = go.Bar(x=new_df['Drink_Name'], y=new_df['Case_Price'], name='Case Price', marker={'color': '#9EA0A1'})
data = [trace1, trace2]

layout = go.Layout(title='Prices of the most popular drinks in the United States that are the least expensive', xaxis_title="Drink Names",
                   yaxis_title="Prices of Drinks in U.S. Dollars", barmode='stack')


fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='Top25_Least_Expensive.html')
