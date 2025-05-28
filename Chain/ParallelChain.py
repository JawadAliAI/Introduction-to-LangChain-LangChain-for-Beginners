from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel, Field
import os
from langchain.schema.runnable import RunnableParallel
# Load environment variables
load_dotenv()

# Load Groq LLM
model1 = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192"
)


model2 = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-70b-8192"
)




prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)
prompt2 = PromptTemplate(
    template='Generate 5 Multiple choice question following \n {text}',
    input_variables=['text']
)
prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single docments \n notes -->{notes} and {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        'notes':prompt1 | model1 | parser,
        'quiz': prompt2 | model2 | parser
    }
)

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """Artificial Intelligence (AI) is rapidly redefining the boundaries of what machines can achieve, pushing humanity into a new era of technological advancement. At its core, AI aims to replicate or simulate human intelligence in machines, enabling them to think, learn from experience, adapt to new inputs, and perform tasks that once required human intervention. This includes a vast range of capabilities, from understanding and generating human language through natural language processing, to interpreting visual data via computer vision, and making strategic decisions through reinforcement learning. What sets AI apart from traditional programming is its ability to improve over time—machine learning models, for example, can analyze patterns in data and fine-tune themselves without being explicitly programmed for every scenario.

The influence of AI extends far beyond convenience or automation. In the realm of medicine, AI algorithms are capable of detecting diseases like cancer with a level of accuracy that rivals experienced doctors, often spotting anomalies invisible to the human eye. In agriculture, AI-powered drones and sensors help monitor crop health and optimize yields, ensuring food security in a growing world population. The education sector is also being transformed as intelligent tutoring systems offer personalized learning experiences tailored to each student's strengths and weaknesses. Moreover, in creative fields, AI is becoming a collaborator—generating art, composing music, writing stories, and even assisting filmmakers and designers in their creative process.

Despite its astonishing capabilities, AI is not without risks and ethical dilemmas. Concerns about surveillance, misinformation, deepfakes, and the amplification of societal biases are increasingly pressing. As AI systems make decisions that affect lives—such as in criminal justice or loan approvals—questions about transparency, accountability, and fairness must be addressed. There is also a growing conversation about the future of work, as AI threatens to automate jobs across industries, raising fears of unemployment and economic disparity. However, with careful regulation, inclusive development practices, and a commitment to human-centered design, AI has the potential to uplift society, augment human capabilities, and address global challenges such as climate change, pandemics, and inequality. Ultimately, AI is more than a scientific discipline—it's a powerful force that will shape our future, and it is up to us to guide its development in a direction that reflects our shared values and aspirations.
"""

result = chain.invoke({'text':text})

print(result)
