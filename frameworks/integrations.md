# Framework Integrations

Prompt engineering frameworks and LLM application frameworks integration guide.

## 📋 Contents

- [LangChain](#langchain)
- [LlamaIndex](#llamaindex)
- [Semantic Kernel](#semantic-kernel)
- [Hugging Face](#hugging-face)
- [Other Frameworks](#other-frameworks)

## 🔗 LangChain

The most comprehensive LLM application framework.

### Core Concepts

#### Prompt Templates

```python
from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI

# Create a prompt template
template = """You are a {role}. Please help me with: {question}"""

prompt = PromptTemplate(
    input_variables=["role", "question"],
    template=template,
)

# Use with LLM
llm = OpenAI(temperature=0.7)
chain = LLMChain(llm=llm, prompt=prompt)
response = chain.run(role="Python expert", question="How to learn Python?")
```

#### Few-shot Prompting

```python
from langchain import FewShotPromptTemplate

examples = [
    {"input": "Hello", "output": "Bonjour"},
    {"input": "Goodbye", "output": "Au revoir"}
]

example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="Input: {input}\nOutput: {output}"
)

few_shot = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="Translate English to French",
    suffix="Input: {new_input}\nOutput:",
    input_variables=["new_input"]
)
```

#### Chain-of-Thought

```python
from langchain.prompts import PromptTemplate

cot_template = """Question: {question}

Let's work through this step by step:
1. First, understand the problem
2. Break it down into parts
3. Solve each part
4. Put it all together

Answer:"""

cot_prompt = PromptTemplate.from_template(cot_template)
```

#### Chat Prompt Templates

```python
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

system_template = "You are a helpful {role}."
system_prompt = SystemMessagePromptTemplate.from_template(system_template)

human_template = "{input}"
human_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_prompt, human_prompt])
```

### Agents

```python
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)
tools = load_tools(["serpapi", "llm-math"], llm=llm)

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

agent.run("What is 25% of 1000?")
```

### Memory

```python
from langchain import ConversationChain
from langchain.memory import ConversationBufferMemory

llm = OpenAI(temperature=0)
conversation = ConversationChain(
    llm=llm,
    memory=ConversationBufferMemory(),
    verbose=True
)

conversation.predict(input="Hello!")
conversation.predict(input="What's my name?")
```

### RAG (Retrieval-Augmented Generation)

```python
from langchain import VectorDBQA
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

# Create embeddings
embeddings = OpenAIEmbeddings()
docsearch = FAISS.from_documents(docs, embeddings)

# RAG QA
qa = VectorDBQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    vectorstore=docsearch,
    return_source_documents=True
)

result = qa({"query": "Your question here"})
```

---

## 🦙 LlamaIndex (GPT Index)

Data framework for LLM applications.

### Simple Index

```python
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader('data/').load_data()
index = GPTVectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

response = query_engine.query("What's in the documents?")
```

### Custom Prompts

```python
from llama_index import Prompt

custom_prompt = Prompt("""
You are an expert researcher. Answer based only on the context.

Context: {context_str}
Query: {query_str}
Answer:
""")

index = GPTVectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine(text_qa_template=custom_prompt)
```

### Vector Stores

```python
from llama_index import GPTVectorStoreIndex
from llama_index.vector_stores import PineconeVectorStore
import pinecone

pinecone.init(api_key="your-key", environment="us-west1-gcp")
index = pinecone.Index("quickstart")
vector_store = PineconeVectorStore(pinecone_index=index)

index = GPTVectorStoreIndex.from_documents(documents, vector_store=vector_store)
```

---

## 💡 Semantic Kernel

Microsoft's SDK for AI apps.

### Plugins

```csharp
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.SemanticFunctions;

var kernel = Kernel.Builder.Build();
var promptConfig = new PromptTemplateConfig
{
    Description = "Summarize",
    Completion =
    {
        MaxTokens = 500,
        Temperature = 0.5
    }
};
```

### Skills

```csharp
var summarize = kernel.CreateSemanticFunction(@"
Summarize this text: {{$input}}

Make it {{$style}}.
", config: promptConfig);

var result = await summarize.InvokeAsync("Your text here");
```

---

## 🤗 Hugging Face

### Transformers

```python
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

generator = pipeline('text-generation', model='gpt2')

# Prompting
result = generator(
    "Once upon a time, ",
    max_length=100,
    num_return_sequences=1
)
```

### PEFT (Parameter-Efficient Fine-Tuning)

```python
from peft import LoraConfig, get_peft_model
import transformers

config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q", "v"],
    lora_dropout=0.05
)
```

---

## 📚 More Frameworks

### LangFlow

Visual LangChain interface.

### AutoGPT

Autonomous agent framework.

### BabyAGI

Task management AI.

### GPT-4 & LangChain

Advanced integrations.

---

## 📖 Resources

- [LangChain Docs](https://python.langchain.com/)
- [LlamaIndex Docs](https://gpt-index.readthedocs.io/)
- [Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/)
- [Hugging Face](https://huggingface.co/docs)
