from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter

import yfinance as yf
from datetime import datetime
import plotly.graph_objects as go

def index(request):

    symbol = "PLTR"
    ticker = yf.Ticker(symbol)
    df = ticker.history(period="1y")

    df = df.reset_index()

    #converting data into float64 to be plotted
    for i in ['Open', 'High', 'Close', 'Low']:
        df[i] = df[i].astype('float64')    

    #plotting the data
    plot_div1 = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])],)

    # this line converts the go.figure() object into a plot() object so it can be
    # output as a div and natively displayed in the webpage without a new tab
    # needing to be opened
    plot_div = plot(plot_div1, output_type='div')

    return render(request, "tutorial/index.html", context={'plot_div': plot_div, 'title': symbol})