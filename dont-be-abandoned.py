import random

# Game Title
print("=== DON'T BE ABANDONED ===")
print("Try to save your relationship while making the right choices.")
print("In each chapter, there's only one correct path...\n")

# Chapters
chapters = {
    1: "Zoo",
    2: "Secret Message",
    3: "Cold Behavior",
    4: "Movie Plan",
    5: "Silence",
    6: "Ex Lover",
    7: "Unexpected Message",
    8: "Argument",
    9: "Kiss Moment",
    10: "Confrontation"
}

# Secret endings dictionary
secret_endings = {
    1: ["The elephant escaped", "You waved at the tiger, and Charlotte got emotional"],
    2: ["You sent the message to the wrong person", "The message was actually Charlotte's number"],
    3: ["Charlotte stalked you", "She spilled coffee on your face"],
    4: ["A fight broke out in the cinema", "The projector broke down"],
    5: ["Charlotte ignored you", "You accidentally sent a message to your ex"],
    6: ["You had tea with your ex", "Charlotte was watching you"],
    7: ["You sent ‘I miss you’ to the wrong person", "Charlotte was behind you at that moment"],
    8: ["The argument escalated into a police situation", "Başak heard everything"],
    9: ["Charlotte took a picture of you from behind", "Başak said, 'I'm leaving'"],
    10: ["Your phone was left in the middle", "Charlotte ignored you"]
}

# Success counter
success_count = 0

# Chapter 1: Zoo
def chapter_1():
    print("You and Charlotte are visiting the zoo. You recall the first time you were here together.")
    print("\n--- Choose your action ---")
    print("1: Talk about how much fun it was on the first visit.")
    print("2: Talk about how much you miss the animals.")
    print("3: Ask if she remembers the time you both got lost here.")
    
    main_choice = int(input("Make a main choice (1/2/3): "))
    correct_choice = 1  # Talking about the first visit is the correct choice
    if main_choice == correct_choice:
        print("Charlotte smiles and starts talking about the good memories. The mood lightens.")
        return True
    else:
        print("Charlotte seems distant and the moment becomes awkward.")
        return False

# Chapter 2: Secret Message
def chapter_2():
    print("You receive a mysterious message. It seems like someone is trying to get your attention.")
    print("\n--- Choose your action ---")
    print("1: Ignore the message and focus on Charlotte.")
    print("2: Open the message and see who it’s from.")
    print("3: Show the message to Charlotte immediately.")
    
    main_choice = int(input("Make a main choice (1/2/3): "))
    correct_choice = 2  # Opening the message and checking it is the correct choice
    if main_choice == correct_choice:
        print("The message turns out to be from an unknown number, leaving you confused. Charlotte looks at you suspiciously.")
        return True
    else:
        print("Charlotte looks disappointed, thinking you’re not focusing on her.")
        return False

# Chapter 3: Cold Behavior
def chapter_3():
    print("Charlotte starts acting distant. You wonder if something’s wrong.")
    print("\n--- Choose your action ---")
    print("1: Ask if she's okay.")
    print("2: Wait for her to speak first.")
    print("3: Get annoyed and ask if she’s mad at you.")
    
    main_choice = int(input("Make a main choice (1/2/3): "))
    correct_choice = 1  # Asking if she's okay is the correct choice
    if main_choice == correct_choice:
        print("Charlotte opens up and talks about feeling insecure. You reassure her, and the mood improves.")
        return True
    else:
        print("Charlotte withdraws even further, making the situation more tense.")
        return False

# Chapter 4: Movie Plan
def chapter_4():
    print("You plan a movie night, but Charlotte seems distracted.")
    print("\n--- Choose your action ---")
    print("1: Ask her to focus and enjoy the movie.")
    print("2: Tell her it’s okay, we can do something else.")
    print("3: Leave the room to give her space.")
    
    main_choice = int(input("Make a main choice (1/2/3): "))
    correct_choice = 2  # Suggesting something else is the correct choice
    if main_choice == correct_choice:
        print("Charlotte appreciates your understanding. You decide to spend time together in a different way.")
        return True
    else:
        print("The situation becomes uncomfortable, and she seems even more distant.")
        return False

# Chapter 5: Silence
def chapter_5():
    print("The atmosphere becomes tense and awkward. Neither of you says anything.")
    print("\n--- Choose your action ---")
    print("1: Break the silence by asking her how her day was.")
    print("2: Wait for her to speak first.")
    print("3: Start an unrelated conversation to ease the tension.")
    
    main_choice = int(input("Make a main choice (1/2/3): "))
    correct_choice = 1  # Asking how her day was is the correct choice
    if main_choice == correct_choice:
        print("Charlotte opens up, and the conversation flows naturally again.")
        return True
    else:
        print("The silence continues, and the tension builds up.")
        return False

# Chapter 6: Ex Lover
def chapter_6():
    print("You bump into your ex at a café. Charlotte notices and looks uneasy.")
    print("\n--- Choose your action ---")
    print("1: Introduce your ex to Charlotte and keep the conversation brief.")
    print("2: Ignore your ex and walk away with Charlotte.")
    print("3: Start a conversation with your ex and ask Charlotte to wait.")
    
    main_choice = int(input("Make a main choice (1/2/3): "))
    correct_choice = 1  # Introducing your ex to Charlotte is the correct choice
    if main_choice == correct_choice:
        print("Charlotte feels more at ease after meeting your ex. The tension fades.")
        return True
    else:
        print("Charlotte seems uncomfortable and doesn’t say much the rest of the day.")
        return False

# Chapter 7: Unexpected Message
def chapter_7():
    print("You receive an unexpected text from Mary. Charlotte notices you reading it.")
    print("\n--- Choose your action ---")
    print("1: Ignore the message and focus on Charlotte.")
    print("2: Tell Charlotte about the message and explain it’s from a friend.")
    print("3: Hide the message and say nothing about it.")
    
    main_choice = int(input("Make a main choice (1/2/3): "))
    correct_choice = 2  # Telling Charlotte about the message is the correct choice
    if main_choice == correct_choice:
        print("Charlotte appreciates your honesty and seems to trust you more.")
        return True
    else:
        print("Charlotte looks suspicious and feels hurt by your secrecy.")
        return False

# Chapter 8: Argument
def chapter_8():
    print("You and Charlotte get into a heated argument. Words are exchanged.")
    print("\n--- Choose your action ---")
    print("1: Apologize and try to calm her down.")
    print("2: Stand your ground and argue back.")
    print("3: Walk away and give her some space.")
    
    main_choice = int(input("Make a main choice (1/2/3): "))
    correct_choice = 1  # Apologizing and calming her down is the correct choice
    if main_choice == correct_choice:
        print("Charlotte listens to your apology and the tension eases.")
        return True
    else:
        print("The argument escalates, and the distance between you grows.")
        return False

# Chapter 9: Kiss Moment
def chapter_9():
    print("You and Charlotte are about to kiss, but something catches her attention.")
    print("\n--- Choose your action ---")
    print("1: Lean in and kiss her.")
    print("2: Ask her what’s wrong and listen to her concerns.")
    print("3: Hold off and try to talk about what’s bothering her.")
    
    main_choice = int(input("Make a main choice (1/2/3): "))
    correct_choice = 2  # Asking her what’s wrong is the correct choice
    if main_choice == correct_choice:
        print("Charlotte opens up about her feelings, and you both connect on a deeper level.")
        return True
    else:
        print("The moment fades, and the distance between you becomes noticeable.")
        return False

# Chapter 10: Confrontation
def chapter_10():
    print("You have a final confrontation. You need to decide what’s next for your relationship.")
    print("\n--- Choose your action ---")
    print("1: Talk about your future together and reassure her.")
    print("2: End things if it feels like it’s not working out.")
    print("3: Avoid talking about it and let things go as they are.")
    
    main_choice = int(input("Make a main choice (1/2/3): "))
    correct_choice = 1  # Talking about your future together is the correct choice
    if main_choice == correct_choice:
        print("Charlotte feels relieved and happy to move forward with you.")
        return True
    else:
        print("The relationship ends, and both of you go separate ways.")
        return False

# Main Game Loop
for ch in range(1, 11):
    print(f"\n--- CHAPTER {ch}: {chapters[ch]} ---")
    
    if ch == 1:
        success = chapter_1()
    elif ch == 2:
        success = chapter_2()
    elif ch == 3:
        success = chapter_3()
    elif ch == 4:
        success = chapter_4()
    elif ch == 5:
        success = chapter_5()
    elif ch == 6:
        success = chapter_6()
    elif ch == 7:
        success = chapter_7()
    elif ch == 8:
        success = chapter_8()
    elif ch == 9:
        success = chapter_9()
    elif ch == 10:
        success = chapter_10()

    if success:
        success_count += 1

# End Game Result
print("\n=== GAME OVER ===")
if success_count >= 7:
    print("END: Charlotte didn't abandon you. You made it!")
elif 4 <= success_count < 7:
    print("END: There’s distance between you, but there's still hope.")
else:
    print("END: Charlotte abandoned you. Maybe she was the wrong person from the start...")
