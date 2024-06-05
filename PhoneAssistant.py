from Frame2 import Frame2
import tkinter as tk

class PhoneAssistant(tk.Tk):
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
        btn_clear=tk.Button(self.frame2, text='초기화',command=lambda: self.clear_btn(Frame2)) # 초기화 버튼
        btn_clear.place()
        
        btn_see=tk.Button(self.frame2, text='결과 보기',command=lambda: self.result_btn(Frame2)) # 결과 확인 버튼
        btn_see.place()
        
        btn_previous=tk.Button(self.frame2, text='이전 페이지로',command=lambda: self.previous_btn(Frame1)) # 이전 프레임 복귀 버튼
        btn_previous.place()
        
        # Frame3 컨트롤 버튼 생성
        
        # 초기 화면 설정
        self.show_frame(Frame1)
        
    # 선택한 화면을 보여주는 함수
    def show_frame(self, frame):
        frame_to_show = self.frames[frame]    
        frame_to_show.tkraise()
        
    # Frame1 결과 확인 버튼 커맨드
    
    # Frame2 결과 확인 버튼 커맨드
    def result_btn(self):
        self.combine_info=self.frame2.entry_combine_info.get()
        self.data_usage=self.frame2.entry_data_usage.get()
        self.monthly_budget=self.frame2.entry_monthly_butget.get()
        self.crash_=self.frame2.crash.get()
        self.payment=[self.frame2.pay_0.get(),self.frame2.pay_1.get()]
        
        # 결과 계산 함수 이용
        self.proposed(self.data_usage, self.combine_info, self.monthly_budget, self.crash_, self.payment)
        
        # 결과 창으로 이동
        self.show_frame(self.frame3)
    # Frame2 초기화 버튼 커맨드
    def clear_btn(self):
        self.frame2.entry_data_usage.delete()
        self.frame2.entry_combine_info.delete()
        self.frame2.monthly_budget.delete()
        
    # Frame2 이전 프레임 복귀 커맨드
    def previous_btn(self, frame_previous):
        self.show_frame(frame_previous)
    
    # 결과 계산 함수
    def proposed(self, data_usage, combine_info, monthly_budget, crash, payment):
        
    # Frame3 이전 프레임 복귀 커맨드
    
    
class Frame2(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        
        # 라벨
        label_data_usage=tk.Label(self, text='월 평균 데이터 사용량')
        label_data_usage.place(x=360, y=180)
        
        label_combine_info=tk.Label(self, text='결합정보 입력')
        label_combine_info.place(x=360 , y=360)
        
        label_monthly_budget=tk.Label(self,text='월 예산')
        label_monthly_budget.place(x=360 , y=540)
        
        label_phone_crash=tk.Label(self,text='휴대폰 파손 경험')
        label_phone_crash.place(x=360 , y=720)
        
        # 입력 엔트리
        entry_data_usage=tk.Entry(self)
        entry_data_usage.place(x=720 , y=180)
        
        entry_combine_info=tk.Entry(self)
        entry_combine_info.place(x=720 , y=360)
        
        entry_monthly_budget=tk.Entry(self)
        entry_monthly_budget.place(x=720 , y=540)
        
        # 파손 정보 갖는 라디오버튼 세 개
        crash=tk.IntVar()
        
        crash_no=tk.Radiobutton(self,text='없음',variable=crash, value=0)
        crash_no.place(x=720 , y=720)
        
        crash_little=tk.Radiobutton(self,text='조금',variable=crash, value=1)
        crash_little.place(x=840 , y=720)
        
        crash_frequent=tk.Radiobutton(self,text='많음',variable=crash, value=2)
        crash_frequent.place(x=960 , y=720)
        
        # 납부 정보 갖는 체크버튼 두 개
        pay_0=tk.IntVar()
        pay_now=tk.Checkbutton(self, text='완납',variable=pay_0)
        pay_now.place(x=360 , y=900)
        
        pay_1=tk.IntVar()
        pay_monthly=tk.Checkbutton(self, text='할부',variable=pay_1)
        pay_monthly.place(x=540 , y=900)