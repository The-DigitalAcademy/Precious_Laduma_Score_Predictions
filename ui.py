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
    
    # feature1 = st.selectbox(label='Choose your Home Team ',options=['Antennae', 'Andromeda', 'Butterfly', 'Cartwheel', 'Sculptor',
    #    'Cigar', 'Comet', 'Cosmos Redshift 7', 'Eye of Sauron',
    #    'Medusa Merger', 'Milky Way', 'Sunflower', 'Tadpole', 'Fireworks',
    #    'Backward', 'Circinus', 'Coma Pinwheel', 'Sombrero', 'Triangulum'])
    CHOICES1={0:'Antennae',1: 'Andromeda',2: 'Butterfly',3: 'Cartwheel', 4:'Sculptor',
       5:'Cigar',6: 'Comet', 7:'Cosmos Redshift 7',8: 'Eye of Sauron',
       9:'Medusa Merger',10: 'Milky Way',11: 'Sunflower', 12:'Tadpole', 13:'Fireworks',
       14:'Backward',15: 'Circinus',16: 'Coma Pinwheel', 17:'Sombrero', 18:'Triangulum'}

    def format_func(option):
    
        return CHOICES1[option]
    
    feature1 = st.selectbox("Choose your Home Team", options=list(CHOICES1.keys()), format_func=format_func)
    
    CHOICES={0:'Andromeda',1: 'Antennae',2: 'Butterfly',3: 'Cigar', 4:'Circinus',
       5:'Cartwheel',6: 'Coma Pinwheel', 7:'Comet',8: 'Cosmos Redshift 7',
       9:'Fireworks',10: 'Medusa Merger',11: 'Milky Way', 12:'Backward', 13:'Sculptor',
       14:'Sunflower',15: 'Triangulum',16: 'Eye of Sauron', 17:'Tadpole', 18:'Sombrero'}

    def format_func(option):
    
        return CHOICES[option]
    
    feature2 = st.selectbox("Choose your Away Team", options=list(CHOICES.keys()), format_func=format_func)

 
    feature3 = st.number_input('Shots on Target', value=0)
    feature4 = st.number_input('Goals Scored', value=0)
    feature5 = st.number_input('Goals Concided', value=0)
    feature6 = st.number_input('Accurate Passes', value=0)
    feature7 = st.number_input('Inaccutate Passes', value=0)

    # Button for predictions
    clicked = st.button('Get Predictions')

    # Perform predictions when the button is clicked
    if clicked:
        # Perform predictions using the selected model
        prediction = model.predict([[feature1, feature2, feature3, feature4, feature5, feature6, feature7]])
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