import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from pytube import YouTube, Playlist

def get_file_size(bytes):
    # Convert bytes to MB
    return bytes / (1024 * 1024)

def get_video_length(seconds):
    # Convert video length in seconds to hours, minutes, and seconds
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return hours, minutes, seconds

def choose_destination_folder():
    global destination_path
    destination_path = filedialog.askdirectory()

def show_video_details(yt):
    video_stream = yt.streams.filter(res="720p", file_extension="mp4").first()

    if video_stream is None:
        messagebox.showerror("Error", "Selected video quality is not available. Please try another quality.")
        return

    # Create a new window to display video details
    video_details_window = tk.Toplevel(root)
    video_details_window.title("Video Details")

    # Get the size and duration of the video
    file_size = get_file_size(video_stream.filesize)
    hours, minutes, seconds = get_video_length(yt.length)

    # Display video details
    video_info = f"Video Title: {yt.title}\nVideo Duration: {hours} hours, {minutes} minutes, {seconds} seconds\nVideo Size: {file_size:.2f} MB"
    video_info_label = tk.Label(video_details_window, text=video_info, font=("Arial", 12), wraplength=400, justify='left', bg="#241468", fg="white")
    video_info_label.pack(padx=20, pady=20)

    # Ask for confirmation for the single video download
    def confirm_download():
        if destination_path:
            video_stream.download(output_path=destination_path)
            messagebox.showinfo("Download Complete", "Video download complete!")
        else:
            messagebox.showwarning("Warning", "Please choose a destination folder before downloading the video.")

        video_details_window.destroy()

    confirm_button = tk.Button(video_details_window, text="Confirm Download", font=("Arial", 14), bg="#EA1179", fg="white", command=confirm_download)
    confirm_button.pack(pady=10)

def download_single_video():
    video_url = url_entry.get()
    try:
        yt = YouTube(video_url)
        show_video_details(yt)
    except Exception as e:
        messagebox.showerror("Error", "An error occurred: " + str(e))

def download_all_videos_in_playlist(playlist):
    if destination_path:
        for url in playlist.video_urls:
            yt = YouTube(url)
            video_stream = yt.streams.filter(res="720p", file_extension="mp4").first()
            if video_stream:
                video_stream.download(output_path=destination_path)
        messagebox.showinfo("Download Complete", "All videos in the playlist have been downloaded!")
    else:
        messagebox.showwarning("Warning", "Please choose a destination folder before downloading the videos.")

def download_playlist():
    playlist_url = url_entry.get()
    try:
        pl = Playlist(playlist_url)
        video_details_window = tk.Toplevel(root)
        video_details_window.title("Playlist Details")

        # Create a LabelFrame for each video in the playlist
        for url in pl.video_urls:
            yt = YouTube(url)

            # Create a LabelFrame for the video details
            video_frame = tk.LabelFrame(video_details_window, text=f"Video Title: {yt.title}", font=("Arial", 14), bg="#241468", fg="white")
            video_frame.pack(padx=20, pady=10, fill="both", expand=True)

            # Get the size and duration of the video
            file_size = get_file_size(yt.streams.filter(res="720p", file_extension="mp4").first().filesize)
            hours, minutes, seconds = get_video_length(yt.length)

            # Display video details for each video in the playlist
            video_info = f"Video Duration: {hours} hours, {minutes} minutes, {seconds} seconds\nVideo Size: {file_size:.2f} MB"
            video_info_label = tk.Label(video_frame, text=video_info, font=("Arial", 12), wraplength=400, justify='left', bg="#241468", fg="white")
            video_info_label.pack(padx=20, pady=5)

            # Download button for each video
            download_button = tk.Button(video_frame, text="Download", font=("Arial", 14), bg="#9F0D7F", fg="white", command=lambda yt=yt: show_video_details(yt))
            download_button.pack(pady=10)

        # Download All Videos button
        download_all_button = tk.Button(video_details_window, text="Download All Videos", font=("Arial", 14), bg="#9F0D7F", fg="white", command=lambda: download_all_videos_in_playlist(pl))
        download_all_button.pack(pady=10)

    except Exception as e:
        messagebox.showerror("Error", "An error occurred: " + str(e))

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("600x400")

# Set the window background color to #241468 (royal blue)
root.configure(bg="#241468")

# Create URL entry field
url_label = tk.Label(root, text="Enter YouTube Video URL or Playlist URL:", font=("Arial", 14), bg="#241468", fg="white")
url_label.pack(pady=10)
url_entry = tk.Entry(root, width=50, font=("Arial", 12))
url_entry.pack(pady=5)

# Create resolution choice options
resolution_label = tk.Label(root, text="Select Video Resolution:", font=("Arial", 14), bg="#241468", fg="white")
resolution_label.pack(pady=5)
resolution_var = tk.IntVar()
resolution_var.set(1)
resolution_choices = [
    ("Standard Quality (720p)", 1),
    ("Low Quality (360p)", 2)
]

for text, val in resolution_choices:
    resolution_radio = tk.Radiobutton(root, text=text, variable=resolution_var, value=val, font=("Arial", 12), bg="#241468", fg="white", selectcolor="#EA1179")
    resolution_radio.pack(anchor=tk.W)

# Create destination folder button
destination_folder_button = tk.Button(root, text="Choose Destination Folder", font=("Arial", 14), bg="#F79BD3", fg="white", command=choose_destination_folder)
destination_folder_button.pack(pady=5)

destination_path = ""

# Create download single video button
download_single_button = tk.Button(root, text="Download Single Video", font=("Arial", 14), bg="#EA1179", fg="white", command=download_single_video)
download_single_button.pack(pady=10)

# Create download playlist button
download_playlist_button = tk.Button(root, text="Download Playlist", font=("Arial", 14), bg="#EA1179", fg="white", command=download_playlist)
download_playlist_button.pack(pady=10)

# Start the main event loop
root.mainloop()
<<<<<<< HEAD
# todo: and also add some more features like download playlist and download audio only
# todo: next step is make these app to exe file and make it more user friendly
=======

# todo : add download playlist
# todo : add download audio only
# todo : add download video only
# todo : add download thumbnail
# todo : add download subtitle
# todo : add download progress bar
# todo : add download speed
# todo : add download percentage
# todo : add download time remaining
# todo : add download time elapsed
# todo : add download time total
# todo : add download cancel button
# todo : add download pause button
# todo : add download resume button
# todo : make these app to exe file   https://www.youtube.com/watch?v=UZX5kH72Yx4
# todo : make icon for the app
# todo : make the app responsive
# todo : make the app look better
# ***************(done)****************