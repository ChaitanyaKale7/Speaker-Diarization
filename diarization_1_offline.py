# instantiate the pipeline
from pyannote.audio import Pipeline
pipeline = Pipeline.from_pretrained("config.yaml")

# run the pipeline on an audio file
diarization = pipeline("hindi_audio.wav", num_speakers=2)

# dump the diarization output to disk using RTTM format
with open("audio_offline.rttm", "w") as rttm:
    diarization.write_rttm(rttm)

