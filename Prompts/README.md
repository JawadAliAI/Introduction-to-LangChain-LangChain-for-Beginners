# LangChain Prompts

This directory contains various prompt templates and examples for use with LangChain. Prompts are a fundamental concept in LangChain that help structure and optimize interactions with language models.

## What are Prompts in LangChain?

Prompts in LangChain are structured templates that help format inputs for language models. They provide a way to:
- Create consistent and reusable templates
- Include dynamic variables
- Format complex instructions
- Maintain context and conversation history
- Optimize model outputs

## Types of Prompts

### 1. Prompt Templates
Basic templates that allow for variable substitution. Example:
```python
from langchain.prompts import PromptTemplate

template = "Tell me a {adjective} joke about {topic}"
prompt = PromptTemplate(
    input_variables=["adjective", "topic"],
    template=template
)
```

### 2. Chat Prompt Templates
Specialized templates for chat-based interactions:
```python
from langchain.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{user_input}")
])
```

### 3. Few-Shot Prompt Templates
Templates that include examples to guide the model:
```python
from langchain.prompts import FewShotPromptTemplate

examples = [
    {"question": "What is 2+2?", "answer": "4"},
    {"question": "What is 3+3?", "answer": "6"}
]
```

## Best Practices

1. **Be Specific**: Clearly define the task and expected output format
2. **Use Variables**: Make prompts reusable with variable substitution
3. **Include Examples**: Provide few-shot examples when possible
4. **Maintain Context**: Use chat history and context appropriately
5. **Error Handling**: Include instructions for handling edge cases

## Common Use Cases

1. **Question Answering**
2. **Text Generation**
3. **Code Generation**
4. **Summarization**
5. **Translation**
6. **Classification**

## Example Structure

```
Prompts/
├── templates/
│   ├── qa_template.py
│   ├── chat_template.py
│   └── few_shot_template.py
├── examples/
│   ├── qa_examples.py
│   └── chat_examples.py
└── README.md
```

## Tips for Effective Prompts

1. **Start with Clear Instructions**: Begin with explicit instructions about the task
2. **Use Formatting**: Utilize markdown, bullet points, and numbered lists
3. **Set Constraints**: Define output format and length limits
4. **Include Context**: Provide relevant background information
5. **Specify Tone**: Indicate the desired tone and style
6. **Handle Edge Cases**: Include instructions for handling exceptions

## Resources

- [LangChain Documentation](https://python.langchain.com/docs/modules/model_io/prompts)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [LangChain GitHub Repository](https://github.com/langchain-ai/langchain)

## Contributing

Feel free to add your own prompt templates and examples to this directory. Make sure to:
1. Follow the existing structure
2. Include clear documentation
3. Add examples of usage
4. Test your prompts with different models 