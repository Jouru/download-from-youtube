import argparse
from ytdl_func import ytdl


def main():
    parser = argparse.ArgumentParser(description="Youtube download script")
    subparsers = parser.add_subparsers(dest="command")
    list = subparsers.add_parser("list", help="Playlist options")
    list.add_argument("-v", help="Download youtube video playlists")
    list.add_argument("-a", help="Download youtube audio playlists")
    parser.add_argument("-v", help="Download youtube video playlists")
    parser.add_argument("-a", help="Download youtube audio playlist")
    args = parser.parse_args()

    dp = "/home/abner/Downloads/yt-downloads"

    if args.command == "list":
        if args.a:
            ytdl.download_playlist_audio_only(args.a, dp)
            print("\nDownload completed!")
        elif args.v:
            ytdl.download_playlist(args.v, dp)
            print("\nDone!")

    elif args.a:
        ytdl.download_audio(args.a, dp)
        print("\nDone!")

    elif args.v:
        ytdl.download_video(args.v, dp)
        print("\nDone!")


if __name__ == "__main__":
    main()
