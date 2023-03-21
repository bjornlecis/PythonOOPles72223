import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tkinter StringVar')
        self.geometry("400x200")
        self.getal1_var = tk.StringVar()
        self.getal2_var = tk.StringVar()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.create_widgets()

    def create_widgets(self):

        padding = {'padx': 5, 'pady': 5}
        # label
        ttk.Label(self, text='Getal 1:').grid(column=0, row=0, **padding)
        ttk.Label(self, text='Getal 2:').grid(column=0, row=1, **padding)

        # Entry
        getal1 = ttk.Entry(self, textvariable=self.getal1_var)
        getal1.grid(column=1, row=0, **padding)
        getal1.focus()

        getal2 = ttk.Entry(self, textvariable=self.getal2_var)
        getal2.grid(column=1, row=1, **padding)

        # Button
        plus_button = ttk.Button(self, text='+', command=self.plus)
        plus_button.grid(column=2, row=0, **padding)
        minus_button = ttk.Button(self, text='-', command=self.min)
        minus_button.grid(column=2, row=1, **padding)
        times_button = ttk.Button(self, text='x', command=self.maal)
        times_button.grid(column=2, row=2, **padding)
        divide_button = ttk.Button(self, text='/', command=self.delen)
        divide_button.grid(column=2, row=3, **padding)
        grootste_button = ttk.Button(self, text='<>', command=self.grootste)
        grootste_button.grid(column=2, row=4, **padding)

        # Output label
        self.output_label = ttk.Label(self)
        self.output_label.grid(column=0, row=3, columnspan=3, **padding)



    def plus(self):
        som = int(self.getal1_var.get())+int(self.getal2_var.get())
        res = f"De uitkomst is: {str(som)}"
        self.config(bg="Pink")
        self.output_label.config(text=res)
        self.output_label.configure(background="Pink")
        self.output_label.configure(foreground="Purple",font=("Comic Sans",20))

    def min(self):
        verschil = int(self.getal1_var.get())-int(self.getal2_var.get())
        res = f"De uitkomst is: {str(verschil)}"
        self.config(bg="Pink")
        self.output_label.config(text=res)
        self.output_label.configure(background="Pink")
        self.output_label.configure(foreground="Purple",font=("Comic Sans",20))

    def maal(self):
        product = int(self.getal1_var.get())*int(self.getal2_var.get())
        res = f"De uitkomst is: {str(product)}"
        self.config(bg="Pink")
        self.output_label.config(text=res)
        self.output_label.configure(background="Pink")
        self.output_label.configure(foreground="Purple",font=("Comic Sans",20))

    def delen(self):
        quotient = float(self.getal1_var.get())/float(self.getal2_var.get())
        res = f"De uitkomst is: {str(round(quotient,3))}"
        self.config(bg="Pink")
        self.output_label.config(text=res)
        self.output_label.configure(background="Pink")
        self.output_label.configure(foreground="Purple",font=("Comic Sans",20))

    def grootste(self):
       if int(self.getal1_var.get()) > int(self.getal2_var.get()):
            res = "het eerste getal is het grootst"
            self.output_label.config(text=res)
       elif int(self.getal1_var.get()) < int(self.getal2_var.get()):
            res = "het tweede getal is het grootst"
            self.output_label.config(text=res)
       else:
           res = "beide getallen zijn even groot"
           self.output_label.config(text=res)






if __name__ == "__main__":
    app = App()
    app.mainloop()
