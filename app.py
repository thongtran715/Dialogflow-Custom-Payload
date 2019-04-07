from flask import Flask, request
from flask_restful import Resource

app = Flask(__name__)

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] ="/home/ubuntu/rcs_mwc_receipt_api/src/SEAT-NINJA.json"
PROJECT_ID = "seatninja-8b96a"
SESSION_ID = "860ff14ccd004e9eb4e2fac49acb454c"
def detect_intent_texts(project_id, session_id, text, language_code, phoneNumber):
     context_short_name = "doesnotmatter"

     context_name = "projects/" + PROJECT_ID + "/agent/sessions/" + SESSION_ID + "/contexts/" + \
               context_short_name.lower()

     import dialogflow_v2 as dialogflow
     parameters = dialogflow.types.struct_pb2.Struct()
     parameters['phoneNumber'] = phoneNumber
     context = dialogflow.types.context_pb2.Context(
             name=context_name,
             lifespan_count = 2,
            parameters = parameters
             )
     query_params_1 = {"contexts":[context]}

     session_client = dialogflow.SessionsClient()

     session = session_client.session_path(project_id, session_id)

     text_input = dialogflow.types.TextInput(
         text=text, language_code=language_code)

     query_input = dialogflow.types.QueryInput(text=text_input)

     response = session_client.detect_intent(
         session=session, query_input=query_input,query_params=query_params_1)
     print (response.query_result)
     return response.query_result.intent.display_name, response.query_result.fulfillment_text
class Diagflow(Resource):
    def post(self):
        data = request.get_json()
        mt = data['text']
        phone = data['phone']
        intent, fullfill = detect_intent_texts(PROJECT_ID, SESSION_ID,mt, "en", phone)
        return {
                "intent": intent,
                "fullfill": fullfill
                }

if __name__ == '__main__':
    app.run()
