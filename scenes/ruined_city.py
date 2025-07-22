from utils import slow_print, pause, prompt_choice
from game_state import Memory

class RuinedCity:
    def __init__(self, game):
        self.game = game

    def intro(self):
        try:
            slow_print("[bold white]Fog and Memory[/bold white]", style="bright_white")
            slow_print("You find yourself in a fog-choked street, the lamppost faintly glowing.", style="bright_black")
            slow_print("A sparkle flickers near the lamppost — a LEGO frog keychain.", style="cyan")
            pause()

            mem_id = "ruined_frog_keychain"
            mem_text = "I know it’s stupid, but frogs make me feel safe. Like the world isn’t watching."
            memory = Memory(mem_id, mem_text, emotional_weight=2)

            slow_print(f'MORGAN (voice): "{mem_text}"', style="magenta")
            slow_print("YOU: I remember this. The park bench. She told me that the night before it all fell apart.", style="cyan")
            pause()

            choice = prompt_choice("Would you like to HOLD ON to this memory? (y/n)", {'y': 'Yes', 'n': 'No'})
            if choice == 'y':
                memory.held = True
                self.game.player.add_memory(memory)
                slow_print("[Memory held]", style="green")
            else:
                slow_print("[Memory not held]", style="yellow")

            return 'ruined_city_bookstore'
        except Exception as e:
            from rich import print
            print(f"[red]Error inside RuinedCity.intro(): {e}[/red]")
            raise

    def bookstore(self):
        slow_print("[bold white]Bookstore Ruins[/bold white]", style="bright_white")
        slow_print("You enter the burned-out bookstore. Ash drifts through shafts of light.", style="bright_black")
        slow_print("Books lie half-buried in rubble, their pages yellowed and torn.", style="bright_black")
        pause()

        mem_id = "ruined_astrology_book"
        mem_text = "I only trust people who know their moon sign. What’s yours again?"
        memory = Memory(mem_id, mem_text, emotional_weight=3)

        slow_print(f'MORGAN (laughing): "{mem_text}"', style="magenta")
        slow_print("YOU: I told her mine. She said we were doomed from the start… but smiled anyway.", style="cyan")
        pause()

        choice = prompt_choice("Would you like to REMEMBER this moment? (y/n)", {'y': 'Yes', 'n': 'No'})
        if choice == 'y':
            self.game.player.add_memory(memory)
            slow_print("[Memory remembered]", style="green")
        else:
            slow_print("[Memory ignored]", style="yellow")

        return 'ruined_city_garden'

    def garden_puzzle(self):
        slow_print("[bold white]Garden Puzzle[/bold white]", style="bright_white")
        slow_print("An abandoned rooftop garden tangled with vines and wildflowers greets you.", style="bright_black")
        slow_print("Scattered pots of various sizes lie cracked or overturned.", style="bright_black")
        pause()

        slow_print('NPC (ghostly child whispers): "She planted stars here. Said if you listened close, they\'d bloom brighter than anywhere else."', style="magenta")
        slow_print("YOU (softly): \"I hope she’s right… I hope these stars still grow.\"", style="cyan")
        pause()

        slow_print("Arrange the plant pots to form the pattern of a star constellation—a symbol Morgan loved.", style="bright_black")
        # Here you would add actual puzzle logic or simulate it for now
        slow_print("[Puzzle solved: Star constellation formed]", style="green")
        pause()

        slow_print("Soft glowing lights flicker along the plants, and the door to the next realm slowly creaks open.", style="bright_black")
        pause()

        return 'underground_intro'
