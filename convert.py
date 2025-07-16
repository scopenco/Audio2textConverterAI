#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This script uses the Whisper library to transcribe audio files.

import whisper
import os

F = '/Users/user/test..mp3'

model = whisper.load_model("turbo")
with open(F, "r") as f:
    result = model.transcribe(F)
    print(result["text"])

