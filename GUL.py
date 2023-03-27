import tkinter

window = tkinter.Tk()
window.title("GUI Program by BAEKJUNGDUCK")
window.geometry("640x400+100+100")
window.resizable(False, False)

def btnclick():
    label.config(font=("Arial",40))
    label.config(text="안산공업고등학교 컴퓨터과")

    

label = tkinter.Label(window, text="안산공업고등학교")
label.pack()

button = tkinter.Button(window,text="확인", command= btnclick)
button.pack()



window.mainloop()
