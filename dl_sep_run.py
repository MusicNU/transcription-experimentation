import subprocess
from pytube import YouTube
from pytube import extract
import sys
import os
from spleeter.separator import Separator
import demucs.separate
from io import BytesIO
def download_audio(link,):
    yt = YouTube(str(link))
    audio_stream = yt.streams.filter(only_audio=True).first()
    buffer = BytesIO()
    audio_stream.stream_to_buffer(buffer)
    print("audio_stream", audio_stream)
    #Converts mp4 from byte stream into a wav which is downloaded as video_id . wav
    filename = extract.video_id(link)  + '.wav'
    process = subprocess.Popen(['ffmpeg', '-i', '-', '-vn', '-ac', '2', '-f', 'wav',  './'+ filename], 
                               stdin=subprocess.PIPE)
    process.communicate(input=buffer.getvalue())
    return filename

def separate_vocals(wav_file_path, output_dir):
    separator = Separator('spleeter:2stems')
    separator.separate_to_file(wav_file_path, output_dir)
    # Spleeter creates a subdirectory in output_dir named after the input file
    input_filename = os.path.basename(wav_file_path).replace('.wav', '')
    output_subdir = os.path.join(output_dir, input_filename)
    vocal_file_path = os.path.join(output_subdir, 'vocals.wav')
    print("Finished separating vocals")
    return vocal_file_path
    
def demuscs_separate(input_file_path):
    demucs.separate.main(["--mp3", "--two-stems", "vocals", "-n", "mdx_extra", input_file_path])
    return os.path.join(os.path.dirname(input_file_path), 'vocals.wav') 
    

def analyze_song(vocal_file_path):
    model_output, midi_data, note_events = predict(vocal_file_path, basic_pitch_model)
    # Save the midi data to a file
    midi_data.write('output.mid')
if __name__ == "__main__":
    link = sys.argv[1]
    output_dir = 'output'

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    wav_file_path = download_audio(link)
    # vocal_file_path = separate_vocals(wav_file_path, output_dir)
    demuscs_separate(wav_file_path)
    subprocess.run(['python', 'basic-pitch.py', vocal_file_path])
    
    
    # print(vocal_file_path)

    # Clean up the temporary files
    # os.remove(wav_file_path)
