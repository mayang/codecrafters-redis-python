import threading

class Store:
    def __init__():
        self.store = {}

    def get(key):
        try:
            val = self.store[key.decode()] 
        except:
            return b"$-1\r\n"

        val_len = len(val)
        return f"${val_len}\r\n{val}\r\n".encode() 

    def set(key, val, opt = None, arg = None):
        self.store[key.decode()] = val.decode()
       
        if arg != None and (opt.upper() == b"EX" or opt.upper() == b"PX"):
            time = int(arg.decode())
            if opt  == b"PX":
                time = time / 1000
            print('wait')
            print(time)
            t = threading.Timer(time, lambda key: self.store.pop(key), args=(key.decode(),))
            t.start()

        return b"+OK\r\n"
