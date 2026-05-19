from transformers import pipeline
from typing import List, Dict, Any, Optional

class Summarizer:
    def __init__(
        self,
        model: str = "sshleifer/distilbart-cnn-12-6",
        max_length: int = 150,
        min_length: int = 30
    ):
        self.summarizer = pipeline("summarization", model=model)
        self.max_length = max_length
        self.min_length = min_length

    def summarize(
        self,
        text: str,
        max_length: Optional[int] = None,
        min_length: Optional[int] = None,
        **kwargs
    ) -> str:
        params = {
            "max_length": max_length or self.max_length,
            "min_length": min_length or self.min_length,
            **kwargs
        }
        result = self.summarizer(text, **params)[0]
        return result["summary_text"]

    def summarize_batch(
        self,
        texts: List[str],
        max_length: Optional[int] = None,
        min_length: Optional[int] = None,
        **kwargs
    ) -> List[str]:
        params = {
            "max_length": max_length or self.max_length,
            "min_length": min_length or self.min_length,
            **kwargs
        }
        results = self.summarizer(texts, **params)
        return [result["summary_text"] for result in results]

    def extract_key_points(self, text: str, num_points: int = 5) -> List[str]:
        summary = self.summarize(text, max_length=200)
        sentences = summary.split(". ")
        return sentences[:num_points]