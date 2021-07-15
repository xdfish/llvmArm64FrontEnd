from datetime import datetime

export_log = False

def log(module, msg):
    text = "{}:\t\t{}\n".format(module, msg)
    print(text)
    if export_log:
        export_log(text)

def export_log(txt):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    f = open("tmp/log.txt", "a")
    f.write("{} \t {}".format(now, txt))
    f.close()