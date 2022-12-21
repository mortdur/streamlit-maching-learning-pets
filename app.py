import streamlit as st
import pandas as pd
import joblib

st.title("¿Perro o gato?")

# Add a Height input
Height = st.number_input("Enter Height:")

# Add a Weight input
Weight = st.number_input("Enter Weight:")

# Add a Eye Colour input
Eye = st.selectbox('Enter Eye Colour?',('Blue', ' Bronw'))
st.write('You selected:', Eye)

# Display the entered name
if st.button("Enviar"):

    pet_model = joblib.load("pet_model.pkl")

    X = pd.DataFrame([[Height,Weight,Eye]],
			   columns = ["Height","Weight","Eye"])
    X = X.replace(["Bronw", "Blue"], [1,0])

    prediction = pet_model.predict(X)[0]

    st.text(f"Es un {prediction}")
