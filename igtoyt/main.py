from dataclasses import dataclass, field
from pathlib import Path

from igtoyt.identify_song import identify_song, shazamio_recognize
from igtoyt.instagram_auth import get_authenticated_loader
from igtoyt.instagram_saved import iter_saved_posts
from igtoyt.processed_store import ProcessedStore
from igtoyt.youtube_auth import get_youtube_client
from igtoyt.youtube_playlist import add_video_to_playlist, ensure_playlist
from igtoyt.youtube_search import real_ytdlp_extractor, search_youtube

PLAYLIST_TITLE = "Músicas do Instagram"
DOWNLOAD_DIR = Path("data")
CLIENT_SECRET_PATH = Path("client_secret.json")
TOKEN_PATH = Path("token.json")
PROCESSED_PATH = Path("processed.json")
COOKIES_TXT_PATH = Path("cookies.txt")


@dataclass
class Report:
    added: list[str] = field(default_factory=list)
    guessed: list[str] = field(default_factory=list)
    skipped_photos: list[str] = field(default_factory=list)
    not_identified: list[str] = field(default_factory=list)
    not_found_on_youtube: list[str] = field(default_factory=list)


def run_pipeline(store, youtube, playlist_id, download_dir, saved_posts, identify, search, add_to_playlist) -> Report:
    report = Report()

    for post in saved_posts:
        if store.is_post_processed(post.shortcode):
            continue

        if not post.is_video:
            report.skipped_photos.append(post.shortcode)
            store.mark(post.shortcode, "skipped_photo", None)
            continue

        match = identify(post, post.video_path)
        if match is None:
            report.not_identified.append(post.shortcode)
            store.mark(post.shortcode, "not_identified", None)
            continue

        video = search(match.query)
        if video is None:
            report.not_found_on_youtube.append(post.shortcode)
            store.mark(post.shortcode, "not_found_on_youtube", None)
            continue

        add_to_playlist(youtube, playlist_id, video.video_id, store)

        if match.confidence == "exact":
            report.added.append(post.shortcode)
            store.mark(post.shortcode, "added", video.video_id)
        else:
            report.guessed.append(post.shortcode)
            store.mark(post.shortcode, "guessed", video.video_id)

    return report


def main() -> None:
    loader = get_authenticated_loader(
        cookies_txt_path=COOKIES_TXT_PATH if COOKIES_TXT_PATH.exists() else None
    )
    youtube = get_youtube_client(CLIENT_SECRET_PATH, TOKEN_PATH)
    playlist_id = ensure_playlist(youtube, PLAYLIST_TITLE)
    store = ProcessedStore.load(PROCESSED_PATH)

    saved_posts = iter_saved_posts(loader, DOWNLOAD_DIR)

    def identify(post, video_path):
        return identify_song(post, video_path, shazamio_recognize)

    def search(query):
        return search_youtube(query, real_ytdlp_extractor)

    report = run_pipeline(store, youtube, playlist_id, DOWNLOAD_DIR, saved_posts, identify, search, add_video_to_playlist)
    store.save(PROCESSED_PATH)

    print(f"Adicionadas: {len(report.added)}")
    print(f"Adicionadas por palpite (confira): {len(report.guessed)}")
    print(f"Fotos ignoradas: {len(report.skipped_photos)}")
    print(f"Não identificadas: {len(report.not_identified)}")
    print(f"Não encontradas no YouTube: {len(report.not_found_on_youtube)}")


if __name__ == "__main__":
    main()
