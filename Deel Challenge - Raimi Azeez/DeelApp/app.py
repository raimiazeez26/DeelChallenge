import dash
from dash import Dash, html, dcc, dash_table
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd
import base64
import plotly.graph_objects as go
import plotly.express as px

# =============================================================================
# functions

deel_data = pd.read_csv('assets/deeldata.csv', index_col=[0])


# define function to calculate acceptance rate based on variable
def calc_acceptance_rate(df, column):
    """
  :param df(DataFrame): transaction dataset to calculate acceptance rate.
  :param column(string): column to calculate acceptance rate for
  :return(list): The acceptance rate of specified culumn.
  """
    accept_rate = []
    for i in list(df[column].unique()):
        accept_count = len(df.loc[(df[column] == i) & (df['state'] == 'ACCEPTED')])
        total_count = len(df.loc[(df[column] == i)])

        rate = round(accept_count / total_count, 2)
        accept_rate.append(rate)

    return accept_rate


def country():
    # accepted dataset
    deel_accept = deel_data[deel_data['state'] == 'ACCEPTED']
    deel_accept_grouped = deel_accept.groupby('country').sum(numeric_only=True).reset_index()

    # declined dataset
    deel_decline = deel_data[deel_data['state'] == 'DECLINED']
    deel_decline_grouped = deel_decline.groupby('country').sum(numeric_only=True).reset_index()
    deel_decline_grouped

    # select columns to plot for declined and accepted transactions
    country_acpt = deel_accept_grouped['country']
    amount_USD_acpt = deel_accept_grouped['amount_USD']

    country_dec = deel_decline_grouped['country']
    amount_USD_dec = deel_decline_grouped['amount_USD']

    # plot
    fig = go.Figure([
        go.Bar(name='Declined', x=country_dec, y=amount_USD_dec,
               text=amount_USD_dec,
               texttemplate='%{text:.2s}', textposition='outside',
               marker_color='red'),
        go.Bar(name='Accepted', x=country_acpt, y=amount_USD_acpt,
               text=amount_USD_acpt,
               texttemplate='%{text:.3s}', textposition='outside',
               marker_color='green')
    ])
    fig.update_layout(barmode='group',
                      title_text='Country vs Amount(USD)',
                      margin=dict(l=50, r=20, t=50, b=50),
                      # width=500,
                      # height=250,
                      yaxis=dict(
                          title_text="Amount(USD)",
                      ),
                      xaxis=dict(
                          title_text="Country",
                      )
                      )

    return fig


def country_accept():
    country_accept_rate = calc_acceptance_rate(deel_data, 'country')

    # plot

    fig = go.Figure([
        go.Bar(name='Declined', y=country_accept_rate, x=deel_data['country'].unique(),
               text=country_accept_rate,
               textposition='outside',
               marker_color='green'),

    ])
    fig.update_layout(barmode='group',
                      title_text='Country Acceptance Rate ',
                      margin=dict(l=50, r=20, t=50, b=50),
                      # width=500,
                      # height=250,
                      yaxis=dict(
                          title_text="Acceptance Rate",
                      ),
                      xaxis=dict(
                          title_text="Country",
                      )
                      )

    return fig

def currency():
    # accepted dataset
    deel_accept = deel_data[deel_data['state'] == 'ACCEPTED']
    deel_accept_grouped = deel_accept.groupby('currency').sum(numeric_only=True).reset_index()

    # declined dataset
    deel_decline = deel_data[deel_data['state'] == 'DECLINED']
    deel_decline_grouped = deel_decline.groupby('currency').sum(numeric_only=True).reset_index()
    deel_decline_grouped

    # select columns to plot for declined and accepted transactions
    country_acpt = deel_accept_grouped['currency']
    amount_USD_acpt = deel_accept_grouped['amount_USD']

    country_dec = deel_decline_grouped['currency']
    amount_USD_dec = deel_decline_grouped['amount_USD']

    # plot
    fig = go.Figure([
        go.Bar(name='Declined', x=country_dec, y=amount_USD_dec,
               text=amount_USD_dec,
               texttemplate='%{text:.2s}', textposition='outside',
               marker_color='red'),
        go.Bar(name='Accepted', x=country_acpt, y=amount_USD_acpt,
               text=amount_USD_acpt,
               texttemplate='%{text:.3s}', textposition='outside',
               marker_color='green')
    ])
    fig.update_layout(barmode='group',
                      title_text='Currency vs Amount(USD)',
                      margin=dict(l=50, r=20, t=50, b=50),
                      # width=500,
                      # height=250,
                      yaxis=dict(
                          title_text="Amount(USD)",
                      ),
                      xaxis=dict(
                          title_text="Currency",
                      )
                      )

    return fig


def currency_accept():
    currency_accept_rate = calc_acceptance_rate(deel_data, 'currency')

    # plot
    fig = go.Figure([
        go.Bar(name='Declined', y=currency_accept_rate, x=deel_data['currency'].unique(),
               text=currency_accept_rate,
               textposition='outside',
               marker_color='green'),

    ])
    fig.update_layout(barmode='group',
                      title_text='Currency Acceptance Rate ',
                      margin=dict(l=50, r=20, t=50, b=50),
                      # width=900,
                      # height=500,
                      yaxis=dict(
                          title_text="Acceptance Rate",
                      ),
                      xaxis=dict(
                          title_text="Currency",
                      )
                      )

    return fig


def month():
    # accepted dataset
    deel_month = deel_data[deel_data['state'] == 'ACCEPTED']
    deel_month_grouped = deel_month.groupby('Month').sum(numeric_only=True).reset_index()
    month_acpt = deel_month_grouped['Month']
    amount_USD_acpt = deel_month_grouped['amount_USD']

    # declined dataset
    deel_month_dec = deel_data[deel_data['state'] == 'DECLINED']
    deel_month_grouped_dec = deel_month_dec.groupby('Month').sum(numeric_only=True).reset_index()
    month_dec = deel_month_grouped_dec['Month']
    amount_USD_dec = deel_month_grouped_dec['amount_USD']

    # plot
    fig = go.Figure([
        go.Bar(name='Declined', x=month_dec, y=amount_USD_dec,
               text=amount_USD_dec,
               texttemplate='%{text:.2s}', textposition='outside',
               marker_color='red'),
        go.Bar(name='Accepted', x=month_acpt, y=amount_USD_acpt,
               text=amount_USD_acpt,
               texttemplate='%{text:.3s}', textposition='outside',
               marker_color='green')
    ])
    fig.update_layout(barmode='group',
                      title_text='Month vs Amount(USD)',
                      margin=dict(l=50, r=20, t=50, b=50),
                      # width=900,
                      # height=500,
                      yaxis=dict(
                          title_text="Amount(USD)",
                      ),
                      xaxis=dict(
                          title_text="Month",
                      )
                      )

    return fig

def month_accept():
    month_accept_rate = calc_acceptance_rate(deel_data, 'Month')

    # plot
    fig = go.Figure([
        go.Bar(x=deel_data['Month'].unique(), y=month_accept_rate,
               text=month_accept_rate,
               textposition='outside',
               marker_color='green'),
    ])
    fig.update_layout(
        title_text='Monthly Acceptance Rate',
        margin=dict(l=50, r=20, t=50, b=50),
        # width=900,
        # height=500,
        yaxis=dict(
            title_text="Acceptance Rate",
        ),
        xaxis=dict(
            title_text="Month",
        )
    )

    return fig

def cvv():
    # accepted dataset
    deel_month = deel_data[deel_data['state'] == 'ACCEPTED']
    deel_month_grouped = deel_month.groupby('cvv_provided').sum(numeric_only=True).reset_index()
    month_acpt = deel_month_grouped['cvv_provided']
    amount_USD_acpt = deel_month_grouped['amount_USD']

    # declined dataset
    deel_month_dec = deel_data[deel_data['state'] == 'DECLINED']
    deel_month_grouped_dec = deel_month_dec.groupby('cvv_provided').sum(numeric_only=True).reset_index()
    month_dec = deel_month_grouped_dec['cvv_provided']
    amount_USD_dec = deel_month_grouped_dec['amount_USD']

    # plot
    fig = go.Figure([
        go.Bar(name='Declined', x=month_dec, y=amount_USD_dec,
               text=amount_USD_dec,
               texttemplate='%{text:.2s}', textposition='outside',
               marker_color='red'),
        go.Bar(name='Accepted', x=month_acpt, y=amount_USD_acpt,
               text=amount_USD_acpt,
               texttemplate='%{text:.3s}', textposition='outside',
               marker_color='green')
    ])
    fig.update_layout(barmode='group',
                      title_text='CVV vs Amount(USD)',
                      margin=dict(l=50, r=20, t=50, b=50),
                      # width=900,
                      # height=500,
                      yaxis=dict(
                          title_text="Amount(USD)",
                      ),
                      xaxis=dict(
                          title_text="CVV",
                      )
                      )

    return fig

def cvv_accept():
    # Acceptance rate for transaction where cvv was provided
    deel_ccv = deel_data[deel_data['cvv_provided'] == True]

    deel_cvv_accepted = deel_ccv[deel_ccv['state'] == 'ACCEPTED']
    cvv_acceptance_rate = round(len(deel_cvv_accepted) / (len(deel_ccv)), 2)

    # Acceptance rate for transaction where cvv was not provided
    deel_ccv = deel_data[deel_data['cvv_provided'] == False]

    deel_cvv_accepted = deel_ccv[deel_ccv['state'] == 'ACCEPTED']
    no_cvv_acceptance_rate = round(len(deel_cvv_accepted) / (len(deel_ccv)), 2)

    # plot
    cvv = [no_cvv_acceptance_rate, cvv_acceptance_rate]
    fig = go.Figure([
        go.Bar(name='Declined', y=cvv, x=deel_data['cvv_provided'].unique(),
               text=cvv,
               textposition='outside',
               marker_color='green'),

    ])
    fig.update_layout(barmode='group',
                      title_text='CVV Provided Acceptance Rate ',
                      margin=dict(l=50, r=20, t=50, b=50),
                      # width=500,
                      # height=500,
                      yaxis=dict(
                          title_text="Acceptance Rate",
                      ),
                      xaxis=dict(
                          title_text="CVV Provided",
                      )
                      )

    return fig

def amount():
    # Create a bin for sales amount
    deel_data['amount_bin_USD'] = pd.qcut(deel_data['amount_USD'], 5)

    # accepted dataset
    deel_month = deel_data[deel_data['state'] == 'ACCEPTED']
    deel_month_grouped = deel_month.groupby('amount_bin_USD').sum(numeric_only=True).reset_index()
    month_acpt = deel_month_grouped['amount_bin_USD'].astype(str)
    amount_USD_acpt = deel_month_grouped['amount_USD']

    # declined dataset
    deel_month_dec = deel_data[deel_data['state'] == 'DECLINED']
    deel_month_grouped_dec = deel_month_dec.groupby('amount_bin_USD').sum(numeric_only=True).reset_index()
    month_dec = deel_month_grouped_dec['amount_bin_USD'].astype(str)
    amount_USD_dec = deel_month_grouped_dec['amount_USD']

    # plot
    fig = go.Figure([
        go.Bar(name='Declined', x=month_dec, y=amount_USD_dec,
               text=amount_USD_dec,
               texttemplate='%{text:.2s}', textposition='outside',
               marker_color='red'),
        go.Bar(name='Accepted', x=month_acpt, y=amount_USD_acpt,
               text=amount_USD_acpt,
               texttemplate='%{text:.3s}', textposition='outside',
               marker_color='green')
    ])
    fig.update_layout(barmode='group',
                      title_text='Amount_bin vs Amount(USD)',
                      margin=dict(l=50, r=20, t=50, b=50),
                      # width=900,
                      # height=500,
                      yaxis=dict(
                          title_text="Amount(USD)",
                      ),
                      xaxis=dict(
                          title_text="Amount_bin",
                      )
                      )

    return fig

def amount_accept():
    # Create a bin for sales amount
    deel_data['amount_bin_USD'] = pd.qcut(deel_data['amount_USD'], 5)

    amount_accept_rate = calc_acceptance_rate(deel_data, 'amount_bin_USD')

    # plot
    fig = go.Figure([
        go.Bar(x=deel_data['amount_bin_USD'].unique().astype(str), y=amount_accept_rate,
               text=amount_accept_rate,
               textposition='outside',
               marker_color='green'),
    ])
    fig.update_layout(
        title_text='Amount(USD) Acceptance Rate',
        margin=dict(l=50, r=20, t=50, b=50),
        # width=900,
        # height=500,
        yaxis=dict(
            title_text="Acceptance Rate",
        ),
        xaxis=dict(
            title_text="Amount(USD)",
        )
    )

    return fig

#Logo encoding
img_path = 'assets/Deel_Logo.png'
img = base64.b64encode(open(img_path, 'rb').read()).decode('ascii')
img_png = 'data:image/png;base64,{}'.format(img)
# =============================================================================


# creates the Dash App
app = Dash(__name__, external_stylesheets=[dbc.themes.MINTY])  # dbc.themes.ZEPHYR]
server = app.server

# creates the layout of the App
app.layout = \
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Img(src=img_png, className='text-center',
                         style={'width': '100%', 'height': '100%'})
            ], width=2),
            dbc.Col([
                html.H1('Globepay Payment Acceptance Rate', className='text-center'), #style={"color": "#FFFFFF"})
                html.H5('A case study of the Acceptance rate of payments made through Globepay API.',
                        className='text-center')
            ], width=10, className='p-3', align='center')
        ]),
        html.Hr(),
        dbc.Row([
            html.Div([
                html.Label(['Please select A Variable: ']),
                dcc.Dropdown(
                    id="dropdown",
                    options=["Country", "Currency", "CVV", "Month", "Amount_bin(USD)"],
                    value="Country",
                    clearable=False,
                ),
            ]),
        ]),
        html.Br(),
        html.Br(),
        dbc.Row([
            dbc.Col([
                html.Div([dcc.Graph(id="vol-graph")],
                         id='volume-output')
            ], width=8),

            dbc.Col([
                html.Div([dcc.Graph(id="acc-graph")],
                         id='accept-output')
            ], width=4)
        ])
    ])


@app.callback(
    Output("vol-graph", 'figure'),
    Output("acc-graph", 'figure'),
    Input('dropdown', 'value'),
    prevent_initial_call = True
)
def data_store(value):
    if value == 'Country':
        volume = country()
        accept = country_accept()

    elif value == 'Currency':
        volume = currency()
        accept = currency_accept()

    elif value == 'Month':
        volume = month()
        accept = month_accept()

    elif value == 'CVV':
        volume = cvv()
        accept = cvv_accept()

    elif value == 'Amount_bin(USD)':
        volume = amount()
        accept = amount_accept()
    else:
        volume = None
        accept = None
    return [volume, accept]

if __name__ == '__main__':
    # starts the server
    app.run_server() #mode='jupyterlab',
