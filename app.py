import streamlit as st
import pickle
import pandas as pd
df = pickle.load(open('df.pkl', 'rb'))
pipe = pickle.load(open('pipe.pkl', 'rb'))
st.header('T20 Score Prediction')
st.image('t20image.jpg', width = 300)


col1, col2 = st.columns(2)
with col1:
    bat = st.selectbox('Batting Team', df['batting_team'].unique())
with col2:
    bowl = st.selectbox('Bowling Team', df['bowling_team'].unique())

city = st.selectbox('City', df['city'].unique())

col3, col4, col5 = st.columns(3)
with col3:
    score = st.number_input('Current Score')
with col4:
    over = st.number_input('Over Done')
with col5:
    wicket = st.number_input('Wickets Out')

last_five = st.number_input('Runs scored in last 5 overs')

if st.button('Predict Score'):
    balls_left = 120- (over*6)
    wickets_left = 10- wicket
    crr = score / over
    input = pd.DataFrame(
        {'batting_team': [bat],
         'bowling_team': [bowl],
         'city': [city],
         'current_score': [score],
         'balls_remainning': [balls_left],
         'wickets_left': [wickets_left],
         'crr': [crr],
         'last_five': [last_five]}
    )
    result = pipe.predict(input)
    st.header(' Predicted Score - ' + str(int(result[0])))
