from django.shortcuts import render, HttpResponse
from plotly.offline import plot
from plotly.graph_objs import Scatter

import yfinance as yf
from datetime import date
import plotly.graph_objects as go

# TODO:
# - Verify ticker symbol at page load
# - Un-hardcode start date for data
# - Add more info about companies from yfinance
# - Add animations on page load
# - Allow users to define date range for price graph
# - Integrate Database

def index(request):
    if request.method == 'POST':
        graph_id = request.POST.get('textfield', None)
        try:
            # Symbol of the ticker to be accessed and plotted
            symbol = graph_id

            # Gathering data on given symbol from yfinance
            ticker = yf.Ticker(symbol)

            '''
            info = None
            try:
                info = ticker.info
            except:
                return HttpResponse("no such ticker")
            '''

            df = ticker.history(period="1y")

            # Converts yf data from dictionary into dataframe
            df = df.reset_index()

            # Converting data into float64 to be plotted
            for i in ['Open', 'High', 'Close', 'Low']:
                df[i] = df[i].astype('float64')    

            # Edit the dimensions of the graph
            layout = go.Layout(
                #autosize=False,
                #width=1000,
                height=1000,)

            # Creates a candlestick graph_object figure using plotly
            plot_div1 = go.Figure(data=[go.Candlestick(x=df['Date'],
                        open=df['Open'],
                        high=df['High'],
                        low=df['Low'],
                        close=df['Close'])], 
                    layout=layout)

            # this line converts the go.figure() object into a plot() object so it can be
            # output as a div and natively displayed in the webpage without a new tab
            # needing to be opened
            plot_div = plot(plot_div1, output_type='div')

            # Sends info to templates/tutorial/index.html
            return render(request, "tutorial/index.html", 
                        context={'plot_div': plot_div, 
                        'symbol': symbol, 
                        'today_date': date.today().strftime("%m/%d/%Y"),})
        except:
            return HttpResponse("no such user")  
    else:
        return render(request, 'tutorial/index0.html')