import json
import os
from utils import clear_screen, slow_print, pause, prompt_choice, prompt_yes_no, print_header, fade_out
from game_state import PlayerState
from scenes.ruined_city import RuinedCity
from scenes.underground import UndergroundKingdom
from scenes.digital_world import DigitalWorld

SAVE_FILE = 'data/savegame.json'

class Game:
    def __init__(self):
        self.player = PlayerState()
        self.scenes = {
            'ruined_city_intro': RuinedCity(self).intro,
            'ruined_city_bookstore': RuinedCity(self).bookstore,
            'ruined_city_garden': RuinedCity(self).garden_puzzle,
            'underground_intro': UndergroundKingdom(self).intro,
            'underground_boss': UndergroundKingdom(self).boss_fight,
            'digital_world_intro': DigitalWorld(self).intro,
            'digital_world_vault': DigitalWorld(self).memory_vault,
            'ending_choice': DigitalWorld(self).ending_choice,
        }

    def save_game(self):
        os.makedirs('data', exist_ok=True)
        with open(SAVE_FILE, 'w') as f:
            json.dump(self.player.to_dict(), f, indent=2)
        slow_print("[Game saved successfully.]", style="green")

    def load_game(self):
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, 'r') as f:
                data = json.load(f)
                self.player = PlayerState.from_dict(data)
            slow_print("[Game loaded successfully.]", style="green")
            return True
        else:
            slow_print("[No save file found.]", style="red")
            return False

    def delete_save(self):
        if os.path.exists(SAVE_FILE):
            os.remove(SAVE_FILE)
            slow_print("[Save file deleted.]", style="red")
        else:
            slow_print("[No save file to delete.]", style="yellow")

    def main_menu(self):
        clear_screen()
        print_header("Signal Lost - Main Menu")
        while True:
            choice = prompt_choice("Select an option:", {
                '1': 'Start New Game',
                '2': 'Load Game',
                '3': 'Delete Save File',
                '4': 'Quit',
            })

            if choice == '1':
                self.player = PlayerState()
                slow_print("Starting new game...", style="bold cyan")
                pause()
                clear_screen()
                return True
            elif choice == '2':
                if self.load_game():
                    pause()
                    clear_screen()
                    return True
                else:
                    pause()
                    clear_screen()
            elif choice == '3':
                confirm = prompt_yes_no("Are you sure you want to delete the save file?")
                if confirm:
                    self.delete_save()
                pause()
                clear_screen()
            elif choice == '4':
                slow_print("Goodbye!", style="bold green")
                return False

    def run(self):
        if not self.main_menu():
            return
        while True:
            current_scene_key = self.player.current_scene
            scene_func = self.scenes.get(current_scene_key)
            if scene_func:
                try:
                    next_scene_key = scene_func()
                except Exception as e:
                    from rich import print
                    print(f"[red]Error in scene '{current_scene_key}':[/red] {e}")
                    break
                fade_out(1)
                if next_scene_key == 'quit':
                    slow_print("Thank you for playing Signal Lost. Goodbye.", style="bold green")
                    break
                elif next_scene_key:
                    self.player.current_scene = next_scene_key
                    self.save_game()
                    clear_screen()
                else:
                    slow_print("An error occurred: Scene did not return next scene key.", style="red")
                    break
            else:
                slow_print(f"Scene '{current_scene_key}' not found.", style="red")
                break

if __name__ == "__main__":
    game = Game()
    game.run()
