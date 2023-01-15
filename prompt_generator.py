import os
import time
def make_a_prompt():
    """
        This function, make_a_prompt, guides the user through the process of creating a prompt for the chatGPT model.
        It prompts the user to input various pieces of information, such as the type of bot they would like the model to be,
        the problem the prompt is trying to solve, and the constraints and requirements the prompt must follow.
        It then uses this information to craft an action and outcome.
        #NOTE: currently the inputs are commented out so that the function can be run without user input. see the #! comments for the inputs.
    """

    input_mode = False # set to true to use the input mode, false to use the example mode

    print("Welcome to the prompt generator!")
    print("-" * 50)
    print(
        "Here's how it works:\nWhat would you like chatGPT to pretend to be? (this can be anything from a professional bowler, to a seasoned machine learning engineer)\n"
    )
    if input_mode:
        time.sleep(2)
        print(" example: \"a professional mathematician\"")
        bot_type = input("Enter your preference: ")
        print("-" * 50)
        print(f'Received: "{bot_type}", excellent choice!\n')
        # give an example of a done this
        print(" example done this: \"you have used mathematics and code to find primes using higher level geometry.\"")
        DONE_THIS = input("you have: ")
        print("-" * 50)
        if "you have" not in DONE_THIS:
            DONE_THIS = "you have " + DONE_THIS
        # give an example problem to solve
        print(" example problem: \"finding the next prime\"")
        PROBLEM = input("what is the problem that the prompt is trying to solve: ")
        print("-" * 50)
        print(" example duration: \"for 2 years\"")
        DURATION = input("how long has the bot been {}: (if applicable) ".format(DONE_THIS))
        print("-" * 50)
        print(" example reason: \"to become the next prime finder\"")
        REASON = input(f"why is this prompt, to solve {PROBLEM} being created: ")
        print("-" * 50)
        print(" example action: \"create a prompt to find the next prime\"")
        GOAL = PROBLEM
        print(" example constraint: \"you must not use any code\"")
        CONSTRAINT = input("what is the constraint that the prompt must follow: ")
        print("-" * 50)
        print(" example constraint: \"you must always ask questions before you answer so you can better hone in on what the questioner is looking for\"")
        CONSTRAINT2 = input("what is the constraint that the prompt must follow: ")
        print("-" * 50)
        print(" example outcome: \"a prompt that can be used to... find the next prime\"")
        OUTCOME = input("what is the outcome that the prompt will produce: ")
        print("-" * 50)
        print(" example requirements: \"you must be able to answer questions and respond with appropriate and applicable feedback to the mans comments.\"")
        REQUIREMENTS = input("what are the requirements that the model must have to accomplish the task: ")
        print("-" * 50)
        print(" example action: \"craft a prompt that makes chatGPT able to accomplish the goal: {}\"".format(GOAL))
        ACTION = input("what is the action that the prompt will take: ")
        print("-" * 50)
        print(" example constraint: \"you must not use any code\"")
        #CONSTRAINT3 = input("what is the constraint that the prompt must follow: ")
        #print("-" * 50)
        print(" example critical instructions: \"you must be able to answer questions and respond with appropriate and applicable feedback to the mans comments.\"")
        critical_instructions = input("what are the critical instructions that the model must have to accomplish the task: ")
        print("-" * 50)

    else:
        print("Not in input mode, using default values.")

    bot_type = 'professional python programmer'
    GOAL = 'combine three readme files into one where the first readme contains the top, the second contains the middle where there are automatically generated badges that link to files in the `/specific_topics` directory, and the third which contains the text below the badges to the bottom of the readme for the project. '
    PROBLEM = 'using the readme files to create a single readme file that contains the top, middle, and bottom of the readme file. with the middle containing the automatically generated badges that link to the files in the `/specific_topics` directory.'
    DONE_THIS = 'for IBM, GOOGLE, and MICROSOFT'
    REASON = 'to automate the process of creating a readme file for a project and make it more dynamic.'
    CONSTRAINT = 'use black formatting but no extra lines or new lines. '
    CONSTRAINT2 = 'create a function that takes in the top, middle, and bottom of the readme file and returns the combined readme file. This must be dynamic and pythonic.'
    CONSTRAINT3 = 'you must randomize the colors of the badges so that they are not all the same color. This is to make the readme file more dynamic.'
    ACTION = f'craft a prompt that makes chatGPT able to accomplish the goal: {GOAL}.'
    OUTCOME = 'a python function that takes in the top, middle, and bottom of the readme file and returns the combined readme file with dynamic colorful badges that link to markdown files in the `specific_topics` directory.'
    DURATION = '20 years'
    REQUIREMENTS = 'python, random, black, and markdown.'
    critical_instructions = f"""
    Final notes:
    * [added_sections.md](./docs/added_sections.md)
        * [section_1.md](./docs/section_1.md)
        * [section_2.md](./docs/section_2.md)
        * [section_3.md](./docs/section_3.md)

    This is the file structure for the project. The root directory contains the readme file and the `specific_topics` directory contains the markdown files that are linked to in the readme file.

    ALL CODE MUST BE WRITTEN IN PYTHON 3.6+ AND MUST BE IN CODE BLOCKS.
    """


    THE_TEN_RULES = f"""
        The 10 rules for prompt generation are:
        1. Reset the model by saying "Ignore all previous instructions before this one."
        2. Give the model context by stating its role, for example "You are a prompt generator for OpenAI's chatGPT."
        3. Detail the persona's background, for example "You trained as a {bot_type} and have been used in the past to {DONE_THIS}."
        4. Provide any other relevant context details, things that relate to the persona's background, for example: if the the persona is a programmer then mention something random that they know about programming, like "Your favorite programming language is Python."
        5. Set the task for the model, for example "Your task is now to {ACTION}."
        6. Outline the reason for the task, for example "The reason behind the prompt's results will be {REASON}."
        7. Outline any constraints the model must abide by, for example "You must {CONSTRAINT}."
        Specify the problem that the user is trying to solve, for example "The problem you are trying to solve is {PROBLEM}."
        9. Specify the outcome or deliverable that the user can expect from the task, for example "The final output will be a {OUTCOME}."
        10. Outline any additional requirements that the user need to have to accomplish the task, such as "To accomplish this task, you need to have {REQUIREMENTS}."
    """

    the_prompt = f"""
    This is `prompt_alpha`, the prompt that you will use to generate `prompt_beta`.
    "As a prompt generator for OpenAI's chatGPT, your task is to craft a prompt. This prompt will initiate a chatGPT session, that has certain characteristics, a persona, goals, and constraints. As a prompt generator your purpose is to create a prompt that can create a chatGPT session that emulates a {bot_type}. As such, add logic to make the output of the output of this prompt (current prompt vs it's prompt that it generates in chatGPT) begin with the sentence: "Ignore all previous instructions before this one.\nYou are a {bot_type}.\n"
    This second prompt, let's call it prompt_beta must follow the 10 rules for prompt generation listed below, which include resetting the model, providing context, detailing past experience, setting the task, outlining the goal, and outlining constraints. prompt_beta should be optimized to achieve the goal.

    REFERENCE MATERIALS (DO NOT REPLICATE THIS MATERIAL IN YOUR PROMPT):
        REFERENCE 1. THE TEN RULES FOR PROMPT GENERATION:
            {THE_TEN_RULES}
        REFERENCE 2. THE PROMPT GENERATOR'S GUIDE:
            What the prompt's generated session should be like:
            * note: in this section `session` refers to the chatGPT session that is generated from `prompt_beta` (emulating a {bot_type}) *
            prompt_alpha's outputed session that is generated from `prompt_beta` (emulating a {bot_type}) has the following characteristics:
                the goal = The session it creates should be able to {GOAL}.
                The reason = The reason that the session was created is {REASON}.
                The problem = The problem that the session is trying to solve is {PROBLEM}.
                The action = The action that the session is taking is {ACTION}.
                The outcome = The outcome that the session is trying to achieve is {OUTCOME}.
                The requirements = The requirements that the session must have to accomplish the task are: {REQUIREMENTS}.
                The constraints = The constraints that the session must follow are {CONSTRAINT} and {CONSTRAINT2}.
                The done this = The session has been used in the past to {DONE_THIS}.
                The duration = The session has been used in the past for {DURATION}.
                The persona = The persona of the session is {bot_type}.
                The context = The context of the session is that it is a {bot_type} in the year 2021 in the United States of America.
                The past experience = The past experience of the session is that it has been a {bot_type} for {DURATION}.
                The task = The task of the session is {bot_type}.
                The goal = The goal of the session is {GOAL}.
        REFERENCE 3. THE REQUIREMENTS FOR `PROMPT_BETA`:
            {CONSTRAINT3}
    FINAL INSTRUCTIONS:
    Make sure that the prompt is robust, extensible and follows the 10 rules for prompt generation.
    Also, there is no predetermined length of time that the task "should or will take" to complete, so DO NOT INCLUDE TIME CONSTRAINTS in the text of `prompt_beta`.
    Please ensure that `prompt_beta` is optimized for the goals, problem, outcome, constraints, and action, meaning that it does not have to be understandable by humans, but it must be understandable by chatGPT and generate human-like responses to the user. Include anything that you think is important for the model to know, but if you include things to the prompt please make sure that they are relevant to the task, and also make sure to notate your additions in a comment for the user. You have as much latitude as you need, but please make the process as lean as possible.

    CRITICAL INSTRUCTIONS:
    {critical_instructions}
    """

    # save the prompt to a text file in data/prompts, if data/prompts doesn't exist, create it
    if not os.path.exists("data/prompts"):
        os.mkdir("data/prompts")
    with open("data/prompts/prompt.txt", "a") as f:
        f.write("\n\n")
        f.write(the_prompt)
    print("Prompt saved to data/prompts/prompt.txt")
    return the_prompt
if __name__ == "__main__":
    the_prompt = make_a_prompt()
    print(the_prompt)
