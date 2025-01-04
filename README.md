# Sonic Assistant

Sonic Assistant is an intelligent virtual assistant designed to simplify everyday tasks.
It integrates speech recognition, text-to-speech synthesis, and functionalities like note-taking, weather updates, web browsing, and more.
Its architecture is super scalable, making it adaptable for future enhancements.


## Features

1. **Voice Interaction:**
   - Responds to commands using natural language processing.
   - Uses text-to-speech for interaction.

2. **Web Browsing:**
   - Opens popular websites like YouTube, Google, Spotify and more.

3. **Music Playback:**
   - Plays predefined music stored locally.

4. **Time Announcements:**
   - Reads out the current time.

5. **Weather Updates:**
   - Fetches and reports current weather conditions for a specified city using the WeatherAPI.

6. **Application Launch:**
   - Opens installed applications like Tableau. We can add many more here

7. **Note-Taking:**
   - Allows users to create, read, and delete notes through voice commands.

8. **Search Functionality:**
   - Performs Google searches based on user queries.

9. **Exit Commands:**
   - Responds to shutdown commands to exit the assistant.



## Requirements

- Python 3.8+
- Internet connection for web-based services (e.g., weather, web browsing)
- Microphone for voice input
- Dependencies:
  - `speechrecognition`
  - `pypiwin32`
  - `requests`
  - `pyttsx3` (optional for speech synthesis)


## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/sonic-assistant.git
   cd sonic-assistant
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up WeatherAPI:**
- Sign up at WeatherAPI to get your API key.
- Replace <your_weather_api_key> in the weather_api variable inside main.py with your API key.
- Run the Assistant:
   ```bash   
   python main.py
   ```

## Usage
1. **Start Sonic Assistant:**
   - On running the script, the assistant will greet you and listen for your commands.

2. **Available Commands:**
Usage
Start Sonic Assistant:

On running the script, the assistant will greet you and listen for your commands.
Available Commands:


| **Command**                | **Action**                                                                                      | **Example**                      |
|----------------------------|-----------------------------------------------------------------------------------------------|----------------------------------|
| **open [website]**          | Opens a specified website in a browser.                                                        | "Open YouTube", "Open Google"    |
| **play music**              | Plays a predefined music file from your system.                                                | "Play music"                     |
| **current time**            | Reports the current time.                                                                     | "What is the current time?"      |
| **open tableau**            | Opens the Tableau application.                                                                 | "Open Tableau"                   |
| **weather in**              | Fetches the current weather for a specified city using the Weather API.                        | "What is the weather in Mumbai?" |
| **search for**              | Performs a Google search for a specified query.                                                | "Search for Python tutorials"    |
| **make note**               | Creates a new note by dictating the content.                                                   | "Make a note"                    |
| **read note**               | Reads a saved note aloud.                                                                      | "Read note"                      |
| **delete note**             | Deletes a saved note.                                                                          | "Delete note"                    |
| **close / shutdown / stop** | Shuts down the assistant.                                                                      | "Stop", "Close", "Shutdown"      |




## Project Structure
```bash
sonic-assistant/
│
├── main.py             # Main script for the assistant
├── requirements.txt    # List of dependencies
└── README.md           # Project documentation
```



## Known Issues
- Speech recognition might fail in noisy environments.
- Weather updates require a valid city name and API key.
- Limited functionality for note management due to fixed filename length.

## Future Enhancements
- Add support for custom voice commands.
- Implement multi-language support.
- Include a graphical user interface (GUI).
- Enhance error handling and command recognition.

## Development Environment
This project was developed using **PyCharm**, a robust and feature-rich IDE for Python development. I personaly loved the code assistance part of it 🙂 

## Contributions
Contributions are welcome! Please fork the repository, make changes, and submit a pull request.

## Acknowledgments
Weather data provided by WeatherAPI(https://www.weatherapi.com/).

## Happy Coding! 🎉

Let me know if you need further modifications! 😃 🫡

