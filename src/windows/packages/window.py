import customtkinter

class Window():
    def configuration(self, window):
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('dark-blue')

        window.title('WinWARE - 1.0.0')
        window.geometry('900x500')

        window.minsize(width=900, height=500)
        window.maxsize(width=900, height=500)

        window.config(background='#1B1B1B')

if __name__ == '__main__':
    app = customtkinter.CTk()
    instance = Window()

    instance.configuration(app)
    app.mainloop()