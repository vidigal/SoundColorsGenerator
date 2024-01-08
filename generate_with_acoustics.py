import acoustics
import numpy as np
from scipy.io.wavfile import write

SEED = 42
amount_of_samples = 44100
state = None

song = acoustics.generator.brown(N=amount_of_samples, state=np.random.RandomState(SEED))

write(f'./output/acoustics.wav', amount_of_samples, song)