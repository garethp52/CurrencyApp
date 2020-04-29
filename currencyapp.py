import tkinter as tk
import json
from urllib.request import urlopen
from Symbols import Currency_symbols

# URL that contains the Euro exchange rates, convert to python object called 'data'
with urlopen("http://data.fixer.io/api/latest?access_key=37423b9a9d3f0702499cc25524ef0f91") as response:
    source = response.read()

data = json.loads(source)

# function to access the currency symbol to be used in output
def currency_symbol(currency_code):
    if currency_code in Currency_symbols.keys():
        for code, symbol in Currency_symbols.items():
            if code == currency_code:
                return symbol
    else:
        return ''

# function to do conversion based on rate and display output
def EUtoconvetor(currency_code, amount):
    try:
        centsamt = float(amount) * 100
        if currency_code in data['rates'].keys():
            for item in data['rates'].items():
                if currency_code == item[0]:
                    conversion = int(centsamt) * item[1]
                    conversioneuro = round(conversion/100, 2)
                    print ('Yes')
                    # run currency_symbol func to insert currency symbol infront of results
                    lbl_results['text'] = str(currency_symbol(currency_code)) + str(conversioneuro)
        else:
            lbl_results['text'] = 'Sorry, we could not make the conversion.'
    except:
        lbl_results['text'] = 'Sorry, we could not make the conversion.'

# tkinter window config
app = tk.Tk()

HEIGHT = 500
WIDTH = 600
bg_color = '#e6f0ff'

canvas = tk.Canvas(app, height=HEIGHT, width=WIDTH)
background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(app, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

canvas.pack()

# Tkinter intro section
frm_intro = tk.Frame(highlightbackground="black", highlightthickness=2, bg=bg_color, bd=5)
frm_intro.place(relx=0.5, rely=0.08, anchor='n')

lbl_greeting = tk.Label(master=frm_intro, text="Welcome to the currency convertor!",
                        font=("Calibri", 20, "bold"), bg=bg_color)
lbl_greeting.pack()

lbl_info = tk.Label(master=frm_intro, text="We convert EURO into any currency of your choice. "
                         "\n Please enter the amount to be converted and the currency code"
                         "\n you would like it converted from.", bg=bg_color)
lbl_info.pack()

# Tkinter input section
frm_input = tk.Frame(highlightbackground="black", highlightthickness=2, bg=bg_color, bd=5)
frm_input.place(relx=0.5, rely=0.35, anchor='n')

lbl_curcode = tk.Label(master=frm_input, text="Currency Code:", bg=bg_color)
ent_curcode = tk.Entry(master=frm_input)
lbl_curcode.grid(row=0, column=0, sticky="w")
ent_curcode.grid(row=0, column=1, sticky="nsew")
lbl_amount = tk.Label(master=frm_input, text="Amount(€):", bg=bg_color)
ent_amount = tk.Entry(master=frm_input)
lbl_amount.grid(row=1, column=0, sticky="w")
ent_amount.grid(row=1, column=1, sticky="nsew")

btn_submit = tk.Button(master=frm_input, text='Get results!',
                       command=lambda: EUtoconvetor(ent_curcode.get(), (ent_amount.get())), bg='#ccffeb')
btn_submit.grid(row=2, column=1, sticky="e")

#RTkinter results section
frm_results = tk.Frame(highlightbackground="black", highlightthickness=2, bg=bg_color)
frm_results.place(relx=0.5, rely=0.6, anchor='n')

lbl_rescopy = tk.Label(master=frm_results, text="Your conversion is: ", bg=bg_color)
lbl_results = tk.Label(master=frm_results, bg=bg_color)
lbl_rescopy.pack()
lbl_results.pack()

app.mainloop()

