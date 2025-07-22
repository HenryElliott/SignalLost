from utils import slow_print, pause, prompt_choice
from game_state import Memory

class DigitalWorld:
    def __init__(self, game):
        self.game = game

    def intro(self):
        slow_print("[bold white]Digital World[/bold white]", style="bright_white")
        slow_print("You enter a glitchy realm of corrupted files and distorted landscapes.", style="bright_black")
        slow_print("You dig through old logs, music fragments, erased messages.", style="cyan")
        pause()
        return 'digital_world_vault'

    def memory_vault(self):
        slow_print("[bold white]Final Memory Vault[/bold white]", style="bright_white")
        slow_print("Screens flash old texts, voice notes, photos - every message, every silence.", style="bright_black")
        slow_print("Arrange corrupted memory files to form a goodbye letter you never sent.", style="cyan")
        pause()

        correct = "goodbye"
        attempts = 3
        while attempts > 0:
            answer = input("Type the final message word to send: ").strip().lower()
            if answer == correct:
                slow_print('Final Message Fragment: "I loved you like stars love the night sky - quietly, completely, endlessly."', style="magenta")
                choice = prompt_choice("Do you want to SEND this memory?", {'y': 'Yes', 'n': 'No'})
                if choice == 'y':
                    slow_print("Memory sent. She smiles, one last time.", style="green")
                else:
                    slow_print("You chose not to send the memory.", style="yellow")
                pause()
                return 'ending_choice'
            else:
                attempts -= 1
                slow_print(f"Incorrect. Attempts left: {attempts}", style="red")

        slow_print("You failed to send the memory. It remains corrupted.", style="red")
        pause()
        return 'ending_choice'

    def ending_choice(self):
        slow_print("[bold white]Ending Choice[/bold white]", style="bright_white")
        slow_print("Morgan appears - not as a memory, but real.", style="magenta")
        slow_print('MORGAN: "If you hold me, you can’t move forward. If you forget me, you won’t be whole."', style="magenta")
        slow_print('YOU: "Then what should I do?"', style="cyan")
        pause()

        choice = prompt_choice("Choose One:", {
            '1': 'Hold On - Live in the loop. Memory eternal but world never changes.',
            '2': 'Let Go - Release her. Fade peacefully and awaken alone but at peace.',
            '3': 'Remember and Move Forward - Send the message. She smiles, one last time.',
        })

        if choice == '1':
            slow_print("You hold on to the memory. The loop begins anew...", style="yellow")
            pause()
            return 'ruined_city_intro'
        elif choice == '2':
            slow_print("You let go. Peace washes over you as the world fades...", style="yellow")
            pause()
            return 'quit'
        elif choice == '3':
            slow_print("You remember and move forward. Light floods your vision.", style="yellow")
            pause()
            return 'quit'
