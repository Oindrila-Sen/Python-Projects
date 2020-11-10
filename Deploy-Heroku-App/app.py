# importing the required libraries
from flask import Flask, render_template, request, redirect, url_for, Response
from flask_table import Table, Col
from joblib import load
from flask import send_file
#import base64
from io import BytesIO
#import io
#import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import random, threading, webbrowser
import sentiment_analysis

####------function to get trening tweets----####
def gettrends():
    # get the twitter trends
    df_world_trends = sentiment_analysis.get_trends_by_location(1, 10)
    df_world_trends["Translated_Trends"] = [sentiment_analysis.get_translation(val) for val in df_world_trends.Trends]
    return df_world_trends[["Trends","Language","Translated_Trends"]]

####------ function to get results for a particular text query----####
def requestResults(search_keyword):
    # get the tweets text
    df_tweets = sentiment_analysis.get_related_tweets(search_keyword)
    # Predict Emotion for the tweets
    df_tweets = sentiment_analysis.predict_emotion(df_tweets)
    # Clean the tweets
    df_tweets = sentiment_analysis.data_cleaning(df_tweets)

    return df_tweets

####------ function to create a plot ----####
def create_plot(df_tweets):
    fig = Figure()
    img = df_tweets.Prediction.value_counts().plot(kind = "bar")
    return fig
# start flask
app = Flask(__name__)

####------render default webpage ----####
@app.route('/')
def home():
    return render_template('home.html')

# when the post method detect, then redirect to trends page
@app.route('/', methods=['POST', 'GET'])
def get_trends():
    if request.method == 'POST':
        trends = gettrends()
        return render_template('trends.html', table=trends.to_html())


# when the post method detect, create a url for success
@app.route('/get_data', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        name = request.form['search']
        return redirect(url_for('success', name=name))

#create a Plot and send a png file
@app.route('/plot_png')
def plot_png():
    #fig = create_plot()
    img = BytesIO()
    plt.savefig(img)
    img.seek(0)
    #plot_url = base64.b64encode(img.getvalue())
    return send_file(img, mimetype='image/png')

####------when the post method detect, then redirect to results page
@app.route('/success/<name>')
def success(name):
    #return "<xmp>" + str(requestResults(name)) + " </xmp> "
    results = requestResults(name)
    #plot_url = plot_png()
    #return render_template('results.html', img=plot_url, table=results.to_html())
    return render_template('results.html', table=results.to_html())


if __name__ == '__main__':
    #port = 5000 + random.randint(0, 999)
    #print(port)
    #url = "http://127.0.0.1:{0}".format(port)
    #print(url)
    #app.run(use_reloader=False, debug=True, port=port)
    app.run(use_reloader=False, debug=True)
    