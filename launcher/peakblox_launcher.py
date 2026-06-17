import tkinter as tk
from tkinter import messagebox
import webbrowser
import requests
import os

def main():
    root = tk.Tk()
    root.title("PeakBlox Launcher")
    root.geometry("600x400")
    root.configure(bg='#0a0a0a')

    tk.Label(root, text="PEAKBLOX", font=("Arial", 24, "bold"), fg="#ff4d4d", bg='#0a0a0a').pack(pady=20)
    tk.Label(root, text="Classic Roblox Revival", font=("Arial", 14), fg="#fff", bg='#0a0a0a').pack(pady=10)

    def launch_game():
        messagebox.showinfo("Launching", "Connecting to PeakBlox servers...\n\n(Integrate with Novetus or Rboxlo2 here)")
        # Example: webbrowser.open('http://localhost:3000')

    def open_studio():
        webbrowser.open('http://localhost:3000/#studio')

    tk.Button(root, text="Play Classic Games", command=launch_game, bg="#ff4d4d", fg="white", font=("Arial", 12), width=30, height=2).pack(pady=10)
    tk.Button(root, text="Open PeakBlox Studio", command=open_studio, bg="#00cc00", fg="white", font=("Arial", 12), width=30, height=2).pack(pady=10)
    tk.Button(root, text="Join Discord", command=lambda: webbrowser.open('https://discord.gg/peakblox'), bg="#7289da", fg="white", font=("Arial", 12), width=30, height=2).pack(pady=10)

    tk.Label(root, text="Version 0.2 • Made for Windows", fg="#666", bg='#0a0a0a').pack(side="bottom", pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()