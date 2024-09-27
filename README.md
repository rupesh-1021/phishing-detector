Install python3 or higher versions onto your PC.
# Import the necessary libraries mentioned below:
        from flask import Flask, render_template, request
        import pandas as pd
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.naive_bayes import MultinomialNB
        from sklearn.model_selection import train_test_split
        from sklearn import metrics
Import the csv file in the python code for datasets
# Steps to be followed for running the app
1. Save the codes to a specified path on your PC,
2. open command prompt,
3. Give the below mentioned commands:
      1. cd your file path (if desktop -> cd desktop)
      2. cd file name (if phishing-detector -> cd phishing-detector)
      3. python App.py
   **This app.py runs on the WSGI server and generates the link to access the app i.e http://127.0.0.1:5000 or localhost:5000**
4. Now open the Browser and enter the above mentioned link by clicking it or type 127.0.0.1:5000 in the url placeholder.
5.  After launching the Website, you can find out the interface of the website and then follow the below steps
# Click upon any of your desired detector mentioned below in Detectors section and follow the procedure below.
        1. Give the input in which how many URLs/IPs/Domains you're willing to predict, and then click generate inputs.
        2. After the inputs were generated, enter the URLs or IPs or Domains to be predicted.
        3. Click on the predict button to predict whether the given URL/IP/Domain is a phishing or a Legitimate URL.
        4. Results will be displayed according to the input given.

