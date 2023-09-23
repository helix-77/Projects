import tkinter as tk
from tkinter import StringVar, ttk, messagebox, filedialog
import base64
import random
import string
from datetime import date
from pytube import YouTube


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
    def evaluate_expression():
        try:
            expression = entry.get()
            result = eval(expression)
            result_label.config(text=f"{result}")
        except Exception:
            result_label.config(text="Error")


    def clear_input():
        entry.delete(0, tk.END)
        result_label.config(text="")

    new_win = tk.Toplevel()
    new_win.title("Arithmetic Calculator")
    new_win.geometry("420x440")

    frame1=ttk.Frame(new_win)
    frame1.pack(padx=10, pady=20)

    lbl_display=ttk.Label(master=frame1, text="Display", justify='left', font=("Arial", 12, "bold"), relief='flat')
    lbl_display.grid(row=0, column=0, padx=5)

    entry = tk.Entry(frame1, width=30, relief='flat')
    entry.grid(row=0, column=1, columnspan=3, ipadx=7,)

    result_lbl = tk.Label(frame1, text="Result", font=("Arial", 12, "bold"))
    result_lbl.grid(row=1, column=0, pady=5)

    result_label = tk.Label(frame1, text="", relief='flat', bg="white", anchor='w')
    result_label.grid(row=1, column=1, pady=5, ipadx=97, )


    frame2=ttk.Frame(new_win)
    frame2.pack(padx=10)

    characters = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', 'C', '=', '+'
    ]

    row_val = 0
    col_val = 0

    for i in characters:
        if i == 'C':
            ttk.Button(frame2, text=i,  command=clear_input).grid(row=row_val, column=col_val, ipady=25)
        elif i == '=':
            ttk.Button(frame2, text=i, command=evaluate_expression).grid(row=row_val, column=col_val ,ipady=25)
        else:
            ttk.Button(frame2, text=i, command=lambda b=i: entry.insert(tk.END, b)).grid(row=row_val, column=col_val,ipady=25)
        
        col_val +=1
        if col_val > 3:
            col_val = 0
            row_val += 1

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
    new_win.geometry("350x280")
    
    lbl_title=ttk.Label(master=new_win, text="Temperature Converter", font=("Arial", 14, "bold"))
    lbl_title.pack(padx=10, pady=20)

    var=tk.IntVar()  # IntVar() to hold the selected option value
    var.set(1)
    option1=ttk.Radiobutton(master=new_win, variable=var, text="Celsius to Fahrenheit", value=1)
    option1.pack(padx=5, pady=5)

    option2=ttk.Radiobutton(master=new_win, variable=var, text="Fahrenheit to Celsius", value=2)
    option2.pack(padx=5, pady=5)

    entry=ttk.Entry(master=new_win, width=20)
    entry.pack(padx=20, pady=10)

    btn_submit=ttk.Button(master=new_win, text="Submit", command=selected_option)
    btn_submit.pack(padx=20, pady=10)

    label_result=ttk.Label(master=new_win, font=("Arial", 12, "bold"))
    label_result.pack(padx=20, pady=10)

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
    new_win.geometry("350x250")

    lbl_title=ttk.Label(master=new_win, text="BMI Calculator", font=("Arial", 14, "bold"))
    lbl_title.pack(padx=10, pady=20)

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
    new_win.resizable(False,False)
    new_win.geometry("350x280")
    
    label_title = ttk.Label(master=new_win, text="Currency Converter", font=("Arial", 14, "bold"))
    label_title.pack(padx=10, pady=20)
    
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
    convert_button.grid(pady=15)
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
    new_win.resizable(False,False)
    new_win.geometry("350x280")

    def convert_length():
        value = float(entry_value.get())
        from_unit = cmb_from_unit.get()
        to_unit = cmb_to_unit.get()

        result = value * CONVERSION_FACTORS[from_unit] / CONVERSION_FACTORS[to_unit]
        label_result["text"] = "Converted Value: "+ str(round(result, 4))


    frame=ttk.Frame(master=new_win)
    frame.pack()
    
    lbl_title=ttk.Label(master=frame, text="Length Converter", font=("Arial", 14, "bold"))
    lbl_title.grid(row=0,column=0, padx=10, pady=10, columnspan=2)
    
    label_value = ttk.Label(frame, text="Value:")
    label_value.grid(row=1,column=0, padx=10, pady=10)

    entry_value = ttk.Entry(frame)
    entry_value.grid(row=1,column=1, padx=10, pady=10)

    label_from_unit = ttk.Label(frame, text="From Unit:")
    label_from_unit.grid(row=2,column=0, padx=10, pady=10)

    cmb_from_unit = ttk.Combobox(frame, values=list(CONVERSION_FACTORS.keys()))
    cmb_from_unit.grid(row=2,column=1, padx=10, pady=10)

    label_to_unit = ttk.Label(frame, text="To Unit:")
    label_to_unit.grid(row=3,column=0, padx=10, pady=10)

    cmb_to_unit = ttk.Combobox(frame, values=list(CONVERSION_FACTORS.keys()))
    cmb_to_unit.grid(row=3,column=1, padx=10, pady=10)

    button_covert = ttk.Button(frame, text="Convert", command=convert_length)
    button_covert.grid(row=4,column=0, padx=10, pady=10, columnspan=2)

    label_result = ttk.Label(frame, text="")
    label_result.grid(row=5,column=0, padx=10, pady=10, columnspan=2)

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

# password generator
def pass_btn_pressed():
    def generate_password():
        try:
            password_length=int(entry_length.get())
        except ValueError:
            lbl_result.config(text="Please enter a valid number") # use config to show the result in the app
            return

        char_sets=[]  # all checkbox selected options will create a character set(list) which will be used to generate random characters
        if upper_var.get():
            char_sets.append(string.ascii_uppercase)  # if checkbox value is 1, insert the uppercase letter type to the set
        if lower_var.get():
            char_sets.append(string.ascii_lowercase)
        if digits_var.get():
            char_sets.append(string.digits)
        if special_var.get():
            char_sets.append(string.punctuation)

        if not char_sets:
            lbl_result.config(text="Please select at least 1 option")
            return

        # implementation
        selected_types="".join(char_sets)  # selected_types -> creating a  string of selected options from the char_set list
        password="".join(random.choice(selected_types) for i in range(password_length))  
        """ here,
            randomly generating characters from the selected types using random() function and for loop,
            then concatenating  it to a string using join() function """

        #show result
        lbl_result.config(text="Generated Password: "+ password)

    new_win=tk.Toplevel()
    new_win.title("Password Generator")
    new_win.resizable(False,False)
    new_win.geometry("350x350")

    pad = {'padx': 30, 'pady': 15}

    label_top=ttk.Label(new_win, text="Password Generator", font=("MADE Evolve Sans EVO", 15, "bold"))
    label_top.pack(**pad)

    lbl_length = ttk.Label(new_win, text="Password Length:")
    lbl_length.pack(padx=25)
    entry_length=ttk.Entry(new_win)
    entry_length.pack(padx=25)

    frame2=tk.Frame(new_win)
    frame2.pack(**pad)
    lbl_checkbox = ttk.Label(frame2, text="Include options: ")
    lbl_checkbox.pack(padx=25)

    upper_var=tk.IntVar()
    upper_chk_btn=ttk.Checkbutton(frame2, text="Upper case letters", variable=upper_var)
    upper_chk_btn.pack(padx=25)

    lower_var=tk.IntVar()
    lower_chk_btn=ttk.Checkbutton(frame2, text="Lower case letters", variable=lower_var)
    lower_chk_btn.pack(padx=25)

    digits_var=tk.IntVar()
    digits_chk_btn=ttk.Checkbutton(frame2, text="Digits", variable=digits_var)
    digits_chk_btn.pack(padx=25, anchor=tk.W)

    special_var=tk.IntVar()
    special_chk_btn=ttk.Checkbutton(frame2, text="Special characters", variable=special_var)
    special_chk_btn.pack(padx=25)

    frame_3=tk.Frame(new_win)
    frame_3.pack(**pad)

    btn_generate = ttk.Button(frame_3, text="Generate Password", command=generate_password)
    btn_generate.pack(padx=25, pady=3)

    lbl_result = ttk.Label(frame_3, text="", font=("Tw Cen MT", 12, "bold"))
    lbl_result.pack(padx=25, pady=5)

# age calculator
def age_btn_pressed():
    def calculate_age():
        try:
            today = date.today()
            
            current_date = today.day
            current_month = today.month
            current_year = today.year
            
            birth_date = int(entry_day.get())
            birth_month = int(entry_month.get())
            birth_year = int(entry_year.get())
            
            age_year = current_year - birth_year
            age_month = current_month - birth_month
            age_date = current_date - birth_date
            
            if age_date < 0:
                age_month -= 1
                age_date += 30  # Assuming a month has 30 days
            
            if age_month < 0:
                age_year -= 1
                age_month += 12
            
            if age_year < 0:
                lbl_result.config(text="Invalid input")
            else:
                lbl_result.config(text=f"Age: {age_year} years, {age_month} months, {age_date} days")
            
        except ValueError:
            lbl_result.config(text="Invalid input")


    # main
    new_window= tk.Toplevel()
    new_window.title('Age Calculator')
    new_window.resizable(False,False)


    lbl_title=ttk.Label(master=new_window, text="Age Calculator", font=("Tw Cen MT", 20, "bold"))
    lbl_title.pack(padx=50, pady=15)

    frame1=tk.Frame(master=new_window)
    frame1.pack(padx=50, pady=15)

    padding_frame1 = {'padx': 10, 'pady': 5}
    lbl_day = ttk.Label(frame1, text='Day:')
    lbl_day.grid(row=0, column=0, **padding_frame1)
    lbl_month = ttk.Label(frame1, text='Month:')
    lbl_month.grid(row=0, column=1, **padding_frame1)
    lbl_year = ttk.Label(frame1, text='Year:')
    lbl_year.grid(row=0, column=2, **padding_frame1)

    entry_day = ttk.Entry(frame1, width=15)
    entry_day.grid(row=1, column=0,**padding_frame1)
    entry_month = ttk.Entry(frame1, width=15)
    entry_month.grid(row=1, column=1,**padding_frame1)
    entry_year = ttk.Entry(frame1, width=15)
    entry_year.grid(row=1, column=2,**padding_frame1)

    btn_calc = ttk.Button(new_window, text='Calculate',command=calculate_age)
    btn_calc.pack(padx=4, pady=15, ipadx=10, ipady=5)

    lbl_result = ttk.Label(new_window, text='', font=("Tw Cen MT", 14))
    lbl_result.pack(padx=10, pady=15)

# youtube video downloader
def yt_btn_pressed():
    def browse():
        location = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH", title="Save Video" )
        download_Path.set(location)
        
    def download():
        Youtube_link = video_Link.get()
        download_Folder = download_Path.get()
        getVideo = YouTube(Youtube_link)

        videoStream = getVideo.streams.first() # selecting the first stream
        videoStream.download(download_Folder)  # Downloading the video to the destination
        messagebox.showinfo("Done!", "Download completed and saved in: \n" + download_Folder)


    new_win = tk.Toplevel()

    new_win.geometry("490x200")
    new_win.title("YouTube Video Downloader")
    new_win.resizable(False, False)

    # Creating the tkinter Variables
    video_Link = StringVar()
    download_Path = StringVar()

    lbl_head = tk.Label(new_win,text="YouTube Video Downloader", font=("Berlin Sans FB", 15))
    lbl_head.grid(row=1, column=0, pady=10, padx=10, columnspan=3)

    lbl_link = tk.Label(new_win, text="YouTube link :", bg="salmon", pady=5, padx=5)
    lbl_link.grid(row=2, column=0, pady=5, padx=5)

    entry_link = tk.Entry(new_win, width=53, textvariable=video_Link, font="Calibri 11")
    entry_link.grid(row=2, column=1, pady=5, padx=5, columnspan=2)

    lbl_destination = tk.Label(new_win, text="Destination :", bg="salmon", pady=5, padx=9)
    lbl_destination.grid(row=3, column=0, pady=5, padx=5)

    entry_dest_path = tk.Entry(new_win, width=40, textvariable=download_Path, font="Calibri 11")
    entry_dest_path.grid(row=3, column=1, pady=5, padx=5)

    btn_browse = ttk.Button(new_win, text="Browse", command=browse, width=9)
    btn_browse.grid(row=3, column=2, pady=1, padx=1)

    btn_dwl = ttk.Button(new_win,text="Download",command=download)
    btn_dwl.grid(row=4, column=1, pady=20, padx=20)


frame_label=ttk.Frame(window)
frame_label.pack()

label_main=ttk.Label(frame_label, text="Utility Software", font=("Tw Cen MT", 20, "bold"))
label_main.pack()
label_main2=ttk.Label(frame_label, text="by HELiX", font=("MADE Evolve Sans EVO", 12))
label_main2.pack()

frame_main=ttk.Frame(master=window)
frame_main.pack()

# by helix ^_^

length_btn=ttk.Button(master=frame_main, text="   Length\nConverter", command=length_btn_pressed)
length_btn.grid(row=0, column=0, **padding_btn)

temp_btn=ttk.Button(master=frame_main, text="Temperature\n  Converter", command=temp_btn_pressed)
temp_btn.grid(row=0, column=2,**padding_btn)

currency_btn=ttk.Button(master=frame_main, text=" Currency\nConverter", command=currency_btn_pressed)
currency_btn.grid(row=2, column=0,**padding_btn)

arith_btn=ttk.Button(master=frame_main, text="Arithmetic\nCalculator", command=arith_btn_pressed)
arith_btn.grid(row=1, column=0,**padding_btn)

base64_btn= ttk.Button(master=frame_main, text="Base64\n  Tool", command=base64_btn_pressed)
base64_btn.grid(row=1, column=1,**padding_btn)

bmi_btn=ttk.Button(master=frame_main, text="     BMI\nConverter", command=bmi_btn_pressed)
bmi_btn.grid(row=1, column=2, **padding_btn)

pass_btn= ttk.Button(master=frame_main, text="Password\nGenerator", command=pass_btn_pressed)
pass_btn.grid(row=0, column=1,**padding_btn)

age_btn=ttk.Button(master=frame_main, text="     Age\nCalculator", command=age_btn_pressed)
age_btn.grid(row=2, column=1,**padding_btn)

yt_btn=ttk.Button(master=frame_main, text="   YouTube\nDownloader", command=yt_btn_pressed)
yt_btn.grid(row=2, column=2,**padding_btn)


window.mainloop()
