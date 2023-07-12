import customtkinter
import configparser
from PIL import Image

class Window():
    def configuration(self, window):
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('dark-blue')

        window.title('WinWARE - 1.0.0')
        window.geometry('900x500')

        window.minsize(width=900, height=500)
        window.maxsize(width=900, height=500)

        window.config(background='#1B1B1B')

    def app_menu(self, window):
        config = configparser.ConfigParser()
        config.read('windows/cache/temps/configuration.config')
        username = config.get('Configuration', 'user_name')
        first_name = config.get('Configuration', 'first_name')
        last_name = config.get('Configuration', 'last_name')

        frame = customtkinter.CTkFrame(master=window, width=200, height=500, fg_color='#1B1B1B', border_width=0, border_color='#1B1B1B')
        frame.grid(row=0, column=0)

        title = customtkinter.CTkLabel(master=frame, width=200, height=75, text='WinWARE', font=customtkinter.CTkFont(family='Roboto', size=18, weight='bold'), text_color='#FFFFFF')
        title.grid(row=0, column=0)


        home_frame = customtkinter.CTkFrame(master=frame, width=200, height=25, fg_color='transparent')
        home_frame.grid(row=1, column=0, pady=25, sticky='w')

        home_image = customtkinter.CTkImage(Image.open('assets/carre.png'),size=(15, 15))
        home_image_text = customtkinter.CTkLabel(master=home_frame, image=home_image, width=54, height=25, compound='right', justify='right', text_color='#1B1B1B', fg_color='transparent')
        home_image_text.grid(row=0, column=0)

        home_button = customtkinter.CTkButton(master=home_frame, height=25, width=100, text='Home', anchor='w', fg_color='transparent', font=customtkinter.CTkFont(family='Roboto', size=12), text_color='#C0C0C0', hover='disable')
        home_button.grid(row=0, column=1, padx=20)


        spymode_frame = customtkinter.CTkFrame(master=frame, width=200, height=25, fg_color='transparent')
        spymode_frame.grid(row=2, column=0, sticky='w')

        spymode_image = customtkinter.CTkImage(Image.open('assets/triangle.png'),size=(15, 18))
        spymode_image_text = customtkinter.CTkLabel(master=spymode_frame, image=spymode_image, width=54, height=25, compound='right', justify='right', text_color='#1B1B1B', fg_color='transparent')
        spymode_image_text.grid(row=0, column=0)

        spymode_button = customtkinter.CTkButton(master=spymode_frame, height=25, width=100, text='Spymode', anchor='w', fg_color='transparent', font=customtkinter.CTkFont(family='Roboto', size=12), text_color='#C0C0C0', hover='disable')
        spymode_button.grid(row=0, column=1, padx=20)


        settings_frame = customtkinter.CTkFrame(master=frame, width=200, height=25, fg_color='transparent')
        settings_frame.grid(row=3, column=0, pady=25, sticky='w')

        settings_image = customtkinter.CTkImage(Image.open('assets/cercle.png'),size=(15, 15))
        settings_image_text = customtkinter.CTkLabel(master=settings_frame, image=settings_image, width=54, height=25, compound='right', justify='right', text_color='#1B1B1B', fg_color='transparent')
        settings_image_text.grid(row=0, column=0)

        settings_button = customtkinter.CTkButton(master=settings_frame, height=25, width=100, text='Settings', anchor='w', fg_color='transparent', font=customtkinter.CTkFont(family='Roboto', size=12), text_color='#C0C0C0', hover='disable')
        settings_button.grid(row=0, column=1, padx=20)

        
        user_frame = customtkinter.CTkFrame(master=frame, width=200, height=50, fg_color='transparent')
        user_frame.grid(row=4, column=0, pady=175, sticky='w')

        user_image = customtkinter.CTkImage(Image.open('assets/photo.png'), size=(35, 35))
        user_image_text = customtkinter.CTkLabel(master=user_frame, image=user_image, width=57, height=35, compound='right', justify='right', text_color='#1B1B1B', text='___')
        user_image_text.grid(row=0, column=0)


        name_frame = customtkinter.CTkFrame(master=user_frame, width=118, height=34, fg_color='transparent')
        name_frame.grid(row=0, column=1, padx=12, sticky='e')

        user_name = customtkinter.CTkLabel(master=name_frame, width=118, height=17, text=username, font=customtkinter.CTkFont(family='Roboto', size=15, weight='bold'), anchor='w', text_color='#FFFFFF')
        user_name.grid(row=0, column=0)
        
        first_last_name = customtkinter.CTkLabel(master=name_frame, width=118, height=17, text=f'{first_name} {last_name}', font=customtkinter.CTkFont(family='Roboto', size=11), anchor='w', text_color='#C0C0C0')
        first_last_name.grid(row=1, column=0)

if __name__ == '__main__':
    app = customtkinter.CTk()
    instance = Window()

    instance.configuration(app)
    instance.app_menu(app)
    app.mainloop()