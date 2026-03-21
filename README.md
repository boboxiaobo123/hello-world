# Python 工具集

本项目包含多个实用的 Python 小工具。

## 文件说明

| 文件 | 功能 | 运行方式 |
|------|------|----------|
| `calculator.py` | 图形界面计算器 | `python3 calculator.py` |
| `gui_timer.py` | 商务风格计时器 | `python3 gui_timer.py` |
| `timer.py` | 终端命令行计时器 | `python3 timer.py` |

## 工具详情

### 计算器 (calculator.py)

基于 tkinter 的图形界面计算器，支持四则运算。

**操作说明：**
- 数字键：输入数字
- `+` `-` `*` `/`：选择运算符
- `=` 或 Enter：计算结果
- `c` 或 Backspace：清除
- `q` 或 ESC：退出

### 商务计时器 (gui_timer.py)

专业风格的图形界面秒表，适合商务场景。

**功能：**
- 开始/暂停/重置计时
- 状态指示灯（绿色=运行中，红色=暂停，灰色=就绪）
- 等宽字体显示，计时过程不跳动
- 深蓝配色商务风格

### 终端计时器 (timer.py)

命令行交互式秒表。

**操作说明：**
- 输入 `1`：开始/继续计时
- 输入 `2`：暂停计时
- 输入 `3`：重置计时器
- 输入 `4`：退出程序

## 系统要求

- Python 3.x
- 无需安装第三方依赖包

## 快速开始

```bash
# 运行计算器
python3 calculator.py

# 运行商务计时器
python3 gui_timer.py

# 运行终端计时器
python3 timer.py
```
