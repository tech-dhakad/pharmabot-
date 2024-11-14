
import streamlit as st 
from langchain_ollama import ChatOllama 

# Dictionary to hold user details
user_data = {
    "name":"Guest",
    "age":"",
    "gender":"",
    "disease":""
}

# Collect user information
with st.sidebar: # Using slidbar for user inputs
    st.header("User Details")
    user_data["name"] = st.text_input("Name:", "Guest")
    user_data["age"] = st.text_input("Age:")
    user_data["gender"] = st.selectbox("Gender:", ["Select","Male", "Female", "Other"])         
    user_data["disease"] = st.selectbox("Disease:",["Select","Blood Cancer","Heart Attack","Depression","Diabetes"])

# Displaying users information as a personalized dashboard
st.image(r"C:\users\Kamlesh\Downloads\hackathon.jpg")
st.title("Pharmabot 🤖") 

# Personalized greeting
st.subheader(f"Hello,{user_data['name']}!👋")
st.write(f"Age:- {user_data['age']}")
st.write(f"Gender:- {user_data['gender']}")
st.write(f"Disease:-{user_data['disease']}") 

st.markdown("___") # line brake to searate dashboard from chat area

# Predefined Q&A for quick responses
predefined_qna = {
    "hi":"Hello. How may I help you",
    "Hi":"Hello. How may I help you",
    "what is your name":"My name is Pharmabot",
    "What is your name":"My name is Pharmabot",
} 

# C ustom CSS for styling
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        transition: background-color
0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextInout>div>div>textarea {
        border: 2px solid #4CAF50;
        border-radius: 8px;
        padding: 10px;
    }
    .typing-indicator {
        display: inline-block;
        width: 8px;
        height: 8px;
        background: 50%;
        animation: blink 1.4s
infinite both;
        margin-left: 3px;
    }
    @keyframes blink {
        0%, 100% { opacity: 0; }
        50% { opacity: 1; }            
    }
    </style>
    """, unsafe_allow_html=True)    

# Display a greeting message    
st.write("👋 Hello! I'm Pharmabot. How can I assist you today?")

# Chat form for user input
with st.form("llm-form"):
    text = st.text_area("Enter Your Question")
    submit = st.form_submit_button("Submit")

# Define function to generate responses
def generate_response(input_text):
    model = ChatOllama(model="llama3.2:1b", base_url="http://localhost:11434/")
    try:
        response = model.invoke(input_text)
        return response.content 
    except Exception as e:
        return f"Error generating response: {e}"

# Process submission
if submit and text:
    normalized_text = text.strip().lower() 
    response = predefined_qna.get(normalized_text) 
    print("Normalized_text:",normalized_text)

    if response:
        st.write(response)
    else:

        with st.spinner("Pharmabot is typing..."):
            response = generate_response(text)
            st.write(response)
            
        
        




    

    
