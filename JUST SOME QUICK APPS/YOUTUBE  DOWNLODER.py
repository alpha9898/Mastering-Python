import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from pytube import YouTube


def set_common_window_properties(window, width, height, bg_color):
    # Calculate the x and y position for the window to be centered
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_position = (screen_width - width) // 2
    y_position = (screen_height - height) // 2

    # Set the window size and position
    window.geometry("{}x{}+{}+{}".format(width, height, x_position, y_position))

    # Set the window background color
    window.configure(bg=bg_color)


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
        set_common_window_properties(details_window, 500, 300, "#241468")

        # Get the size and duration of the video
        file_size = get_file_size(video_stream.filesize)
        hours, minutes, seconds = get_video_length(yt.length)

        # Display video details
        video_info = f"Video Title: {yt.title}\nVideo Duration: {hours} hours, {minutes} minutes, {seconds} seconds\nVideo Size: {file_size:.2f} MB\nDownload Location: {destination_path}"
        info_label = tk.Label(details_window, text=video_info, font=("Arial", 14), wraplength=400, justify='left')
        info_label.pack(padx=20, pady=20)

        # Ask for confirmation
        def confirm_download():
            video_stream.download(output_path=destination_path)
            messagebox.showinfo("Download Complete", "Video download complete!")
            details_window.destroy()

        confirm_button = tk.Button(details_window, text="Confirm Download", font=("Arial", 14), bg="#9F0D7F",
                                   fg="white", command=confirm_download)
        confirm_button.pack(pady=10)

    except Exception as e:
        messagebox.showerror("Error", "An error occurred: " + str(e))


# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")
set_common_window_properties(root, 600, 300, "#241468")

# Create URL entry field
url_label = tk.Label(root, text="Enter YouTube Video URL:", font=("Arial", 16), bg="#241468", fg="white")
url_label.pack(pady=10)
url_entry = tk.Entry(root, width=50, font=("Arial", 14))
url_entry.pack(pady=5)

# Create resolution choice options
resolution_label = tk.Label(root, text="Select Video Resolution:", font=("Arial", 16), bg="#241468", fg="white")
resolution_label.pack(pady=5)
resolution_var = tk.IntVar()
resolution_var.set(1)
resolution_choices = [
    ("Standard Quality (720p)", 1),
    ("Low Quality (360p)", 2)
]

for text, val in resolution_choices:
    resolution_radio = tk.Radiobutton(root, text=text, variable=resolution_var, value=val, font=("Arial", 14),
                                      bg="#241468", fg="white", selectcolor="#EA1179")
    resolution_radio.pack(anchor=tk.W)

# Create download button
download_button = tk.Button(root, text="Download", font=("Arial", 16), bg="#9F0D7F", fg="white",
                            command=download_youtube_video)
download_button.pack(pady=10)

# Start the main event loop
root.mainloop()
# todo: and also add some more features like download playlist and download audio only
# todo: next step is make these app to exe file and make it more user friendly