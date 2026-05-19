"""任务规划器模块"""

from typing import Dict, List, Any
import json


class TaskPlanner:
    """任务规划器"""
    
    def __init__(self, llm):
        self.llm = llm
    
    def create_plan(self, task: str) -> Dict[str, Any]:
        """创建任务计划
        
        Args:
            task: 任务描述
            
        Returns:
            计划字典
        """
        prompt = f"""将以下任务分解成具体的执行步骤。

任务: {task}

请按顺序列出每个步骤，每个步骤应该：
1. 有明确的描述
2. 可以独立执行
3. 有明确的输出

请用 JSON 格式返回：
{{
    "task": "任务名称",
    "steps": [
        {{"id": 1, "description": "步骤描述", "status": "pending"}}
    ],
    "estimated_time": "估计时间"
}}"""
        
        try:
            result = self.llm.generate(prompt)
            
            # 尝试解析 JSON
            try:
                plan = json.loads(result)
                return plan
            except:
                # 如果解析失败，手动解析
                return self._parse_plan_manually(result, task)
        
        except Exception as e:
            return {
                "task": task,
                "steps": [{"id": 1, "description": task, "status": "pending"}],
                "estimated_time": "未知"
            }
    
    def _parse_plan_manually(self, text: str, task: str) -> Dict[str, Any]:
        """手动解析计划"""
        lines = text.strip().split("\n")
        steps = []
        
        for i, line in enumerate(lines, 1):
            line = line.strip()
            if line and (line[0].isdigit() or "-" in line):
                # 清理行
                line = line.lstrip("0123456789.-) ")
                if line:
                    steps.append({
                        "id": len(steps) + 1,
                        "description": line,
                        "status": "pending"
                    })
        
        if not steps:
            steps = [{"id": 1, "description": task, "status": "pending"}]
        
        return {
            "task": task,
            "steps": steps,
            "estimated_time": f"{len(steps) * 5} 分钟"
        }
    
    def refine_plan(self, plan: Dict[str, Any], feedback: str) -> Dict[str, Any]:
        """根据反馈优化计划
        
        Args:
            plan: 当前计划
            feedback: 用户反馈
            
        Returns:
            优化后的计划
        """
        prompt = f"""根据以下反馈优化任务计划。

当前计划:
{json.dumps(plan, ensure_ascii=False, indent=2)}

反馈: {feedback}

请优化计划，返回优化后的 JSON。
只返回 JSON，不要其他内容。"""
        
        try:
            result = self.llm.generate(prompt)
            return json.loads(result)
        except:
            return plan


if __name__ == "__main__":
    from building_blocks.tools.llm_wrappers.openai_wrapper import OpenAIWrapper
    
    llm = OpenAIWrapper()
    planner = TaskPlanner(llm)
    
    plan = planner.create_plan("帮我写一篇关于 AI 的文章")
    print(json.dumps(plan, ensure_ascii=False, indent=2))
