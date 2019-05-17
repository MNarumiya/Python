import numpy as np
from scipy.io import wavfile

# 波形を生成
import scipy.signal

frequency = 440.0  # 生成するサイン波の周波数
seconds = 1.0      # 生成する音の秒数
rate = 44100       # 出力する wav ファイルのサンプリング周波数

phases = np.cumsum(2.0 * np.pi * frequency / rate * np.ones(int(rate * seconds)))

# 波形を生成
# wave = scipy.signal.sawtooth(phases) とすると鋸歯状波、
wave = scipy.signal.square(phases)

# 16bit の wav ファイルに書き出す
wave = (wave * float(2 ** 15 - 1)).astype(np.int16)  # 値域を 16bit にする
wavfile.write("sine.wav", rate, wave)
