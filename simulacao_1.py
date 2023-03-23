import numpy as np
import soundfile as sf

# Lendo o arquivo de áudio da resposta ao impulso e amostra gravada e extraindo apenas o primeiro canal (mono)
impulse_data, impulse_rate = sf.read("Church_Schellingwoude.wav")
impulse_data = impulse_data[:, 0]

voice_data, voice_rate = sf.read("amostraOriginal.wav")
voice_data = voice_data[:, 0]

# Realizando uma convolução entre a amostra de voz e a resposta ao impulso 
convolution_data = np.convolve(voice_data, impulse_data)

# Salvar o resultado da convolução em um arquivo de áudio 
sf.write("Convolution.wav", convolution_data, voice_rate)