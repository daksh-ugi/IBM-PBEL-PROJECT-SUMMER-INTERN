import streamlit as st
import pandas as pd
import joblib

# CSS
def inject_bw_css():
    css = """
    body, .stApp {
        background: linear-gradient(110deg, #111 0%, #222 100%);
        color: #ededed !important;
        font-family: 'Inter', 'Segoe UI', Arial, sans-serif;
        min-height: 100vh;
    }
    .glass-card {
        background: rgba(30,30,30,0.86);
        border-radius: 18px;
        border: 2.5px solid #333;
        padding: 39px 34px 39px 37px;
        margin-bottom: 38px;
        backdrop-filter: blur(14.5px);
        position: relative; overflow: hidden; min-width: 220px;
    }
    
    @keyframes fadeInUp {
        0%{opacity:0;transform:translateY(24px);}
        100%{opacity:1;transform:translateY(0);}
    }
 
    /* Hide spinners/arrows */
    input[type=number]::-webkit-inner-spin-button, 
    input[type=number]::-webkit-outer-spin-button {
        -webkit-appearance: none;
        margin: 0;
    }
    input[type=number] {
        -moz-appearance: textfield;
    }
    .stNumberInput button {
        display: none !important;
    }

    input:invalid, .stTextInput input:invalid, .stTextInput input[aria-invalid="true"],
    .stTextInput input:focus:invalid, .stTextInput input:focus[aria-invalid="true"] {
        border-color: #333 !important;
        box-shadow: none !important;
        outline: none !important;
        background: inherit !important;
    }
    """
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

inject_bw_css()

# Model
@st.cache_resource(show_spinner=True)
def load_model_features():
    model = joblib.load("model.pkl")
    features = joblib.load("features.pkl")
    return model, features
model, features = load_model_features()

# Placeholder
def numeric_text_input(label, placeholder, min_value, max_value, key):
    user_val = st.text_input(label, value="", placeholder=placeholder, key=key)
    if user_val.strip() == "":
        return None  
    try:
        val = float(user_val)
        if min_value is not None and val < min_value:
            st.warning(f"Value must be ≥ {min_value}")
            return None
        if max_value is not None and val > max_value:
            st.warning(f"Value must be ≤ {max_value}")
            return None
        return val
    except ValueError:
        st.warning("Please enter a valid number")
        return None

# UI
st.markdown(' <h1 style="text-align:center; margin-top: 12px;">₹ Salary Prediction</h1>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="glass-card" style="position:relative;><div class="glass-card">'
    ' <pre>Every pro was once an amateur. Every expert was once a beginner. So dream big and start now.</pre>'
    ' </div>', unsafe_allow_html=True)
    
    st.markdown('**Step 1 : – Enter Numeric Details**')
    c1, c2 = st.columns(2)
    with c1:
        years_exp = numeric_text_input("Years of Experience", "e.g. 5.0", 0.0, 50.0, "years_exp_input")
        age = numeric_text_input("Your Age", "e.g. 25", 18, 100, "age_input")
    with c2:
        certifications = numeric_text_input("Certifications", "e.g. 3", 0, 200, "certifications_input")
        working_hours = numeric_text_input("Weekly Working Hours", "e.g. 40", 1, 168, "working_hours_input")

    st.markdown('**Step 2 : – Select Your Background**')
    categories = {
        "education_level": ["--","High School", "PhD", "Bachelors", "Masters"],
        "job_title": ["--","Data Scientist", "Software Engineer", "Analyst", "Manager"],
        "industry": ["--","Education", "IT", "Healthcare", "Finance"],
        "location": ["--","New York", "London", "Bangalore", "San Francisco"],
        "company_size": ["--","Small", "Medium", "Large"],
    }
    cc1, cc2, cc3 = st.columns(3)
    cat_inputs = {}
    with cc1:
        cat_inputs["education_level"] = st.selectbox("Education Level", categories["education_level"])
        cat_inputs["industry"] = st.selectbox("Industry", categories["industry"])
    with cc2:
        cat_inputs["job_title"] = st.selectbox("Job Title", categories["job_title"])
        cat_inputs["location"] = st.selectbox("Location", categories["location"])
    with cc3:
        cat_inputs["company_size"] = st.selectbox("Company Size", categories["company_size"])

    ready = (
        years_exp is not None and certifications is not None and 
        age is not None and working_hours is not None and
        cat_inputs["education_level"] != "--" and
        cat_inputs["job_title"] != "--" and
        cat_inputs["industry"] != "--" and
        cat_inputs["location"] != "--" and
        cat_inputs["company_size"] != "--"
    )

    if ready:
        numerical_inputs = {
            "years_experience": years_exp,
            "certifications": certifications,
            "age": age,
            "working_hours": working_hours,
        }
        row = {**numerical_inputs}
        for col, val in cat_inputs.items():
            for option in categories[col]:
                row[f"{col}_{option}"] = 1 if val == option else 0
        input_df = pd.DataFrame([row])
        for col in features:
            if col not in input_df.columns:
                input_df[col] = 0
        input_df = input_df[features]
    else:
        input_df = None

    clicked = st.button("Predict Salary", disabled=not ready, help="Complete all fields to enable prediction.")

    if clicked and input_df is not None:
        with st.spinner("Calculating..."):
            salary = model.predict(input_df)[0]
        st.success(f"💰 Estimated Salary: ₹ {salary:,.2f}")
        avg_salaries = {
            ("Data Scientist", "IT"): 120000,
            ("Software Engineer", "IT"): 100000,
            ("Analyst", "Finance"): 90000,
            ("Manager", "Healthcare"): 110000,
        }
        avg = avg_salaries.get((cat_inputs["job_title"], cat_inputs["industry"]))
        if avg is not None:
            diff = salary - avg
            compare_html = f"""
            <div class="compare-chip">
                <span>{'↑' if diff > 0 else ('↓' if diff < 0 else '')}</span>
                <span>{'Above' if diff>0 else ('Below' if diff<0 else 'At')} Avg.</span>
                <span>₹ {abs(diff):,.0f}</span>
            </div>
            """
            st.markdown(compare_html, unsafe_allow_html=True)
            if diff > 0:
                st.success(f"↑ ₹ {diff:,.0f} above average salary.")
            elif diff < 0:
                st.info(f"↓ ₹ {abs(diff):,.0f} below average salary.")
            else:
                st.info("You're right at the average salary.")
        else:
            st.info("No comparison data for this combo.")
    else:
        st.info("Enter all fields and hit Predict.")

    st.markdown('</div>', unsafe_allow_html=True)

