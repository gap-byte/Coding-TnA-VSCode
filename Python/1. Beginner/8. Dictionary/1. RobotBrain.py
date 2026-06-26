# 1. The Dictionary (The Bot's Brain)
print("🤖 Booting up Robo-Buddy...")

chatbot_brain = {
    "hello": "Hi there! I am Robo-Buddy. Nice to meet you!",
    "bye": "Goodbye! Have a great day!",
    "name": "I don't have a real name, I'm just a Python dictionary.",
    "joke": "Why did the programmer quit his job? Because he didn't get arrays (a raise)!",
    "weather": "I am stuck in your computer, I have no idea what the weather is!",
    "space": "Did you know one million Earths can fit inside the Sun?", # Added from AI brainstorm
    "animal": "My favorite animal is a Python. Get it?"
}

# 2. The Game Loop
while True:
    # Get user input
    user_input = input("\nYou: ")
    
    # 3. Algorithm Magic: Convert input to lowercase to match our dictionary keys
    # This prevents errors if the user types "HELLO" or "Hello"
    clean_input = user_input.lower()
    
    # 4. Check for exit condition
    if clean_input == "quit" or clean_input == "exit":
        print("🤖 Robo-Buddy: " + chatbot_brain["bye"])
        break
        
    # 5. Check if the word is in our dictionary
    if clean_input in chatbot_brain:
        # If yes, print the matching value
        print("🤖 Robo-Buddy: " + chatbot_brain[clean_input])
    else:
        # If no, give a default error message
        print("🤖 Robo-Buddy: I don't know how to respond to that yet. Try saying 'hello', 'joke', or 'space'!")
