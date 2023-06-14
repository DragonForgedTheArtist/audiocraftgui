import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write
import os
from utils import generate_random_filename
import json
import sys

# Generate audio based on input melody.  Working on a way to work this
# into the gui

config = {}

if len(sys.argv) < 2:
    print("Usage: %s <config json file>" % sys.argv[0])
    print("  See melody_config.json for example")
    exit()

f = open(sys.argv[1], "r", encoding="utf-8")
config = json.loads(f.read())
f.close()

if config.get("melody") is None:
    print("Malformed json config file")
    print("  See melody_config.json for example")
    exit()

temppath = "temp"

if not os.path.exists(temppath):
    os.makedirs(temppath)

descriptions = []
for i in range(config['generations']):
    descriptions.append(config["prompt"])

model = MusicGen.get_pretrained('melody')
model.set_generation_params(duration=config["duration"])

melody_waveform, sr = torchaudio.load(config["melody"])
melody_waveform = melody_waveform.unsqueeze(0).repeat(config["generations"], 1, 1)

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
