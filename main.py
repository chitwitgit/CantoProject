def main():
    import soundfile as sf
    import torch
    from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

    # load pretrained model
    processor = Wav2Vec2Processor.from_pretrained("scottykwok/wav2vec2-large-xlsr-cantonese")
    model = Wav2Vec2ForCTC.from_pretrained("scottykwok/wav2vec2-large-xlsr-cantonese")

    # load audio
    audio_input, sample_rate = sf.read('audio_cantonese.wav')

    # pad input values and return pt tensor
    input_values = processor(audio_input, sampling_rate=sample_rate, return_tensors="pt").input_values

    # INFERENCE
    # retrieve logits & take argmax
    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)

    # transcribe
    transcription = processor.decode(predicted_ids[0])
    print("-" * 20)
    print("Transcription:\n", transcription.lower())
    print("-" * 20)
if __name__ == '__main__':
    main()
