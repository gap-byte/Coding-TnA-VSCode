# --- ALIEN MESSAGE DECODER ---

# 1. The intercepted transmission (Space junk + hidden message)
transmission = ["X-77", "Bzzzt", "WE", "HAVE", "CANDY", "SPACE", "Gurgle", "Bloop"]

print("--- INCOMING TRANSMISSION ---")
print(transmission)
print("-----------------------------\n")

# 2. Decoding the message using slicing
# The message "WE HAVE CANDY SPACE" starts at index 2.
# It ends at index 5. To include index 5, our stop number must be 6.
decoded_message = transmission[2:6]

print("--- DECODED MESSAGE ---")
print(decoded_message)

# 3. AI Exploration (Testing empty start/stop)
print("\n--- EXTRACTION TESTS ---")
print(f"First two items (Junk): {transmission[:2]}") 
print(f"Last two items (Junk): {transmission[6:]}")
