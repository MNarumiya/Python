import numpy as np
from scipy.io import wavfile

# コマンドライン引数用
import sys


def create_sin_sound():
    args = sys.argv

    if (len(args) < 1):
        print("input: python create_sin.py frequency")
        return

    frequency = int(args[1])  # 生成するサイン波の周波数
    seconds = 1.0      # 生成する音の秒数
    rate = 44100       # 出力する wav ファイルのサンプリング周波数

    phases = np.cumsum(2.0 * np.pi * frequency / rate * np.ones(int(rate * seconds)))


    wave = np.sin(phases) # -1.0 〜 1.0 の値の矩形波

    # 16bit の wav ファイルに書き出す
    wave = (wave * float(2 ** 15 - 1)).astype(np.int16)  # 値域を 16bit にする
    wavfile.write("sin"+str(frequency)+".wav", rate, wave)

if __name__ == '__main__':
    create_sin_sound()
