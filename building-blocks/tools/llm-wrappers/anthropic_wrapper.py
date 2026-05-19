from anthropic import Anthropic, AsyncAnthropic
from typing import List, Dict, Any, Optional, AsyncGenerator, Generator

class AnthropicWrapper:
    def __init__(self, api_key: str, model: str = "claude-3-sonnet-20240229"):
        self.client = Anthropic(api_key=api_key)
        self.async_client = AsyncAnthropic(api_key=api_key)
        self.model = model

    def chat_completion(
        self,
        messages: List[Dict[str, str]],
        max_tokens: int = 1024,
        temperature: float = 0.7,
        **kwargs
    ) -> str:
        response = self.client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=messages,
            **kwargs
        )
        return response.content[0].text

    def streaming_chat_completion(
        self,
        messages: List[Dict[str, str]],
        max_tokens: int = 1024,
        temperature: float = 0.7,
        **kwargs
    ) -> Generator[str, None, None]:
        with self.client.messages.stream(
            model=self.model,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=messages,
            **kwargs
        ) as stream:
            for chunk in stream.text_stream:
                yield chunk

    async def async_chat_completion(
        self,
        messages: List[Dict[str, str]],
        max_tokens: int = 1024,
        temperature: float = 0.7,
        **kwargs
    ) -> str:
        response = await self.async_client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=messages,
            **kwargs
        )
        return response.content[0].text

    async def async_streaming_chat_completion(
        self,
        messages: List[Dict[str, str]],
        max_tokens: int = 1024,
        temperature: float = 0.7,
        **kwargs
    ) -> AsyncGenerator[str, None]:
        async with self.async_client.messages.stream(
            model=self.model,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=messages,
            **kwargs
        ) as stream:
            async for chunk in stream.text_stream:
                yield chunk

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

    def get_model_info(self) -> Dict[str, Any]:
        return {
            "provider": "Anthropic",
            "model": self.model,
            "max_tokens": 4096
        }