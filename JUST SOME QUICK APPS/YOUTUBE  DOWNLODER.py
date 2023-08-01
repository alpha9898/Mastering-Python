from pytube import YouTube

def get_file_size(bytes):
    # Convert bytes to MB
    return bytes / (1024 * 1024)

def get_video_length(seconds):
    # Convert video length in seconds to hours, minutes, and seconds
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return hours, minutes, seconds

def download_youtube_video(url):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get video details
        video_title = yt.title
        video_duration_seconds = yt.length

        # Display video details
        print("Video Title:", video_title)

        # Get video length in hours, minutes, and seconds
        hours, minutes, seconds = get_video_length(video_duration_seconds)
        print("Video Duration: {} hours, {} minutes, {} seconds".format(hours, minutes, seconds))

        print("Available Video Resolutions:")
        for stream in yt.streams.filter(only_video=True, file_extension="mp4"):
            print(stream.resolution)

        # Ask for the desired video quality
        print("\nSelect the desired video quality:")
        print("1. High Quality (1080p)")
        print("2. Standard Quality (720p)")
        print("3. Low Quality (360p)")
        choice = int(input("Enter your choice (1, 2, or 3): "))

        # Choose the appropriate stream
        if choice == 1:
            video_stream = yt.streams.filter(res="1080p", file_extension="mp4").first()
        elif choice == 2:
            video_stream = yt.streams.filter(res="720p", file_extension="mp4").first()
        elif choice == 3:
            video_stream = yt.streams.filter(res="360p", file_extension="mp4").first()
        else:
            print("Invalid choice.")
            return

        if video_stream is None:
            print("Selected video quality is not available. Please try another quality.")
            return

        # Get the size of the video in MB
        file_size = get_file_size(video_stream.filesize)

        # Display video size
        print("Video Size:", f"{file_size:.2f} MB")

        # Ask for confirmation
        confirm = input("Do you want to proceed with the download? (yes/no): ")
        if confirm.lower() != "yes":
            print("Download canceled.")
            return

        # Set the destination path on the D: drive
        destination_path = "D:"

        # Download the video
        print("Downloading...")
        video_stream.download(output_path=destination_path)
        print("Download complete!")
    except KeyboardInterrupt:
        print("Download canceled by user.")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_youtube_video(video_url)
