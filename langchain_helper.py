import os
from langchain.llms.openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import LLMChain,SimpleSequentialChain
from langchain.chains import SequentialChain
from dotenv import load_dotenv

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

llm = OpenAI(temperature = 0.6)

def generate_response(text):

    prompt_template1 = PromptTemplate(
        input_variables = ['text'],
        template = "who is the father of {text} music industry?"
    )

    chain1 = LLMChain(llm = llm, prompt=prompt_template1, output_key="artist_name")

    prompt_template2 = PromptTemplate(
        input_variables = ['artist_name'],
        template = "who is the date of birth of {artist_name}?"
    )

    chain2 = LLMChain(llm = llm ,prompt=prompt_template2, output_key="dob")

    chain = SequentialChain(
        chains = [chain1,chain2],
        input_variables = ['text'],
        output_variables = ['artist_name','dob']
    )
    response =  chain({'text':text})

    return response


