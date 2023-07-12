import configparser

def configuration():
    CONFIG_FILE_PATH = 'windows/cache/temps/configuration.config'

    first_name = input('\nEnter your first name:\n> ')
    last_name = input('\nEnter your last name:\n> ')
    user_name = input('\nEnter your user name:\n> ')

    print('Creating the .config file...')
    config = configparser.ConfigParser()

    print('Configuring the .config file...')
    config['Configuration'] = {
        'first_name': first_name,
        'last_name': last_name,
        'user_name': user_name
    }

    print('Saving data...')
    with open(CONFIG_FILE_PATH, 'w') as configfile:
        config.write(configfile)
    
    print('Setup complete!')

if __name__ == '__main__':
    print('Be careful, the information you enter will be stored in a .config file locally on your PC.')
    print('To learn more, enter the command "about".')

    configuration()
