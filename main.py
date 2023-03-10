import os
import time
import colorama
from colorama import Fore, Style
import openai
from dotenv import load_dotenv
load_dotenv()

colorama.init()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_title():
    print(Fore.RED + '''
#######                                              #####  ######  ####### 
   #    ###### #####  #    # # #    #   ##   #      #     # #     #    #    
   #    #      #    # ##  ## # ##   #  #  #  #      #       #     #    #    
   #    #####  #    # # ## # # # #  # #    # #      #  #### ######     #    
   #    #      #####  #    # # #  # # ###### #      #     # #          #    
   #    #      #   #  #    # # #   ## #    # #      #     # #          #    
   #    ###### #    # #    # # #    # #    # ######  #####  #          #    
''' + Style.RESET_ALL)

def print_welcome_message():
    print("Welcome to TerminalGPT! This program uses the OpenAI GPT-3 API to respond to your prompts.")
    print("Please note that you need to have an OpenAI API key in order to use this program.")
    print("To get an API key, visit the OpenAI website: https://openai.com/api/")
    print("Once you have your API key, save it in a file named '.env' in the same directory as this script.")
    print("The file should contain a single line, like this:")
    print("OPENAI_API_KEY=your-api-key-goes-here")
    print("Don't forget to replace 'your-api-key-goes-here' with your actual API key!")
    print("If you're ready to get started, type 'y' and press Enter. If you want to quit, type 'n' and press Enter.")

def get_input():
    return input("> ")

def process_input(input_str):
    if input_str.lower() == 'y':
        clear()
        print_title()
        print("You can now start chatting with TerminalGPT!")
        print("Type your message and press Enter. TerminalGPT will respond with a message of its own.")
        print("When you're ready to quit, type 'quit' and press Enter.")
        while True:
            prompt = get_input()
            if prompt == 'quit':
                break
            response = openai.Completion.create(
                engine="davinci",
                prompt=prompt,
                max_tokens=60,
                n=1,
                stop=None,
                temperature=0.5,
            )
            message = response.choices[0].text.strip()
            print(message)
    elif input_str.lower() == 'n':
        clear()
        print_title()
        print_welcome_message()
    else:
        print("Invalid input. Please type 'y' or 'n' and press Enter.")

def main():
    print_title()
    print_welcome_message()
    while True:
        input_str = get_input()
        process_input(input_str)
        if input_str.lower() == 'n':
            clear()

if __name__ == "__main__":
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if openai.api_key is None:
        print("Error: Please set your OpenAI API key in a file named '.env' in the same directory as this script.")
        print("The file should contain a single line, like this:")
        print("OPENAI_API_KEY=your-api-key-goes-here")
        print("Don't forget to replace 'your-api-key-goes-here' with your actual API key!")
    else:
        main()
        
