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
from hashlib import sha256
password="ab0098"
evaluate={"username":"alibidaran",
"password":sha256(password.encode('utf-8')).hexdigest(),'session':12}
app=Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
login_layout=dbc.Container([
    dbc.Row(dbc.Col(dbc.Card([html.H1("Entering Member")]), width={"size": 4, "offset": 3})),
    dbc.Row(dbc.Col([
        dbc.Card(dbc.Input(id="lusername",placeholder="type your Fullname",type="text"))
    ], width={"size": 4, "offset": 3})),
    dbc.Row(dbc.Col(html.Div())),
    dbc.Row(dbc.Col(dbc.Card(dbc.Input(id="lpassword",placeholder="type your password",type="password")),width={"size": 4, "offset": 3})),
        dbc.Row(dbc.Col(html.Div())),
    dbc.Row(dbc.Col(dbc.Card(dbc.Button("Login",id="login-button",color="primary", className="me-1")), width={"size": 1, "offset": 3})),
    dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Welcome to Gym")),
                dbc.ModalBody(id='message'),
            ],
            id="lmodal",
            is_open=False,
        ),
])


#if __name__=="__main__":
    #app.run_server(debug=True)
