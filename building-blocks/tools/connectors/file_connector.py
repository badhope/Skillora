"""文件连接器模块

这个模块提供了文件读写功能，方便智能体处理本地文件。

使用示例:
    from file_connector import FileConnector
    
    file_conn = FileConnector()
    content = file_conn.read_file("document.txt")
    file_conn.write_file("output.txt", "Hello World")
"""

import os
from typing import List, Optional, Dict
from pathlib import Path


class FileConnector:
    """文件连接器类
    
    提供文件读写和管理功能。
    
    Args:
        base_path: 基础路径，默认为当前目录
        
    使用示例:
        file_conn = FileConnector(base_path="./data")
        content = file_conn.read_file("document.txt")
    """
    
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)
    
    def read_file(self, file_path: str) -> str:
        """读取文件
        
        Args:
            file_path: 文件路径
            
        Returns:
            文件内容
        """
        full_path = self.base_path / file_path
        
        if not full_path.exists():
            raise FileNotFoundError(f"文件不存在: {file_path}")
        
        with open(full_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def write_file(self, file_path: str, content: str) -> None:
        """写入文件
        
        Args:
            file_path: 文件路径
            content: 文件内容
        """
        full_path = self.base_path / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def append_file(self, file_path: str, content: str) -> None:
        """追加文件内容
        
        Args:
            file_path: 文件路径
            content: 追加内容
        """
        full_path = self.base_path / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(full_path, 'a', encoding='utf-8') as f:
            f.write(content)
    
    def list_files(
        self,
        pattern: str = "*",
        recursive: bool = False
    ) -> List[str]:
        """列出文件
        
        Args:
            pattern: 文件模式，如 "*.txt"
            recursive: 是否递归搜索
            
        Returns:
            文件列表
        """
        if recursive:
            files = list(self.base_path.rglob(pattern))
        else:
            files = list(self.base_path.glob(pattern))
        
        return [str(f.relative_to(self.base_path)) for f in files if f.is_file()]
    
    def read_directory(
        self,
        directory: str = ".",
        extensions: Optional[List[str]] = None
    ) -> Dict[str, str]:
        """读取目录下所有文件
        
        Args:
            directory: 目录路径
            extensions: 文件扩展名过滤，如 [".txt", ".md"]
            
        Returns:
            文件名到内容的字典
        """
        dir_path = self.base_path / directory
        
        if not dir_path.exists():
            raise FileNotFoundError(f"目录不存在: {directory}")
        
        files = {}
        
        for file_path in dir_path.rglob("*"):
            if file_path.is_file():
                # 检查扩展名
                if extensions and file_path.suffix not in extensions:
                    continue
                
                rel_path = str(file_path.relative_to(dir_path))
                try:
                    content = file_path.read_text(encoding='utf-8')
                    files[rel_path] = content
                except Exception as e:
                    files[rel_path] = f"[读取错误: {e}]"
        
        return files
    
    def delete_file(self, file_path: str) -> None:
        """删除文件
        
        Args:
            file_path: 文件路径
        """
        full_path = self.base_path / file_path
        
        if full_path.exists():
            full_path.unlink()
    
    def get_file_info(self, file_path: str) -> Dict[str, any]:
        """获取文件信息
        
        Args:
            file_path: 文件路径
            
        Returns:
            文件信息字典
        """
        full_path = self.base_path / file_path
        
        if not full_path.exists():
            raise FileNotFoundError(f"文件不存在: {file_path}")
        
        stat = full_path.stat()
        
        return {
            "name": full_path.name,
            "path": str(full_path),
            "size": stat.st_size,
            "modified": stat.st_mtime,
            "is_file": full_path.is_file(),
            "is_dir": full_path.is_dir()
        }


# 使用示例
if __name__ == "__main__":
    print("=== 文件连接器示例 ===\n")
    
    file_conn = FileConnector(base_path="./test_files")
    
    # 写入文件
    print("写入文件...")
    file_conn.write_file("hello.txt", "Hello, World!")
    
    # 读取文件
    print("读取文件...")
    content = file_conn.read_file("hello.txt")
    print(f"内容: {content}")
    
    # 列出文件
    print("\n列出所有 .txt 文件...")
    files = file_conn.list_files("*.txt")
    print(f"文件: {files}")
    
    # 获取文件信息
    print("\n获取文件信息...")
    info = file_conn.get_file_info("hello.txt")
    print(f"信息: {info}")
