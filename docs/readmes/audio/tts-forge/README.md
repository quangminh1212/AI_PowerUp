<!-- source: https://github.com/thechandanbhagat/tts-forge.git sha: 2f448e7d0d094498879da61e197843773e2c485f readme: main/README.md -->
# thechandanbhagat/tts-forge

End-to-end Text-to-Speech training pipeline that clones your voice. Record samples, train XTTS/VITS models, and generate natural speech in your own voice.

---

# Custom Voice TTS Training Pipeline

Complete pipeline for training a Text-to-Speech (TTS) model with your own voice using XTTS v2.

## About This Project

This is a comprehensive end-to-end solution for creating a custom Text-to-Speech system that speaks in your own voice. The project provides all the tools needed to record your voice, prepare training data, train a neural TTS model, and generate speech with your custom voice.

### What It Does

- **Voice Recording**: Interactive recording system with guided prompts to capture your voice samples
- **Dataset Preparation**: Automated audio processing pipeline that normalizes, cleans, and formats recordings
- **Model Training**: Fine-tune state-of-the-art XTTS v2 or train VITS models with your voice data
- **Speech Generation**: Generate natural-sounding speech in your voice from any text input
- **Zero-Shot Cloning**: Use XTTS for instant voice cloning without training (requires reference audio)

### Key Features

**Recording System**
- Interactive voice recording with automatic sample management
- Support for custom text prompts and sample texts files
- Built-in audio quality checks and playback preview
- Metadata tracking for all recordings

**Dataset Processing**
- Automatic audio normalization and resampling
- Silence trimming and noise reduction options
- Train/validation split generation (90/10)
- LJSpeech format compatibility
- Dataset validation and statistics

**Training Options**
- **VITS**: Traditional training approach, best with 20-30 minutes of audio
- **XTTS v2**: Fine-tuning pretrained model, works with less data (10-15 minutes)
- Optimized for 6GB VRAM (RTX A1000 tested)
- Mixed precision training for memory efficiency
- TensorBoard monitoring integration

**Inference Capabilities**
- Interactive mode for testing multiple texts
- Batch processing support
- Voice cloning with reference audio
- XTTS zero-shot cloning (no training required)
- Multiple output format options

### Technology Stack

- **TTS Engine**: Coqui TTS (XTTS v2, VITS)
- **Deep Learning**: PyTorch with CUDA acceleration
- **Audio Processing**: librosa, soundfile, sounddevice
- **Monitoring**: TensorBoard for training visualization
- **Languages**: Python 3.10/3.11
- **Platform**: Windows with NVIDIA GPU support

### Use Cases

- Personal voice assistants and chatbots
- Audiobook narration in your own voice
- Accessibility tools for voice preservation
- Content creation and video narration
- Custom voice for games or applications
- Voice preservation for medical conditions
- Educational content with personalized narration

### Project Status

This is a working implementation with successful training completed on:
- Hardware: NVIDIA RTX A1000 6GB Laptop GPU
- Dataset: 89 voice samples (~5 minutes total)
- Models: VITS trained (4000+ steps), XTTS zero-shot working
- Quality: Production-ready for both training approaches

## System Requirements

- **GPU**: NVIDIA RTX A1000 6GB (or any GPU with 4GB+ VRAM)
- **CUDA**: 12.8 (already installed)
- **Python**: 3.13.5 (already installed)
- **Storage**: ~10-20GB free space
- **OS**: Windows (current setup)

## Quick Start Guide

### Step 1: Environment Setup

Create a virtual environment and install dependencies:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install additional audio recording dependency
pip install sounddevice
```

### Step 2: Record Your Voice

Record 10-30 minutes of your voice reading diverse sentences:

```bash
# Interactive recording (recommended)
python scripts/record_voice.py --output_dir datasets/raw_audio --num_samples 100

# With sample texts provided
python scripts/record_voice.py --output_dir datasets/raw_audio --sample_texts scripts/sample_texts.txt
```

**Recording Tips:**
- Use a quiet room with minimal background noise
- Use a good quality microphone (USB condenser mic recommended)
- Maintain consistent distance from microphone (6-8 inches)
- Speak naturally at a normal pace
- Read clearly without filler words (um, uh, etc.)
- Take breaks every 20-30 samples to maintain consistency

**Target:**
- Minimum: 10 minutes (50-100 samples)
- Recommended: 20-30 minutes (150-200 samples)
- More data = better quality

### Step 3: Prepare Dataset

Process your recordings for training:

```bash
# Basic preparation
python scripts/prepare_dataset.py --input_dir datasets/raw_audio --output_dir datasets/processed

# With noise reduction (if recording has background noise)
python scripts/prepare_dataset.py --input_dir datasets/raw_audio --output_dir datasets/processed --noise_reduction
```

This will:
- Normalize audio levels
- Trim silence
- Resample to 22050 Hz
- Create train/validation split (90/10)
- Generate metadata files

### Step 4: Train the Model

Train XTTS v2 with your voice data:

```bash
# Start training (optimized for 6GB VRAM)
python scripts/train_xtts.py --dataset_path datasets/processed --output_path training_output --num_epochs 10

# Advanced options
python scripts/train_xtts.py \
  --dataset_path datasets/processed \
  --output_path training_output \
  --batch_size 2 \
  --grad_accum 8 \
  --num_epochs 10 \
  --language en
```

**Training Parameters (optimized for RTX A1000 6GB):**
- Batch size: 2 (fits in 6GB VRAM)
- Gradient accumulation: 8 (effective batch size = 16)
- Mixed precision: Enabled (saves VRAM)
- Expected training time: 2-6 hours (depends on dataset size)

**Monitor Training:**
```bash
# In a new terminal, start TensorBoard
tensorboard --logdir training_output
```
Then open http://localhost:6006 in your browser.

### Step 5: Generate Speech (Inference)

Test your trained model:

```bash
# Interactive mode (recommended for testing)
python scripts/inference.py \
  --model_path training_output/best_model.pth \
  --speaker_wav datasets/processed/wavs/audio_0001.wav \
  --interactive

# Single text synthesis
python scripts/inference.py \
  --model_path training_output/best_model.pth \
  --speaker_wav datasets/processed/wavs/audio_0001.wav \
  --text "Hello, this is my custom voice!" \
  --output_path my_voice_output.wav

# Compare with pretrained XTTS (for reference)
python scripts/inference.py \
  --use_pretrained \
  --speaker_wav datasets/processed/wavs/audio_0001.wav \
  --text "Hello, this is the pretrained voice." \
  --output_path pretrained_output.wav
```

## Project Structure

```
chandan-tts/
├── datasets/
│   ├── raw_audio/              # Your raw voice recordings
│   │   ├── sample_*.wav
│   │   └── metadata.txt
│   └── processed/              # Processed dataset ready for training
│       ├── wavs/
│       │   └── audio_*.wav
│       ├── metadata.txt
│       ├── metadata_train.txt
│       ├── metadata_val.txt
│       └── dataset_config.json
├── training_output/            # Training outputs
│   ├── best_model.pth         # Best model checkpoint
│   ├── config.json            # Model configuration
│   └── events.out.tfevents.*  # TensorBoard logs
├── models/                     # Pretrained models cache
├── outputs/                    # Generated audio outputs
├── scripts/
│   ├── record_voice.py        # Voice recording script
│   ├── prepare_dataset.py     # Dataset preparation
│   ├── train_xtts.py          # Training script
│   ├── inference.py           # Inference script
│   └── sample_texts.txt       # Sample texts for recording
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Detailed Workflow

### Phase 1: Data Collection

1. **Review sample texts** in `scripts/sample_texts.txt`
2. **Set up recording environment**:
   - Quiet room
   - Good microphone
   - Pop filter (recommended)
3. **Record in batches** of 20-30 samples with breaks
4. **Listen to recordings** to ensure quality
5. **Aim for 150-200 samples** (20-30 minutes total)

### Phase 2: Data Preparation

1. **Run preparation script** to process recordings
2. **Review statistics**:
   - Check total duration (should be 10+ minutes)
   - Verify train/validation split
3. **Listen to processed samples** to ensure quality maintained

### Phase 3: Training

1. **Start training** with default parameters
2. **Monitor progress**:
   - Check TensorBoard for loss curves
   - Listen to generated samples periodically
3. **Training completes** after specified epochs
4. **Best model** saved automatically based on validation loss

### Phase 4: Inference & Testing

1. **Test with short sentences** first
2. **Compare quality** with pretrained model
3. **Test various text types**:
   - Questions
   - Statements
   - Different emotions
   - Numbers and dates
4. **Fine-tune if needed** with more data or epochs

## Troubleshooting

### Out of Memory (OOM) Errors

If you encounter CUDA out of memory errors:

```bash
# Reduce batch size
python scripts/train_xtts.py --batch_size 1 --grad_accum 16

# Close other GPU applications
# Check GPU usage: nvidia-smi
```

### Poor Audio Quality

If generated audio quality is poor:

1. **Record more data** (aim for 30+ minutes)
2. **Improve recording quality**:
   - Use better microphone
   - Reduce background noise
   - Maintain consistent volume
3. **Enable noise reduction** during preparation
4. **Train for more epochs** (15-20 epochs)

### Training Too Slow

If training is very slow:

1. **Check GPU usage**: `nvidia-smi` (should show high utilization)
2. **Verify CUDA**: Ensure PyTorch is using GPU
3. **Reduce dataset size** for initial testing
4. **Use gradient accumulation** instead of larger batch size

### Model Not Loading

If pretrained model fails to download:

```bash
# Manually download XTTS v2
python -c "from TTS.api import TTS; TTS('tts_models/multilingual/multi-dataset/xtts_v2')"
```

## Advanced Usage

### Resume Training from Checkpoint

```bash
python scripts/train_xtts.py \
  --dataset_path datasets/processed \
  --output_path training_output \
  --restore_path training_output/checkpoint_5000.pth
```

### Batch Inference

Create a file `texts.txt` with one sentence per line, then:

```bash
# Process multiple texts
while IFS= read -r text; do
  python scripts/inference.py \
    --model_path training_output/best_model.pth \
    --speaker_wav datasets/processed/wavs/audio_0001.wav \
    --text "$text" \
    --output_path "outputs/$(echo $text | md5sum | cut -d' ' -f1).wav"
done < texts.txt
```

### Multi-Language Support

XTTS supports multiple languages. To train on another language:

```bash
# Example for Spanish
python scripts/train_xtts.py \
  --dataset_path datasets/processed \
  --language es
```

Supported languages: en, es, fr, de, it, pt, pl, tr, ru, nl, cs, ar, zh-cn, ja, ko

## Performance Benchmarks

**RTX A1000 6GB:**
- Training speed: ~5-10 seconds/iteration (batch_size=2)
- Inference speed: ~3-5 seconds for 10-second audio
- VRAM usage: ~4.5-5.5GB during training

## Tips for Best Results

1. **Quality over quantity**: 15 minutes of clean audio > 30 minutes of noisy audio
2. **Consistency matters**: Keep same environment, mic position, and speaking style
3. **Diverse content**: Include various phonemes, emotions, and sentence structures
4. **Monitor training**: Check TensorBoard regularly for loss convergence
5. **Test early**: Generate samples after 2-3 epochs to verify progress
6. **Patience**: Good results typically need 8-12 epochs

## Next Steps

After successful training:

1. **Integrate into applications**: Use the inference script in your projects
2. **Fine-tune further**: Add more data and retrain
3. **Experiment**: Try different speaking styles or emotions
4. **Share**: Export and share your custom voice model

## Resources

- **Coqui TTS Documentation**: https://docs.coqui.ai/
- **XTTS Paper**: https://arxiv.org/abs/2311.00430
- **TTS Training Guide**: https://github.com/coqui-ai/TTS
- **Community Forum**: https://github.com/coqui-ai/TTS/discussions

## Code Navigation

![Code Organization](assets/groupcode.png)

This project uses GroupCode ([VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=thechandanbhagat.groupcode) | [Open VSX](https://open-vsx.org/extension/thechandanbhagat/groupcode)) for organized code navigation by functionality. Use `@groupcode` in VS Code Copilot Chat to explore the codebase by functional areas (Dataset Creation, Model Training, Inference, Testing).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Note: This project uses Coqui TTS, which is licensed under MPL 2.0. When using this project, you must comply with both licenses.

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review TensorBoard logs
3. Check Coqui TTS GitHub issues
4. Consult the official documentation

---

**Happy Voice Cloning!**
