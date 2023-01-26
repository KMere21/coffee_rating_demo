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

# load coffee review website image
image0 = ('coffeebeans.jpg')
st.image(image0)

# insert page title
st.title("Predict Coffee Ratings from Reviews")

# insert subheader
st.subheader("Project Background")

# insert text
st.markdown("Online ratings and reviews are a valuable tool for helping consumers make decisions. For businesses, this means ratings and reviews matter a lot. This project examined coffee reviews and ratings provided by a small team of expert reviewers at Coffee Review. Specifically, this project asks **How might we better understand the relationship between review and rating, so that coffee roasters can achieve top scores and distinguish themselves in a highly competitive market?**")

st.markdown("As of 2021, the global coffee market was valued at over 100 billion USD and growing (Businesswire). Increased concern about the social and environmental impact of products created a competitive market for high quality, responsibly sourced coffee (Research and Markets, 2022). This project primarily focuses on this subset of the industry, as the data is scraped from [CoffeeReview](https://www.coffeereview.com/). While reviews span 1997 to today, the site’s focus in the last 10 years has shifted to high quality coffee (Coffee Review, 2015).")

st.markdown("At Coffee Review, the evaluation (cupping) is conducted by a small, trained team on unidentified coffee. The reviewer scores five subcomponents (aroma, acidity, body, flavor, and aftertaste) from 1-10. Evaluative and descriptive narrative is also provided. A final overall rating from 50-100 is given (in both cases, higher scores are better). Top scores are in the 90s, with anything above 94 exceptional. More details on the reviewing process are available [here](https://www.coffeereview.com/how-coffee-review-works/).")

st.subheader("Try the Text-Based Model!")

st.markdown("Part of this project involved creating a text-based model to predict a coffee’s rating. **The model was trained using only the text from the *Blind Assessment* portion of reviews posted before November 2022.**") 

st.markdown("Give it a try! Pick a review from [CoffeeReview](https://www.coffeereview.com/). Click into the review to see the *Blind Assessment* text. Copy and paste it into the box below. **Any reviews posted November 2022 or later will be new to the model**. You can see how well it does by comparing the prediction to the actual rating.")


# Load the model using joblib
model = joblib.load('./public_rating_pipeline.pkl')

# Set up input field
review = st.text_area('', '')

# Use the model to predict sentiment & write result
prediction = model.predict({review})

if review != '':
    st.subheader('The predicted score is:') 
    st.header(np.round_(prediction).astype(int))
else: 
    st.write('Enter text above to get the predicted score. You can compare it to the actual score on Coffee Review.')


# insert subheader
st.subheader("How to Find the Review Information")

st.markdown("Go to the [latest reviews](https://www.coffeereview.com/). Click the *Read Complete Review* button. Then copy and paste the narrative text under *Blind Assessment*")

# show where to click to see more of the review
image1 = ('ReviewStep1.png')
st.image(image1)

# show what text to copy
image2 = ('ReviewStep2.png')
st.image(image2)


