from creds import openapi_key # Stores my personal OpenAI API Key
import os 
os.environ['OPENAI_API_KEY']= openapi_key

from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

chat = ChatOpenAI(model_name='gpt-3.5-turbo-1106', temperature= 0.6)

def generate_startup_name_pitch(finalIndustryList):
    
    # Defining the prompts
    template = (
        "You are a creative and knowledgeable assistant. I will provide you with a list of industries, and you will brainstorm and provide me with a compelling startup name, and a 200 word pitch of a startup at the intersection of these industries. Focus on business model, innovation, market potential, and uniqueness in the proposed startup"
    )
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    human_template = "{text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    #get a chat completion from the formatted messages
    response= chat(
        chat_prompt.format_prompt(text=str(finalIndustryList)).to_messages() 
    )    
    return response.content  

if __name__ == "__main__":
    print(generate_startup_name_pitch(["Tobacco", "Diagnostics & Research", "Credit Services"]))

