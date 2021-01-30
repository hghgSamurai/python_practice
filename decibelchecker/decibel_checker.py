# -*- coding: utf-8 -*-

import sys
import wave
import pyaudio
import numpy as np
import scipy as fromstring
from scipy.io.wavfile import read

## 定数
SAMPLE_RATE = 44100
N = 2048 #1サンプルは(1/44100)[s]なので，約0.02秒の幅で音量を算出

np.set_printoptions(threshold=np.inf)

####################################################################
## db変換
####################################################################
def to_db(x, N):
    pad = np.zeros(N//2)
    pad_data = np.concatenate([pad, x, pad])
    with np.errstate(divide='ignore'):  #無音区間の0除算を回避する
        rms = np.array([np.sqrt((1/N) * (np.sum(pad_data[i:i+N]))**2) for i in range(len(x))])

    return 20 * np.log10(rms)

####################################################################
## 
####################################################################
#ファイルを取得
sound_file = "./data/" + sys.argv[1]
print("sound_file:", sound_file)
wr = wave.open(sound_file, 'rb')
amp  = (2**8) ** wr.getsampwidth() / 2      # 65536/2
data = wr.readframes(wr.getnframes())

bdata = np.frombuffer(data, dtype='int16')
sbdata = bdata / amp   #16bitの音声ファイルのデータを-1から1に正規化

##ファイルの情報
print("########### SoundFile Info ##############")
print("#Channel num : ", wr.getnchannels())
print("#Sample size : ", wr.getsampwidth())
print("#Sampling rate : ", wr.getframerate())
print("#Frame num : ", wr.getnframes())
print("#Params : ", wr.getparams())
print("#Sec : ", float(wr.getnframes()) / wr.getframerate())
print("#########################################")

##dbに変換する
db = to_db(bdata, N)

print("########### loudest ##############")
print("dbmax:", db.max())