import tkinter as tk

class Frame2(tk.Frame):
    data_usage, 
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        
        label_data_usage=tk.Label(self, text='월 평균 데이터 사용량')
        label_data_usage.place()
        
        label_combine_info=tk.Label(self, text='결합정보 입력')
        label_combine_info.place()
        
        label_monthly_budget=tk.Label(self,text='월 예산')
        label_monthly_budget.place()
        
        label_phone_crash=tk.Label(self,text='휴대폰 파손 경험')
        label_phone_crash.place()
        
        entry_data_usage=tk.Entry(self)
        entry_data_usage.place()
        
        entry_combine_info=tk.Entry(self)
        entry_combine_info.place()
        
        entry_monthly_budget=tk.Entry(self)
        entry_monthly_budget.place()
        
        crash_no=tk.Radiobutton(self,text='없음')
        crash_no.place()
        
        crash_little=tk.Radiobutton(self,text='조금')
        crash_little.place()
        
        crash_frequent=tk.Radiobutton(self,text='많음')
        crash_frequent.place()
        
        pay_now=tk.Checkbutton(self, text='완납',variable=tk.BooleanVar())
        pay_now.place()
        
        pay_monthly=tk.Checkbutton(self, text='할부',variable=tk.BooleanVar())
        pay_monthly.place()
        
        
        
        
        
    def clear_btn(self):
        
    def see_btn(self):
        
    def previous_btn(self):
        