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
        pass

    def window_home_interface(self, window):
        pass


if __name__ == '__main__':
    window = customtkinter.CTk()
    instance = Window()

    instance.window_configuration(window)
    instance.window_interface(window)
    instance.window_home_interface(window)
    window.mainloop()