# audiocraftgui
 A wxPython gui for AudioCraft

# Installation

- git clone https://github.com/DragonForgedTheArtist/audiocraftgui.git
- cd audiocraftgui
- python -m venv .
- .\Scripts\activate
- pip install -r requirements.txt

# Running

## Windows
- In Exploror, navigate to the folder where you cloned audiocraftgui
- type cmd in the location bar
- .\Scripts\activate
- python audiogen.py

You can use the "Load" button to load a song you want to continue into the main track.  The "Save" button saves your composition from the main track.  The "Clear" button clears the main track. 

Set the duration for the _total_ duration you want to generate (length + overlap.) Generations is how many options you want to generate and the Overlap is how large of a window you want the generator to take into account in your continuation.  You can select which model you want to use from the dropdown.

If there is no track in the main audio, it will generate for the full length.

After it is finished generating, you can select from the options by clicking the corresponding "Keep" button and that selection will be appended onto the main track.

A neat trick.  You can load an audio into the main track, generate, clear it, and then select one of the generations.  The ability to do this is intentional.  It allows you to create an audio based on a continuation of another song without including that song if you choose.