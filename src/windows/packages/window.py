import customtkinter

class Window:
    def window_configuration(self, window):
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('dark-blue')

        window.title('WinWARE')
        window.geometry('900x500')

        window.minsize(width=900, height=500)
        window.maxsize(width=900, height=500)

        window.config(background='#111111')

    def window_interface(self, window):
        frame = customtkinter.CTkFrame(master=window, height=500, width=200)
        frame.grid(row=0, column=0)

        title = customtkinter.CTkLabel(master=frame, height=50, width=200, text='WinWARE', font=customtkinter.CTkFont('Roboto', size=25, weight='bold'))
        title.grid(pady=15)

        home_button = customtkinter.CTkButton(master=frame, height=35, width=200, text='Home', font=customtkinter.CTkFont('Roboto', size=17), fg_color='transparent', hover_color='#2b2b2b', corner_radius=0)
        home_button.grid()

        settings_button = customtkinter.CTkButton(master=frame, height=35, width=200, text='Settings', font=customtkinter.CTkFont('Roboto', size=17), fg_color='transparent', hover_color='#2b2b2b', corner_radius=0)
        settings_button.grid(pady=350)

    def window_home_interface(self, window):
        frame = customtkinter.CTkFrame(master=window, height=500, width=700, fg_color='#ffbb00')
        frame.grid()


if __name__ == '__main__':
    window = customtkinter.CTk()
    instance = Window()

    instance.window_configuration(window)
    instance.window_interface(window)
    instance.window_home_interface(window)
    window.mainloop()