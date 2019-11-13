#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import jieba
import os
import pickle
from . import AUDIO_DATA


# store the response audio data. 
def audio_storage(key, audio_data):
    pass


# cut the word by jieba package
def word_cut(origin_words):
    return ','.join(jieba.lcut(origin_words, cut_all=True, HMM=True))