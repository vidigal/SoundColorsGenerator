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

duration_s = 35
freq_hz = 9990.0
plt.style.use('dark_background')
sps = 48000
plt.figure(figsize=(12, 8), tight_layout=True)
for G, c in zip(
        [brownian_noise, pink_noise, white_noise, blue_noise, violet_noise],
        ['brown', 'hotpink', 'white', 'blue', 'violet']):
    plot_spectrum(G(duration_s*sps)).set(color=c, linewidth=3)

    each_sample_number = np.arange(duration_s * sps)
    waveform = np.sin(2 * np.pi * G(duration_s*sps) * freq_hz / sps)
    waveform_quiet = waveform * 0.3
    waveform_integers = np.int16(waveform_quiet * 32767)
    plot_spectrum(np.int16(waveform_quiet * 32767)).set(color=c, linewidth=3)


    write(f'./output/{c}.wav', sps, waveform_integers)

plt.legend(['brownian', 'pink', 'white', 'blue', 'violet'])
plt.suptitle("Colored Noise");
plt.ylim([1e-3, None]);
plt.show(block=True)

