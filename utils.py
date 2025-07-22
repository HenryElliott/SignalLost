import time
import random
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.align import Align

console = Console()

def slow_print(text, delay=0.03, style=None):
    styled_text = Text(text, style=style) if style else Text(text)
    for char in styled_text.plain:
        if char == ' ':
            time.sleep(delay / 2)
        else:
            time.sleep(delay * random.uniform(0.8, 1.2))
        console.print(char, end='', style=style, soft_wrap=True)
        console.file.flush()
    console.print()

def clear_screen():
    console.clear()

def pause(prompt="Press Enter to continue..."):
    console.print(f"[bold magenta]{prompt}[/]")
    input()

def prompt_choice(message, choices):
    """choices = dict of key: description"""
    while True:
        console.print(f"\n[bold cyan]{message}[/]")
        for key, desc in choices.items():
            console.print(f"  [yellow]{key}[/]: {desc}")
        choice = input("> ").strip().lower()
        if choice in choices:
            return choice
        console.print("[red]Invalid choice, please try again.[/]")

def prompt_yes_no(message):
    while True:
        ans = input(f"{message} (y/n): ").strip().lower()
        if ans in ('y', 'yes'):
            return True
        elif ans in ('n', 'no'):
            return False
        else:
            console.print("[red]Please enter y or n.[/]")

def print_header(title):
    header_panel = Panel(Align.center(f"[bold white]{title}[/]"), style="blue")
    console.print(header_panel)

def fade_out(duration=1.0):
    time.sleep(duration)
    clear_screen()
