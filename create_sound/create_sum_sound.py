from synthesizer import Synthesizer, Waveform, Writer

def create_sum_sound():
    # 書き込み用インスタンス
    writer = Writer()

    # 長3度のハモリ
    # osc2_freq_transpose の値がポイント
    synth1 = Synthesizer(
        osc1_waveform=Waveform.sine, osc1_volume=1.0,
        use_osc2=True, osc2_waveform=Waveform.sine,
        osc2_volume=0.8, osc2_freq_transpose=1.25,
    )
    writer.write_wave("third.wav", synth1.generate_constant_wave(frequency=440.0, length=1.0))

    # 完全5度のハモリ
    synth2 = Synthesizer(
        osc1_waveform=Waveform.sine, osc1_volume=1.0,
        use_osc2=True, osc2_waveform=Waveform.sine,
        osc2_volume=0.8, osc2_freq_transpose=1.5,
    )
    writer.write_wave("fifth.wav", synth2.generate_constant_wave(frequency=440.0, length=1.0))


if __name__ == '__main__':
    create_sum_sound()
