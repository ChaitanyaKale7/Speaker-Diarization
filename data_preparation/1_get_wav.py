import json
import os
import librosa
import soundfile as sf
import csv

# Load the JSON file
with open('output.json', 'r') as file:
    transcript_data = json.load(file)

# Extract the dialogue segments
if 'dialogue' in transcript_data:
    segments = transcript_data['dialogue']
else:
    raise ValueError("The transcript data does not contain the expected 'dialogue' key.")

# Load the large audio file
audio_file = 'test.wav'
y, sr = librosa.load(audio_file, sr=None)

# Directory to save the audio chunks
output_dir = 'audio_chunks'
os.makedirs(output_dir, exist_ok=True)

# CSV file to save the mappings
csv_file = 'audio_transcript_mapping.csv'

# Function to extract and save audio chunks based on timestamps and create mappings
def save_audio_chunks_and_create_mapping(segments, y, sr, output_dir, csv_file):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['chunk_index', 'audio_chunk_path', 'speaker', 'text', 'start_time', 'end_time'])

        for i, segment in enumerate(segments):
            start_time = segment['start_time']
            end_time = segment['end_time']

            start_sample = int(start_time * sr)
            end_sample = int(end_time * sr)

            chunk = y[start_sample:end_sample]

            # Define the chunk file name
            chunk_filename = os.path.join(output_dir, f'chunk_{i+1:03d}.wav')

            # Save the chunk as a WAV file
            sf.write(chunk_filename, chunk, sr)
            print(f'Saved {chunk_filename}')

            # Write the mapping to the CSV file
            writer.writerow([i+1, chunk_filename, segment['speaker'], segment['text'], start_time, end_time])

# Save the audio chunks and create the CSV mapping file
save_audio_chunks_and_create_mapping(segments, y, sr, output_dir, csv_file)

print('Audio chunks have been saved and mapped to transcript in CSV file.')




















