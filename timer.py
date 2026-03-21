import time

def timer():
    start_time: float | None = None
    elapsed = 0.0
    running = False

    while True:
        print("\n=== 秒表计时器 ===")
        print("1. 开始/继续")
        print("2. 暂停")
        print("3. 重置")
        print("4. 退出")
        
        if running and start_time is not None:
            current = elapsed + (time.time() - start_time)
        else:
            current = elapsed
        
        print(f"\n当前时间: {format_time(current)}")
        
        choice = input("\n请选择操作 (1-4): ").strip()
        
        if choice == '1':
            if not running:
                start_time = time.time()
                running = True
                print("计时已开始!")
        elif choice == '2':
            if running and start_time is not None:
                elapsed += time.time() - start_time
                running = False
                print("计时已暂停!")
        elif choice == '3':
            elapsed = 0
            start_time = None
            running = False
            print("计时已重置!")
        elif choice == '4':
            print("退出计时器")
            break
        else:
            print("无效选择，请重试")

def format_time(seconds):
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 100)
    return f"{mins:02d}:{secs:02d}.{millis:02d}"

if __name__ == "__main__":
    timer()
