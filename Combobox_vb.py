import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tkinter StringVar')
        self.geometry("400x300")
        self.configure(bg="white")
        self.basis_var = tk.StringVar()
        self.hoogte_var = tk.StringVar()
        self.keuze_kleur = tk.StringVar()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.create_widgets()

    def create_widgets(self):

        padding = {'padx': 5, 'pady': 5}
        # label
        ttk.Label(self, text='Basis:').grid(column=0, row=0, **padding)
        ttk.Label(self, text='Hoogte:').grid(column=0, row=1, **padding)
        ttk.Label(self, text="Kleur:").grid(column=0, row=2)

        # Entry
        getal1 = ttk.Entry(self, textvariable=self.basis_var)
        getal1.grid(column=1, row=0, **padding)
        getal1.focus()

        getal2 = ttk.Entry(self, textvariable=self.hoogte_var)
        getal2.grid(column=1, row=1, **padding)

        #combobox
        keuzelijst = ttk.Combobox(self, textvariable=self.keuze_kleur)
        kleuren = ["Blauw","Groen","Rood","Roze"]
        keuzelijst['values'] = kleuren
        keuzelijst.grid(column=1, row=2)

        # Button
        submit_button = ttk.Button(self, text='Bereken', command=self.submit)
        submit_button.grid(column=2, row=0, **padding)

        # Output label
        self.output_label = ttk.Label(self)
        self.output_label.grid(column=0, row=4, columnspan=3, **padding)



    def submit(self):
        oppervlakte = int(self.basis_var.get())*int(self.hoogte_var.get())
        res = f"De oppervlakte is {str(oppervlakte)} m²"
        if self.keuze_kleur.get() == "Blauw":
            self.configure(bg="Blue")
        elif self.keuze_kleur.get() == "Groen":
            self.configure(bg="Green")
        elif self.keuze_kleur.get() == "Rood":
            self.configure(bg="Red")
        elif self.keuze_kleur.get() == "Roze":
            self.configure(bg="Pink")
        else:
            print("Fout in kleur keuze")
        self.output_label.config(text=res)
        self.output_label.configure(background="Navy")
        self.output_label.configure(foreground="Yellow",font=("Comic Sans",20))





if __name__ == "__main__":
    app = App()
    app.mainloop()
    print("programma 1")
