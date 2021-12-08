import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

#Load the data
df = pd.read_csv('dataset/Alcohol_Prices.csv')

#Filter Out the rest of the sizes
df = df[(df['Size'] != '750 ML') & (df['Size'] != '200 ML') & (df['Size'] != '375 ML') & (df['Size'] != 'LITER') & (df['Size'] != '1.75 L')]
       
#Prep Data and Set Marker Size
data =[ 
       go.Scatter(x=df['Proof'],
               y=df['Unit Price'],
               text=df['Drink Name'],
                mode = 'markers',
                marker_size= 25)
                ]
    
# Preparing layout
layout = go.Layout(title='Unit Price of Brands Based on Alcohol Proof for 50 ML botlles', xaxis_title="Proof",
                   yaxis_title="Unit Price", hovermode='closest')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='cluster_graph.html')

