import keyboard
import time

class KeyboardListener:
    def on_key_press(self, key_name: str):
        raise NotImplementedError()


class KeyLogger(KeyboardListener):
    def on_key_press(self, key_name: str):
        print(f"[Консоль] Натиснуто клавішу: {key_name}")


class KeyFileLogger(KeyboardListener):
    def __init__(self, filename="key_log.txt"):
        self.filename = filename

    def on_key_press(self, key_name: str):
        try:
            with open(self.filename, "a", encoding="utf-8") as file:
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"[{timestamp}] {key_name}\n")
        except IOError:
            pass


class KeyboardSpy:
    def __init__(self):
        self._listeners = []

    def attach(self, listener: KeyboardListener):
        if listener not in self._listeners:
            self._listeners.append(listener)

    def detach(self, listener: KeyboardListener):
        if listener in self._listeners:
            self._listeners.remove(listener)

    def notify(self, key_name: str):
        for listener in self._listeners:
            listener.on_key_press(key_name)

    def _callback(self, event):
        if event.event_type == keyboard.KEY_DOWN:
            self.notify(event.name)

    def start(self):
        print("Програму KeyboardSpy запущено.")
        print("Для завершення роботи натисніть комбінацію клавіш 'Ctrl+Q'...\n")
        keyboard.hook(self._callback)
        keyboard.wait('ctrl+q')
        keyboard.unhook_all()
        print("\nРоботу програми KeyboardSpy успішно завершено.")


if __name__ == "__main__":
    spy = KeyboardSpy()

    console_logger = KeyLogger()
    file_logger = KeyFileLogger("spy_output.txt")

    spy.attach(console_logger)
    spy.attach(file_logger)

    spy.start()