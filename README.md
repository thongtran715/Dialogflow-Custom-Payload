# Objective
The project is created to demonstrate how we can make a custom payload for Dialogflow
# Motivation 
It is good to start with the problem that I personally had when dealing with Dialogflow. Dialogflow is powered by Google in order to build smart chat bot using Deep Neural Network. I was tasked to create the chat bot that utilizes our Sinch RCS Api with Dialogflow, and encountered one problem which Dialogflow does not return the MSIDN to the callback. Thus, the chatBot callback receives the data after the POST request, but it does not know the MSIDN to send for. 
As a result, I managed to make a custom payload with the MSIDN attach to Dialogflow before it reachs to chatBot callback.
# Flow
![alt text](https://s3.us-east-2.amazonaws.com/rcs-demo/github/Screen+Shot+2019-04-08+at+10.45.44+AM.png)

# Configuration
1. Install all the dependencies 
```
pip install -r requirements.txt
```
2. Get JSON file, Project ID from Google Cloud Console. 
3. Get SESSION ID from Dialogflow console under Bot -> Settings -> Client access token

# Usage 
1. Run the server by
```
python app.py
```
2. Make a custom curl post to 
```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"text":"Hello","phone":"+15417773313"}' \
  http://localhost:4041/api/diagflow/intent
```

After making the request, this script will re-direct to Dialogflow , and automatically check the Webhook that is already set up on Dialogflow and the response will forward to the bot server. 
