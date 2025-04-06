import streamlit as st # importing python library

st.set_page_config(
    page_title="Converto", 
    page_icon="transfer.png",
    layout="wide"
)

# Custom CSS
# Custom CSS with light yellow theme
st.markdown("""
<style>
    /* Main app background */
    .stApp {
        background-color:rgb(255, 234, 0);  /* Soft light yellow */
    }
    
    /* Content container */
    .main {
        background-color: #fffde7;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #1565c0;
        font-family: 'Arial', sans-serif;
    }
    
    /* Select boxes */
    .stSelectbox {
        background-color: white;
        padding: 5px;
        
    }
    .stSelectbox label {
        color: #0d47a1;
        font-weight: bold;
        font-size: 1.1rem;
    }
    
    /* Number input */
    .stNumberInput {
        background-color: white;
    }
    .stNumberInput label {
        color: #0d47a1;
        font-weight: bold;
        font-size: 1.1rem;
    }
    
    /* Button */
    .stButton>button {
        background-color: #1976d2;
        color: white;
        font-weight: bold;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 8px;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #0d47a1;
        transform: scale(1.02);
    }
    
    /* Result box */
    .stAlert {
        background-color: #e3f2fd;
        border-radius: 8px;
        padding: 1rem;
    }
    
    /* Input fields */
    .stTextInput input, .stNumberInput input {
        background-color: white;
        color: #333;
    }
</style>
""", unsafe_allow_html=True)
  
def input():
    # Initialize session state
    if 'input_valid' not in st.session_state:
        st.session_state.input_valid = False
        st.session_state.input_value = 0.0
    
    # Input field (will show previous value if any)
    value = st.number_input(
        "Enter a positive value:")
    
    # Validation and messaging
    if value <= 0:
        # st.warning("Please enter a value greater than zero!")
        st.session_state.input_valid = False
    else:
        st.session_state.input_valid = True
        st.session_state.input_value = value
    
    # Only proceed when valid
    if not st.session_state.input_valid:
        st.stop()  # Pauses execution here until valid input
    
    return st.session_state.input_value
def temp_convert(value, from_unit, to_unit):
    # Convert to Celsius first
    if from_unit == "FAHRENHEIT":
        celsius = (value - 32) * 5/9
    elif from_unit == "KELVIN":
        celsius = value - 273.15
    elif from_unit == "RANKINE":
        celsius = (value - 491.67) * 5/9
    else:  # Celsius
        celsius = value
    
    # Convert from Celsius to target unit
    if to_unit == "FAHRENHEIT":
        result = (celsius * 9/5) + 32
    elif to_unit == "KELVIN":
        result = celsius + 273.15
    elif to_unit == "RANKINE":
        result = (celsius + 273.15) * 9/5
    else:  # Celsius
        result = celsius
    
    return result
def length_convert(value, from_unit, to_unit):
    # Convert to meters first (base unit)
    if from_unit == "Kilometer":
        meters = value * 1000
    elif from_unit == "METER":
        meters = value * 1
    elif from_unit == "CENTIMETER":
        meters = value * 0.01
    elif from_unit == "MILES":
        meters = value * 1609.34
    elif from_unit == "FOOT":
        meters = value * 0.3048
    elif from_unit == "INCH":
        meters = value * 0.0254
    elif from_unit == "YARD":
        meters = value * 0.9144
    else:
        meters = value  # fallback
    
    # Convert from meters to target unit
    if to_unit == "Kilometer":
        result = meters / 1000
    elif to_unit == "METER":
        result = meters / 1
    elif to_unit == "CENTIMETER":
        result = meters / 0.01
    elif to_unit == "MILES":
        result = meters / 1609.34
    elif to_unit == "FOOT":
        result = meters / 0.3048
    elif to_unit == "INCH":
        result = meters / 0.0254
    elif to_unit == "YARD":
        result = meters / 0.9144
    else:
        result = meters 
    
    return result
def area_convert(value, from_unit, to_unit):
    # Conversion factors to square meters (base unit)
    factors = {
        # Metric units
        "SQUARE KILOMETER": 1_000_000,
        "SQUARE METER": 1,
        "SQUARE CENTIMETER": 0.0001,
        "HECTARE": 10_000,
        "ARE": 100,
        
        # Imperial units
        "SQUARE MILE": 2_589_988,
        "SQUARE FOOT": 0.092903,
        "SQUARE INCH": 0.00064516,
        "SQUARE YARD": 0.836127,
        "ACRE": 4_046.86
    }
    
    # Convert to square meters first
    sq_meters = value * factors[from_unit]
    
    # Convert from square meters to target unit
    result = sq_meters / factors[to_unit]
    
    return result

def area_unit_selection():
    from_unit = st.selectbox(
            "FROM:",
            ["SQUARE KILOMETER", "SQUARE METER", "HECTARE", "ACRE", "SQUARE MILE", "SQUARE FOOT", "SQUARE YARD"]
        )
    to_unit = st.selectbox(
            "TO:",
             ["SQUARE KILOMETER", "SQUARE METER", "HECTARE", "ACRE","SQUARE MILE", "SQUARE FOOT", "SQUARE YARD"]
        )
    return from_unit, to_unit

def volume_convert(value, from_unit, to_unit):
    # Conversion factors to liters (base unit)
    factors = {
        # Metric units
        "CUBIC METER": 1000,
        "LITER": 1,
        "MILLILITER": 0.001,
        "CUBIC CENTIMETER": 0.001,
        "CUBIC KILOMETER": 1e12,
        # Imperial units
        "GALLON": 3.78541,
        "QUART": 0.946353,
        "PINT": 0.473176,
        "CUP": 0.236588,
        "FLUID OUNCE": 0.0295735,
        "CUBIC FOOT": 28.3168,
        "CUBIC INCH": 0.0163871,
        "BARREL": 158.987
    }
    
    # Convert to liters first
    liters = value * factors[from_unit]
    
    # Convert from liters to target unit
    result = liters / factors[to_unit]
    
    return result

def volume_unit_selection():

        from_unit = st.selectbox(
            "FROM:",
            ["CUBIC METER","LITER","MILLILITER","GALLON","QUART","PINT","CUP","FLUID OUNCE"]
        )
        to_unit = st.selectbox(
            "TO:",
            ["CUBIC METER","LITER","MILLILITER","GALLON","QUART","PINT","CUP","FLUID OUNCE"]
        )
        return from_unit, to_unit

def length_unit_selection():
    from_unit = st.selectbox(
        "FROM:",
        ["Kilometer", "METER", "CENTIMETER", "MILES", "FOOT", "INCH", "YARD"]
    )
    to_unit = st.selectbox(
        "To:",
        ["Kilometer", "METER", "CENTIMETER", "MILES", "FOOT", "INCH", "YARD"]
    )
    return from_unit, to_unit
def weight_convert(value, from_unit, to_unit):
    # Conversion factors to grams (base unit)
    factors = {
        # Metric units
        "KILOGRAM": 1000,
        "GRAM": 1,
        "MILLIGRAM": 0.001,
        "METRIC TON": 1_000_000,
        "CARAT": 0.2,
        # Imperial/US units
        "POUND": 453.592,
        "OUNCE": 28.3495,
        "STONE": 6350.29,
        "TON (US)": 907_185,
        "TON (UK)": 1_016_047
    }
    
    # Convert to grams first
    grams = value * factors[from_unit]
    
    # Convert from grams to target unit
    result = grams / factors[to_unit]
    
    return result

def weight_unit_selection():
        
    from_unit = st.selectbox(
        "FROM:",
        ["KILOGRAM","GRAM","POUND","OUNCE","TON(US)","TON(UK)","STONE","CARAT"]
    )
    to_unit = st.selectbox(
        "TO:",
        ["KILOGRAM","GRAM","POUND","OUNCE","TON (US)","TON (UK)","STONE","CARAT"]
    )
    return from_unit, to_unit
def time_convert(value, from_unit, to_unit):
    # Conversion factors to seconds (base unit)
    factors = {
        "NANOSECOND": 1e-9,
        "MICROSECOND": 1e-6,
        "MILLISECOND": 0.001,
        "SECOND": 1,
        "MINUTE": 60,
        "HOUR": 3600,
        "DAY": 86400,
        "WEEK": 604800,
        "MONTH": 2_629_746,  # Average month (365.2425/12 days)
        "YEAR": 31_556_952,  # Julian year (365.2425 days)
        "DECADE": 315_569_520,
        "CENTURY": 3_155_695_200
    }
    
    # Convert to seconds first
    seconds = value * factors[from_unit]
    
    # Convert from seconds to target unit
    result = seconds / factors[to_unit]
    
    return result

def time_unit_selection():
    from_unit = st.selectbox(
            "FROM:",
            ["SECOND", "MINUTE", "HOUR", "DAY", 
             "WEEK", "MONTH", "YEAR", "DECADE"]
    )

    to_unit = st.selectbox(
            "TO:",
            ["SECOND","MINUTE","HOUR", "DAY","WEEK", "MONTH", "YEAR", "DECADE"]
    )
    return from_unit, to_unit

def temp_unit_selection():
    from_unit = st.selectbox(
    "FROM:",
    ["FAHRENHEIT", "KELVIN", "CELSIUS", "RANKINE"]
    )
    to_unit = st.selectbox(
    "TO:",
    ["FAHRENHEIT", "KELVIN", "CELSIUS", "RANKINE"]
    )
    return from_unit,to_unit
st.title("welcome to converto App")
if __name__=="main":

# Create a single-select dropdown
 st.header("QUANTITIES")
Quantities = st.selectbox(
    " Select From Given Quantities:",
    ["LENGTH", "AREA", "TEMPERATURE", "VOLUME", "WEIGHT", "TIME"]
)

if Quantities == "LENGTH":
    from_unit, to_unit = length_unit_selection()   
elif Quantities == "TEMPERATURE":
    from_unit, to_unit = temp_unit_selection()
elif Quantities=="AREA":
    from_unit, to_unit = area_unit_selection()
elif Quantities=="VOLUME":
    from_unit, to_unit = volume_unit_selection()
elif Quantities=="WEIGHT":
    from_unit, to_unit = weight_unit_selection()
elif Quantities=="TIME":
    from_unit, to_unit = time_unit_selection()

value=input()
if st.button("Convert"):
    if Quantities == "TEMPERATURE":
        
        result=temp_convert(value, from_unit, to_unit)
        st.success(f"Converted value: {result:.4f} {to_unit}")
    
    elif Quantities == "LENGTH":
        result=length_convert(value,from_unit,to_unit)
        st.success(f"Converted value: {result:.4f} {to_unit}")
    elif Quantities =="AREA":
        result=area_convert(value,from_unit,to_unit)
        st.success(f"Converted value: {result:.4f} {to_unit}")     
    elif Quantities=="VOLUME":
        result=volume_convert(value,from_unit,to_unit)
        st.success(f"Converted value: {result:.4f} {to_unit}") 
    elif Quantities=="WEIGHT":
        result=weight_convert(value,from_unit,to_unit)
        st.success(f"Converted value: {result:.4f} {to_unit}")    
    elif Quantities=="TIME":
        result=time_convert(value,from_unit,to_unit)
        st.success(f"Converted value: {result:.4f} {to_unit}")    
