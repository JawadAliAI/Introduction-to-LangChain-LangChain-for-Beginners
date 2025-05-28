from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel,RunnableSequence, RunnablePassthrough, RunnableLambda

load_dotenv()


prompt = PromptTemplate(
    template = "write a joke about the {topic}",
    input_variables = ['topic']
)

model = ChatOpenAI()


parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(lambda x: len(x.split()))
})


final = RunnableSequence(joke_gen_chain, parallel_chain)

print(final)