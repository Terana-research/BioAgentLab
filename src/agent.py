from dataclasses import dataclass

from tools import ESMTool, ToolResult, UniProtTool


@dataclass
class Task:
    """Agent 对用户任务的结构化理解。"""

    raw_input: str
    task_type: str
    sequence: str


class ProteinAgent:
    """一个具有任务识别、工具路由和故障恢复能力的简单 Agent。"""

    def __init__(self, esm_available: bool = True) -> None:
        self.esm_tool = ESMTool(available=esm_available)
        self.uniprot_tool = UniProtTool()

    def understand_task(self, user_input: str, sequence: str) -> Task:
        """理解用户希望完成什么任务。"""

        normalized_input = user_input.lower()

        if "protein" in normalized_input or "蛋白" in user_input:
            task_type = "protein_function_prediction"
        else:
            task_type = "unknown"

        return Task(
            raw_input=user_input,
            task_type=task_type,
            sequence=sequence,
        )

    def plan(self, task: Task) -> list[str]:
        """根据任务类型生成执行计划。"""

        if task.task_type == "protein_function_prediction":
            return [
                "validate_sequence",
                "try_esm_prediction",
                "fallback_to_uniprot_if_needed",
                "generate_response",
            ]

        return ["reject_unsupported_task"]

    def validate_sequence(self, sequence: str) -> bool:
        """验证输入是否像蛋白质序列。"""

        valid_amino_acids = set("ACDEFGHIKLMNPQRSTVWY")
        normalized_sequence = sequence.strip().upper()

        return (
            len(normalized_sequence) > 0
            and set(normalized_sequence).issubset(valid_amino_acids)
        )

    def select_and_execute_tool(self, sequence: str) -> ToolResult:
        """优先调用 ESM；失败时自动使用 UniProt。"""

        if self.esm_tool.health_check():
            esm_result = self.esm_tool.run(sequence)

            if esm_result.success:
                return esm_result

        print("ESM unavailable or failed. Switching to UniProt.")

        return self.uniprot_tool.run(sequence)

    def generate_response(self, result: ToolResult) -> str:
        """把工具结果转化为用户能够理解的文本。"""

        if not result.success:
            return f"Task failed: {result.error}"

        return (
            f"Analysis completed.\n"
            f"Source: {result.source}\n"
            f"Result: {result.data}"
        )

    def run(self, user_input: str, sequence: str) -> str:
        """执行完整 Agent 流程。"""

        task = self.understand_task(user_input, sequence)
        plan = self.plan(task)

        print(f"Task type: {task.task_type}")
        print(f"Plan: {plan}")

        if task.task_type == "unknown":
            return "Unsupported task type."

        if not self.validate_sequence(task.sequence):
            return "Invalid protein sequence."

        result = self.select_and_execute_tool(task.sequence)

        return self.generate_response(result)