# -*- coding: utf-8 -*-

import sys
import wave
import librosa
import numpy as np

####################################################################
## 定数
####################################################################
SAMPLE_RATE = 44100
THRESHOLD = 1.0

####################################################################
## 音割れチェック
####################################################################
print("########### START ##############")

# 音声ファイルを取得
sound_file = "./data/" + sys.argv[1]
print("sound_file:", sound_file)
wav, sr = librosa.load(sound_file, sr=SAMPLE_RATE, mono=False)  #wav:波形データ sr:サンプリング周波数

# 配列の絶対値を取得
n_arr = np.abs(wav)

# 音割れを判定
print("frombuffer:", wav)
print("fbmax:", wav.max())
print("fbmin:", wav.min())
print("fbmax_s:", n_arr.max())
peak = round(n_arr.max(),1)
print("peak:", peak)

if peak >= THRESHOLD:
    print("音声データの音割れが発生しています。やり直してください。")
else:
    print("音声データを受付けました。")

print("########### END ##############")