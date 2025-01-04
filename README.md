# Sonic Assistant

Sonic Assistant is an intelligent virtual assistant designed to simplify everyday tasks. 
It integrates speech recognition, text-to-speech synthesis and various functionalities like note-taking, weather updates, web browsing, and many more.
Its Super Scalable


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
- Replace the placeholder in the weather_api variable with your API key.
- Run the Assistant:
   ```bash   
   python main.py
   ```

## Usage
1. **Start Sonic Assistant:**
   - On running the script, the assistant will greet you and listen for your commands.

2. **Available Commands:**
   - Web Browsing: "Open YouTube", "Open Google"
   - Music Playback: "Play music"
   - Time Inquiry: "What is the current time?"
   - Weather Updates: "What is the weather in [city]?"
   - Note-Taking:
      - "Make a note"
      - "Read note"
      - "Delete note"
   - Application Launch: "Open Tableau"
   - Search: "Search for [query]"
   - Shutdown: "Close", "Stop", or "Shutdown"



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

## Contributions
Contributions are welcome! Please fork the repository, make changes, and submit a pull request.

## Acknowledgments
Weather data provided by WeatherAPI(https://www.weatherapi.com/).

## Happy Coding! 🎉

Let me know if you need further modifications! 😃 

