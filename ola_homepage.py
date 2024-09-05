import streamlit as st
st.title("Ola's Work Gallery")
st.sidebar.header('Projects')

st.sidebar.markdown("[Co2 Emission by Cars](https://caremission.streamlit.app/)")
st.sidebar.markdown("[Heart Disease Prediction](https://heart-rates.streamlit.app/)")
st.sidebar.markdown("[Laptop Price Prediction](https://notebook-predict.streamlit.app/)")
st.sidebar.markdown("[Pose Classification]""(https://teachablemachine.withgoogle.com/models/1aeq6TPZ1/)")
st.sidebar.markdown("[Hand and Feet Classification](https://teachablemachine.withgoogle.com/models/hmI07XBoL/)")
st.sidebar.markdown("[Chatbot](https://911chatbot.streamlit.app)")


col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)
with col1:
    st.image("cars.jpg", width=200, caption="Co2 Emission")
with col2:
    st.image("heart.jpg", width=200, caption="Heart Disease")
with col3:
    st.image("laptops.jpg", width=200, caption="Laptop Price")
with col4:
    st.image("pose.jpg", width=200, caption="Pose")
with col5:
    st.image("feet.jpg", width=200, caption="Hand and Feet Classification")
with col6:
    st.image("chat.jpg", width=200, caption="Chatbot")


st.header("My Experience")
st.write("During my time here AI Rolof, i learnt how to code and create ai models."
        " My experience with Rolof Computers was a memorable one."
         "I really hope to come back again and learn something new.")
