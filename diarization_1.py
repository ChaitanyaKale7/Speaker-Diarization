# instantiate the pipeline
from pyannote.audio import Pipeline
pipeline = Pipeline.from_pretrained(
  "pyannote/speaker-diarization-3.1",
  use_auth_token="YOUR_TOKEN")

# run the pipeline on an audio file
diarization = pipeline("Nikhil-Kamath.wav", num_speakers=2)

# dump the diarization output to disk using RTTM format
with open("audio1.rttm", "w") as rttm:
    diarization.write_rttm(rttm)

