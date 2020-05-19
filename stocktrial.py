from flask import Flask, render_template, request
import pandas as pd
from bokeh.plotting import figure,show
from bokeh.resources import CDN
from bokeh.embed import file_html, components

app = Flask(__name__)

companies = [ 'T', 'NFLX']

def retrieve_prices(ticker, option = 'compact'):
  '''
  
  
  '''

 url = 'https://www.alphavantage.co/query?
function=TIME_SERIES_DAILY' \
    + '&symbol=' + ticker \
    + '&apikey= SX223MXD7CFJ2YDW' \
    + '&outputsize=' + option \
    + '&datatype=csv'
data = pd.read_csv(url, usecols=['timestamp', 'close'])
data['timestamp'] = pd.to_datetime(data['timestamp'])
data = data.rename({'timestamp' : 'date'}, axis = 'columns')
return data


def make_plot(data,company):
    '''

    '''
p = figure(#plot_width = 500, 
           #plot_height = 300, 
x_axis_type = 'datetime', 
title = company + ' closing stock price')
p.xaxis.axis_label = 'Date'
p.yaxis.axis_label = 'Price'
p.background_fill_alpha = 0
p.border_fill_alpha = 0
p.ygrid.grid_line_color = 'black'
p.ygrid.grid_line_alpha = 0.3
p.xgrid.grid_line_color = 'black'
p.xgrid.grid_line_alpha = 0.3
p.line(data['date'], data['close'])
script, div = components(p)
return script, div


@app.route('/')
def index():
    #Retreive company and data size selections from template
    current_company = request.args.get('company')
    full = request.args.get('full')
    # Set default company selection
    if current_company == None:
        current_company = 'T'  
    # Make API call based on selections and generate Bokeh information

    if full:
        data = retrieve_prices(current_company, option = 'full')
    else:
        data = retrieve_prices(current_company, option = 'compact')
    script, div = make_plot(data, current_company) 
    # Create template with Bokeh plot
    return render_template('index.html', script = script, div = div,
    companies = companies, current_company = current_company)

if __name__ == '__main__':
    app.run(port=3000, ...)
