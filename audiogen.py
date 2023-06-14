from AudioGenUI import AudioGenUI
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write
from audiocraft.data.audio_utils import convert_audio
from ConsoleOutput import ConsoleOutput
import os
import random
import string
import sys
import time
import torch
import torchaudio
import wx

temppath = "temp"
emptyfile = "assets%sempty.mp3" % os.path.sep

# Using small model, better results would be obtained with `medium` or `large`.
class MyApp(wx.App):
    def OnInit(self):
        self.frame = AudioGenUI(None)
        self.SetTopWindow(self.frame)
        self.option_tracks=[]
        self.audio_options=[]

        for i in range(5):
            self.audio_options.append(None)
        self.option_tracks.append(self.frame.mctrlOption1)
        self.option_tracks.append(self.frame.mctrlOption2)
        self.option_tracks.append(self.frame.mctrlOption3)
        self.option_tracks.append(self.frame.mctrlOption4)
        self.option_tracks.append(self.frame.mctrlOption5)

        self.keepButtons=[]
        self.frame.btnGenerate.Bind(wx.EVT_BUTTON, self.Generate)
        self.frame.btnLoad.Bind(wx.EVT_BUTTON, self.LoadWav)
        self.frame.btnSave.Bind(wx.EVT_BUTTON, self.SaveFile)
        self.frame.btnClear.Bind(wx.EVT_BUTTON, self.Clear)
        self.frame.btnOption1.Bind(wx.EVT_BUTTON, self.SelectOption)
        self.frame.btnOption2.Bind(wx.EVT_BUTTON, self.SelectOption)
        self.frame.btnOption3.Bind(wx.EVT_BUTTON, self.SelectOption)
        self.frame.btnOption4.Bind(wx.EVT_BUTTON, self.SelectOption)
        self.frame.btnOption5.Bind(wx.EVT_BUTTON, self.SelectOption)
        self.keepButtons.append(self.frame.btnOption1)
        self.keepButtons.append(self.frame.btnOption2)
        self.keepButtons.append(self.frame.btnOption3)
        self.keepButtons.append(self.frame.btnOption4)
        self.keepButtons.append(self.frame.btnOption5)
        # Redirect console output to custom output stream
        sys.stdout = ConsoleOutput(self.frame.progress_bar)
        self.joined_audio = None

        for ctrl in self.option_tracks:
            ctrl.ShowPlayerControls(wx.media.MEDIACTRLPLAYERCONTROLS_DEFAULT)
            ctrl.Load(emptyfile)
        self.frame.mctrlMain.ShowPlayerControls(wx.media.MEDIACTRLPLAYERCONTROLS_DEFAULT)
        self.frame.mctrlMain.Load(emptyfile)
        self.audio = None

        self.temp_audio = None
        self.sample_rate = 32000
        self.frame.Show()
        return True
    
    def SelectOption(self, event):
        button = event.GetEventObject()
        for i in range(len(self.keepButtons)):
            if button == self.keepButtons[i]:
                if not self.audio is None:
                    start_waveform, sample_rate = torchaudio.load(self.audio)
                    start_waveform = convert_audio(start_waveform,sample_rate,self.sample_rate,1)
                    end_waveform, sample_rate = torchaudio.load(self.audio_options[i])
                    end_waveform = convert_audio(end_waveform,sample_rate,self.sample_rate,1)

                    full_audio = torch.cat([start_waveform, end_waveform], dim=1)
                    fn = self.generate_random_filename()
                    fn = "%s%s%s" % (temppath, os.path.sep, fn)
                    audio_write(fn, full_audio.cpu(), self.sample_rate)

                    self.temp_audio = "%s.wav" % fn
                    self.frame.mctrlMain.Load(self.temp_audio)
                else:
                    self.temp_audio = self.audio_options[i]
                    self.frame.mctrlMain.Load(self.temp_audio)

    def extend_audio(self, model, prompt):
        overlap = self.overlap
        generations = self.frame.spnGenerations.GetValue()

        #prompt_waveform, self.sample_rate = torchaudio.load("%s.wav" % self.audio)
        end_waveform, sample_rate = torchaudio.load(self.audio)
        end_waveform = convert_audio(end_waveform,sample_rate,self.sample_rate,1)

        # Calculate the number of samples corresponding to the overlap
        overlap_samples = int(overlap * self.sample_rate)

        # Grab the end of the wafeform
        end_waveform = end_waveform[...,-overlap_samples:]

        batch = torch.cat(generations*[torch.unsqueeze(end_waveform,0)])
        prompts = []
        for i in range(generations):
            prompts.append(prompt)

        # Process the trimmed waveform using the model
        output = model.generate_continuation(batch, descriptions=prompts,prompt_sample_rate=self.sample_rate, progress=True)

        # Cut the seed audio off the newly generated audio
        output = output[...,overlap_samples:]

        return output
    

    def Clear(self, event):
        self.frame.mctrlMain.Load(emptyfile)
        self.audio = None
        self.temp_audio = None
        pass

    def SaveFile(self, event):
        if self.temp_audio is None:
            return
        wildcard = "Wave Audio (*.wav)|*.wav"
        dlg = wx.FileDialog(self.frame, defaultDir=os.getcwd(), message="Choose an audio file", wildcard=wildcard, style=wx.FD_SAVE)

        if dlg.ShowModal() == wx.ID_OK:
            selected_file = dlg.GetPath()
            outfile = selected_file[:selected_file.rfind(".")]
            end_waveform, sample_rate = torchaudio.load(self.temp_audio)
            end_waveform = convert_audio(end_waveform,sample_rate,self.sample_rate,2)
            audio_write(outfile, end_waveform.cpu(), self.sample_rate)
            print(outfile, type)
        dlg.Destroy()

    def LoadWav(self, event):
        wildcard = "Supported Audio Files|*.wav;*.mp3|Wave Audio (*.wav)|*.wav|MP3 Audio (*.mp3)|*.mp3|All files (*.*)|*.*"
        dlg = wx.FileDialog(self.frame, defaultDir=os.getcwd(), message="Choose an audio file", wildcard=wildcard, style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if dlg.ShowModal() == wx.ID_OK:
            selected_file = dlg.GetPath()
            # Process the selected file here
            self.temp_audio = selected_file
            self.frame.mctrlMain.Load(selected_file)
        dlg.Destroy()

    def Generate(self, event):
        start_time = time.time()
        prompt = self.frame.txtPrompt.GetValue()
        duration = self.frame.spnDuration.GetValue()
        generations = self.frame.spnGenerations.GetValue()
        total_duration =duration

        self.audio = self.temp_audio

        if not os.path.exists(temppath):
            os.makedirs(temppath)

        # Cleanup the temp dir
        for f in os.listdir(temppath):
            fn = "%s%s%s" % (temppath, os.path.sep, f)
            if not fn == self.audio:
                os.remove(fn)
            pass

        # TODO: Add form fields for these properties
        self.top_k = 250
        self.overlap = self.frame.spnOverlap.GetValue()

        prompts=[]
        for i in range(generations):
            prompts.append(prompt)

        model = MusicGen.get_pretrained(self.frame.chcModel.GetString(self.frame.chcModel.GetSelection()))
        model.set_generation_params(
            use_sampling=True,
            top_k=self.top_k,
            duration=duration
        )

        output = None
        for i in range(5):
            self.audio_options[i]=None
            self.keepButtons[i].Enabled=False
            self.option_tracks[i].Load(emptyfile)

        self.frame.lblStatus.SetLabelText("Generating...")

        output=[]
        if self.audio is None:
            output = model.generate(descriptions=prompts,progress=True)
        else:
            output = self.extend_audio(model, prompt)
            total_duration -= self.overlap;
        for i in range(len(output)):
            fn = self.generate_random_filename()
            fn = "%s%s%s" % (temppath, os.path.sep, fn)
            self.audio_options[i]="%s.wav" % fn
            audio_write(fn, output[i].cpu(), self.sample_rate)
            self.option_tracks[i].Load(self.audio_options[i])
            self.keepButtons[i].Enabled=True

        end_time = time.time()
        execution_time = end_time - start_time
        self.frame.progress_bar.SetValue(0)
        self.frame.lblStatus.SetLabelText("%d seconds of audio generated in %.2f seconds" % (total_duration, execution_time))

    def generate_random_filename(self, length=8, extension=''):
        # Generate a random string of uppercase letters, lowercase letters, and digits
        letters_and_digits = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(letters_and_digits) for _ in range(length))
        
        # Combine the random string with the given extension (if any)
        filename = random_string + extension
        
        return filename

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()


#filename = self.generate_random_filename(10, '.txt')