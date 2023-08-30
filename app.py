import streamlit as st
import os
import openai
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





# 5. Build an app with streamlit
def main():
    os.environ["OPENAI_API_KEY"] = "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"
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

    conversation = LLMChain(
        llm=llm,
        prompt=prompt,
        verbose=False,
        memory=ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    )
    st.set_page_config(
        page_title="Project Pulse AI")
 
    st.image('images/logo.png', width=450)


    st.header("Project Pulse AI")
    response = conversation({"question": "Go"})

    st.info("Hi there! I'm Stella, your friendly project assistant. Let's dive in and see how your project is doing. 😊")     

    st.info(response.get('text'))     

    response_1 = st.text_area("response",key=1)
    
    if response_1:
        BotResponse = conversation({"question": response_1})
        st.info(BotResponse.get('text'))  
        response_2 = st.text_area("response",key=2)
        if response_2:
            BotResponse = conversation({"question": response_2})
            st.info(BotResponse.get('text'))
            response_3 = st.text_area("response",key=3)
            if response_3:
                BotResponse = conversation({"question": response_3})
                st.info(BotResponse.get('text'))
                response_4 = st.text_area("response",key=4)
                if response_4:
                    BotResponse = conversation({"question": response_4})
                    st.info(BotResponse.get('text'))
                    response_5 = st.text_area("response",key=5)
                    if response_5:
                        BotResponse = conversation({"question": response_5})
                        #st.info(BotResponse.get('text'))
                        st.info("Great! Thanks for that input. I'll generate you a project report summary now")
                        summary = "Can you now write a short project status report rating 1-10 how the project is going on the dimentions of scope, budget, and schedule and give it a 1-10 rating on overall risk of failure"
                        BotResponse = conversation({"question": summary})
                        st.info(BotResponse.get('text'))
                        st.info("Have a great day :)")
                        

if __name__ == '__main__':
    main()