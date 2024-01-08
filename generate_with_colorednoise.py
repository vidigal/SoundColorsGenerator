import colorednoise as cn
from matplotlib import pylab as plt
from scipy.io.wavfile import write

#input values
beta = 2         # the exponent: 0=white noite; 1=pink noise;  2=red noise (also "brownian noise")
samples = 2**32  # number of samples to generate (time series extension)

#Deffing some colores
A = cn.powerlaw_psd_gaussian(beta, samples)

#Ploting first subfiure
plt.plot(A, color='black', linewidth=1)
plt.title('Colored Noise for β='+str(beta))
plt.xlabel('Samples (time-steps)')
plt.ylabel('Amplitude(t)', fontsize='large')
plt.xlim(1, 5000)
plt.show()

write('./output/generated_with_colorednoise.wav', 44100, A)