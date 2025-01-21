
from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# # Load the trained RandomForestClassifier model
# with open('random_forest_model.pkl', 'rb') as file:
#     model_rf = pickle.load(file)


# Load the trained RandomForestClassifier model
with open('trained_model.pkl', 'rb') as f:
    model_rf = pickle.load(f)


with open('NAME_CONTRACT_TYPELE.pickle', 'rb') as f:
    name_contract_type_encoder = pickle.load(f)

with open('CODE_GENDERLE.pickle', 'rb') as f:
    code_gender_encoder = pickle.load(f)

with open('NAME_INCOME_TYPELE.pickle', 'rb') as f:
    name_income_type_encoder = pickle.load(f)

with open('NAME_EDUCATION_TYPELE.pickle', 'rb') as f:
    name_education_type_encoder = pickle.load(f)

with open('NAME_HOUSING_TYPELE.pickle', 'rb') as f:
    name_housing_type_encoder = pickle.load(f)

with open('ORGANIZATION_TYPELE.pickle', 'rb') as f:
    organization_type_encoder = pickle.load(f)


# Define route for home page
@app.route('/')
def home():
    return render_template('user_form.html')

# Route for the project overview page
@app.route('/overview')
def overview():
    # Redirect to the project overview page
    return render_template('overview.html')

# Route for the members page
@app.route('/members')
def members():
    # Redirect to the members page
    return render_template('members.html')


# Define route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Load pickled encoders

    # Load the trained RandomForestClassifier model
    # with open('trained_model.pkl', 'rb') as file:
    #     model_rf = pickle.load(file)


    # with open('NAME_CONTRACT_TYPELE.pickel', 'rb') as f:
    #     name_contract_type_encoder = pickle.load(f)

    # with open('CODE_GENDERLE.pickel', 'rb') as f:
    #     code_gender_encoder = pickle.load(f)

    # with open('NAME_INCOME_TYPELE.pickel', 'rb') as f:
    #     name_income_type_encoder = pickle.load(f)

    # with open('NAME_EDUCATION_TYPELE.pickel', 'rb') as f:
    #     name_education_type_encoder = pickle.load(f)

    # with open('NAME_HOUSING_TYPELE.pickel', 'rb') as f:
    #     name_housing_type_encoder = pickle.load(f)

    # with open('ORGANIZATION_TYPELE.pickel', 'rb') as f:
    #     organization_type_encoder = pickle.load(f)



    
    # Get user input from form
    input_data = [
        int(request.form['region_rating_client_w_city']), 
        int(request.form['region_rating_client']),        
        int(request.form['reg_city_not_work_city']),      
        name_education_type_encoder.transform([request.form['name_education_type']])[0],              
        code_gender_encoder.transform([request.form['code_gender']])[0],                      
        name_income_type_encoder.transform([request.form['name_income_type']])[0],                 
        int(request.form['flag_emp_phone']),              
        int(request.form['reg_city_not_live_city']),      
        int(request.form['flag_document_3']),             
        name_housing_type_encoder.transform([request.form['name_housing_type']])[0],                
        int(request.form['live_city_not_work_city']),     
        name_contract_type_encoder.transform([request.form['name_contract_type']])[0],               
        organization_type_encoder.transform([request.form['organization_type']])[0],                
        float(request.form['region_population_relative']), 
        float(request.form['days_registration']),         
        int(request.form['days_employed']),               
        int(request.form['days_id_publish']),             
        float(request.form['days_last_phone_change']),   
        int(request.form['days_birth'])                  
    ]
    print(input_data)
    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data], columns=[ 'REGION_RATING_CLIENT_W_CITY', 'REGION_RATING_CLIENT',
                                                'REG_CITY_NOT_WORK_CITY', 'NAME_EDUCATION_TYPE', 'CODE_GENDER',
                                                'NAME_INCOME_TYPE', 'FLAG_EMP_PHONE', 'REG_CITY_NOT_LIVE_CITY',
                                                'FLAG_DOCUMENT_3', 'NAME_HOUSING_TYPE', 'LIVE_CITY_NOT_WORK_CITY',
                                                'NAME_CONTRACT_TYPE', 'ORGANIZATION_TYPE', 'REGION_POPULATION_RELATIVE',
                                                'DAYS_REGISTRATION', 'DAYS_EMPLOYED', 'DAYS_ID_PUBLISH',
                                                'DAYS_LAST_PHONE_CHANGE', 'DAYS_BIRTH'])

    # Make prediction using the model
    prediction = model_rf.predict(input_df)[0]

    
    # Render predict.html template with prediction value
    return render_template('predict.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)


