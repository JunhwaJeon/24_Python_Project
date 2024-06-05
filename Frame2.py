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