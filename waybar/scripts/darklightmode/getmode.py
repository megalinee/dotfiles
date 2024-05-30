import subprocess
import sys

command = "hyprctl hyprpaper listactive"
current_wallpaper = subprocess.run([command, '-l'], shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
if "DP-2 = ~/.config/hypr/darkbg.jpg" in current_wallpaper:
    sys.stdout.write("")
else:
    sys.stdout.write("")