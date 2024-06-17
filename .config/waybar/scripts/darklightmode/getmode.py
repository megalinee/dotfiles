import subprocess
import sys

command = "hyprctl hyprpaper listactive"
current_wallpaper = subprocess.run([command, '-l'], shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
if "darkbg.jpg" in current_wallpaper.split("\n")[0]:
    sys.stdout.write(" ")
else:
    sys.stdout.write("  ")
