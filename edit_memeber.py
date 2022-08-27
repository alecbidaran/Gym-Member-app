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
edit_layout=dbc.Container([
    dbc.Row(dbc.Col(dbc.Card([html.H1("Evaluating new Account")]), width={"size": 4, "offset": 3})),
    dbc.Row(dbc.Col([
        dbc.Card(dbc.Input(id="eusername",placeholder="type your Fullname",type="text"))
    ], width={"size": 4, "offset": 3})),
    dbc.Row(dbc.Col(html.Div())),

    dbc.Row(dbc.Col(dbc.Card(dbc.Input(id="epassword",placeholder="type your password",type="password")),width={"size": 4, "offset": 3})),
        dbc.Row(dbc.Col(html.Div())),
    dbc.Row(dbc.Col(dbc.Card(dcc.Dropdown([12,16,20,24],12,id='esessions',)),width={"size": 4, "offset": 3})),
    dbc.Row(dbc.Col(dbc.Card(dbc.Button("Revaluate",id="eval_button",color="primary", className="me-1")), width={"size": 1, "offset": 3})),
    dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Welcome Again")),
                dbc.ModalBody("You sessions Registered!"),
            ],
            id="emodal",
            is_open=False,
        ),
  
])

#if __name__=="__main__":
 #   app.run_server(debug=True)