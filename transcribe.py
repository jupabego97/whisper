import os
import streamlit as st
import whisper

# Load the Whisper model once at startup (choose your preferred model size)
model = whisper.load_model("base")

def main():
    st.title("Audio Transcriber with Whisper")
    st.write("Upload an audio file and let Whisper transcribe it for you.")
    
    # Create a file uploader for audio files
    audio_file = st.file_uploader("Upload an Audio File", type=["mp3", "wav", "m4a", "flac", "ogg"])

    if audio_file is not None:
        # Save the uploaded file to a temporary location
        with open("temp_audio_file", "wb") as f:
            f.write(audio_file.getbuffer())
        
        st.info("Transcribing... This may take a moment.")

        # Use the Whisper model to transcribe
        result = model.transcribe("temp_audio_file")
        transcription = result["text"]

        # Display the transcription
        st.success("Transcription:")
        st.write(transcription)

        # Optionally remove the temporary file
        os.remove("temp_audio_file")

if __name__ == "__main__":
    main()
