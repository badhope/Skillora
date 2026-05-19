"""网页连接器模块

这个模块提供了网页抓取功能，方便智能体获取网页内容。

使用示例:
    from web_connector import WebConnector
    
    web = WebConnector()
    content = web.fetch("https://example.com")
"""

from typing import Optional, Dict, List
from urllib.parse import urlparse
import re

try:
    import requests
except ImportError:
    print("需要安装 requests: pip install requests")
    requests = None


class WebConnector:
    """网页连接器类
    
    提供网页抓取和解析功能。
    
    Args:
        timeout: 请求超时时间（秒）
        headers: 请求头
        
    使用示例:
        web = WebConnector()
        content = web.fetch("https://example.com")
    """
    
    def __init__(
        self,
        timeout: int = 30,
        headers: Optional[Dict] = None
    ):
        if requests is None:
            raise ImportError("请先安装 requests: pip install requests")
        
        self.timeout = timeout
        self.headers = headers or {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
    
    def fetch(self, url: str) -> str:
        """获取网页内容
        
        Args:
            url: 网页 URL
            
        Returns:
            网页文本内容
        """
        try:
            response = requests.get(
                url,
                headers=self.headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            
            # 自动检测编码
            response.encoding = response.apparent_encoding
            
            return response.text
        
        except Exception as e:
            return f"获取失败: {e}"
    
    def fetch_and_clean(self, url: str) -> str:
        """获取并清理网页内容
        
        Args:
            url: 网页 URL
            
        Returns:
            清理后的文本内容
        """
        content = self.fetch(url)
        
        if content.startswith("获取失败"):
            return content
        
        # 移除脚本和样式
        content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL)
        content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)
        
        # 移除 HTML 标签
        content = re.sub(r'<[^>]+>', ' ', content)
        
        # 清理空白字符
        content = re.sub(r'\s+', ' ', content)
        
        return content.strip()
    
    def extract_links(self, url: str) -> List[str]:
        """提取网页中的链接
        
        Args:
            url: 网页 URL
            
        Returns:
            链接列表
        """
        content = self.fetch(url)
        
        if content.startswith("获取失败"):
            return []
        
        # 提取 href 属性
        href_pattern = r'href=["\']([^"\']+)["\']'
        links = re.findall(href_pattern, content)
        
        # 清理并过滤
        clean_links = []
        base_domain = urlparse(url).netloc
        
        for link in links:
            # 跳过空链接和锚点
            if not link or link.startswith('#'):
                continue
            
            # 处理相对链接
            if link.startswith('/'):
                parsed = urlparse(url)
                link = f"{parsed.scheme}://{parsed.netloc}{link}"
            
            # 过滤外部链接
            if urlparse(link).netloc == base_domain or link.startswith('/'):
                clean_links.append(link)
        
        return list(set(clean_links))[:20]  # 最多返回 20 个
    
    def get_metadata(self, url: str) -> Dict[str, str]:
        """获取网页元数据
        
        Args:
            url: 网页 URL
            
        Returns:
            元数据字典（title, description, keywords 等）
        """
        content = self.fetch(url)
        
        if content.startswith("获取失败"):
            return {}
        
        metadata = {}
        
        # 提取 title
        title_match = re.search(r'<title>([^<]+)</title>', content, re.IGNORECASE)
        if title_match:
            metadata['title'] = title_match.group(1).strip()
        
        # 提取 meta description
        desc_match = re.search(
            r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']+)["\']',
            content,
            re.IGNORECASE
        )
        if not desc_match:
            desc_match = re.search(
                r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+name=["\']description["\']',
                content,
                re.IGNORECASE
            )
        if desc_match:
            metadata['description'] = desc_match.group(1).strip()
        
        return metadata
    
    def is_valid_url(self, url: str) -> bool:
        """验证 URL 是否有效
        
        Args:
            url: URL 字符串
            
        Returns:
            是否有效
        """
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except:
            return False


# 使用示例
if __name__ == "__main__":
    print("=== 网页连接器示例 ===\n")
    
    web = WebConnector()
    
    # 测试 URL
    test_url = "https://example.com"
    
    print(f"获取 {test_url} ...")
    content = web.fetch(test_url)
    print(f"原始内容长度: {len(content)} 字符\n")
    
    # 获取元数据
    print("获取元数据...")
    metadata = web.get_metadata(test_url)
    for key, value in metadata.items():
        print(f"  {key}: {value}")
    
    # 清理内容
    print("\n清理后的内容（前 200 字符）:")
    clean_content = web.fetch_and_clean(test_url)
    print(f"{clean_content[:200]}...")
