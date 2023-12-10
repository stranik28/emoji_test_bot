from transformers import HubertForSequenceClassification, Wav2Vec2FeatureExtractor
import torchaudio
import torch

feature_extractor = Wav2Vec2FeatureExtractor.from_pretrained("facebook/hubert-large-ls960-ft")
model = HubertForSequenceClassification.from_pretrained("xbgoose/hubert-speech-emotion-recognition-russian-dusha"
                                                        "-finetuned")
num2emotion = {0: 'Нейтральный', 1: 'Злой', 2: 'Позитивный', 3: 'Грустный', 4: 'Другое'}


async def predict(filepath: str):
        waveform, sample_rate = torchaudio.load(filepath, normalize=True)
        transform = torchaudio.transforms.Resample(sample_rate, 16000)
        waveform = transform(waveform)

        inputs = feature_extractor(
                waveform,
                sampling_rate=feature_extractor.sampling_rate,
                return_tensors="pt",
                padding=True,
                max_length=16000 * 10,
                truncation=True
            )

        logits = model(inputs['input_values'][0]).logits
        predictions = torch.argmax(logits, dim=-1)
        predicted_emotion = num2emotion[predictions.numpy()[0]]
        return predicted_emotion


