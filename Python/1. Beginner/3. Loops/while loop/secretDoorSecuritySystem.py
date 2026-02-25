# 1. Setup the Security Database
correct_name = "Agent Ruby"
correct_code = "Pizza123"
access_granted = False

print("--- TOP SECRET SECURITY DOOR ---")
print("Identify yourself to enter the base.")

# 2. The Security Loop
while access_granted == False:
    user_name = input("\nWho is there? ")
    
    if user_name == correct_name:
        print("Hello, Agent Ruby.")
        passcode = input("What is the secret passcode? ")
        
        if passcode == correct_code:
            print("ACCESS GRANTED! Opening the vault...")
            access_granted = True # This 'unlocks' the loop
        else:
            print("WRONG PASSCODE! Alarm ringing! Try again.")
    else:
        print("Intruder detected! We don't know you.")
        print("Hint: You are Agent Ruby!")

# 3. Final Summary
print("\nWelcome back to the Secret Base. Your mission is waiting.")