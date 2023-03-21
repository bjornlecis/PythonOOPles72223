import tkinter as tk
from tkinter import ttk
from klasse_persoon import Persoon
from dummy_personen import lijst_personen




class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tkinter StringVar')
        self.geometry("1000x750")
        self.configure(bg="#A8D0DB")
        self.naam = tk.StringVar()
        self.leeftijd = tk.StringVar()
        self.geslacht = tk.StringVar()
        self.keuze = tk.StringVar()
        self.nieuw_naam = tk.StringVar()
        self.nieuw_leeftijd = tk.StringVar()
        self.nieuw_geslacht = tk.StringVar()


        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

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
        ttk.Label(self, text='Naam_nieuw_persoon').grid(column=0, row=5)
        ttk.Label(self, text='Leeftijd_nieuw_persoon').grid(column=2, row=5)
        ttk.Label(self, text='Geslacht_nieuw_persoon').grid(column=4, row=5)

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

        n_naam_entry = ttk.Entry(self, textvariable=self.nieuw_naam)
        n_naam_entry.grid(column =1, row=5)
        n_lft_entry = ttk.Entry(self, textvariable=self.nieuw_leeftijd)
        n_lft_entry.grid(column =3, row=5)
        n_geslacht_entry = ttk.Entry(self, textvariable=self.nieuw_geslacht)
        n_geslacht_entry.grid(column =5, row=5)


        # Button
        submit_button = ttk.Button(self, text='Submit', command=self.submit)
        submit_button.grid(column=2, row=1, **padding)
        get_item_button = ttk.Button(self,text="Haal item op",command=self.haal_item)
        get_item_button.grid(column=1, row=0)
        voeg_item_toe_button = ttk.Button(self,text="Voeg Item Toe",command=self.voeg_item_toe)
        voeg_item_toe_button.grid(column=0, row=6)

        # Output label
        self.output_label = ttk.Label(self)
        self.output_label.grid(column=0, row=4, columnspan=3, **padding)

        #combobox
        self.combo_box_personen = ttk.Combobox(self,textvariable=self.keuze)
        self.combo_box_personen["values"] = self.geef_namen_in_lijst()
        self.combo_box_personen.grid(row=0, column=0)


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

    def voeg_item_toe(self):
        naam = self.nieuw_naam.get()
        lft = int(self.nieuw_leeftijd.get())
        geslacht = self.nieuw_geslacht.get()
        p = Persoon(naam,lft,geslacht)
        lijst_personen.append(p)
        self.combo_box_personen["values"] = self.geef_namen_in_lijst()




if __name__ == "__main__":
    app = App()
    app.mainloop()



