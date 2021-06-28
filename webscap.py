from __future__ import print_function
import sys, warnings
import deepsecurity
from deepsecurity.rest import ApiException
from pprint import pprint
import numpy as np
import pandas as pd
import requests
import json

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

f = open("dsfile.csv", "w") 
f.write (str(api_response))

#JSONContent = requests.get(api_response).json()
#content = json.dumps(JSONContent, indent = 0, sort_keys=True)
#print(content)


		
f.close()


