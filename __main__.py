from src.cli import cli
from src.oas import scrape_songs

if __name__ == "__main__":
    args = cli().parse_args()

    scrape_songs(
        src=f"{args.osu}//Songs",
        dest=args.dest
    )
