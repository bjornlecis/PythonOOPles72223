import tkinter as tk
from tkinter import ttk
from klasse_persoon import Persoon


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tkinter StringVar')
        self.geometry("300x150")
        self.configure(bg="#A8D0DB")
        self.naam = tk.StringVar()
        self.leeftijd = tk.StringVar()
        self.geslacht = tk.StringVar()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.per = Persoon("Bart", 25, "Man")
        self.create_widgets()

    def create_widgets(self):
        padding = {'padx': 5, 'pady': 5}
        # label
        ttk.Label(self, text='Naam:').grid(column=0, row=0, **padding)
        ttk.Label(self, text='Leeftijd:').grid(column=0, row=1, **padding)
        ttk.Label(self, text='Geslacht:').grid(column=0, row=2, **padding)

        # Entry
        self.naam.set(self.per.naam)
        naam_entry = ttk.Entry(self, textvariable=self.naam)
        naam_entry.grid(column=1, row=0, **padding)
        naam_entry.focus()

        self.leeftijd.set(str(self.per.leeftijd))
        lft_entry = ttk.Entry(self, textvariable=self.leeftijd)
        lft_entry.grid(column=1, row=1, **padding)

        self.geslacht.set(self.per.geslacht)
        geslacht_entry = ttk.Entry(self, textvariable=self.geslacht)
        geslacht_entry.grid(column=1, row=2, **padding)

        # Button
        submit_button = ttk.Button(self, text='Submit', command=self.submit)

        submit_button.grid(column=2, row=0, **padding)

        # Output label
        self.output_label = ttk.Label(self)
        self.output_label.grid(column=0, row=3, columnspan=3, **padding)

    def submit(self):
        self.per.naam = self.naam.get()
        self.per.leeftijd = int(self.leeftijd.get())
        self.per.geslacht = self.geslacht.get()
        print(self.per)
        self.output_label.config(text=self.per.__str__())


if __name__ == "__main__":
    app = App()
    app.mainloop()
