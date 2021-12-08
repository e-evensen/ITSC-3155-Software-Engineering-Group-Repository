import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('dataset/ingredients.csv')

# Removing empty spaces from State column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

df=df.sort_values(by='Prices', ascending = False)

# Preparing data
data = [go.Bar(x=df['Ingredients'], y=df['Prices'])]

# Preparing layout
layout = go.Layout(title='Top 20 Drink Ingredients and How Much you Should Pay For Them', xaxis_title="Ingredient Name",
                   yaxis_title="Prices")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bar.html')
 
 

