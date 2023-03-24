from polygon import RESTClient
import tkinter as tk


client = RESTClient(api_key="uOB0nFhRExhfiz8PI78OH6BgSejf_xLU")
tickerInput = input("Enter desired companys ticker symbol: ")

ticker = tickerInput.upper()

tickerInfo = client.get_ticker_details(ticker=ticker, date="20223-03-24")
print(tickerInfo)

main = tk.Tk()
main.title("Company stock monitor")

# sets screen width and height
window_width = 300
window_height = 200

# get the screen dimension
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# set the position of the window to the center of the screen
main.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
# sets window to not be resizable
main.resizable(False, False)

message = tk.Label(main, text="Company stock monitor")
message.pack()
main.mainloop()
