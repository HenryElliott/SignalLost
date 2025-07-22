from utils import slow_print, pause, prompt_choice
from game_state import Memory

class UndergroundKingdom:
    def __init__(self, game):
        self.game = game

    def intro(self):
        slow_print("[bold white]Underground Kingdom[/bold white]", style="bright_white")
        slow_print("Moonlit caves and glowing mushrooms surround you.", style="bright_black")
        slow_print("Creatures speak in poetry; a cult worships “Mo.”", style="cyan")
        pause()
        return 'underground_boss'

    def boss_fight(self):
        slow_print("[bold white]Reflection Boss Fight[/bold white]", style="bright_white")
        slow_print("A nursery carved into stone. An empty cradle glows under bioluminescent mushrooms.", style="bright_black")
        slow_print("BOSS (Reflection of You): “You don’t deserve her memory. You let her go. You let it happen.”", style="red")
        slow_print("YOU: I didn’t choose… I didn’t know what to do.", style="cyan")
        pause()

        ew = self.game.player.emotional_weight
        if ew >= 3:
            slow_print("Your memories calm the boss. It fades into silence.", style="green")
            pause()
            return 'digital_world_intro'
        else:
            slow_print("The boss demands you forget a key memory to proceed.", style="red")
            memories = [m for m in self.game.player.memories.values() if m.held or m.remembered]
            if not memories:
                slow_print("But you have no memories to forget! You must face the consequences.", style="red")
                pause()
                return 'digital_world_intro'

            slow_print("Choose a memory to LET GO:")
            for i, mem in enumerate(memories, 1):
                slow_print(f"{i}. {mem.text} (Weight: {mem.emotional_weight})")
            while True:
                choice = input(f"Enter number (1-{len(memories)}): ").strip()
                if choice.isdigit():
                    idx = int(choice) - 1
                    if 0 <= idx < len(memories):
                        mem_to_forget = memories[idx]
                        self.game.player.remove_memory(mem_to_forget.id)
                        slow_print(f"You let go of: {mem_to_forget.text}", style="yellow")
                        pause()
                        return 'digital_world_intro'
                slow_print("Invalid choice, try again.", style="red")
