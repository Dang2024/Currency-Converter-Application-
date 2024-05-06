
import tkinter as tk
import currency_info as ci
import requests 

def process():
    initial_currency=start_option.get()[:3] #gets initial currency from start_option, also only displays the first 3 letters of currency
    amount_value=amount.get()           #gets amount from typed entry box
    converted_currency=end_option.get()[:3]     #gets fianl currency from end_option
    print("Initial_currency=",initial_currency)
    print("Amount Value=",amount_value)
    print("final_currency=",converted_currency)
    

    url = "https://api.frankfurter.app/latest?amount=" + amount_value + "&from=" + initial_currency + "&to=" + converted_currency
    print("URL =", url)

    response = requests.get(url)
    data = response.json()

    result = data['rates'][converted_currency]
    print("Result =", result, converted_currency)

    
    result_label.config(text=(result, converted_currency))  # repalces result with the converted currency amount + currency


mainwin=tk.Tk()
mainwin.title("Currency Converter")

top_label = tk.Label(mainwin, text="Enter requested information. Then press the Process button.")
top_label.grid(row=0,columnspan=2, sticky=tk.W)   #organizes text cells above

start_label = tk.Label(mainwin, text="Select Initial Currency Type:")
start_label.grid(row=1,column=0, sticky=tk.W)  

currencyList=ci.currencyList

start_option = tk.StringVar()
start_option.set(currencyList[0])   #sets equal to first currency

start_dropdown = tk.OptionMenu(mainwin, start_option, *currencyList)
start_dropdown.grid(row=1, column=1, sticky=tk.W) #this section of code places dropdown button

amount_label = tk.Label(mainwin, text="Enter The Currency Amount:")
amount_label.grid(row=2,column=0, sticky=tk.W)
amount = tk.Entry(mainwin)
amount.grid(row=2, column=1, sticky=tk.W)


end_label = tk.Label(mainwin, text="Select Final Currency Type:")
end_label.grid(row=3,column=0, sticky=tk.W)  

end_option = tk.StringVar()            #end option currency
end_option.set(currencyList[0])

end_dropdown = tk.OptionMenu(mainwin, end_option, *currencyList)
end_dropdown.grid(row=3, column=1, sticky=tk.W) #t

result_label = tk.Label(mainwin, text = "Result:" )   # displays results: above process
result_label.grid(row=4, columnspan=2)

process_button = tk.Button(mainwin, text = "Process", command = process) 
process_button.grid(row=5, columnspan=2)

tk.mainloop()  # do not add code below this line

