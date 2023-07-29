import tkinter as tk
from tkinter import ttk
import base64

window = tk.Tk()
window.title("Utility Software")
window.resizable(False, False)

style=ttk.Style()
style.configure('TFrame' )
style.configure('TLabel', font=('Calibri', 12) )
style.configure('TButton', font=('Calibri', 12) )
style.configure('TEntry', font=('Calibri', 13))


padding_btn = {'padx': 25, 'pady': 30, 'ipadx':20, 'ipady':15}

# Arithmetic Calculation
def arith_btn_pressed():
    def evaluate():
        value=eval(entry.get())
        lbl_result["text"]="Result: " + str(value)

    new_win=tk.Toplevel() # to create new window
    new_win.title("Arithmetic Calculator")
    new_win.resizable(False, False)
    new_win.focus()  #To focus on the new window by default

    label_input=ttk.Label(master=new_win, text="Input numbers and symbols: ")
    label_input.grid(row=0, column=0, padx=10, pady=5)

    entry=ttk.Entry(master=new_win, width=20)
    entry.grid(row=1, column=0, padx=10, pady=5)

    btn_calc=ttk.Button(master=new_win, text="Calculate", command=evaluate)
    btn_calc.grid(row=2, column=0, padx=10, pady=5)

    lbl_result=ttk.Label(master=new_win, text="")
    lbl_result.grid(row=3, column=0, padx=10, pady=5)

# Temperature Converter
def temp_btn_pressed():
    def selected_option():
        temp=entry.get()     # retrieves the entry value (which is a string)
        selected=var.get()    # retrieves the selected option value from var
        if selected==1:
            temp=(float(temp) * 9/5) + 32
            label_result["text"]="Result: "+ str(temp)+" \N{DEGREE FAHRENHEIT}"

        if selected==2:
            temp=(float(temp) - 32) * 5/9
            label_result["text"]="Result: " + str(temp) + " \N{DEGREE CELSIUS}"

    new_win=tk.Toplevel()
    new_win.title("Temperature Converter")
    new_win.resizable(False, False)

    var=tk.IntVar()  # IntVar() to hold the selected option value
    var.set(1)
    option1=ttk.Radiobutton(master=new_win, variable=var, text="Celsius to Fahrenheit", value=1)
    option1.grid(row=0, column=0, padx=5, pady=2)

    option2=ttk.Radiobutton(master=new_win, variable=var, text="Fahrenheit to Celsius", value=2)
    option2.grid(row=1, column=0,padx=5, pady=2)

    entry=ttk.Entry(master=new_win, width=20)
    entry.grid(row=2, column=0,padx=20, pady=10)

    btn_submit=ttk.Button(master=new_win, text="Submit", command=selected_option)
    btn_submit.grid(row=3, column=0,padx=20, pady=10)

    label_result=ttk.Label(master=new_win, font=("Arial", 12, "bold"))
    label_result.grid(row=4,column=0,padx=20, pady=10)

# bmi
def bmi_btn_pressed():
    def bmi():
        h=float(entry_height.get())
        w=float(entry_weight.get())
        bmi=w/(h*h)
        result=round(bmi, 4)
        label_result["text"]="BMI: " + str(result)

    new_win=tk.Toplevel()
    new_win.title("BMI converter")
    new_win.resizable(False,False)

    frame1=ttk.Frame(master=new_win)
    frame1.pack()

    label_height= ttk.Label(master=frame1, text="Height : ")
    label_height.grid(row=0, column=0, padx=10, pady=10)
    entry_height=ttk.Entry(master=frame1, width=10)
    entry_height.grid(row=0, column=1, padx=10, pady=10)
    label_M=ttk.Label(master=frame1, text="Meter")
    label_M.grid(row=0, column=2, padx=10)

    label_weight= ttk.Label(master=frame1, text="Weight : ")
    label_weight.grid(row=1, column=0, padx=5, pady=5)
    entry_weight=ttk.Entry(master=frame1, width=10)
    entry_weight.grid(row=1, column=1, padx=5, pady=5)
    label_kg=ttk.Label(master=frame1, text="KG")
    label_kg.grid(row=1, column=2, padx=10)

    frame2=ttk.Frame(master=new_win)
    frame2.pack()

    btn_compute=ttk.Button(master=frame2, text="Compute", command=bmi)
    btn_compute.grid(row=0, column=0, pady=10)
    label_result=ttk.Label(master=frame2, text="", font=("Arial", 12, "bold"))
    label_result.grid(row=1, column=0, pady=5)

# currency converter
def currency_btn_pressed():
    USD_TO_BDT = 108.36
    EUR_TO_BDT = 116.60
    EUR_TO_USD = 1.09

    def convert_currency():
        amount = float(entry_amount.get())
        from_currency = from_currency_combo.get()
        to_currency = to_currency_combo.get()

        converted_amount = 0.0

        if from_currency == "USD" and to_currency == "BDT":
            converted_amount = amount * USD_TO_BDT
        elif from_currency == "BDT" and to_currency == "USD":
            converted_amount = amount / USD_TO_BDT
        elif from_currency == "EUR" and to_currency == "BDT":
            converted_amount = amount * EUR_TO_BDT
        elif from_currency == "BDT" and to_currency == "EUR":
            converted_amount = amount / EUR_TO_BDT
        elif from_currency == "USD" and to_currency == "EUR":
            converted_amount = amount / EUR_TO_USD
        elif from_currency == "EUR" and to_currency == "USD":
            converted_amount = amount * EUR_TO_USD
        else:
            converted_amount = amount
        result_label["text"]="Converted Amount: "+ str(round(converted_amount, 4)) + to_currency

    new_win = tk.Toplevel()
    new_win.title("Currency Converter")
    frame1=tk.Frame(master=new_win)
    frame1.pack()

    label_amount = tk.Label(master=frame1, text="Amount:")
    label_amount.grid(row=0 , column=0, padx=5, pady=5, sticky="e")
    entry_amount = ttk.Entry(master=frame1, width=15)
    entry_amount.grid(row=0 ,column=1, padx=5, pady=5)

    label_from = ttk.Label(master=frame1, text="From Currency:")
    label_from.grid(row=1 ,column=0, padx=5, pady=5, sticky="e")
    from_currency_combo = ttk.Combobox(master=frame1, values=["USD", "EUR", "BDT"], width=12)
    from_currency_combo.grid(row=1 ,column=1, padx=5, pady=5)

    label_to = ttk.Label(master=frame1, text="To Currency:")
    label_to.grid(row=2 ,column=0, padx=5, pady=5, sticky="e")
    to_currency_combo = ttk.Combobox(master=frame1, values=["USD", "EUR", "BDT"], width=12)
    to_currency_combo.grid(row=2 ,column=1, padx=5, pady=5)


    frame2=tk.Frame(master=new_win)
    frame2.pack()

    convert_button = ttk.Button(master=frame2, text="Convert", command=convert_currency)
    convert_button.grid(pady=5)
    result_label = ttk.Label(master=frame2, text="")
    result_label.grid(pady=5)

# length converter
def length_btn_pressed():
    CONVERSION_FACTORS = {
        "Meter": 1,
        "Kilometer": 0.001,
        "Centimeter": 100,
        "Millimeter": 1000,
        "Foot": 3.28084,
    }

    new_win = tk.Toplevel()
    new_win.title("Length Converter")

    def convert_length():
        value = float(entry_value.get())
        from_unit = cmb_from_unit.get()
        to_unit = cmb_to_unit.get()

        result = value * CONVERSION_FACTORS[from_unit] / CONVERSION_FACTORS[to_unit]
        label_result["text"] = "Converted Value: "+ str(round(result, 4))


    label_value = ttk.Label(new_win, text="Value:")
    label_value.grid(row=0,column=0, padx=5, pady=5)

    entry_value = ttk.Entry(new_win)
    entry_value.grid(row=0,column=1, padx=5, pady=5)

    label_from_unit = ttk.Label(new_win, text="From Unit:")
    label_from_unit.grid(row=1,column=0, padx=5, pady=5)

    cmb_from_unit = ttk.Combobox(new_win, values=list(CONVERSION_FACTORS.keys()))
    cmb_from_unit.grid(row=1,column=1, padx=5, pady=5)

    label_to_unit = ttk.Label(new_win, text="To Unit:")
    label_to_unit.grid(row=2,column=0, padx=5, pady=5)

    cmb_to_unit = ttk.Combobox(new_win, values=list(CONVERSION_FACTORS.keys()))
    cmb_to_unit.grid(row=2,column=1, padx=5, pady=5)

    button_covert = ttk.Button(new_win, text="Convert", command=convert_length)
    button_covert.grid(row=3,column=0, padx=5, pady=5)

    label_result = ttk.Label(new_win, text="")
    label_result.grid(row=3,column=1, padx=5, pady=5)

# base64
def base64_btn_pressed():
    def encode_text():
        # get text -> encode(ascii) -> base64 encode -> insert
        input_text = text_input.get("1.0", "end") # "1.0", "end" --> to take all characters from the text field
        text_byte=input_text.encode("ascii")    # converting to ascii form
        base64_byte = base64.b64encode(text_byte)   # converting to base64 (byte form)
        
        text_output.delete("1.0", "end")    # clearing the output text field
        text_output.insert("1.0", base64_byte.decode())     # decode the base64_byte and showing in output field 

    def decode_text():
        # get text -> encode(ascii) -> base64 decode -> insert
        input_text = text_input.get("1.0", "end")
        try:
            text_byte=input_text.encode("ascii")
            base64_byte = base64.b64decode(text_byte) 

            text_output.delete("1.0", "end")
            text_output.insert("1.0", base64_byte.decode())

        # if > base64.binascii.Error < this error shows, throw "Invalid Base64 input!"
        except base64.binascii.Error:   # if 
            text_output.delete("1.0", "end")
            text_output.insert("1.0", "Invalid Base64 input!")

    # Create the main window
    new_win = tk.Tk()
    new_win.title("Base64 Tool")

    frame1=ttk.Frame(new_win)
    frame1.pack(pady=2)
    lbl_input = ttk.Label(frame1, text="Input:")
    lbl_input.pack()
    text_input = tk.Text(frame1, height=10, width=50, relief="flat")
    text_input.pack(pady=5)

    btn_encode = ttk.Button(frame1, text="Encode", command=encode_text)
    btn_encode.pack()
    btn_decode = ttk.Button(frame1, text="Decode", command=decode_text)
    btn_decode.pack()

    frame2=ttk.Frame(new_win)
    frame2.pack()
    lbl_output = tk.Label(frame2, text="Output:")
    lbl_output.pack(pady=2)
    text_output = tk.Text(frame2, height=10, width=50, relief="flat")
    text_output.pack()

frame_label=ttk.Frame(window)
frame_label.pack()

label_main=ttk.Label(frame_label, text="Utility Software", font=("Tw Cen MT", 20, "bold"))
label_main.pack()
label_main2=ttk.Label(frame_label, text="by HELiX", font=("MADE Evolve Sans EVO", 12))
label_main2.pack()


frame_main=ttk.Frame(master=window)
frame_main.pack()

length_btn=ttk.Button(master=frame_main, text="   Length\nConverter", command=length_btn_pressed)
length_btn.grid(row=0, column=0, **padding_btn)

temp_btn=ttk.Button(master=frame_main, text="Temperature\n  Converter", command=temp_btn_pressed)
temp_btn.grid(row=0, column=1,**padding_btn)

currency_btn=ttk.Button(master=frame_main, text=" Currency\nConverter", command=currency_btn_pressed)
currency_btn.grid(row=0, column=2,**padding_btn)

arith_btn=ttk.Button(master=frame_main, text="Arithmetic\nCalculator", command=arith_btn_pressed)
arith_btn.grid(row=1, column=2,**padding_btn)

bmi_btn=ttk.Button(master=frame_main, text="     BMI\nConverter", command=bmi_btn_pressed)
bmi_btn.grid(row=1, column=1, **padding_btn)

base64_btn= ttk.Button(master=frame_main, text="Base64\n  Tool", command=base64_btn_pressed)
base64_btn.grid(row=1, column=0,**padding_btn)

window.mainloop()
