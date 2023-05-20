# This script will walk the whole OS & delete all 802.11 capture files that have been modified in the last # of days.

# MUST BE RUN WITH SUDO PRIVLEDGES! 

import os
import time

# Define the extensions of the files you want to delete
extensions = ('.kismet', '.pcap', '.cap', '.pcapng', '.kismet-journal')
print(" ")
print(" ")
print("Hey there, your mom doesn't live here... Let's clean up!")
print(" ")

# Prompt the user for the number of days before deleting the files
days = int(input("Delete WiFi capture files from the last how many days?: "))
print(" ")

# Define the time threshold for file deletion (in seconds)
time_threshold = time.time() - (days * 24 * 60 * 60)

# Define a function to walk through the directory tree and delete files with the given extensions
def delete_files():
    for root, dirs, files in os.walk('/'):
        for file in files:
            filename, extension = os.path.splitext(file)
            if extension in extensions:
                file_path = os.path.join(root, file)
                file_mod_time = os.path.getmtime(file_path)
                if file_mod_time >= time_threshold:
                    os.remove(file_path)
                    print(f'Deleted file: {file_path}')
    print(" ")
    print("         _nnnn_       ,---------------------------------.")
    print("        dGGGGMMb      | Remember kids, life is short!   |")
    print("       @p~qp~~qMb     |     Get good at command line.   |")
    print("       M|@||@) M|   _;.---------------------------------'")
    print("       @,----.JM| -'")
    print("      JS^\__/  qKL")
    print("     dZP        qKRb")
    print("    dZP          qKKb")
    print("   fZP            SMMb")
    print("   HZM            MMMM")
    print("   FqM            MMMM")
    print(" __| '.        |\dSoqML")
    print(" |    `.       | `' \Zq")
    print("_)      \.___.,|     .'")
    print("\____   )MMMMMM|   .'")
    print("     `-'       `--'")
    print(" ")
    print("~~~ Thank you for cleaning up all your dirty packets! ~~~")
	  print(" ")

# Call the function to start deleting the files
delete_files()
