# Housing_price_pred
Prediction of House Prices

# Descrpition
This model takes in only numeric values for 3 required fields, LSTAT, RM and PTRATIO of a House in Boston to predict its price. The model is connected to a basic HTML website using Flask and displays the output depending on the values inputted by the user.

# Contents
The Boston.py file contains the model we used to predict the Boston housing prices.
The templates folder contains the html part of the code.
The connect.py and app.py files have the linkage of the front-end with the back-end using flask

# Running the code on your device locally:
If you download the code from the GIT repository, you will need to have all the software mentioned in the requirements file installed on your local pc. Then on setting the path on command prompt where you have saved the files, run the command app.py (or python app.py) and copy paste the link provided on your browser.

```bash
  pip install -r requirements.txt
```

# Deployment on Heroku
Deploying the app on Heroku platform is as easy as possible. Create an app on heroku with a suitable name and start deploying it with GITHUB or Heroku CLI by connecting it to your Github account. On successful connection and deploying from the repository the app is successfully build. Then you can visit the web app with the link you are provided with.

A Procfile is used to tell Heroku how to run various pieces of the app.
This is the Procfile content of my web app. 
```bash
  web: gunicorn app:app
```


## Link to the Website on Heroku
https://bostonprice.herokuapp.com/
