import time
print("----- Simple Typing Tester -----")
original_text = input("Enter the text for typing test:\n")
input("\nPress Enter when you are ready to start typing...")
# Start time
start_time = time.time()
# User types the text
typed_text = input("\nStart typing:\n")
# End time
end_time = time.time()
time_taken = end_time - start_time
words = len(original_text.split())
# Typing speed (WPM)
speed = (words / time_taken) * 60
# Accuracy check 
if typed_text == original_text:
    accuracy = 100
else:
    accuracy = 0
print("\n----- Result -----")
print("Time Taken:", round(time_taken, 2), "seconds")
print("Typing Speed:", round(speed, 2), "words per minute")
print("Accuracy:", accuracy, "%")