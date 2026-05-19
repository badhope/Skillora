import litellm
from typing import List, Dict, Any, Optional, Generator

class LiteLLMWrapper:
    def __init__(self, api_key: str = None, model: str = "gpt-3.5-turbo"):
        if api_key:
            litellm.api_key = api_key
        self.model = model

    def chat_completion(
        self,
        messages: List[Dict[str, str]],
        max_tokens: int = 1024,
        temperature: float = 0.7,
        **kwargs
    ) -> str:
        response = litellm.completion(
            model=self.model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
            **kwargs
        )
        return response.choices[0].message.content

    def streaming_chat_completion(
        self,
        messages: List[Dict[str, str]],
        max_tokens: int = 1024,
        temperature: float = 0.7,
        **kwargs
    ) -> Generator[str, None, None]:
        response = litellm.completion(
            model=self.model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
            stream=True,
            **kwargs
        )
        for chunk in response:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

    def generate_text(
        self,
        prompt: str,
        max_tokens: int = 1024,
        temperature: float = 0.7,
        system_prompt: Optional[str] = None,
        **kwargs
    ) -> str:
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        return self.chat_completion(messages, max_tokens, temperature, **kwargs)

    def embedding(
        self,
        text: str,
        model: str = "text-embedding-ada-002",
        **kwargs
    ) -> List[float]:
        response = litellm.embedding(
            model=model,
            input=text,
            **kwargs
        )
        return response.data[0].embedding

    def get_model_info(self) -> Dict[str, Any]:
        return {
            "provider": "LiteLLM (Multi-Provider)",
            "model": self.model,
            "supported_providers": [
                "openai", "anthropic", "azure", "google",
                "aws", "replicate", "huggingface", "cohere"
            ]
        }