"""搜索连接器模块

这个模块提供了网络搜索功能，方便智能体获取实时信息。

使用示例:
    from search_connector import SearchConnector
    
    search = SearchConnector()
    results = search.search("今天的天气")
"""

import os
from typing import Optional, List, Dict, Any

try:
    from tavily import TavilyClient
except ImportError:
    TavilyClient = None


class SearchConnector:
    """搜索连接器类
    
    支持多种搜索提供商。
    
    Args:
        provider: 搜索提供商，"tavily" 或 "duckduckgo"
        api_key: API Key（Tavily 需要）
        
    使用示例:
        search = SearchConnector(provider="duckduckgo")
        results = search.search("Python 教程")
    """
    
    def __init__(
        self,
        provider: str = "duckduckgo",
        api_key: Optional[str] = None
    ):
        self.provider = provider.lower()
        self.api_key = api_key or os.getenv("TAVILY_API_KEY")
        
        if self.provider == "tavily":
            if TavilyClient is None:
                raise ImportError("请先安装 tavily-python: pip install tavily-python")
            if not self.api_key:
                raise ValueError("Tavily 需要 API Key")
            self.client = TavilyClient(api_key=self.api_key)
        elif self.provider == "duckduckgo":
            try:
                from duckduckgo_search import DDGS
                self.client = DDGS()
            except ImportError:
                print("建议安装 duckduckgo-search: pip install duckduckgo-search")
                self.client = None
        else:
            raise ValueError(f"不支持的搜索提供商: {provider}")
    
    def search(
        self,
        query: str,
        max_results: int = 5
    ) -> List[Dict[str, Any]]:
        """搜索
        
        Args:
            query: 搜索关键词
            max_results: 最大结果数
            
        Returns:
            搜索结果列表
        """
        if self.provider == "tavily":
            results = self.client.search(
                query=query,
                max_results=max_results
            )
            return results.get("results", [])
        
        elif self.provider == "duckduckgo" and self.client:
            results = list(self.client.text(query, max_results=max_results))
            return [
                {
                    "title": r.get("title", ""),
                    "url": r.get("href", ""),
                    "content": r.get("body", "")
                }
                for r in results
            ]
        
        return []
    
    def search_with_summary(
        self,
        query: str,
        max_results: int = 3
    ) -> str:
        """搜索并返回摘要
        
        Args:
            query: 搜索关键词
            max_results: 最大结果数
            
        Returns:
            搜索结果摘要
        """
        results = self.search(query, max_results)
        
        if not results:
            return "没有找到相关结果"
        
        summary = f"关于 '{query}' 的搜索结果:\n\n"
        
        for i, result in enumerate(results, 1):
            title = result.get("title", "无标题")
            url = result.get("url", "")
            content = result.get("content", "")[:200]
            
            summary += f"{i}. **{title}**\n"
            summary += f"   {content}...\n"
            summary += f"   来源: {url}\n\n"
        
        return summary


# 使用示例
if __name__ == "__main__":
    print("=== 搜索连接器示例 ===\n")
    
    print("使用 DuckDuckGo 搜索...")
    search = SearchConnector(provider="duckduckgo")
    results = search.search("Python 教程", max_results=3)
    
    print(f"找到 {len(results)} 个结果:\n")
    for i, r in enumerate(results, 1):
        print(f"{i}. {r.get('title', '无标题')}")
        print(f"   {r.get('url', '')}")
