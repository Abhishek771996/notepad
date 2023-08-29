import tkinter as tk

from tkinter import filedialog

class Notepad():
    def __init__(self,window):
        self.window=window
        self.window.geometry('700x500')
        self.window.resizable(0,0)
        self.window.title('notepad')
        self.window.config(background='gray')

        self.open_file=tk.Button(text='open',font=('havana',23),bg='darkgray',relief='ridge',command=self.open_file)
        self.save_file=tk.Button(text='save',font=('havana',23),bg='darkgray',relief='groove',command=self.save_file)
        self.save_as_file=tk.Button(text='save as',font=('havana',23),bg='darkgray',relief='groove',command=self.save_as_file)
        self.clear=tk.Button(text='clear',font=('havana',23),bg='darkgray',relief='groove',command=self.clear)
        self.help=tk.Button(text='help',font=('havana',23),bg='darkgray',relief='groove',command=self.help)
     

        self.text_area=tk.Text(bg='dark gray',font=('havana',18),width=45,height=12,relief='solid',wrap='word')
        
        self.text_area.grid(row=2,column=1,columnspan=5)

        self.open_file.grid(row=1,column=1,padx=45,pady=12)
        self.save_file.grid(row=1,column=2,pady=45,padx=12)
        self.save_as_file.grid(row=1,column=3,pady=45,padx=12)
        self.clear.grid(row=1,column=4,pady=45,padx=12)
        self.help.grid(row=1,column=5,pady=45,padx=12)

    def clear(self):
        self.text_area.delete(0.0,tk.END)

    def help(self):
        self.text_area.delete(0.0,tk.END)
        what_is_notepad='its is very good software'
        self.text_area.insert(tk.END,what_is_notepad)

    def open_file(self):
        self.find_file=filedialog.askopenfilename()
        if self.find_file:
         with open(self.find_file,'r')as myfile:
          file_text=myfile.read()
          self.text_area.delete(0.0,tk.END)
          self.text_area.insert(tk.END,file_text)
          root.title(f'notepad{self.find_file}')

    def save_file(self):
     if self.find_file:
      with open(self.find_file,'w')as myfile:
        file_text=self.text_area.get(0.0,tk.END)
        myfile.write(file_text)

     else:
        self.save_as_file()

            
    def save_as_file(self):
      file_options= [('.txt','*.txt'),('.bat','*.bat'), ('All files','*.*')]
      file_save= filedialog.asksaveasfilename (defaultextension='.txt', filetypes= file_options)
      if file_save:
        file_text = self.text_area.get(0.0,tk.END) 
        with open(file_save, 'w') as f:
         f.write(file_text)
                    
                    
root=tk.Tk()
note=Notepad(root)       # isko quotation mai nahi lena
root.mainloop()    
