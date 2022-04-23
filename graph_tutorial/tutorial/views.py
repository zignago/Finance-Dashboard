from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter

import yfinance as yf
from datetime import datetime
import plotly.graph_objects as go

def index(request):

    msft = yf.Ticker("MSFT")
    df = msft.history(period="1y")

    df = df.reset_index()

    for i in ['Open', 'High', 'Close', 'Low']:
        df[i] = df[i].astype('float64')    

    '''#data to be plotted
    x_data = [0,1,2,3,4,8] #for yfinance - date
    y_data = [9,2,3,0,11,8] #for yfinance - price

    #plotting the data
    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')'''
    
    fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

    fig.show()
    
    #rendering data
    #return render(request, "tutorial/index.html", context={'plot_div': plot_div})
    return render(request, "tutorial/index.html", context={'fig': fig})