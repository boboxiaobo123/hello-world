# AGENTS.md - Python GUI 工具集开发规范

## 项目概述
Python 3 GUI 工具集，使用 tkinter 开发图形界面应用（计算器、计时器等）。

## 构建/运行命令

```bash
# 运行计算器
python3 calculator.py

# 运行商务计时器
python3 gui_timer.py

# 运行终端计时器
python3 timer.py

# 语法检查（Python 内置）
python3 -m py_compile calculator.py
python3 -m py_compile gui_timer.py
python3 -m py_compile timer.py
```

## 代码风格规范

### 缩进与格式
- **缩进**: 2 空格（gui_timer.py 标准）
- **行宽**: 建议不超过 100 字符
- **空行**: 类之间 2 空行，方法之间 1 空行

### 命名规范
- **类名**: PascalCase（如 `BusinessTimerApp`）
- **方法/函数**: snake_case（如 `create_main_card`）
- **变量**: snake_case（如 `start_time`）
- **常量**: UPPER_CASE（如 `COLORS`）
- **私有成员**: 下划线前缀（如 `_private_method`）

### 类型注解
- 使用 Python 3.10+ 类型注解
- 可选类型使用 `| None` 语法（如 `start_time: float | None = None`）

### 导入规范
```python
# 标准库分组导入
import tkinter as tk
from tkinter import font as tkfont
import time
```

### 文档字符串
- 使用三引号中文文档字符串
- 描述类的用途和方法的参数
```python
def draw_status_dot(self, state):
  """绘制状态指示圆点
  
  参数:
    state: 'idle' | 'running' | 'paused'
  """
```

### 错误处理
- 使用 try-except 捕获特定异常
- 用户界面友好地显示错误（如显示"错误"而非抛出异常）

### UI 规范（tkinter）
- 使用配色字典统一管理颜色
- 字体使用等宽字体显示时间（如 'Courier New'）
- 控件使用网格/放置布局，避免复杂 pack
- 添加悬停效果提升用户体验
- 窗口大小固定（resizable(False, False)）

### 代码组织
- 每个文件一个主类
- 使用 `if __name__ == "__main__":` 作为入口
- 界面元素创建按功能拆分为独立方法

## 注释规范
- 所有注释和文档字符串使用中文
- 关键逻辑添加简要注释
- UI 代码注释说明配色和功能
