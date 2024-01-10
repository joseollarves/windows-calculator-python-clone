# Importing the necesary

import customtkinter as tk
from PIL import Image

# Class Calculator
class Calculator(tk.CTk):
    def __init__(self):
        # Essential
        super().__init__()
        self.geometry('330x370') # Default Geometry
        self.resizable(0,0) # Fixed size
        self.title('Calculator') # The Title
        self.iconbitmap('_internal/img/calc.ico') # The Logo
        
        # Input
        self.input = ''
        self.textInput = tk.StringVar()

        # Delete icon
        self.deleteIcon = tk.CTkImage(light_image=Image.open('_internal/img/delete_black.png'),dark_image=Image.open('_internal/img/delete_white.png'))

        # Declaring components
        self.components() # The components of the calculator

    def components(self):

        # Input
        frameInput = tk.CTkFrame(self, width=100, height=50, fg_color='#202020')
        frameInput.grid(row=1,column=0)

        input = tk.CTkEntry(frameInput, font=('segoe ui', 18, 'bold'), textvariable=self.textInput, 
                            width=330, corner_radius=1, justify=tk.RIGHT, placeholder_text='0')
        input.grid(row=1,column=0,ipady=10, pady=30)

        # Buttons
        frameButtons = tk.CTkFrame(self, width=80, height=80, fg_color='#202020')
        frameButtons.grid(row=2,column=0)

        # C Button
        cButton = tk.CTkButton(frameButtons, width=80, height=50, 
                                text='C', font=('segoe ui', 16), fg_color='#343434', 
                                hover_color='#555555', corner_radius=6, command=self.deleteAll).grid(
                                    row=3,column=1, padx=1, pady=1)

        # Delete Button 
        deleteButton = tk.CTkButton(frameButtons, cursor='arrow', width=80, 
                                    height=50, text='', fg_color='#343434', hover_color='#555555', 
                                    corner_radius=6, image=self.deleteIcon, command=self.deleteLastDigit).grid(
                                        row=3,column=2, padx=1, pady=1)
        
        # Divide button (÷)
        tk.CTkButton(frameButtons, cursor='arrow', width=80, 
                     height=50, text='÷', font=('segoe ui', 24),
                     fg_color='#343434', hover_color='#555555', corner_radius=6, 
                     command=lambda: self.calcButton('/')).grid(
                         row=3, column=3, padx=1, pady=1)
    
        # 7 button
        tk.CTkButton(frameButtons, text='7', width=80, 
                     height=50, font=('segoe ui', 16), command=lambda: self.calcButton(7),
                     fg_color='#3c3c3c', hover_color='#2f2f2f', corner_radius=6).grid(
                         row=4,column=0, padx=1,pady=1)
        
        # 8 button
        tk.CTkButton(frameButtons, text='8', width=80, 
                     height=50, font=('segoe ui', 16), command=lambda: self.calcButton(8),
                     fg_color='#3c3c3c', hover_color='#2f2f2f', corner_radius=6).grid(
                         row=4,column=1, padx=1,pady=1)
        
        # 9 button
        tk.CTkButton(frameButtons, text='9', width=80, 
                     height=50, font=('segoe ui', 16), command=lambda: self.calcButton(9),
                     fg_color='#3c3c3c', hover_color='#2f2f2f', corner_radius=6).grid(
                         row=4,column=2, padx=1,pady=1)
        
        # x button
        tk.CTkButton(frameButtons, text='x', width=80, 
                     height=50, font=('segoe ui', 18), command=lambda: self.calcButton('*'),
                     fg_color='#343434', hover_color='#555555', corner_radius=6).grid(
                         row=4,column=3, padx=1,pady=1)
        
        # 4 button
        tk.CTkButton(frameButtons, text='4', width=80, 
                     height=50, font=('segoe ui', 16), command=lambda: self.calcButton(4),
                     fg_color='#3c3c3c', hover_color='#2f2f2f', corner_radius=6).grid(
                         row=5,column=0, padx=1,pady=1)
        
        # 5 button
        tk.CTkButton(frameButtons, text='5', width=80, 
                     height=50, font=('segoe ui', 16), command=lambda: self.calcButton(5),
                     fg_color='#3c3c3c', hover_color='#2f2f2f', corner_radius=6).grid(
                         row=5,column=1, padx=1,pady=1)
        
        # 6 button
        tk.CTkButton(frameButtons, text='6', width=80, 
                     height=50, font=('segoe ui', 16), command=lambda: self.calcButton(6),
                     fg_color='#3c3c3c', hover_color='#2f2f2f', corner_radius=6).grid(
                         row=5,column=2, padx=1,pady=1)
        
        # - button
        tk.CTkButton(frameButtons, text='-', width=80, 
                     height=50, font=('segoe ui', 25), command=lambda: self.calcButton('-'),
                     fg_color='#343434', hover_color='#555555', corner_radius=6).grid(
                         row=5,column=3, padx=1,pady=1)
        
        # 1 button
        tk.CTkButton(frameButtons, text='1', width=80, 
                     height=50, font=('segoe ui', 16), command=lambda: self.calcButton(1),
                     fg_color='#3c3c3c', hover_color='#2f2f2f', corner_radius=6).grid(
                         row=6,column=0, padx=1,pady=1)
        
        # 2 button
        tk.CTkButton(frameButtons, text='2', width=80, 
                     height=50, font=('segoe ui', 16), command=lambda: self.calcButton(2),
                     fg_color='#3c3c3c', hover_color='#2f2f2f', corner_radius=6).grid(
                         row=6,column=1, padx=1,pady=1)
        
        # 3 button
        tk.CTkButton(frameButtons, text='3', width=80, 
                     height=50, font=('segoe ui', 16), command=lambda: self.calcButton(3),
                     fg_color='#3c3c3c', hover_color='#2f2f2f', corner_radius=6).grid(
                         row=6,column=2, padx=1,pady=1)
        
        # + button
        tk.CTkButton(frameButtons, text='+', width=80, 
                     height=50, font=('segoe ui', 25), command=lambda: self.calcButton('+'),
                     fg_color='#343434', hover_color='#555555', corner_radius=6).grid(
                         row=6,column=3, padx=1,pady=1)
        
        # 0 button
        tk.CTkButton(frameButtons, text='0', width=80, 
                     height=50, font=('segoe ui', 16), command=lambda: self.calcButton(0),
                     fg_color='#3c3c3c', hover_color='#2f2f2f', corner_radius=6).grid(
                         row=7,column=1, padx=1,pady=1)
        
        # , button
        tk.CTkButton(frameButtons, text=',', width=80, 
                     height=50, font=('segoe ui', 16), command=lambda: self.calcButton(','),
                     fg_color='#3c3c3c', hover_color='#2f2f2f', corner_radius=6).grid(
                         row=7,column=2, padx=1,pady=1)
        
        # = button
        tk.CTkButton(frameButtons, text='=', text_color=('#fff','#202020'), width=80, 
                     height=50, hover_color='#66b2ff', font=('segoe ui', 24), 
                     command=self.equalButton, fg_color='#58a3dc', corner_radius=6).grid(
                        row=7,column=3, padx=1,pady=1)

    # Delete button function
    def deleteLastDigit(self):
        temp = list(self.textInput.get())
        self.input = ''.join(str(temp[i]) for i in range(0, len(temp)-1))
        self.textInput.set(self.input)

    # C button function
    def deleteAll(self):
        self.input = ''
        self.textInput.set(self.input)

    # The function for almost every button on the calculator
    def calcButton(self, digit):
        input = list(self.input)
        if '+' in input or '-' in input or '*' in input or '/' in input:
            if type(digit) == int:
                self.input = f'{self.input}{digit}'
                self.textInput.set(self.input)
            
            elif digit == ',':
                self.input = f'{self.input}{'.'}'
                self.textInput.set(self.input)
                
            else:
                self.input = str(eval(self.input))
                self.input = f'{self.input}{digit}'
                self.textInput.set(self.input)
        else:
            if digit == ',':
                self.input = f'{self.input}{'.'}'
                self.textInput.set(self.input)
            else:
                self.input = f'{self.input}{digit}'
                self.textInput.set(self.input)
    
    # = button function
    def equalButton(self):
        resultado = str(eval(self.input))
        self.textInput.set(resultado)
 
if __name__ == '__main__':
    calculator = Calculator() # Declare the calculator
    calculator.configure(fg_color='#202020') # Change the background of the calculator
    calculator.mainloop() # Run

