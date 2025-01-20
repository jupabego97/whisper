import os
import streamlit as st
import whisper



# Load the Whisper model once at startup (choose your preferred model size)
model = whisper.load_model("small")

def main():
    st.title("Transcripcion de audio para albita")
    st.write("Suba el audio que quiere transcirbir")
    
    # Create a file uploader for audio files
    audio_file = st.file_uploader("Suba al archivo de audio", type=["mp3", "wav", "m4a", "flac", "ogg"])

    if audio_file is not None:
        # Save the uploaded file to a temporary location
        with open("temp_audio_file", "wb") as f:
            f.write(audio_file.getbuffer())
        
        st.info("Transcribiendo... esto se demora, pero funciona,tengale paciencia")

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
