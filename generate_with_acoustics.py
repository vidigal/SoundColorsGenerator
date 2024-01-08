import acoustics
import numpy as np
from scipy.io.wavfile import write

SEED = 42
rate = 44_100
duration = 3600
state = None

song = acoustics.generator.brown(N=duration*rate, state=np.random.RandomState(SEED))

write(f'./output/acoustics.wav', rate, song)