# Importar os módulos necessários
import numpy as np
import soundfile as sf

# Ler o arquivo de áudio da resposta ao impulso e extrair apenas o primeiro canal (mono)
impulse_data, impulse_rate = sf.read("Church_Schellingwoude.wav")
impulse_data = impulse_data[:, 0]

# Ler o arquivo de áudio da amostra de voz e extrair apenas o primeiro canal (mono)
voice_data, voice_rate = sf.read("amostraOriginal.wav")
voice_data = voice_data[:, 0]

# Realizar uma convolução entre a amostra de voz e a resposta ao impulso usando numpy
convolution_data = np.convolve(voice_data, impulse_data)

# Salvar o resultado da convolução em um arquivo de áudio usando soundfile
sf.write("Convolution.wav", convolution_data, voice_rate)