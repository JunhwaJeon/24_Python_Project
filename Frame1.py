import tkinter as tk
from tkinter import PhotoImage
import os

class Frame1(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        
        self.parent = parent

        btn_samsung = tk.Button(self, text='삼성', command=self.show_samsung_phones, width=20, height=2)
        btn_apple = tk.Button(self, text='애플', command=self.show_apple_phones, width=20, height=2)
        
        btn_samsung.place(x=720, y=270, width=200, height=50)
        btn_apple.place(x=1000, y=270, width=200, height=50)

        # 선택된 폰 저장
        self.selected_phone = tk.StringVar()
        self.selected_phone.set("선택한 기종은 없습니다.")

        # 어떤 폰 선택했는지 알려줌
        self.selected_phone_label = tk.Label(self, textvariable=self.selected_phone)
        self.selected_phone_label.place(x=860, y=930)

        
        self.canvas = tk.Canvas(self, width=1440, height=540)
        self.phone_frame = tk.Frame(self.canvas)
        self.phone_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.phone_frame, anchor="nw")

        
        # 스크롤바
        self.scrollbar = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.scrollbar.place(x=720, y=750, width=500)
        self.canvas.place(x=240, y=370, width=1440, height=540)
        self.canvas.configure(xscrollcommand=self.scrollbar.set)

        
        btn_next_frame2 = tk.Button(self, text='다음 페이지로', command=self.show_frame2)
        btn_next_frame2.place(x=1600, y=800, width=150, height=50)

    def show_frame2(self):
        self.parent.show_frame(Frame2)

    def select_phone(self, phone):
        self.selected_phone.set("선택한 기종은 {}입니다.".format(phone))
        self.parent.selected_phone.set("선택한 기종은 {}입니다.".format(phone))

    def clear_phone_frame(self):
        self.phone_frame.destroy()
        self.phone_frame = tk.Frame(self.canvas)
        self.phone_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.phone_frame, anchor="nw")
        
    def display_phones(self, phones):
        images_path = './images'
        
        for i, (phone, image_file) in enumerate(phones):
            frame = tk.Frame(self.phone_frame)
            frame.pack(side='left', padx=20)

            
            image_path = os.path.join(images_path, image_file)
            try:
                img = PhotoImage(file=image_path)
                img_label = tk.Label(frame, image=img)
                img_label.image = img
                img_label.pack()
            except tk.TclError:
                print(f"Image {image_path} could not be loaded.")

            # 휴대폰 버튼
            phone_button = tk.Button(frame, text=phone, command=lambda p=phone: self.select_phone(p))
            phone_button.pack()

    def show_samsung_phones(self):
        self.clear_phone_frame()
        phones = [
            ('Galaxy S24', 'galaxy_s24.png'),
            ('Galaxy S24 Plus', 'galaxy_s24_plus.png'),
            ('Galaxy S24 Ultra', 'galaxy_s24_ultra.png'),
            ('Galaxy Z Flip 5', 'galaxy_z_flip_5.png'),
            ('Galaxy Z Fold 5', 'galaxy_z_fold_5.png')
        ]
        self.display_phones(phones)
        
    def show_apple_phones(self):
        self.clear_phone_frame()
        phones = [
            ('iPhone 15', 'iphone_15.png'),
            ('iPhone 15 Plus', 'iphone_15_plus.png'),
            ('iPhone 15 Pro', 'iphone_15_pro.png'),
            ('iPhone 15 Pro Max', 'iphone_15_pro_max.png'),
            ('iPhone 14', 'iphone_14.png'),
            ('iPhone 14 Plus', 'iphone_14_plus.png'),
            ('iPhone 14 Pro', 'iphone_14_pro.png'),
            ('iPhone 14 Pro Max', 'iphone_14_pro_max.png')
        ]
        self.display_phones(phones)




class Frame2(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # 선택한 휴대폰 정보 레이블
        self.selected_phone_label = tk.Label(self, textvariable=parent.selected_phone)
        self.selected_phone_label.pack()

        self.comment_label = tk.Label(self, text = 'Frame2 화면')
        self.comment_label.pack()




class PhoneAssistant(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.title('휴대폰 구입 보조 프로그램')
        self.geometry('1920x1080')

        self.selected_phone = tk.StringVar()
        self.selected_phone.set("선택한 기종은 없습니다.")
        
        self.frames = {}
        
       #Frame1
        self.frame1 = Frame1(self)
        self.frames[Frame1] = self.frame1
        self.frame1.place(relwidth=1, relheight=1)
        
        #Frame2
        self.frame2 = Frame2(self)
        self.frames[Frame2] = self.frame2
        self.frame2.place(relwidth=1, relheight=1)
        self.frame2.lower()
        
        #초기화면
        self.show_frame(Frame1)


        
    # 선택한 화면을 보여주는 함수
    def show_frame(self, frame):
        frame_to_show = self.frames[frame]
        frame_to_show.tkraise()

if __name__ == "__main__":
    app = PhoneAssistant()
    app.mainloop()
