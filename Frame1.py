import tkinter as tk
from tkinter import PhotoImage
import os

class Frame1(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        
        self.parent = parent
        

        btn_samsung = tk.Button(self, text='삼성', command=self.show_samsung_phones, width=20, height=2)
        btn_apple = tk.Button(self, text='애플', command=self.show_apple_phones, width=20, height=2)
        btn_others = tk.Button(self, text='기타', command=self.show_other_phones, width=20, height=2)
        
        btn_samsung.place(x=640, y=270, width=200, height=50)
        btn_apple.place(x=880, y=270, width=200, height=50)
        btn_others.place(x=1120, y=270, width=200, height=50)


        # 선택된 폰 저장
        self.selected_phone = tk.StringVar()
        self.selected_phone.set("선택한 기종은 없습니다.")

        # 어떤 폰 선택했는지 알려줌
        self.selected_phone_label = tk.Label(self, textvariable=self.selected_phone)
        self.selected_phone_label.place(x=860, y=930)
        

        self.phone_frame = tk.Frame(self)
        self.phone_frame.place(x=240, y=370, width=1440, height=540)
    



        # Frame2로 전환하는 버튼
        def show_frame2(self):
            self.parent.show_frame(Frame2)

        btn_next_frame2 = tk.Button(self, text='다음 페이지로', command=self.parent.show_frame2)
        btn_next_frame2.place(x=1500, y=950, width=150, height=50)







    def select_phone(self, phone):
        self.selected_phone.set("선택한 기종은 {}입니다.".format(phone))


    def clear_phone_frame(self):
        for widget in self.phone_frame.winfo_children():
            widget.destroy()
    

    def display_phones(self, phones):
        images_path = 'C:\\Users\\bestw\\OneDrive\\바탕 화면\\images'
        
        for i, (phone, image_file) in enumerate(phones):
            frame = tk.Frame(self.phone_frame)
            frame.pack(side='left', padx=20)
            
            image_path = os.path.join(images_path, image_file)
            try:
                img = PhotoImage(file=image_path)
            except tk.TclError:
                img = PhotoImage()
                print(f"Image {image_path} could not be loaded.")
                
            img_label = tk.Label(frame, image=img)
            img_label.image = img
            img_label.pack()
            
            phone_button = tk.Button(frame, text=phone, command=lambda p=phone: self.select_phone(p))
            phone_button.pack()


    def show_samsung_phones(self):
        self.clear_phone_frame()
        phones = [
            ('갤럭시 S24', 'file.png'),
            ('갤럭시 S23', 'file.png'),
            ('갤럭시 Z플립5', 'file.png')
        ]
        self.display_phones(phones)
        
    def show_apple_phones(self):
        self.clear_phone_frame()
        phones = [
            ('아이폰 14', 'file.png'),
            ('아이폰 13', 'file.png'),
            ('아이폰 12', 'file.png')
        ]
        self.display_phones(phones)
        
    def show_other_phones(self):
        self.clear_phone_frame()
        phones = [
            ('A사', 'file.png'),
            ('B사', 'file.png'),
            ('C사', 'file.png')
        ]
        self.display_phones(phones)
    






class PhoneAssistant(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.title('휴대폰 구입 보조 프로그램')
        self.geometry('1920x1080')
        
        self.frames = {}
        
        # Frame 생성
        self.frame1 = Frame1(self)
        self.frames[Frame1] = self.frame1
        self.frame1.place(relwidth=1, relheight=1)
        
        # 초기 화면 설정
        self.show_frame(Frame1)
        
    # 선택한 화면을 보여주는 함수
    def show_frame(self, frame):
        frame_to_show = self.frames[frame]
        frame_to_show.tkraise()



if __name__ == "__main__":
    app = PhoneAssistant()
    app.mainloop()


