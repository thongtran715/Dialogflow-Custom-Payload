# Objective
The project is created to demonstrate how we can make a custom payload for Dialogflow
# Motivation 
It is good to start with the problem that I personally had when dealing with Dialogflow. Dialogflow is powered by Google in order to build smart chat bot using Deep Neural Network. I was tasked to create the chat bot that utilizes our Sinch RCS Api with Dialogflow, and encountered one problem which Dialogflow does not return the MSIDN to the callback. Thus, the chatBot callback receives the data after the POST request, but it does not know the MSIDN to send for. 
As a result, I managed to make a custom payload with the MSIDN attach to Dialogflow before it reachs to chatBot callback.
# Flow

