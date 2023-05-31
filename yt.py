import argparse
from ytdl_func import ytdl

def main():
    parser = argparse.ArgumentParser(description="Youtube download script")
    parser.add_argument('--list', help='Playlist options', action='store_true')
    parser.add_argument('playlist',nargs='?', help='Download all the videos of a youtube Playlist')
    parser.add_argument('-a', help='Download the audio tracks from a playlist')
    parser.add_argument('video', nargs='?', help='Download a youtube video')
    args = parser.parse_args()

    dp = "/home/abner/Downloads/yt-downloads"

    if args.list:
        if args.a:
            ytdl.download_playlist_audio_only(args.a, dp)
            print('\nDownload completed!')
        else:
            ytdl.download_playlist(args.playlist, dp)
            print('\nDone!')

    elif args.a:
        ytdl.download_audio(args.a, dp)
        print('\nDone!')

    else:
        ytdl.download_video(args.video, dp)
        print('\nDone!')


if __name__=="__main__":
    main()
