import os
from pytube import Playlist, YouTube
from pytube.cli import on_progress
from pydub import AudioSegment

class ytdl:
    @staticmethod
    def download_playlist(pl, dp):
        """Download all the videos in a playlist from youtube"""
        # Create a Playlist object and create a directory named as the playlist's name
        p = Playlist(pl)
        playlist_dir = f'{dp}/{p.title.replace("/", "")}'
        os.mkdir(playlist_dir)
        print(f'Downloading Playlist: {p.title}, {p.length} videos', end='\r')

        # Download every single file from the playlist
        for video in p.video_urls:
            ytdl.download_video(video, playlist_dir)

    @staticmethod
    def download_video(url, dp):
        """Download a video from youtube"""
        vid = YouTube(url, on_progress_callback=on_progress).streams.get_highest_resolution()
        print(f'\nDownloading: {vid.title} {vid.filesize_mb} MB')
        vid.download(dp)


    @staticmethod
    def download_playlist_audio_only(pl, dp):
        """Download all the audio tracks in a playlist from youtube"""
        # Create a Playlist object and create a directory named as the playlist's name
        p = Playlist(pl)
        playlist_dir = f'{dp}/{p.title.replace("/", "")}'
        os.mkdir(playlist_dir)
        print(f'Downloading audio playlist: {p.title}, {p.length} tracks', end='\r')

        # Download every single track from the playlist
        for track in p.video_urls:
            ytdl.download_audio(track, playlist_dir)

    @staticmethod
    def download_audio(url, output_path):
        """Download the audio from a youtube video"""
        # Create a youtube object and download it as mp4 file
        audio = YouTube(url, on_progress_callback=on_progress).streams.get_audio_only()
        print(f'\nDownloading: {audio.title} {audio.filesize_mb} MB')
        name = audio.title.replace("/","")
        audio.download(output_path,filename=name)

        # Convert the mp4 file to a flac file
        AudioSegment.from_file(f'{output_path}/{name}').export(f'{output_path}/{name}.flac', format='flac')
        os.remove(f'{output_path}/{name}')


    @staticmethod
    def on_progress(stream, chunk, bytes_remaining):
        """Callback function"""
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        pct_completed = bytes_downloaded / total_size * 100
        print(f"\nStatus: {round(pct_completed, 2)} %")


