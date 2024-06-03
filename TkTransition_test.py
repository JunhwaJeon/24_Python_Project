import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.title("화면 전환 예제")
        self.geometry("400x300")
        
        self.frames = {}
        
        # 각 화면(Frame)을 생성합니다.
        self.frame1 = Frame1(self)
        self.frame1.place(x=0, y=0, relwidth=1, relheight=1)
        self.frames[Frame1] = self.frame1
        
        
        self.frame2 = Frame2(self)
        self.frame2.place(x=0, y=0, relwidth=1, relheight=1)
        self.frames[Frame2] = self.frame2
        
        
        self.frame3 = Frame3(self)
        self.frame3.place(x=0, y=0, relwidth=1, relheight=1)
        self.frames[Frame3] = self.frame3
        
        
        # 컨트롤 버튼을 생성합니다.
        self.button1 = tk.Button(self.frame1, text="화면 1로 이동", command=lambda: self.show_frame(Frame1))
        self.button1.place(x=50, y=250)
        
        self.button2 = tk.Button(self.frame1, text="화면 2로 이동", command=lambda: self.show_frame(Frame2))
        self.button2.place(x=150, y=250)
        
        self.button3 = tk.Button(self.frame1, text="화면 3로 이동", command=lambda: self.show_frame(Frame3))
        self.button3.place(x=250, y=250)
        
        
        # 초기 화면 설정
        self.show_frame(Frame1)
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        
    def show_frame(self, frame):
        # 선택한 화면을 보여줍니다.
        frame_to_show = self.frames[frame]
        frame_to_show.tkraise()

class Frame1(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="이곳은 화면 1 입니다.")
        label.pack(pady=50)
        
class Frame2(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="이곳은 화면 2 입니다.")
        label.pack(pady=50)

class Frame3(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="이곳은 화면 3 입니다.")
        label.pack(pady=50)

# 애플리케이션 실행
app = App()
app.mainloop()