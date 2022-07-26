![cover](https://user-images.githubusercontent.com/33999466/180988596-7b6a199f-148c-471b-828d-c1bc702728a8.jpg)

# Alexa Virtual Assistant in Python
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/shilu143/Alexa/blob/main/LICENSE)<br/><br/>
This is a Virtual Assistant built in Python which can do certain operations using the Voice Command given to it.

Things that this program can do are listed below,
 * Current weather of the current location
 * Open Command prompt
 * Open Visual Studio Code
 * IP Address 
 * Open Youtube
 * Open Google
 * Play videos on Youtube
 * Search on Web

  
## Run Locally

Clone the project

```bash
  git clone https://github.com/shilu143/Alexa.git
```

Go to the project directory

```bash
  cd Alexa
```

Install dependencies

```bash
  pip install SpeechRecognition PyAudio pyttsx3 secure-smtplib
  pip install pywhatkit geocoder pycopy-webbrowser wikipedia
```
Launch 
```bash
  python alexa.py
```
<br />
<br />

### For some of the functionalities, you have to provide some information in the code, ###
  * #### Whatsapp message sending ####
      Have to add the number whom you want to send the message(in the code line 155) <br />
      and also you should be logged in Whatsapp web
  
  * #### Email Sending ####
      Have to add the receiver's email id (in the code line 168) <br />
      Have to add you email id and password (int the code line 69 & 70)

