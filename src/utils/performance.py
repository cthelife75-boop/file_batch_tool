# -*- coding: utf-8 -*-
"""性能监控模块"""

import time
from functools import wraps
from typing import Callable, Any


class PerformanceMonitor:
    """性能监控器"""

    def __init__(self):
        self.metrics = {}

    def record(self, operation: str, duration: float, files_processed: int = 0):
        """记录操作性能指标

        Args:
            operation: 操作名称
            duration: 耗时（秒）
            files_processed: 处理的文件数
        """
        if operation not in self.metrics:
            self.metrics[operation] = {
                'count': 0,
                'total_duration': 0,
                'total_files': 0,
                'avg_duration': 0,
                'avg_files_per_sec': 0
            }

        m = self.metrics[operation]
        m['count'] += 1
        m['total_duration'] += duration
        m['total_files'] += files_processed

        if m['count'] > 0:
            m['avg_duration'] = m['total_duration'] / m['count']

        if duration > 0:
            m['avg_files_per_sec'] = files_processed / duration

    def get_report(self) -> str:
        """获取性能报告

        Returns:
            格式化的性能报告
        """
        lines = ["=" * 60, "性能监控报告", "=" * 60]

        for op, m in self.metrics.items():
            lines.append(f"\n操作: {op}")
            lines.append(f"  执行次数: {m['count']}")
            lines.append(f"  总耗时: {m['total_duration']:.2f}秒")
            lines.append(f"  平均耗时: {m['avg_duration']:.2f}秒")
            lines.append(f"  处理文件数: {m['total_files']}")
            lines.append(f"  平均速度: {m['avg_files_per_sec']:.2f} 文件/秒")

        lines.append("\n" + "=" * 60)
        return "\n".join(lines)

    def reset(self):
        """重置所有指标"""
        self.metrics.clear()


def measure_time(operation_name: str = None):
    """测量函数执行时间的装饰器

    Args:
        operation_name: 操作名称（默认为函数名）

    Returns:
        装饰器函数
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            name = operation_name or func.__name__
            start_time = time.time()

            result = func(*args, **kwargs)

            duration = time.time() - start_time
            print(f"⏱️  {name} 完成，耗时: {duration:.2f}秒")

            return result

        return wrapper
    return decorator
