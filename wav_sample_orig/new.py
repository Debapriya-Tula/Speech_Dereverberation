# Import the package and create an audio effects chain function.
from pysndfx import AudioEffectsChain

fx = (
    AudioEffectsChain()
    .highshelf()
    .reverb()
    .phaser()
    .delay()
    .lowshelf()
)

infile = 'S2_class_english.wav'
outfile = 'my_processed_audio_file.wav'

# Apply phaser and reverb directly to an audio file.
fx(infile, outfile)
