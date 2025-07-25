# Streamlit Documentation: https://docs.streamlit.io/

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image  # to deal with images (PIL: Python imaging library)

# TEXT ELEMENTS
# Title/Text
st.title("This is ZAFER'S page")
st.text("This is some test.")
st.text("zafer's text is here.")

st.markdown("Streamlit is **_really_ cool** :+1:" )
st.markdown("# This is a markdown")
st.markdown("## This is a markdown")
st.markdown("### This is a markdown")

st.header("header icin .header")
st.subheader("subheader da boyle")

# STATUS ELEMENTS
# Success/Info/Error
st.success('This is a success message!')
st.info('This is a purely informational message')
st.error("This is an error.")
st.warning("This is a warning message!")
st.exception("NameError('name there is not defined')")

# Help
st.help(range)

# Write
st.write("Hello World! :sunglasses:")
st.write(range(10))

# MEDIA ELEMENTS
# Add image
img = Image.open("images.jpeg")
st.image(img, caption="cattie", width=300)

# Add youtube video
st.video("https://www.youtube.com/watch?v=uHKfrz65KSU")



# INPUT WIDGETS


# Add checkbox
st.checkbox("Up and Down")
cbox = st.checkbox("Hide and Seek")

if cbox :
    st.write("Hide")
else :
    st.write("Seek")


# Add radio button
status = st.radio("Select a color",("blue","orange","yellow","esma"))
st.write("My favorite color is ", status)

# Add button
st.button("Click me")

if st.button("Press me") :
    st.success("Analyze Results are..")


# Add select box
occupation = st.selectbox("Your Occupation", ["Programmer", "DataScientist", "Doctor"])
st.write("Your Occupation is ", occupation)


# Multi_select
multi_select = st.multiselect("Select multiple numbers",[1,2,3,4,5])
st.write(f"You selected {len(multi_select)} number(s)")
st.write("Your selection is/are", multi_select)
for i in range(len(multi_select)):
    st.write(f"Your {i+1}. selection is {multi_select[i]}")

# Slider
option1 = st.slider("Select a number", min_value=5, max_value=70, value=30, step=5)
option2 = st.slider("Select a number", min_value=0.2, max_value=30.2, value=5.2, step=0.2)
result = option1*option2
st.write("multiplication of two options is:",result)


# Text_input
name = st.text_input("Enter your name", placeholder="Your name here")
if st.button("Submit"):
    st.write("Hello {}".format(name.title()))

# Number_input
number = st.number_input("Insert a number")  # st.number("select a number", min_value, max_value, value, step)
st.write("The current number is ", number)


# Code  # to show as if code
st.code("import pandas as pd")
st.code("import pandas as pd\nimport numpy as np")


# Echo  # it is used "with block" to draw some code on the app, then execute it
with st.echo():
    import pandas as pd
    import numpy as np
    df = pd.DataFrame({"a":[1,2,3], "b":[4,5,6]})
    df


# Date input
import datetime
today = st.date_input("Today is", datetime.datetime.now())
date = st.date_input("Enter the date")

st.write(date)

# Time input
the_time = st.time_input("The time is", datetime.time(8, 45))
hour = st.time_input(str(pd.Timestamp.now()))
st.write("Hour is", hour)


# Sidebar
st.sidebar.title("Sidebar title")
st.sidebar.header("Sidebar header")



# Sidebar with slider
a = st.sidebar.slider("input1",0,5,2,1)
x = st.sidebar.slider("input2")
st.write("# sidebar input result")
st.success(a*x)

# Dataframe
df = pd.read_csv("Advertising.csv")
# To display dataframe there are 3 methods
# Method 1
st.table(df.head())
# Method 2
st.write(df.head())  # dynamic, you can sort
st.write(df.isnull().sum())
# Method 3
st.dataframe(df.describe().T)  # dynamic, you can sort

# ############################################
# To load machine learning model
import pickle
filename = "my_model"
model = pickle.load(open(filename, "rb"))


# To take feature inputs
TV = st.sidebar.number_input("TV:",min_value=5, max_value=300)
radio = st.sidebar.number_input("radio:",min_value=1, max_value=50)
newspaper = st.sidebar.number_input("newspaper:",min_value=0, max_value=120)

# Create a dataframe using feature inputs
my_dict = {"TV":TV,
           "radio":radio,
           "newspaper":newspaper}


df = pd.DataFrame.from_dict([my_dict])
st.table(df)

# Prediction with user inputs
predict = st.button("Predict")
result = model.predict(df)
if predict :
    st.success(result[0])



st.balloons()
st.snow()


st.write("Hello World! :sunglasses:")












































