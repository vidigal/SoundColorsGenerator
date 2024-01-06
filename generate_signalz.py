import signalz
from scipy.io.wavfile import write

rate = 48000

x = signalz.brownian_noise(1000000, leak=0.1, start=10, std=1, source="gaussian")

write(f'./output/b.wav', rate, x)