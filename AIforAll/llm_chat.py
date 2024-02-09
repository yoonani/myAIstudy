# https://colab.research.google.com/drive/1Ain-2t_OI_llY0lSn0NEPJ1E7kNVdx5J?usp=sharing#scrollTo=3_671qNBu7El
from dotenv import load_dotenv

if __name__ == "__main__" :
    load_dotenv()

    # from langchain_openai import OpenAI
    # llm = OpenAI()
    # res = llm.invoke("Python이 인기있는 이유를 말해줘")
    # print( res )

    from langchain_openai import ChatOpenAI
    chat = ChatOpenAI(model_name="gpt-3.5-turbo")
    answer = chat.invoke("Python이 인기있는 이유를 말해줘")
    print( answer.content )

    chat2 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1)
    answer = chat2.invoke("Python이 인기있는 이유를 말해줘")
    print( answer.content )
