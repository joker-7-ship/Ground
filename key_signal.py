from pynput import keyboard, mouse
import time
#
# exit_program = False
#
#
# def on_press(key):
#     global exit_program
#     try:
#         if key.char == 'q':
#             print('你进行了 键盘按键q，程序退出！')
#             exit_program = True
#     except AttributeError:
#         pass
#
#
# def on_click(x, y, button, pressed):
#     global exit_program
#     if pressed:
#         print('你进行了鼠标点击，程序退出！')
#         exit_program = True
#
#
# keyboard_listener = keyboard.Listener(on_press=on_press)
# mouse_listener = mouse.Listener(on_click=on_click)
#
# keyboard_listener.start()
# mouse_listener.start()
#
#
# def main():
#     global exit_program
#
#     try:
#         while True:
#             if exit_program:
#                 break
#             print('程序正在进行...')
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print('你按下了 Ctrl+C!')
#     finally:
#         keyboard_listener.stop()
#         mouse_listener.stop()
#
#
# if __name__ == '__main__':
#     main()


if __name__ == '__main__':
    try:
        while 1:
            x = 2+2
            print(x)
            time.sleep(2)
    except KeyboardInterrupt as e:
        print('yo')
