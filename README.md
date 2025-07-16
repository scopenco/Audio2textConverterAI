# Install 

## on MacOS using Homebrew (https://brew.sh/)
```bash
brew install ffmpeg
```

## Install delepndancies
```bash
pip install -r requirements.txt
```

# Use whisper tool
```bash
whisper --help
whisper ~/Downloads/test.mp3 --language en --model turbo
```

# Available models by performance
https://github.com/openai/whisper?tab=readme-ov-file#available-models-and-languages

# Tips
Downloaded models are stoked in cache ~/.cache/whisper/ so you don't need to download it again.
