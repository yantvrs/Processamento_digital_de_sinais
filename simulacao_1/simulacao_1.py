import numpy as np
import soundfile as sf
# 1. Implemente a Convolução da Soma e a utilize para processar um sinal de voz considerando a resposta ao impulso definida pelo arquivo de áudio ’Church Schellingwoude.wav’.Essa resposta ao impulso caracteriza a distorção acústica causada na voz ao se falar no interior da igreja de Schellingwoude em Amsterdã.

# a) O sistema deve armazenar esse audio em um vetor. O áudio fornecido tem formato estéreo (2 canais). Utilize apenas o primeiro canal do áudio (mono), daqui por diante chamado de resposta ao impulso.
impulse_data, impulse_rate = sf.read("Church_Schellingwoude.wav")
impulse_data = impulse_data[:, 0]

# b) Capture uma amostra de sua voz e a armazene em um vetor.
voice_data, voice_rate = sf.read("amostraOriginal.wav")
voice_data = voice_data[:, 0]

# c) Realize uma convolução entre a sua amostra de voz e a resposta ao impulso.
convolution_data = np.convolve(voice_data, impulse_data)

# d) Salve o resultado da convolução em um arquivo de áudio.
sf.write("Convolution.wav", convolution_data, voice_rate)