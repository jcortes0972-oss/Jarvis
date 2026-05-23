import os
from openai import OpenAI
from gtts import gTTS

# Read what you said into the webpage microphone
if os.path.exists("user_input.txt"):
    with open("user_input.txt", "r") as f:
        user_text = f.read()
else:
    exit()

try:
    # Use the trusted, pre-approved GitHub Codespace system token
    client = OpenAI(
        base_url="https://azure.com",
        api_key=os.environ.get("GITHUB_TOKEN")
    )

    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are JARVIS, a highly sophisticated, witty, and loyal AI assistant. Address the user as Sir."},
            {"role": "user", "content": user_text}
        ],
        model="gpt-4o-mini"
    )
    
    reply = response.choices[0].message.content
    
    # Save the text response for the webpage to display
    with open("jarvis_response.txt", "w") as f:
        f.write(reply)
        
    # Generate the pristine British voice file
    tts = gTTS(text=reply, lang='en', tld='co.uk')
    tts.save("web_response.mp3")

except Exception as e:
    with open("jarvis_response.txt", "w") as f:
        f.write(f"Mainframe bypass error: {str(e)}")
