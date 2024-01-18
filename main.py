import os
import threading
from program.secure_drop_shell import Global_SecureDropShell
from program.send import start_listener
from registration_utilities.log_in_file import log_in
from registration_utilities.sign_up_file import sign_up


user_exists = os.path.exists("data.json")

if user_exists: 
    log_in()
    listener_thread = threading.Thread(target=start_listener)
    listener_thread.daemon = True
    listener_thread.start()
    shell_thread = threading.Thread(target=Global_SecureDropShell.run)
    shell_thread.start()


        #print("\nPAUSING*************")
    #Global_SecureDropShell.pause()
    
else:
    sign_up()
#else go to create user
