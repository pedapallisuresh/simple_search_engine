# simple_search_engine
creation of assistant using api.

The Wolfram|Alpha Webservice API provides a web-based API allowing the computational and presentation capabilities of Wolfram|Alpha to be integrated into web, mobile, desktop, and enterprise applications. Wolfram Alpha is an API which can compute expert-level answers using Wolfram’s algorithms, knowledgebase and AI technology. It is made possible by the Wolfram Language. This article tells how to create a simple assistant application in Python which can answer simple questions like the ones listed below.

Input : What is the capital of India? 
Output : New Delhi

Input : What is sin(30)?
Output : 0.5

PREREQUISITES : 
 1. Create a account at Wolfram alpha. The account can be created at the official website.
 2. After signing up, sign in using your Wolfram ID.
 3. Now you will see the homepage of the website. Head to the section in the top right corner        where you see your email. In the drop down menu, select the My Apps (API) option.
 4. Click the Get an AppID button to get the id.
 5. In the next dialog box, give the app a suitable name and description.
 6. Note down the APPID that appears in the next dialog box. This app id will be specific to the     application.


Implementation :  Make sure that wolframalpha python package is installed beforehand. It can be done by running the following command in the terminal or cmd –

pip install wolframalpha
   if in vs code editor then use  "!pip install wolframalpha"


