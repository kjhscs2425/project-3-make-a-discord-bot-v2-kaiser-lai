import random

def russian():
    game = input("Let's play, shall we... casual or extreme? ").lower()

    if game == "extreme":
        input("3 bullets loaded. Press Enter to start.")
        cylinder = ["click"] * 3 + ["boom"] * 3  # 3 bullets, 3 empty chambers
        random.shuffle(cylinder)

        while True:
            input("Press Enter to pull the trigger.")
            trigger = cylinder.pop()  # Corrected .pop() usage
            print(trigger)  # Shows the result of firing

            if trigger == "boom":
                print("Game over.")
                break  # Exit loop when boom is hit

            if not cylinder:  # If chamber is empty, reload
                print("Reloading...")
                cylinder = ["click"] * 3 + ["boom"] * 3
                random.shuffle(cylinder)

russian()
