import tempfile
import argparse
import os
from pytube import Playlist, YouTube
from pydub import AudioSegment


def main():
    parser = argparse.ArgumentParser(description="Youtube download script")
    parser.add_argument('--list', help='Playlist options', action='store_true')
    parser.add_argument('-p', help='Download a youtube Playlist')
    parser.add_argument('-a', help='Download the audio tracks from a playlist')
    parser.add_argument('-v', help='Download a youtube video')
    args = parser.parse_args()

    dp = "/home/abner/Downloads/yt-downloads"

    if args.list:
        if args.a:
            download_playlist_audio_only(args.a, dp)
            print('Download completed!')
        elif args.p:
            download_playlist(args.p, dp)
            print('Done!')
    elif args.v:
        download_video(args.v, dp)
        print('Done!')
    else:
        download_video(args, dp)


def download_playlist(pl, dp):
    p = Playlist(pl)
    print(f'Downloading Playlist: {p.title}')
    playlist_dir = f'{dp}/{p.title}'
    os.mkdir(playlist_dir)
    for video in p.videos:
        video = video.streams.get_highest_resolution()
        video.download(playlist_dir)


def download_playlist_audio_only(pl, dp):
    p = Playlist(pl)
    playlist_dir = f'{dp}/{p.title}'
    os.mkdir(playlist_dir)
    print(f'Downloading audio playlist: {p.title}')
    with tempfile.TemporaryDirectory(dir=dp) as tempdir:
        for track in p.videos:
            audio = track.streams.get_audio_only()
            print(f'Downloading {audio.title}')
            audio.download(tempdir)
            print(f'Done!\nConverting {audio.title} to flac file')
            new_audio = AudioSegment.from_file(f'{tempdir}/{audio.title}.mp4')
            new_audio.export(f'{playlist_dir}/{track.title}.flac', format='flac')
            print('Done!')


def download_video(link, dp):
    vid = YouTube(link).streams.get_highest_resolution()
    print(f'Downloading: {vid.title}')
    vid.download(dp)


if __name__=="__main__":
    main()
