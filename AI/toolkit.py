from JanexBot import *

def main():
    chatbot = JanexBot("AI/database.json", "en_core_web_sm")
    question = chatbot.ask_question(None)
    print(f"Chatbot: {question}")
    while True:
        answer = input("You: ")
        IsQuestion = chatbot.CheckForQuestion(answer)
        if IsQuestion:
            answer = chatbot.give_answer(answer)
            print(f"Chatbot: {answer}")
        else:
            question = chatbot.ask_question(answer)
            print(f"Chatbot: {question}")
            chatbot.save_answer(answer)

if __name__ == "__main__":
    main()
