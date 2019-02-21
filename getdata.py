from __future__ import print_function
# apiclient has been chenged to googleapiclient
from googleapiclient import errors
from httplib2 import Http
from googleapiclient.discovery import build
from oauth2client import file
from oauth2client.file import Storage
import base64
import email
# from helpers import get_amount, get_balance, get_category
import re
import os
from nltk.corpus import stopwords
from gensim.models import doc2vec
from collections import namedtuple
from google.auth import credentials
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import OAuth2WebServerFlow
import http
import json
import time

def return_uri():

    f = open('extras/gmailstorecopy2.txt','r').readlines() #create your file with the details 
    # Credentials you get from registering a new application
    client_id = f[0].strip()
    client_secret = f[1].strip()
    redirect_url = f[2].strip()
    SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'

    flow = OAuth2WebServerFlow(client_id=client_id, client_secret=client_secret,scope=SCOPES,redirect_uri=redirect_url)
    auth_uri = flow.step1_get_authorize_url()
    return auth_uri