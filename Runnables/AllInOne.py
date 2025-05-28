from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableSequence,
    RunnableMap,
    RunnablePassthrough,
    RunnableLambda,
    RunnableBranch,
    RunnableFunction
)
from dotenv import load_dotenv
load_dotenv()

# ----------- PROMPTS -------------
joke_prompt = PromptTemplate.from_template("Write a joke about {topic}")
explain_prompt = PromptTemplate.from_template("Explain the following joke: {text}")

# ----------- MODEL & PARSER -------------
model = ChatOpenAI()
parser = StrOutputParser()

# ----------- RUNNABLE: Generate a joke -------------
generate_joke_chain = RunnableSequence(joke_prompt, model, parser)

# ----------- RUNNABLE: Passthrough -------------
passthrough = RunnablePassthrough()

# ----------- RUNNABLE: Lambda to get joke length -------------
get_length = RunnableLambda(lambda x: {"text": x, "length": len(x)})

# ----------- RUNNABLE: Branch logic -------------
def condition(input):
    return input["length"] > 100

branch = RunnableBranch(
    (condition, RunnableLambda(lambda x: {"explanation": "Joke too long to explain."})),
    (lambda x: True,  # else
     RunnableSequence(
         lambda x: {"text": x["text"]},
         explain_prompt,
         model,
         parser,
         RunnableLambda(lambda x: {"explanation": x})
     ))
)

# ----------- FINAL COMPOSED CHAIN -------------
full_chain = RunnableSequence(
    generate_joke_chain,
    passthrough,  # passes joke as-is
    get_length,
    RunnableMap({
        "joke": lambda x: x["text"],
        "length": lambda x: x["length"],
        "explanation": branch
    })
)

# ----------- RUN -------------
output = full_chain.invoke({"topic": "AI"})
print("🔹 Joke:", output["joke"])
print("🔹 Length:", output["length"])
print("🔹 Explanation:", output["explanation"])
