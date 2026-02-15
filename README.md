# Voice Assistant - AI JONAS PHOTO

A Python-based voice recognition and command system that integrates speech-to-text, AI response generation, and Arduino microcontroller communication. This project implements continuous monitoring with ambient noise calibration and context-aware microphone input.

## 📋 Table of Contents

- [Features](#features)
- - [Project Structure](#project-structure)
  - - [Requirements](#requirements)
    - - [Installation](#installation)
      - - [Configuration](#configuration)
        - - [Usage](#usage)
          - - [File Descriptions](#file-descriptions)
            - - [API & Dependencies](#api--dependencies)
              - - [Troubleshooting](#troubleshooting)
                - - [Contributing](#contributing)
                  - - [License](#license)
                   
                    - ## ✨ Features
                   
                    - - **Voice Recognition**: Real-time speech-to-text conversion using Google Speech Recognition API
                      - - **Continuous Monitoring**: Always-listening system with ambient noise calibration
                        - - **AI Response Generation**: Intelligent text responses based on recognized commands
                          - - **Arduino Integration**: Serial communication with microcontroller devices (baud rate: 9600)
                            - - **Audio Feedback**: Text-to-speech output with configurable playback
                              - - **Audio Recording**: Automatic recording and storage of voice inputs in dedicated folder
                                - - **Noise Filtering**: Dynamic ambient noise adjustment (0.5s adjustment period)
                                  - - **Error Handling**: Graceful timeout handling and user feedback mechanisms
                                    - - **Energy Efficient**: Configurable energy thresholds and dynamic sensitivity adjustment
                                     
                                      - ## 📁 Project Structure
                                     
                                      - ```
                                        Voice/
                                        ├── main.py              # Main application entry point with continuous monitoring loop
                                        ├── jarvis.py            # Arduino communication and helper functions module
                                        ├── test.py              # Testing and debugging utilities
                                        ├── README.md            # Documentation (this file)
                                        └── rekaman/             # Directory for storing voice recordings
                                            └── [audio files]    # Recorded audio files (.wav format)
                                        ```

                                        ## 🔧 Requirements

                                        ### System Requirements
                                        - Python 3.6 or higher
                                        - - Microphone input device
                                          - - Speaker or audio output device
                                            - - Arduino board (for hardware integration, optional)
                                              - - USB Serial connection (for Arduino communication)
                                               
                                                - ### Python Dependencies
                                                - - `speech_recognition` - Voice recognition and audio processing
                                                  - - `pyttsx3` - Text-to-speech conversion
                                                    - - `pyaudio` - Audio input/output interface
                                                      - - `pyserial` - Arduino serial communication
                                                        - - `winsound` - Audio feedback notifications (Windows)
                                                         
                                                          - ## 📦 Installation
                                                         
                                                          - ### 1. Clone the Repository
                                                          - ```bash
                                                            git clone https://github.com/FakhriadiRasyaad/Voice.git
                                                            cd Voice
                                                            ```

                                                            ### 2. Create Virtual Environment (Recommended)
                                                            ```bash
                                                            # Windows
                                                            python -m venv venv
                                                            venv\Scripts\activate

                                                            # Linux/macOS
                                                            python3 -m venv venv
                                                            source venv/bin/activate
                                                            ```

                                                            ### 3. Install Dependencies
                                                            ```bash
                                                            pip install SpeechRecognition pyttsx3 PyAudio pyserial
                                                            ```

                                                            ### 4. Create Recording Directory
                                                            ```bash
                                                            mkdir rekaman
                                                            ```

                                                            ### 5. Hardware Setup (Optional)
                                                            - Connect Arduino to USB port
                                                            - - Verify COM port in Device Manager (Windows) or `/dev/ttyUSB*` (Linux)
                                                             
                                                              - ## ⚙️ Configuration
                                                             
                                                              - ### Audio Settings
                                                              - Edit `main.py` to configure audio parameters:
                                                             
                                                              - ```python
                                                                # Energy threshold for voice detection (higher = less sensitive)
                                                                rec.energy_threshold = 400

                                                                # Dynamic energy adjustment (enables adaptive sensitivity)
                                                                rec.dynamic_energy_threshold = True

                                                                # Phrase time limit for audio capture (seconds)
                                                                phrase_time_limit = 3
                                                                ```

                                                                ### Ambient Noise Calibration
                                                                The system automatically calibrates to ambient noise levels:

                                                                ```python
                                                                with sr.Microphone() as source:
                                                                    # Adjust for ambient noise (1.5 second duration)
                                                                    rec.adjust_for_ambient_noise(source, duration=1.5)
                                                                ```

                                                                ### Arduino Configuration
                                                                Modify COM port and baud rate in `jarvis.py`:

                                                                ```python
                                                                # Serial port configuration
                                                                COM_PORT = 'COM3'      # Change to your Arduino port
                                                                BAUD_RATE = 9600      # Standard Arduino baud rate
                                                                ```

                                                                ### Beep Settings
                                                                Configure feedback notifications in `main.py`:

                                                                ```python
                                                                # Success feedback: 1000Hz for 500ms
                                                                winsound.Beep(1000, 500)

                                                                # Ready status: Single beep
                                                                winsound.Beep(1000, 500)
                                                                ```

                                                                ## 🚀 Usage

                                                                ### Basic Usage
                                                                ```bash
                                                                python main.py
                                                                ```

                                                                ### Running with Python 3
                                                                ```bash
                                                                python3 main.py
                                                                ```

                                                                ### System Output Example
                                                                ```
                                                                === AI JONAS PHOTO: CONTINUOUS MONITORING (HEMING) ===
                                                                Menyesuaikan noise latar belakang... silakan diam sebentar.
                                                                Sistem Standby. Silakan sebutkan perintah (Hai/Preset/Angka/Bye).
                                                                Terdeteksi suara: [detected text]

                                                                1. Logika Sapaan
                                                                   - Input: "halo"
                                                                   - Output: "Halo juga!"

                                                                2. Logika Preset
                                                                   - Input: "preset"
                                                                   - Output: Executes preset commands

                                                                3. Numeric Input
                                                                   - Input: Number-based commands
                                                                   - Output: Processes numeric actions
                                                                ```

                                                                ### Voice Commands
                                                                The system recognizes several command types:

                                                                1. **Greetings** ("halo", "hai")
                                                                2.    - System responds with greeting feedback
                                                                  
                                                                      -    2. **Presets** ("preset")
                                                                           3.    - Triggers pre-configured automation sequences
                                                                             
                                                                                 -    3. **Numeric** (0-99)
                                                                                      4.    - Executes number-based operations
                                                                                        
                                                                                            -    4. **Exit** ("bye", "exit")
                                                                                                 5.    - Gracefully terminates the program
                                                                                                   
                                                                                                       - ## 📄 File Descriptions
                                                                                                   
                                                                                                       - ### main.py
                                                                                                       - **Purpose**: Main application controller
                                                                                                   
                                                                                                       - **Key Functions**:
                                                                                                       - - `play_audio(file_name)`: Plays audio file from `rekaman/` directory with feedback beep
                                                                                                         - - `main()`: Core event loop implementing continuous monitoring
                                                                                                          
                                                                                                           - **Key Features**:
                                                                                                           - - Initializes speech recognizer with ambient noise calibration
                                                                                                             - - Implements 3-second phrase time limit for voice capture
                                                                                                               - - Stores recognized audio in rekaman folder
                                                                                                                 - - Provides user feedback with status messages and beeps
                                                                                                                   - - Handles multiple command types (greeting, preset, numeric)
                                                                                                                     - - Graceful error handling for timeout and unknown phrases
                                                                                                                      
                                                                                                                       - ### jarvis.py
                                                                                                                       - **Purpose**: Hardware integration and utility functions module
                                                                                                                      
                                                                                                                       - **Key Functions**:
                                                                                                                       - - `init_arduino()`: Initializes serial connection to Arduino board
                                                                                                                         - - `send_to_arduino(data)`: Transmits command data to microcontroller
                                                                                                                           - - `play_audio(file_name)`: Manages audio playback operations
                                                                                                                             - - `main()`: Support function for main application
                                                                                                                              
                                                                                                                               - **Features**:
                                                                                                                               - - Serial port configuration and management
                                                                                                                                 - - Arduino communication protocol handling
                                                                                                                                   - - Integrated audio system controls
                                                                                                                                     - - Error handling for hardware failures
                                                                                                                                      
                                                                                                                                       - ### test.py
                                                                                                                                       - **Purpose**: Development and testing utilities
                                                                                                                                      
                                                                                                                                       - **Usage**:
                                                                                                                                       - - Run debugging and functional tests
                                                                                                                                         - - Test individual components in isolation
                                                                                                                                           - - Validate microphone and speaker configuration
                                                                                                                                             - - Verify Arduino communication (if connected)
                                                                                                                                              
                                                                                                                                               - ## 🔌 API & Dependencies
                                                                                                                                              
                                                                                                                                               - ### SpeechRecognition Library
                                                                                                                                               - ```python
                                                                                                                                                 import speech_recognition as sr

                                                                                                                                                 # Initialize recognizer
                                                                                                                                                 rec = sr.Recognizer()

                                                                                                                                                 # Capture audio
                                                                                                                                                 with sr.Microphone() as source:
                                                                                                                                                     audio = rec.listen(source, phrase_time_limit=3)

                                                                                                                                                 # Recognize speech
                                                                                                                                                 text = rec.recognize_google(audio, language='id-ID')
                                                                                                                                                 ```
                                                                                                                                                 
                                                                                                                                                 ### PyTTSX3 (Text-to-Speech)
                                                                                                                                                 ```python
                                                                                                                                                 from pyttsx3 import init

                                                                                                                                                 engine = init()
                                                                                                                                                 engine.say("Your text here")
                                                                                                                                                 engine.runAndWait()
                                                                                                                                                 ```
                                                                                                                                                 
                                                                                                                                                 ### PySerial (Arduino Communication)
                                                                                                                                                 ```python
                                                                                                                                                 import serial

                                                                                                                                                 ser = serial.Serial('COM3', 9600)
                                                                                                                                                 ser.write(b'command')
                                                                                                                                                 ser.close()
                                                                                                                                                 ```
                                                                                                                                                 
                                                                                                                                                 ### Winsound (Audio Notifications)
                                                                                                                                                 ```python
                                                                                                                                                 import winsound

                                                                                                                                                 # Play beep: frequency=1000Hz, duration=500ms
                                                                                                                                                 winsound.Beep(1000, 500)
                                                                                                                                                 ```
                                                                                                                                                 
                                                                                                                                                 ## 🐛 Troubleshooting
                                                                                                                                                 
                                                                                                                                                 ### Microphone Not Detected
                                                                                                                                                 ```
                                                                                                                                                 Error: Could not understand audio
                                                                                                                                                 Solution:
                                                                                                                                                 1. Check microphone connection and permissions
                                                                                                                                                 2. Verify audio input device in system settings
                                                                                                                                                 3. Run audio testing in test.py
                                                                                                                                                 4. Increase phrase_time_limit in main.py
                                                                                                                                                 ```
                                                                                                                                                 
                                                                                                                                                 ### Arduino Connection Failed
                                                                                                                                                 ```
                                                                                                                                                 Error: Cannot open serial port
                                                                                                                                                 Solution:
                                                                                                                                                 1. Verify USB cable connection
                                                                                                                                                 2. Check Arduino COM port in Device Manager
                                                                                                                                                 3. Update COM_PORT variable in jarvis.py
                                                                                                                                                 4. Ensure correct baud rate (9600)
                                                                                                                                                 5. Install CH340 driver if using Chinese Arduino clones
                                                                                                                                                 ```
                                                                                                                                                 
                                                                                                                                                 ### Audio Playback Issues
                                                                                                                                                 ```
                                                                                                                                                 Error: Cannot play audio from rekaman folder
                                                                                                                                                 Solution:
                                                                                                                                                 1. Verify speaker connections
                                                                                                                                                 2. Check Windows/system volume settings
                                                                                                                                                 3. Ensure audio files exist in rekaman/ directory
                                                                                                                                                 4. Test with test.py audio playback function
                                                                                                                                                 ```
                                                                                                                                                 
                                                                                                                                                 ### Google Speech Recognition Timeout
                                                                                                                                                 ```
                                                                                                                                                 Error: Listening timed out while waiting for phrase to start
                                                                                                                                                 Solution:
                                                                                                                                                 1. Check internet connection
                                                                                                                                                 2. Increase phrase_time_limit value
                                                                                                                                                 3. Reduce energy_threshold for better sensitivity
                                                                                                                                                 4. Recalibrate ambient noise: adjust_for_ambient_noise()
                                                                                                                                                 ```
                                                                                                                                                 
                                                                                                                                                 ### Out of Memory / Slow Performance
                                                                                                                                                 ```
                                                                                                                                                 Error: System becomes sluggish over time
                                                                                                                                                 Solution:
                                                                                                                                                 1. Monitor rekaman/ folder size (clear old recordings)
                                                                                                                                                 2. Increase pause_threshold value (0.5 to 1.0)
                                                                                                                                                 3. Reduce audio quality if needed
                                                                                                                                                 4. Restart application periodically
                                                                                                                                                 ```
                                                                                                                                                 
                                                                                                                                                 ## 🤝 Contributing
                                                                                                                                                 
                                                                                                                                                 We welcome contributions! Please follow these guidelines:
                                                                                                                                                 
                                                                                                                                                 1. **Fork** the repository
                                                                                                                                                 2. 2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
                                                                                                                                                    3. 3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
                                                                                                                                                       4. 4. **Push** to the branch (`git push origin feature/amazing-feature`)
                                                                                                                                                          5. 5. **Open** a Pull Request
                                                                                                                                                            
                                                                                                                                                             6. ### Contribution Areas
                                                                                                                                                             7. - Additional voice command logic
                                                                                                                                                                - - Improved error handling
                                                                                                                                                                  - - Enhanced Arduino integration
                                                                                                                                                                    - - Multi-language support
                                                                                                                                                                      - - Performance optimization
                                                                                                                                                                        - - Documentation improvements
                                                                                                                                                                         
                                                                                                                                                                          - ## 📝 License
                                                                                                                                                                         
                                                                                                                                                                          - This project is open source. Please check the repository for license information.
                                                                                                                                                                         
                                                                                                                                                                          - ## 📞 Support & Contact
                                                                                                                                                                         
                                                                                                                                                                          - For issues, questions, or suggestions:
                                                                                                                                                                          - - Open an issue on GitHub
                                                                                                                                                                            - - Check existing documentation
                                                                                                                                                                              - - Review test.py for debugging examples
                                                                                                                                                                               
                                                                                                                                                                                - ## 🔄 Version History
                                                                                                                                                                               
                                                                                                                                                                                - - **v1.0.0** (Feb 12, 2026): Initial release with core features
                                                                                                                                                                                  -   - Voice recognition and response system
                                                                                                                                                                                      -   - Arduino communication
                                                                                                                                                                                          -   - Audio playback and recording
                                                                                                                                                                                              -   - Continuous monitoring loop
                                                                                                                                                                                               
                                                                                                                                                                                                  - ---
                                                                                                                                                                                                  
                                                                                                                                                                                                  **Last Updated**: February 15, 2026
                                                                                                                                                                                                  **Author**: FakhriadiRasyaad
                                                                                                                                                                                                  **Status**: Active Development
                                                                                                                                                                                                  
