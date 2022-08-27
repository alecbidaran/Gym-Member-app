from dash import Dash,dcc,html,Input,Output,State
import dash_bootstrap_components as dbc
import pandas as pd 
import dash
import plotly.express as px
import dash 
from datetime import date
import cv2 
import base64
import io
import numpy as np  
#app=Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
signup_layout=dbc.Container([
    dbc.Row(dbc.Col(dbc.Card([html.H1("Registering new Account")]), width={"size": 4, "offset": 3})),
    dbc.Row(dbc.Col([
        dbc.Card(dbc.Input(id="susername",placeholder="type your Fullname",type="text"))
    ], width={"size": 4, "offset": 3})),
    dbc.Row(dbc.Col(html.Div())),
    dbc.Row(dbc.Col(
        dbc.Card(dbc.Input(id="email",placeholder="type your email",type="text")
    ),width={"size": 4, "offset": 3})),
        dbc.Row(dbc.Col(html.Div())),

    dbc.Row(dbc.Col(dbc.Card(dbc.Input(id="spassword",placeholder="type your password",type="password")),width={"size": 4, "offset": 3})),
        dbc.Row(dbc.Col(html.Div())),
    dbc.Row(dbc.Col(dbc.Card(dcc.Dropdown([12,16,20,24],12,id='sessions',)),width={"size": 4, "offset": 3})),

    dbc.Row(dbc.Col(dcc.DatePickerSingle(id='my-date-picker-single',
        min_date_allowed=date(1950, 8, 5),
        initial_visible_month=date(2017, 8, 5),
        date=date(2017, 8, 25)),width={"size": 4, "offset": 3})),
    dbc.Row(dbc.Col(dbc.Card(dcc.Upload(id="image_upload",children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),)),width={'size':4,'offset':3})),
    dbc.Row(dbc.Col(dbc.Card(dbc.Button("SignUp",id="sign_up",color="primary", className="me-1")), width={"size": 1, "offset": 3})),
    dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Header")),
                dbc.ModalBody("You signed up sucessfuly!"),
            ],
            id="smodal",
            is_open=False,
        ),
])

#if __name__=="__main__":
 #   app.run_server(debug=True)