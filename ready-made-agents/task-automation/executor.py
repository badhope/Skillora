"""任务执行器模块"""

from typing import Dict, Any


class TaskExecutor:
    """任务执行器"""
    
    def __init__(self, llm):
        self.llm = llm
        self.execution_log = []
    
    def execute_step(self, step: Dict[str, Any]) -> str:
        """执行单个步骤
        
        Args:
            step: 步骤信息
            
        Returns:
            执行结果
        """
        description = step.get("description", "")
        
        prompt = f"""执行以下任务步骤：

步骤: {description}

请详细执行这个步骤，并给出执行结果。"""
        
        try:
            result = self.llm.generate(prompt)
            
            # 记录执行日志
            self.execution_log.append({
                "step": description,
                "result": result,
                "status": "success"
            })
            
            return result
        
        except Exception as e:
            error_msg = f"执行失败: {e}"
            
            self.execution_log.append({
                "step": description,
                "result": error_msg,
                "status": "error"
            })
            
            return error_msg
    
    def get_log(self) -> list:
        """获取执行日志"""
        return self.execution_log
    
    def clear_log(self):
        """清空日志"""
        self.execution_log = []
    
    def execute_plan(self, steps: list) -> list:
        """执行整个计划
        
        Args:
            steps: 步骤列表
            
        Returns:
            执行结果列表
        """
        results = []
        
        for step in steps:
            result = self.execute_step(step)
            results.append({
                "step": step,
                "result": result
            })
        
        return results


if __name__ == "__main__":
    from building_blocks.tools.llm_wrappers.openai_wrapper import OpenAIWrapper
    
    llm = OpenAIWrapper()
    executor = TaskExecutor(llm)
    
    step = {
        "id": 1,
        "description": "搜索关于 AI 的最新资讯",
        "status": "pending"
    }
    
    result = executor.execute_step(step)
    print(f"执行结果: {result}")
