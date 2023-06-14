import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write
import os
from utils import generate_random_filename

# Generate audio based on input melody.  Working on a way to work this
# into the gui

temppath = "temp"
generations = 3
prompt = '80s pop track with bassy drums and synth, 110 bpm'
duration = 30

if not os.path.exists(temppath):
    os.makedirs(temppath)

descriptions = []
for i in range(generations):
    descriptions.append(prompt)

model = MusicGen.get_pretrained('melody')
model.set_generation_params(duration=duration)

melody_waveform, sr = torchaudio.load("assets/bach.mp3")
melody_waveform = melody_waveform.unsqueeze(0).repeat(generations, 1, 1)

output = model.generate_with_chroma(
    descriptions=descriptions,
    melody_wavs=melody_waveform,
    melody_sample_rate=sr,
    progress=True
)
for i in range(len(output)):
    fn = generate_random_filename()
    fn = "%s%s%s" % (temppath, os.path.sep, fn)
    audio_write(fn, output[i].cpu(), 32000)
    print("%s.wav" % fn)
