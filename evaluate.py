from dash import Dash,dcc,html,Input,Output,State
import dash_bootstrap_components as dbc
import pandas as pd 
import dash
import plotly.express as px
import dash 
from datetime import date
import datetime
import cv2 
import base64
import io
import numpy as np  
from apps.login import login_layout,evaluate
from apps.SignUp import signup_layout
from apps.edit_memeber import edit_layout
from hashlib import sha256
from database import db,Members,server
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP],server=server)

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Gym App", className="display-4"),
        html.Hr(),
        html.P(
            "A simple sidebar layout with navigation links", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Enter", href="/login", active="exact"),
                dbc.NavLink("Register", href="/SignUp", active="exact"),
                dbc.NavLink("Update", href="/edit_memeber", active="exact"),

            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.P("This is the content of the home page!")
    elif pathname == "/login":
        return login_layout
    elif pathname == "/SignUp":
        return signup_layout
    elif pathname=="/edit_memeber":
        return edit_layout
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )
@app.callback([Output("lmodal","is_open"),Output("message","children")],[Input('login-button','n_clicks')],[State("lmodal","is_open"), State('lusername','value'),State('lpassword', 'value')])
def login(n_clicks,is_open,username,password):
    if n_clicks>0:
        objects=Members.query.filter_by(Fullname=username,password=sha256(str(password).encode('utf-8')).hexdigest()).first()
        if objects is not None:
            is_open=True
            objects.sessions-=1
            new_val=Members.query.filter_by(Fullname=username,password=sha256(str(password).encode('utf-8')).hexdigest()).update({'sessions':objects.sessions})
            db.session.commit()
            return is_open, "You have{} sessons".format(objects.sessions)
        else: 
            is_open=False
            return is_open
@app.callback(Output("smodal","is_open"),[Input("sign_up","n_clicks")],
[State("smodal","is_open"),State("susername","value"),State("spassword","value"),State("email","value"),State('my-date-picker-single','date'),State("image_upload",'contents'),
State("image_upload","filename"),State('image_upload','last_modified'),State("sessions","value")])
def do_process(s_clicks,is_open,username,password,email,date,contents,filename,im_date,session):
    if s_clicks:
        contents_string=contents.split(',')[1]
        nparr=np.fromstring(base64.b64decode(contents_string),dtype=np.uint8)
        img=cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        cv2.imwrite("imgs/"+username+".jpg",img)
        date=datetime.datetime.strptime(date,'%Y-%m-%d').date()
        data=Members(Fullname=username,email=email,password=sha256(str(password).encode('utf-8')).hexdigest(),sessions=session,date=date)
        db.session.add(data)
        db.session.commit()
        return not is_open 
        
    else:
        return is_open

@app.callback(Output("spassword","invalid"),Input("spassword","value"))
def check_password(value):
    if len(value)<=8:
        return True
    else:
        return False
@app.callback(Output("emodal","is_open"),[Input("eval_button","n_clicks")],
[State("emodal","is_open"),State("eusername","value"),State("epassword","value"),State("esessions","value")])
def do_process(n_clicks,is_open,username,password,session):
    if n_clicks:
        user=Members.query.filter_by(Fullname=username,password=sha256(str(password).encode('utf-8')).hexdigest()).update({'sessions':session})
        db.session.commit()
        return not is_open 
        
    else:
        return is_open

if __name__ == "__main__":
    app.run_server(port=8888)