import pandas as pd
import random
import requests
from application import app


@app.route('/', methods=['GET','POST'])
def shufflecards():
    df=pd.read_csv('\QAProject2\cards\application\cards.csv')
    #give a random row
    card=df.sample(n=1) 
    return card
