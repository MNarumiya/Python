from synthesizer import Synthesizer, Waveform, Writer

# コマンドライン引数用
import sys

def create_sin_sound():
    args = sys.argv

    if (len(args) < 1):
        print("input: python create_sin_syn.py frequency")
        return

    # ここの説明は 音作り を参照
    synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    # 一定音程の波形を生成する
    wave = synth.generate_constant_wave(frequency=int(args[1]), length=1.0)

    # オーディオファイル出力用クラス
    writer = Writer()
    writer.write_wave("sine.wav", wave)

if __name__ == '__main__':
    create_sin_sound()
