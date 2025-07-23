import customtkinter

def button_callback():
    print("Button pressed")


app = customtkinter.CTk()

app.title("Test App")
app.geometry("400x150")
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure((0,1), weight=1)

button = customtkinter.CTkButton(app, text="Test Button", command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

checkbox1 = customtkinter.CTkCheckBox(app, text="Checkbox 1")
checkbox1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
checkbox2 = customtkinter.CTkCheckBox(app, text="Checkbox 2")
checkbox2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")


app.mainloop()
