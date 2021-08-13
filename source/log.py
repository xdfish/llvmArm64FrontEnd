from datetime import datetime
import os.path

export_log = False

def log(module: str, msg: str):
    """
    This Function is used for a log-like output with timestamp

    :param module: Name of the module, the log was triggered from
    :type module: str
    :param msg: Message for the output
    :type msg: str
    """
    
    text = "{}:\t\t{}\n".format(module, msg)
    print(text)
    if export_log:
        export_log(text)

def export_log(txt: str):
    """exports the log output from log() in a text-file.

    :param txt: text added to the file
    :type txt: str
    """

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    directory = "../tmp"
    if not os.path.exists(directory):
        os.makedirs(directory)
    f = open(directory + "/log.txt", "a")
    f.write("{} \t {}".format(now, txt))
    f.close()