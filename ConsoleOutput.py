import wx
import sys

class ConsoleOutput:
    def __init__(self, progress_bar):
        self.progress_bar = progress_bar
        
        # Store the original sys.stdout
        self.original_stdout = sys.stdout
        
    def write(self, text):
        self.original_stdout.write(text)
        
        # Update progress bar based on the captured output
        self.update_progress_bar(text)
        
    def update_progress_bar(self, text):
        # Extract the progress and total from the text
        progress, total = self.extract_progress(text)
        
        if progress is not None and total is not None:
            # Update the progress bar
            self.progress_bar.SetValue(progress)
            self.progress_bar.SetRange(total)
        
    def extract_progress(self, text):
        # Parse the progress and total from the text
        try:
            progress, total = map(int, text.strip().split('/'))
            return progress, total
        except (ValueError, IndexError):
            return None, None
