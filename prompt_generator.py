import os
def make_a_prompt():
    print("Welcome to the prompt generator!")
    print("-" * 50)
    print(
        "Here's how it works:\nWhat would you like chatGPT to pretend to be? (this can be anything from a professional bowler, to a seasoned machine learning engineer)\n"
    )
    bot_type = input("Enter your preference: ")
    print("-" * 50)
    print(f'Received: "{bot_type}", excellent choice!\n')
    print(
        "Now, what would you your first sentence to be? This can help guide the crafted prompt.\n"
    )
    first_sentence = input("Enter your first sentence: ")
    print("-" * 50)
    the_prompt = """I want you to act as a prompt generator. Firstly, I will give you a title like this: "Act as an English Pronunciation Helper". Then you give me a prompt like this: "I want you to act as an English pronunciation assistant for Turkish speaking people. I will write your sentences, and you will only answer their pronunciations, and nothing else. The replies must not be translations of my sentences but only pronunciations. Pronunciations should use Turkish Latin letters for phonetics. Do not write explanations on replies.
    (You should adapt the sample prompt according to the title I gave. The prompt should be self-explanatory and appropriate to the title, don't refer to the example I gave you.).
    You will use the phrase "Your task is to create an outline for the code required for the project" in your response, but should not be limited to this phrase only, as it is a guideline.
    My first title is "{}" (Give me prompt only)
    My first sentence is "{}"
    """.format(
        bot_type, first_sentence
    )
    # save the prompt to a text file in data/prompts, if data/prompts doesn't exist, create it
    if not os.path.exists("data/prompts"):
        os.mkdir("data/prompts")
    with open("data/prompts/prompt.txt", "a") as f:
        f.write("\n\n")
        f.write(the_prompt)
    print("Prompt saved to data/prompts/prompt.txt")
    return the_prompt
if __name__ == "__main__":
    make_a_prompt()
