import subprocess
import sys

command = "pactl get-default-sink"
current_device = subprocess.run([command, '-l'], shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
if "FiiO" in current_device.split("\n")[0]:
    subprocess.run(["pactl set-default-sink alsa_output.usb-Razer_Razer_Nommo_Chroma-02.analog-stereo", '-l'], shell=True, stdout=subprocess.PIPE)
else:
    subprocess.run(["pactl set-default-sink alsa_output.usb-FiiO_DigiHug_USB_Audio-01.analog-stereo", '-l'], shell=True, stdout=subprocess.PIPE)
