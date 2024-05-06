my_string = """In the dim glow of his monitor, he deciphered the code, 
            each keystroke a heartbeat of determination. 
            Lines of algorithms danced before his eyes, a symphony of logic and reason. 
            As the world teetered on the brink of chaos, he toiled tirelessly, 
            weaving a digital fortress to withstand the impending storm. With deft precision, 
            he patched vulnerabilities, fortified defenses, and unleashed a cascade of updates. 
            As the clock ticked its ominous cadence, his fingers never faltered. And in the eleventh hour, 
            as chaos reared its head, his program stood as a bastion of order, 
            a beacon of salvation in the digital abyss."""

leet_dict = {"a" : "@", "b" : "8", "e" : "3", "i" : "!", "l" : "1", "o" : "0", "s" : "5"}

def leet_speak(text: str, leet_dict: dict) -> str:
    for key, value in leet_dict.items():
        text = text.replace(key, value)
        text = text.replace(key.upper(), value)
    return text

print(leet_speak(my_string, leet_dict))