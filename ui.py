import streamlit as st
import pickle

#Function to load the selected model
def load_model(model_name):
    model_path = f'/Users/da_m1_19/Desktop/new project laduma/Precious_Laduma_Score_Predictions/{model_name}.pkl'
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

def main():
    # Title of the web app
    st.title('Laduma Score Prediction')

    # Subheader
    st.subheader('Welcome! Select a model and input features for prediction.')

    # Dropdown to select the model
    model_options = ['RandomForestClassifier', 'KNeighbors', 'DecisionTree']
    selected_model = st.selectbox('Select Model', model_options)

    # Load the selected model
    model = load_model(selected_model)

    # User input for features
    st.header('Feature Input')
    feature1 = st.number_input('Season_x', value=0)
    feature2 = st.number_input('X', value=0)
    feature3 = st.number_input('Y', value=0)
    feature4 = st.number_input('Team', value=0)
    feature5 = st.number_input('SoT', value=0)
    feature6 = st.number_input('Accurate passes', value=0)
    feature7 = st.number_input('Start_minutes', value=0)
    feature8 = st.number_input('End_minutes', value=0)

    # Button for predictions
    clicked = st.button('Get Predictions')

    # Perform predictions when the button is clicked
    if clicked:
        # Perform predictions using the selected model
        prediction = model.predict([[feature1, feature2, feature3, feature4, feature5, feature6, feature7,feature8]])
        if prediction[0] == 0:
            ss = "Home Win"
        elif prediction[0] == 1:
            ss = "Draw"
        else:
            ss = "Away Win"
        # Display the prediction result
        st.header('Prediction')
        st.write(f'The prediction result is: {ss}')

if __name__ == '__main__':
    main()