import numpy as np
import matplotlib.pyplot as plt
import math

# signal amplitude (Unitless)
A = 1

# signal frequency (Hertz)
signal_frequency = 100

# from the frequency find the period (seconds)
signal_period = 1 / signal_frequency

# sampling rate (Hertz)
sampling_rate = 20

# make a simple plot of the signal sampled at the rate over 5 periods
# use np.line space to create a linearly spaced array
time = np.arange(0, 2, 1/sampling_rate)

# now calculate the signal from the resulting sample rate
# signal = Asin(2*pi*f*time+ phase)
signal = A * np.sin(2 * math.pi * signal_frequency * time)

# plot the resulting signal in matplotlib
plt.title('Sample of ' + str(signal_frequency) + ' sine wave at ' + str(sampling_rate) + ' Hertz')
plt.xlabel('Time (s)')
plt.ylabel('Signal')
plt.scatter(time, signal, marker='x', label='Samples')
plt.plot(time, signal, label='Continuous Signal')
plt.legend()
plt.show()
