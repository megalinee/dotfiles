import subprocess
import sys

command = "hyprctl hyprpaper listactive"
current_wallpaper = subprocess.run([command, '-l'], shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
print(current_wallpaper)
if "DP-2 = /home/murad/.config/hypr/darkbg.jpg" in current_wallpaper:
    subprocess.run(["hyprctl hyprpaper wallpaper \"DP-1,/home/murad/.config/hypr/lightbg.jpg\"", '-l'], shell=True, stdout=subprocess.PIPE)
    subprocess.run(["hyprctl hyprpaper wallpaper \"DP-2,/home/murad/.config/hypr/lightbg.jpg\"", '-l'], shell=True, stdout=subprocess.PIPE)
else:
    subprocess.run(["hyprctl hyprpaper wallpaper \"DP-1,/home/murad/.config/hypr/darkbg.jpg\"", '-l'], shell=True, stdout=subprocess.PIPE)
    subprocess.run(["hyprctl hyprpaper wallpaper \"DP-2,/home/murad/.config/hypr/darkbg.jpg\"", '-l'], shell=True, stdout=subprocess.PIPE)