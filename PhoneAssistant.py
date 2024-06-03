import tkinter as tk

class PhoneAssistant:
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.title('휴대폰 구입 보조 프로그램')
        self.geometry('1920x1080')
        
        self.frames={}
        
        # Frame 생성
        self.frame1=Frame1(self)
        self.frames[Frame1]=self.frame1
        
        self.frame2=Frame2(self)
        self.frames[Frame2]=self.frame2
        
        self.frame1=Frame3(self)
        self.frames[Frame3]=self.frame3
        
        # Frame1 컨트롤 버튼 생성
        
        # Frame2 컨트롤 버튼 생성
        btn_clear=tk.Button(Frame2,text='초기화',command=lambda: self.clear_btn(Frame2)) # 초기화 버튼
        btn_clear.place()
        
        btn_see=tk.Button(Frame2,text='결과 보기',command=lambda: self.result_btn(Frame2)) # 결과 확인 버튼
        btn_see.place()
        
        btn_previous=tk.Button(Frame2,text='이전 페이지로'command=lambda: self.previous_btn(Frame1)) # 이전 프레임 복귀 버튼
        btn_previous.place()
        
        # Frame3 컨트롤 버튼 생성
        
        # 초기 화면 설정
        self.show_frame(Frame1)
        
        # Frame1 결과 확인 버튼 커맨드
        
        # Frame2 결과 확인 버튼 커맨드
        def result_btn(self, frame):
            frame.
        # Frame2 초기화 버튼 커맨드
        def clear_btn(self, frame):
            
        # Frame2 이전 프레임 복귀 커맨드
        def previous_btn(self, frame_previous):
            
        # Frame3 이전 프레임 복귀 커맨드