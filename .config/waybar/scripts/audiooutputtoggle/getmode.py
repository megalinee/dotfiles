import subprocess
import sys

command = "pactl get-default-sink"
current_device = subprocess.run([command, '-l'], shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
if "FiiO" in current_device.split("\n")[0]:
    sys.stdout.write("  ")
else:
    sys.stdout.write("󰓃")
