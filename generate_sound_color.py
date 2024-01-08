import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

def plot_spectrum(s):
    f = np.fft.rfftfreq(len(s))
    return plt.loglog(f, np.abs(np.fft.rfft(s)))[0]

def noise_psd(N, psd=lambda f: 1):
    X_white = np.fft.rfft(np.random.randn(N));
    S = psd(np.fft.rfftfreq(N))
    # Normalize S
    S = S / np.sqrt(np.mean(S ** 2))
    X_shaped = X_white * S;
    return np.fft.irfft(X_shaped);

def PSDGenerator(f):
    return lambda N: noise_psd(N, f)

@PSDGenerator
def white_noise(f):
    return 1;

@PSDGenerator
def blue_noise(f):
    return np.sqrt(f);

@PSDGenerator
def violet_noise(f):
    return f;

@PSDGenerator
def brownian_noise(f):
    return 1 / np.where(f == 0, float('inf'), f)

@PSDGenerator
def pink_noise(f):
    return 1 / np.where(f == 0, float('inf'), np.sqrt(f))


rate = 44_100
duration = 3600 # in seconds
write(f'./output/brown.wav', rate, brownian_noise(duration*rate))

# plt.style.use('dark_background')
# plt.figure(figsize=(12, 8), tight_layout=True)
# for G, c in zip(
#         [brownian_noise, pink_noise, white_noise, blue_noise, violet_noise],
#         ['brown', 'hotpink', 'white', 'blue', 'violet']):
#     plot_spectrum(G(duration*rate)).set(color=c, linewidth=3)
#     write(f'./output/{c}.wav', rate, G(duration*rate))
#
# plt.legend(['brownian', 'pink', 'white', 'blue', 'violet'])
# plt.suptitle("Colored Noise")
# plt.ylim([1e-3, None])
# plt.show()
