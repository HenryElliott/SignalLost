# Signal Lost

**Signal Lost** is a narrative-driven terminal game about longing, memory, and unconditional love.  
Explore shattered worlds and reconnect with Morgan through emotional choices and vivid memories.
Longing for a girl (Morgan) you keep reconnecting with across shattered worlds.
She is peace, beauty, and pain all at once. Every place you visit carries her echoes. The game is about remembering her, understanding yourself, and choosing what parts of love to hold or let go.

## Features

- Three immersive worlds:  
  - **Ruined City** — grief and memory  
  - **Underground Kingdom** — love and reflection  
  - **Digital World** — loss and rewriting  
- Emotional memory system: Remember, Hold On, or Let Go  
- No combat — puzzles and emotional confrontations only  
- Save/load/delete save system  
- Rich terminal colors and slow text for atmosphere  
- Thoughtful branching endings based on player choices

## Installation

1. **Requirements:**  
   - Python 3.8 or higher  
   - `rich` library (`pip install rich`)

2. **Clone or download the repository**  
   ```bash
   git clone https://github.com/yourusername/signal-lost.git
   cd signal-lost
   ```

3. **Install dependencies:**  
   If you have a `requirements.txt` file:  
   ```bash
   pip install -r requirements.txt
   ```  
   Or just install `rich` directly:  
   ```bash
   pip install rich
   ```

## Running the Game

### Windows

Use the provided batch file to launch the game in PowerShell with color support:  
```bat
start_game.bat
```

Or open PowerShell manually and run:  
```powershell
python main.py
```

### Linux / macOS

Make the shell script executable:  
```bash
chmod +x start_game.sh
./start_game.sh
```

Or run manually:  
```bash
python3 main.py
```

## Controls & Navigation

- Use number keys or y/n keys to make choices when prompted.  
- Text appears with a slow typing effect for immersion — wait or press Enter to skip.  
- Save/load/delete your progress anytime from the main menu.  
- Follow on-screen prompts for puzzles and memory management.

## Project Structure

```
SignalLost/
├── assets/
│   ├── images/
│   ├── music/
│   └── fonts/
├── scenes/
│   ├── ruined_city.py
│   ├── underground.py
│   └── digital_world.py
├── data/
│   └── savegame.json
├── utils.py
├── game_state.py
├── main.py
├── start_game.bat
├── start_game.sh
└── README.md
```

## Contributing

Contributions and suggestions are welcome! Feel free to open issues or pull requests.

## License

MIT License © 2025 Henry Elliott

Thank you for playing **Signal Lost**.

