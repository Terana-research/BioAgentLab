from dataclasses import dataclass
from typing import Any


@dataclass
class ToolResult:
    """统一表示工具的执行结果。"""

    success: bool
    data: Any = None
    error: str | None = None
    source: str | None = None


class ESMTool:
    """模拟 ESM 蛋白质模型工具。"""

    name = "esm"

    def __init__(self, available: bool = True) -> None:
        self.available = available

    def health_check(self) -> bool:
        """检查工具是否可用。"""
        return self.available

    def run(self, sequence: str) -> ToolResult:
        if not self.health_check():
            return ToolResult(
                success=False,
                error="ESM service is unavailable.",
                source=self.name,
            )

        # 这里暂时不调用真实 ESM，只模拟预测结果。
        prediction = {
            "sequence_length": len(sequence),
            "predicted_function": "Possible enzyme-related protein",
            "confidence": 0.72,
        }

        return ToolResult(
            success=True,
            data=prediction,
            source=self.name,
        )


class UniProtTool:
    """模拟 UniProt 数据库查询工具。"""

    name = "uniprot"

    def health_check(self) -> bool:
        return True

    def run(self, sequence: str) -> ToolResult:
        result = {
            "sequence_length": len(sequence),
            "matched_function": "Function inferred from similar proteins",
            "evidence_type": "database similarity search",
        }

        return ToolResult(
            success=True,
            data=result,
            source=self.name,
        )