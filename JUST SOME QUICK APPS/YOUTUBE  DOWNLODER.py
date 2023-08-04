import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from pytube import YouTube

def get_file_size(bytes):
    # Convert bytes to MB
    return bytes / (1024 * 1024)

def get_video_length(seconds):
    # Convert video length in seconds to hours, minutes, and seconds
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return hours, minutes, seconds

def download_youtube_video():
    url = url_entry.get()
    choice = resolution_var.get()

    try:
        yt = YouTube(url)
        video_stream = None

        if choice == 1:
            video_stream = yt.streams.filter(res="720p", file_extension="mp4").first()
        elif choice == 2:
            video_stream = yt.streams.filter(res="360p", file_extension="mp4").first()
        else:
            messagebox.showerror("Error", "Invalid choice.")
            return

        if video_stream is None:
            messagebox.showerror("Error", "Selected video quality is not available. Please try another quality.")
            return

        # Ask user to select the download location
        destination_path = filedialog.askdirectory()

        if not destination_path:
            return  # User canceled, do not proceed with the download

        # Create a new window to display video details
        details_window = tk.Toplevel()
        details_window.title("Video Details")

        # Get the size and duration of the video
        file_size = get_file_size(video_stream.filesize)
        hours, minutes, seconds = get_video_length(yt.length)

        # Display video details
        video_info = f"Video Title: {yt.title}\nVideo Duration: {hours} hours, {minutes} minutes, {seconds} seconds\nVideo Size: {file_size:.2f} MB\nDownload Location: {destination_path}"
        info_label = tk.Label(details_window, text=video_info, wraplength=400, justify='left')
        info_label.pack(padx=20, pady=20)

        # Ask for confirmation
        def confirm_download():
            video_stream.download(output_path=destination_path)
            messagebox.showinfo("Download Complete", "Video download complete!")
            details_window.destroy()

        confirm_button = tk.Button(details_window, text="Confirm Download", command=confirm_download)
        confirm_button.pack(pady=10)

    except Exception as e:
        messagebox.showerror("Error", "An error occurred: " + str(e))

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Calculate the x and y position for the window to be centered
window_width = 500
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# Set the window size and position
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_position, y_position))

# Create URL entry field
url_label = tk.Label(root, text="Enter YouTube Video URL:")
url_label.pack(pady=10)
url_entry = tk.Entry(root, width=40)
url_entry.pack(pady=5)

# Create resolution choice options
resolution_label = tk.Label(root, text="Select Video Resolution:")
resolution_label.pack(pady=5)
resolution_var = tk.IntVar()
resolution_var.set(1)
resolution_choices = [
    ("Standard Quality (720p)", 1),
    ("Low Quality (360p)", 2)
]

for text, val in resolution_choices:
    resolution_radio = tk.Radiobutton(root, text=text, variable=resolution_var, value=val)
    resolution_radio.pack(anchor=tk.W)

# Create download button
download_button = tk.Button(root, text="Download", command=download_youtube_video)
download_button.pack(pady=10)

# Start the main event loop
root.mainloop()
# next step is make these app to exe file and make it more user friendly