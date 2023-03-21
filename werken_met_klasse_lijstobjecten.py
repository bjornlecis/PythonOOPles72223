import tkinter as tk
from tkinter import ttk
from klasse_persoon import Persoon
from dummy_personen import lijst_personen




class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tkinter StringVar')
        self.geometry("300x150")
        self.configure(bg="#A8D0DB")
        self.naam = tk.StringVar()
        self.leeftijd = tk.StringVar()
        self.geslacht = tk.StringVar()
        self.keuze = tk.StringVar()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.per = Persoon("Test", 0, "None")
        self.create_widgets()

    def geef_namen_in_lijst(self):
        lijst = []
        for x in lijst_personen:
            lijst.append(x.naam)
        return lijst

    def create_widgets(self):
        padding = {'padx': 5, 'pady': 5}
        # label
        ttk.Label(self, text='Naam:').grid(column=0, row=1, **padding)
        ttk.Label(self, text='Leeftijd:').grid(column=0, row=2, **padding)
        ttk.Label(self, text='Geslacht:').grid(column=0, row=3, **padding)

        # Entry
        self.naam.set(self.per.naam)
        naam_entry = ttk.Entry(self, textvariable=self.naam)
        naam_entry.grid(column=1, row=1, **padding)
        naam_entry.focus()

        self.leeftijd.set(str(self.per.leeftijd))
        lft_entry = ttk.Entry(self, textvariable=self.leeftijd)
        lft_entry.grid(column=1, row=2, **padding)

        self.geslacht.set(self.per.geslacht)
        geslacht_entry = ttk.Entry(self, textvariable=self.geslacht)
        geslacht_entry.grid(column=1, row=3, **padding)

        # Button
        submit_button = ttk.Button(self, text='Submit', command=self.submit)
        submit_button.grid(column=2, row=1, **padding)
        get_item_button = ttk.Button(self,text="Haal item op",command=self.haal_item)
        get_item_button.grid(column=1, row=0)

        # Output label
        self.output_label = ttk.Label(self)
        self.output_label.grid(column=0, row=4, columnspan=3, **padding)

        #combobox
        combo_box_personen = ttk.Combobox(self,textvariable=self.keuze)
        combo_box_personen["values"] = self.geef_namen_in_lijst()
        combo_box_personen.grid(row=0, column=0)


    def submit(self):
        keuze_naam = self.keuze.get()
        for x in lijst_personen:
            if keuze_naam == x.naam:
                x.naam = self.naam.get()
                x.leeftijd = int(self.leeftijd.get())
                x.geslacht = self.geslacht.get()
                self.output_label.config(text=Persoon.__str__(x))

    def haal_item(self):
        keuze_naam = self.keuze.get()
        for x in lijst_personen:
            if keuze_naam == x.naam:
                self.naam.set(x.naam)
                self.leeftijd.set(str(x.leeftijd))
                self.geslacht.set(x.geslacht)


if __name__ == "__main__":
    app = App()
    app.mainloop()



