import streamlit as st
import pickle

# Function to select the product type
def get_product_type():
    product_type = st.selectbox("Select Product Type", ["Cosmetics", "Pharmaceuticals", "Electronics", "Food"])
    return product_type

# Function to select the material type
def get_material_type():
    material_type = st.selectbox("Select Material Type", ["HDPE", "PET", "Glass", "PLA"])
    return material_type

# Function to input storage temperature
def get_storage_temperature():
    storage_temperature = st.selectbox("Select Storage Temperature (°C)", ["15-25", "30", "100", "-20"])
    return storage_temperature

# Function to input storage humidity
def get_storage_humidity():
    storage_humidity = st.slider("Select Storage Humidity (%)", min_value=0, max_value=100, step=5)
    return storage_humidity

# Function to make a prediction using the decision tree model
def predict_shelf_life(product_type, material_type, temperature, humidity):
    # Load the trained model
    loaded_model = pickle.load(open('decision_tree_model.pkl', 'rb'))
    
    # Convert input data to numerical format expected by the model
    product_dict = {"Cosmetics": 0, "Pharmaceuticals": 1, "Electronics": 2, "Food": 3}
    material_dict = {"HDPE": 0, "PET": 1, "Glass": 2, "PLA": 3}
    temp_dict = {"15-25": 0, "30": 1, "100": 2, "-20": 3}

    new_data = [[product_dict[product_type], material_dict[material_type], temp_dict[temperature], float(humidity)]]

    # Use the model to predict the shelf life
    prediction = loaded_model.predict(new_data)
    return prediction[0]

# Main streamlit app
if __name__ == "__main__":
    st.title('Shelf Life Prediction for Packaged Products')
    st.image('packaging_image.png')  # Add an image for illustration

    # Get user inputs
    product_type = get_product_type()
    material_type = get_material_type()
    storage_temperature = get_storage_temperature()
    storage_humidity = get_storage_humidity()

    st.write("You selected:")
    st.write(f"Product Type: {product_type}")
    st.write(f"Material Type: {material_type}")
    st.write(f"Storage Temperature: {storage_temperature}°C")
    st.write(f"Storage Humidity: {storage_humidity}%")

    # Predict shelf life when the "Predict" button is clicked
    if st.button("Predict Shelf Life"):
        shelf_life = predict_shelf_life(product_type, material_type, storage_temperature, storage_humidity)
        st.write(f"Predicted Shelf Life: {shelf_life} days")
