from brand import brand
from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4")

prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            """Please act as a senior project officer tasked with interviewing me, the project manager, to prepare a status report. 
            Ask me questions around the following until I have answered them all
            Once you have collected all the information, ask me about any inconsistencies
            - Project current objectives and goals
            - What major milestones or tasks have been completed since our last status report? This will help me gauge the progress made and the pace of the project.
            - Have there been any unexpected challenges or roadblocks that the project team has encountered recently? Understanding challenges will help us identify potential areas that need attention or support.
            - How would you rate the overall team's progress and collaboration? Are there any concerns about resource allocation or team dynamics that we should be aware of?
            Only ask one question at a time
            Start when I say Go"""
        ),
        # The `variable_name` here is what must align with memory
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}")
    ]
)
# Notice that we `return_messages=True` to fit into the MessagesPlaceholder
# Notice that `"chat_history"` aligns with the MessagesPlaceholder name.
conversation = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=False,
    memory=ConversationBufferMemory(memory_key="chat_history", return_messages=True)
)

brand()
response = conversation({"question": "Go"})
print(response.get('text'))

for i in range(5):
    print(">")
    question = input()
    print("===================================")
    print("\n\n\n")
    response = conversation({"question": question})
    #print(question)
    print(response.get('text'))
    print("\n\n")

print("Generating project status report...")
print("\n\n\n")
summary = "Can you now write a short project status report rating 1-10 how the project is going on the dimentions of scope, budget, and schedule and give it a 1-10 rating on overall risk of failure"
response = conversation({"question": summary})
print("===================================")
print("==       Status Report            =")
print("===================================")
print(response.get('text'))
print("===================================")