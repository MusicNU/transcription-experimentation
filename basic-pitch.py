from basic_pitch.inference import predict, Model
from basic_pitch import ICASSP_2022_MODEL_PATH
import sys
import os

basic_pitch_model = Model(ICASSP_2022_MODEL_PATH)

def analyze_song(vocal_file_path):
    model_output, midi_data, note_events = predict(vocal_file_path, basic_pitch_model)
    # Save the midi data to a file
    midi_data.write('output.mid')

if __name__ == "__main__":
    vocal_file_path = sys.argv[1]
    analyze_song(vocal_file_path)