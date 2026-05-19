from transformers import pipeline
from typing import List, Dict, Any

class SentimentAnalyzer:
    def __init__(self, model: str = "distilbert-base-uncased-finetuned-sst-2-english"):
        self.classifier = pipeline("sentiment-analysis", model=model)

    def analyze(self, text: str) -> Dict[str, Any]:
        result = self.classifier(text)[0]
        return {
            "label": result["label"],
            "score": result["score"],
            "text": text
        }

    def analyze_batch(self, texts: List[str]) -> List[Dict[str, Any]]:
        results = self.classifier(texts)
        return [
            {
                "label": result["label"],
                "score": result["score"],
                "text": texts[i]
            }
            for i, result in enumerate(results)
        ]

    def get_sentiment_score(self, text: str) -> float:
        result = self.classifier(text)[0]
        if result["label"] == "POSITIVE":
            return result["score"]
        else:
            return -result["score"]