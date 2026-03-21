import tkinter as tk
from tkinter import font as tkfont
import time


class BusinessTimerApp:
  """商务风格秒表计时器
  
  专业的计时工具，适用于商务场景
  采用深蓝/灰色配色方案，扁平化设计
  """
  
  # 配色方案 - 商务风格
  COLORS = {
    'bg_primary': '#1e3a5f',      # 深蓝背景
    'bg_secondary': '#2c4a6e',    # 次级背景
    'bg_card': '#ffffff',          # 卡片背景（白色）
    'text_primary': '#1e3a5f',    # 主文字颜色
    'text_secondary': '#5a6c7d',  # 次级文字颜色
    'accent': '#3498db',          # 强调色（亮蓝）
    'accent_hover': '#2980b9',    # 强调色悬停
    'success': '#27ae60',         # 成功色（绿色）
    'warning': '#e74c3c',         # 警告色（红色）
    'border': '#d5d8dc',          # 边框色
    'shadow': '#000000',          # 阴影色
  }
  
  def __init__(self, root):
    """初始化商务计时器应用"""
    self.root = root
    self.root.title("专业计时器")
    self.root.geometry("500x350")
    self.root.configure(bg=self.COLORS['bg_primary'])
    self.root.resizable(False, False)
    
    # 计时器状态变量
    self.start_time = None
    self.elapsed = 0.0
    self.running = False
    self.update_id = None
    
    # 创建字体
    self.font_time = tkfont.Font(family='Segoe UI', size=56, weight='bold')
    self.font_label = tkfont.Font(family='Segoe UI', size=11)
    self.font_button = tkfont.Font(family='Segoe UI', size=12, weight='bold')
    self.font_status = tkfont.Font(family='Segoe UI', size=10)
    
    # 创建主容器（卡片效果）
    self.create_main_card()
    
    # 创建界面元素
    self.create_header()
    self.create_time_display()
    self.create_status_indicator()
    self.create_control_buttons()
    
  def create_main_card(self):
    """创建主卡片容器"""
    self.card = tk.Frame(
      self.root,
      bg=self.COLORS['bg_card'],
      highlightbackground=self.COLORS['border'],
      highlightthickness=1
    )
    self.card.place(relx=0.5, rely=0.5, anchor='center', width=460, height=310)
    
  def create_header(self):
    """创建标题栏"""
    header = tk.Frame(self.card, bg=self.COLORS['bg_card'])
    header.pack(fill='x', padx=20, pady=(20, 0))
    
    title = tk.Label(
      header,
      text="PROFESSIONAL TIMER",
      font=('Segoe UI', 9, 'bold'),
      fg=self.COLORS['text_secondary'],
      bg=self.COLORS['bg_card']
    )
    title.pack(anchor='w')
    
    subtitle = tk.Label(
      header,
      text="专业计时器",
      font=('Segoe UI', 14, 'bold'),
      fg=self.COLORS['text_primary'],
      bg=self.COLORS['bg_card']
    )
    subtitle.pack(anchor='w')
    
    # 分隔线
    separator = tk.Frame(self.card, height=2, bg=self.COLORS['border'])
    separator.pack(fill='x', padx=20, pady=(10, 0))
    
  def create_time_display(self):
    """创建时间显示区域"""
    time_frame = tk.Frame(self.card, bg=self.COLORS['bg_card'])
    time_frame.pack(pady=30)
    
    self.time_label = tk.Label(
      time_frame,
      text="00:00.00",
      font=self.font_time,
      fg=self.COLORS['text_primary'],
      bg=self.COLORS['bg_card']
    )
    self.time_label.pack()
    
    # 时间单位标签
    unit_frame = tk.Frame(self.card, bg=self.COLORS['bg_card'])
    unit_frame.pack()
    
    units = tk.Label(
      unit_frame,
      text="分 : 秒 . 毫秒",
      font=self.font_label,
      fg=self.COLORS['text_secondary'],
      bg=self.COLORS['bg_card']
    )
    units.pack()
    
  def create_status_indicator(self):
    """创建状态指示器"""
    status_frame = tk.Frame(self.card, bg=self.COLORS['bg_card'])
    status_frame.pack(pady=(0, 20))
    
    # 状态圆点
    self.status_dot = tk.Canvas(
      status_frame,
      width=12,
      height=12,
      bg=self.COLORS['bg_card'],
      highlightthickness=0
    )
    self.status_dot.pack(side='left', padx=(0, 8))
    self.draw_status_dot('idle')
    
    # 状态文字
    self.status_text = tk.Label(
      status_frame,
      text="准备就绪",
      font=self.font_status,
      fg=self.COLORS['text_secondary'],
      bg=self.COLORS['bg_card']
    )
    self.status_text.pack(side='left')
    
  def draw_status_dot(self, state):
    """绘制状态指示圆点
    
    参数:
      state: 'idle' | 'running' | 'paused'
    """
    colors = {
      'idle': self.COLORS['text_secondary'],
      'running': self.COLORS['success'],
      'paused': self.COLORS['warning']
    }
    
    self.status_dot.delete('all')
    self.status_dot.create_oval(
      2, 2, 10, 10,
      fill=colors.get(state, self.COLORS['text_secondary']),
      outline=''
    )
    
  def create_control_buttons(self):
    """创建控制按钮"""
    btn_frame = tk.Frame(self.card, bg=self.COLORS['bg_card'])
    btn_frame.pack(pady=(0, 20))
    
    # 开始按钮
    self.start_btn = self.create_styled_button(
      btn_frame,
      text="开始",
      bg=self.COLORS['success'],
      command=self.start
    )
    self.start_btn.grid(row=0, column=0, padx=8)
    
    # 暂停按钮（初始禁用）
    self.pause_btn = self.create_styled_button(
      btn_frame,
      text="暂停",
      bg=self.COLORS['warning'],
      command=self.pause,
      state=tk.DISABLED
    )
    self.pause_btn.grid(row=0, column=1, padx=8)
    
    # 重置按钮
    self.reset_btn = self.create_styled_button(
      btn_frame,
      text="重置",
      bg=self.COLORS['text_secondary'],
      command=self.reset
    )
    self.reset_btn.grid(row=0, column=2, padx=8)
    
  def create_styled_button(self, parent, text, bg, command, state=tk.NORMAL):
    """创建样式化的按钮
    
    参数:
      parent: 父容器
      text: 按钮文字
      bg: 背景色
      command: 点击回调
      state: 初始状态
      
    返回:
      配置好的按钮控件
    """
    btn = tk.Button(
      parent,
      text=text,
      font=self.font_button,
      fg='black',
      bg=bg,
      activebackground=self.lighten_color(bg, 0.2),
      activeforeground='black',
      width=12,
      height=1,
      bd=0,
      relief='flat',
      cursor='hand2',
      command=command,
      state=state
    )
    
    # 添加悬停效果
    btn.bind('<Enter>', lambda e: btn.configure(bg=self.lighten_color(bg)))
    btn.bind('<Leave>', lambda e: btn.configure(bg=bg))
    
    return btn
    
  def lighten_color(self, hex_color, factor=0.15):
    """将颜色变亮
    
    参数:
      hex_color: 十六进制颜色值
      factor: 变亮因子
      
    返回:
      变亮后的十六进制颜色
    """
    # 移除 # 号
    hex_color = hex_color.lstrip('#')
    
    # 转换为 RGB
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    
    # 变亮
    r = min(255, int(r + (255 - r) * factor))
    g = min(255, int(g + (255 - g) * factor))
    b = min(255, int(b + (255 - b) * factor))
    
    # 转回十六进制
    return f'#{r:02x}{g:02x}{b:02x}'
    
  def update_status(self, state):
    """更新状态显示
    
    参数:
      state: 'idle' | 'running' | 'paused'
    """
    status_texts = {
      'idle': '准备就绪',
      'running': '计时中...',
      'paused': '已暂停'
    }
    
    self.draw_status_dot(state)
    self.status_text.config(text=status_texts.get(state, '准备就绪'))
    
  def update(self):
    """更新显示的时间"""
    if self.running and self.start_time is not None:
      current = self.elapsed + (time.time() - self.start_time)
      self.time_label.config(text=self.format_time(current))
    
    self.update_id = self.root.after(10, self.update)
    
  def start(self):
    """开始计时"""
    if not self.running:
      self.start_time = time.time()
      self.running = True
      self.start_btn.config(state=tk.DISABLED)
      self.pause_btn.config(state=tk.NORMAL)
      self.update_status('running')
      self.update()
      
  def pause(self):
    """暂停计时"""
    if self.running and self.start_time is not None:
      self.elapsed += time.time() - self.start_time
      self.running = False
      self.start_btn.config(state=tk.NORMAL)
      self.pause_btn.config(state=tk.DISABLED)
      self.update_status('paused')
      if self.update_id:
        self.root.after_cancel(self.update_id)
        
  def reset(self):
    """重置计时器"""
    self.running = False
    self.elapsed = 0.0
    self.start_time = None
    self.time_label.config(text="00:00.00")
    self.start_btn.config(state=tk.NORMAL)
    self.pause_btn.config(state=tk.DISABLED)
    self.update_status('idle')
    if self.update_id:
      self.root.after_cancel(self.update_id)
      
  def format_time(self, seconds):
    """格式化时间为 MM:SS.ms"""
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 100)
    return f"{mins:02d}:{secs:02d}.{millis:02d}"


if __name__ == "__main__":
  root = tk.Tk()
  app = BusinessTimerApp(root)
  root.mainloop()
