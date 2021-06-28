from __future__ import print_function
import sys, warnings
import deepsecurity
from deepsecurity.rest import ApiException
from pprint import pprint
import numpy as np
import pandas as pd
import requests
import json
import csv

# Setup
if not sys.warnoptions:
	warnings.simplefilter("ignore")
configuration = deepsecurity.Configuration()
configuration.host = 'https://cloudone.trendmicro.com/api'

# Authentication
configuration.api_key['api-secret-key'] = 'D1124FFD-2AA4-D76B-0BB8-6CC22102A5C5:13D1AC8B-6E72-7728-872B-60F339199E02:SRSkbml7EjHll4M6VCSxXbxDgwIjEDXNB1ZuhI/oO+E='

# Initialization
# Set Any Required Values
api_instance = deepsecurity.ComputersApi(deepsecurity.ApiClient(configuration))
api_version = 'v1'
expand_options = deepsecurity.Expand()
expand_options.add(expand_options.none)
expand = expand_options.list()
overrides = False

try:
	api_response = api_instance.list_computers(api_version, expand=expand, overrides=overrides)
	pprint(api_response)

except ApiException as e:
	print("An exception occurred when calling ComputersApi.list_computers: %s\n" % e)

api_response = str(api_response)
api_response_dq = api_response.replace("'",'"')
api_response_new = api_response_dq.replace('""', "None")
api_response_final = api_response_new.replace('None', '"None"')
#json.load() takes a file object and returns the json object. 
# A JSON object contains data in the form of key/value pair. The keys are strings and the values are the JSON types.
#  Keys and values are separated by a colon. Each entry (key/value pair) is separated by a comma.
data = json.loads(api_response_final)
#It return json object.


f = csv.writer(open("test.csv", "w+"))
#print(data["computers"][0]["host_name"])
# Write CSV Header, If you dont need that, remove this line
f.writerow([ "Display Name","Host Name", "Description" , "Platform" , "PolicyID"])
for x in data["computers"]:
    f.writerow([x["display_name"],
                x["host_name"],
                x["description"],
                x["platform"],
                x["policy_id"]])


