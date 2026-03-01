from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
import os
from dotenv import load_dotenv

from tools import search, AVAILABLE_COOKWARE

load_dotenv()
llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=os.getenv("GROQ_API_KEY")
)

def run_agent(req):
    result = {
        "in_scope": False,
        "response": None
    }
    # Classify if it's a cooking question
    messages = [
        SystemMessage(content = "You are a cooking assistant. Analyze the following message. " \
                                "Output 1 if it is a general cooking question. " \
                                "Output 2 if it's a recipe request for a specific dish (ex. how do I cook X?) " \
                                "Output 3 if it's a 'What can I cook with these ingredients?' query. " \
                                "Output 0 if it's an irrelevant message. " \
                                "Do NOT output anything else"),
        HumanMessage(content = req)
    ]

    category = llm.invoke(messages).content
    print("\n\n\n\n\n" + category)

    result["in_scope"] = (category != '0')
    if (not result["in_scope"]):
        result["response"] = "Please ask a relevant cooking question"
        return result
    
    searched = False


    if (category == '1'):
        messages = [
            SystemMessage(content = "You are a cooking assistant. Answer the following question. " \
                                    "If you require external resources to validate your answer, output -1 and nothing else."),
            HumanMessage(content = req)
        ]

        response = llm.invoke(messages).content
        if (response == '-1'):
            # result["response"] = search(req)
            searched = True
        else:
            result['response'] = response
    elif (category == '2'):
        messages = [
            SystemMessage(content = f"Keep in mind that the user is limited in cookware and has only the following items: {AVAILABLE_COOKWARE}" \
                                    "IMPORTANT: if the user CANNOT cook the recipe with their cookware, output 0 and nothing else"
                                    "If you require external resources to validate your answer, output -1 and nothing else." \
                                    "Else, answer the question holistically."
                                    ),
            HumanMessage(content = req)
        ]

        response = llm.invoke(messages).content
        if (response == '-1'):
            result["response"] = search(req)
            print("Searching!!!!!")
            searched = True
        elif (response == '0'):
            result['response'] = "You cannot make this with your cookware."
        else:
            result['response'] = response
    elif (category == '3'):
        messages = [
            SystemMessage(content = f"You are a cooking assistant. Answer the following question. " \
                                    "Keep in mind that the user is limited in cookware and has only the following items: {AVAILABLE_COOKWARE}" \
                                    "If you are not confident in your answer, output -1 and nothing else. " \
                                    "Only output recipes that the user can cook with their cookware"),
            HumanMessage(content = req)
        ]

        response = llm.invoke(messages).content
        if (response == '-1'):
            result["response"] = search(req)
            searched = True
        else:
            result['response'] = response
    
    if (searched):
        search_results = search(req)
        messages = [
            SystemMessage(content="You are a cooking assistant. Use these search results to answer the question. " \
            "Keep in mind that the user is limited in cookware and has only the following items: {AVAILABLE_COOKWARE}. " \
            "If they cannot cook the recipe with their cookware, output 'You cannot make this with your cookware.' AND NOTHING ELSE"),
            HumanMessage(content=f"Question: {req}\n\nSearch results: {search_results}")
        ]

        result["response"] = llm.invoke(messages).content
    
    
    return result