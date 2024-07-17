from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_cohere.llms import Cohere
import os

from Linkedin_Lookup.Linkedin_Lookup_Agent import lookup
from Third_Parties.Linkedin_Summary import scrape_linkedin_profile


linkedin_URL = lookup(name="Albin_sabu_Germany_bavaria_FAU_Electromobility_sagar_enterprises ")

print('found it', linkedin_URL)

if __name__ == "__main__":
    load_dotenv()

    print("Hello LangChain")

    summary_template = """
    given the  linkedin information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    3. analyze profile for Project Management in production job and give ranking from 0 to 100(only number no extra information)
    4. chances of getting hired by top tier companies (yes or no)
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = Cohere(temperature=0, max_tokens=1000)
    chain = summary_prompt_template | llm
    print('happening')
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_URL, mock=False)
    res = chain.invoke(input={"information": linkedin_data})
    print(res)
