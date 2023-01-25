### borrowed code from BrainStation streamlit kick off 

### import libraries
import pandas as pd
import streamlit as st
import numpy as np
import joblib
from matplotlib import pyplot as plt

#######################################################################################################################################
### LAUNCHING THE APP ON THE LOCAL MACHINE
### 1. Save your *.py file (the file and the dataset should be in the same folder)
### 2. Open git bash (Windows) or Terminal (MAC) and navigate (cd) to the folder containing the *.py and *.csv files
### 3. Execute... streamlit run <name_of_file.py>
### 4. The app will launch in your browser. A 'Rerun' button will appear every time you SAVE an update in the *.py file


#######################################################################################################################################
##### Model Demo 1##########

# load coffee review website image
image0 = ('CoffeeReview.png')
st.image(image0)

# insert page title
st.title("Predicting Coffee Ratings with Review Data")

# insert subheader
st.subheader("Let's test some  new reviews!")

# Load the model using joblib
model = joblib.load('/Users/katemondal/Documents/BrainStation/CapstoneProject/rating_pipeline.pkl')

# Set up input field
review = st.text_area('', '')

# Use the model to predict sentiment & write result
prediction = model.predict({review})

if review != '':
    st.subheader('The predicted score is:') 
    st.header(np.round_(prediction).astype(int))
else: 
    st.write('Enter text above to get predicted score.')

# Link to review page 1
st.write('[Review One](https://www.coffeereview.com/review/tinamit-toliman/)')
image1 = ('Review_1.png')
st.image(image1)

# Link to review page 2
st.write('[Review Two](https://www.coffeereview.com/review/kenya-aa/)')
image2 = ('Review_2.png')
st.image(image2)




