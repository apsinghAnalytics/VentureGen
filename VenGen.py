import streamlit as st
import langchain_helper as lh
import user_input_list as ui
from PIL import Image
from annotated_text import annotated_text

# Set up the page layout and title
st.set_page_config(page_title="VentureGen", page_icon='rocket.png', layout="wide")

# Load your background image
background_image = Image.open('background.png')  # Replace 'path_to_your_image.png' with the path to your image file

# Create a container for the sidebar
with st.sidebar:
    generateButton = st.button("Generate :bulb:")
    industry1 = st.selectbox("Pick the First Industry", ui.industry_list)
    industryList2 = [industry for industry in ui.industry_list if industry1 not in industry]
    industry2 = st.selectbox("Pick the Second Industry", industryList2)
    industryList3 = [industry for industry in industryList2 if industry2 not in industry]
    industry3 = st.selectbox("Pick the Third Industry", industryList3)
    st.markdown("<br><br><br>&copy; Aditya Prakash Singh", unsafe_allow_html=True) # Add the copyright symbol

finalIndustryList = [industry for industry in [industry1, industry2, industry3] if 'None' not in industry]
# Create containers for the main content
with st.container():
    col1, col2 = st.columns([4, 2])  # Adjust the width ratio as needed
    # In the first column, display the background image
    with col1:
        st.image(background_image, use_column_width=True, caption= "generated using DALL·E 3")
        
    # In the second column, place the title and annotated text
    with col2:
        st.write("### VentureGen :rocket: \n")
        st.write("#### A startup name and pitch generator :brain: \n\n")
        annotated_text(
            "Hi there! This",
            ("app", "Proof of Concept", "black"),
            "powered by ",
            ("Langchain", "LLM App Framework", "green"),
            " and ",
            ("GPT 3.5 Turbo", "OpenAI LLM", "grey"),
            ", lets the user to ",
            ("generate ", "brainstorm", "orange"),
            " a compelling name and ",
            ("pitch", "summary", "brown"),
            " for a ",
            ("startup", "hypothetical", "magenta"),
            " at the intersection of selected industries.\n\n",
            
        )

        # Display copyright, name, and GitHub link 
        st.markdown("""
        <p style='text-align: left;'>
            © Aditya Prakash Singh
            <a href="https://github.com/apsinghAnalytics/streamlit_VentureGen" target="_blank">
                <img src="https://simpleicons.org/icons/github.svg" alt="GitHub" style="height:24px; display:inline-block; vertical-align: middle;">
            </a>
        </p>
        """, unsafe_allow_html=True)


if generateButton:
   response= lh.generate_startup_name_pitch(finalIndustryList)
   
   # Split the response string into paragraphs
   paragraphs = [paragraph.strip() for paragraph in response.split('\n\n') if paragraph.strip()]
   
   if ":" in paragraphs[0]:
    split_result= paragraphs[0].split(":", 1) # The first paragraph containing the startup name is split
    paragraphs[0]= split_result[1]  # the "Startup Name:" string is removed
   
   if ":" in paragraphs[1]:
     split_result= paragraphs[1].split(":", 1) # The second paragraph containing the "Pitch:" string is split
     paragraphs[1]= ":microphone:" +":chart_with_upwards_trend:" + split_result[1] #  "Pitch:" string is removed and replaced by upward chart and microphone emoji
    
   st.write(f"##### :rocket: {paragraphs[0]}") # Outputs the startup Name with rocket logo to the app 
   
   paragraphs[1]= ":chart_with_upwards_trend:"+ ":microphone:"+ split_result[1] #  "Pitch:" string is removed

   for i, paragraph in enumerate(paragraphs[1:], start=2): #
     st.write(f"\n > {paragraph}\n") #blockquotes each of the pitch paragraphs




