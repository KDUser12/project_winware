import customtkinter

class Window:
    def window_configuration(self, window):
        pass

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