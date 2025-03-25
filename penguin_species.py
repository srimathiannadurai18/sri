import streamlit as st
import pickle



def get_culmen_length():
    culmen_length = st.text_input("Culmen Length of Penguin")
    return culmen_length

def get_culmen_depth():
    culmen_depth = st.text_input("Culmen depth of Penguin")
    return culmen_depth

def get_flipper_length():
    flipper_length = st.text_input("Flipper Length")
    return flipper_length

def get_body_mass():
    body_mass = st.text_input("Body Mass")
    return body_mass

def get_island_dream():
    island_dream = st.text_input("Dream Island")
    return island_dream

def get_island_torgersen():
    island_torgersen = st.text_input("Torgersen Island")
    return island_torgersen

def get_island_female():
    island_female = st.text_input("Female")
    return island_female

def get_island_male():
    island_male = st.text_input("Male")
    return island_male 

def predict_species(cl,cd,fl,bm,id,it,fem,mal):
    loaded_model = pickle.load(open('decision_tree_model.pkl','rb'))
    new_data = [[float(cl),float(cd),float(fl),float(bm),float(id),float(it),float(fem),float(mal)]]
    prediction = loaded_model.predict(new_data)
    st.write("Prediction with new data: ")
    st.write(prediction)
    



if __name__ == "__main__":
    st.title('Penguin Species prediction with Decision Tree model 2025')
    st.image('penguin.png')    
    culmen_length_value = get_culmen_length()
    culmen_depth_value = get_culmen_depth()
    flipper_length = get_flipper_length()
    body_mass = get_body_mass()
    island_dream = get_island_dream()
    island_torgersen = get_island_torgersen()
    island_female = get_island_female()
    island_male = get_island_male()
    st.write("The parameters you entered are: ")
    st.write("Culmen length ", culmen_length_value)
    st.write("Culmen depth ", culmen_depth_value)
    st.write("Flipper length ", flipper_length)
    st.write("Body mass ", body_mass)
    st.write("Dream Island ", island_dream)
    st.write("Torgensen Island ", island_torgersen)
    st.write("Female ", island_female)
    st.write("Male ", island_male)


if st.button("Predict"):
    predict_species(culmen_length_value,culmen_depth_value,flipper_length,body_mass,island_dream,island_torgersen,island_female,island_male)
    
