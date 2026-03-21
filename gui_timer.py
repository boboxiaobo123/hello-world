import tkinter as tk
import time

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("秒表计时器")
        self.root.geometry("400x300")
        
        self.start_time = None
        self.elapsed = 0.0
        self.running = False
        self.update_id = None
        
        self.time_label = tk.Label(root, text="00:00.00", font=("Arial", 48))
        self.time_label.pack(pady=30)
        
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=20)
        
        self.start_btn = tk.Button(btn_frame, text="开始", width=10, command=self.start)
        self.start_btn.grid(row=0, column=0, padx=5)
        
        self.pause_btn = tk.Button(btn_frame, text="暂停", width=10, command=self.pause, state=tk.DISABLED)
        self.pause_btn.grid(row=0, column=1, padx=5)
        
        self.reset_btn = tk.Button(btn_frame, text="重置", width=10, command=self.reset)
        self.reset_btn.grid(row=0, column=2, padx=5)
        
    def update(self):
        if self.running and self.start_time is not None:
            current = self.elapsed + (time.time() - self.start_time)
            self.time_label.config(text=self.format_time(current))
        self.update_id = self.root.after(10, self.update)
        
    def start(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True
            self.start_btn.config(state=tk.DISABLED)
            self.pause_btn.config(state=tk.NORMAL)
            self.update()
            
    def pause(self):
        if self.running:
            self.elapsed += time.time() - self.start_time
            self.running = False
            self.start_btn.config(state=tk.NORMAL)
            self.pause_btn.config(state=tk.DISABLED)
            if self.update_id:
                self.root.after_cancel(self.update_id)
                
    def reset(self):
        self.running = False
        self.elapsed = 0.0
        self.start_time = None
        self.time_label.config(text="00:00.00")
        self.start_btn.config(state=tk.NORMAL)
        self.pause_btn.config(state=tk.DISABLED)
        if self.update_id:
            self.root.after_cancel(self.update_id)
            
    def format_time(self, seconds):
        mins = int(seconds // 60)
        secs = int(seconds % 60)
        millis = int((seconds % 1) * 100)
        return f"{mins:02d}:{secs:02d}.{millis:02d}"

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
