import sys
import json
import pandas as pd
from google.api_core.client_options import ClientOptions
#from google.cloud import automl
from google.cloud import automl_v1
from google.cloud.automl_v1.proto import service_pb2

def inline_text_payload(file_path):
  with open(file_path, 'rb') as ff:
    content = ff.read()
  return {'text_snippet': {'content': content, 'mime_type': 'text/plain'} }

def read_pandas_csv(file_path,column_name=None):
    df = pd.read_csv(file_path)
    items = df[column_name].values.tolist()
    for item in items:
      


    


def pdf_payload(file_path):
  return {'document': {'input_config': {'gcs_source': {'input_uris': [file_path] } } } }

def get_prediction(file_path, model_name,column_name=None):
  options = ClientOptions(api_endpoint='automl.googleapis.com')
  prediction_client = automl_v1.PredictionServiceClient(client_options=options)

  payload = inline_text_payload(file_path)
  # Uncomment the following line (and comment the above line) if want to predict on PDFs.
  # payload = pdf_payload(file_path)

  params = {}
  request = prediction_client.predict(model_name, payload, params)
  return request  # waits until request is returned

if __name__ == '__main__':
  file_path = sys.argv[1]
  model_name = sys.argv[2]
  try:
    column_name = sys.argv[3]
  except IndexError:
    column_name = 'null'


  if (column_name != 'null'):
    prediction = (get_prediction(file_path, model_name,column_name))

  else:
    prediction = (get_prediction(file_path, model_name))
