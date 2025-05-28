from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain.schema.runnable import RunnableBranch, RunnableLambda

# 1. Load environment variables
load_dotenv()

# 2. Initialize the Groq LLM (LLaMA3 8B)
model = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192"
)

# 3. Define structured output schema using Pydantic
class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description='Sentiment of the feedback')

# 4. Set up the Pydantic output parser
parser = PydanticOutputParser(pydantic_object=Feedback)

# 5. Define the prompt template with explicit JSON-only instruction
prompt = PromptTemplate(
    template=(
        "Classify the sentiment of the following feedback text into 'positive' or 'negative'.\n"
        "Respond ONLY with a JSON object exactly matching the format below and nothing else:\n"
        "{format_instructions}\n\n"
        "Feedback text:\n{feedback}"
    ),
    input_variables=["feedback"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# 6. Create the LangChain chain
classifier_chain = prompt | model | parser

# 7. Define follow-up prompts for positive and negative feedback responses
prompt_positive = PromptTemplate(
    template='Write an appropriate response to this positive feedback:\n{feedback}',
    input_variables=['feedback']
)

prompt_negative = PromptTemplate(
    template='Write an appropriate response to this negative feedback:\n{feedback}',
    input_variables=['feedback']
)


# 8. Branching logic based on sentiment classification
branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt_positive | model | parser),
    (lambda x: x.sentiment == 'negative', prompt_negative | model | parser),
    RunnableLambda(lambda x: "Could not determine the sentiment.")
)


# 9. Combine chains
chain = classifier_chain | branch_chain

# 10. Test input
test_input = {"feedback": "The product quality is really poor and I want a refund."}

# 11. Run the chain and print the output
print(chain.invoke(test_input))
