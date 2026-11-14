import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator, Optional

import instaloader


@dataclass
class SavedPost:
    shortcode: str
    caption: str
    hashtags: list[str]
    is_video: bool
    video_path: Optional[Path]
    audio_title: Optional[str]
    audio_artist: Optional[str]


def _music_attribution(post) -> tuple[Optional[str], Optional[str]]:
    metadata = getattr(post, "_full_metadata", None) or {}
    music = metadata.get("clips_music_attribution_info")
    if not music:
        return None, None
    return music.get("song_name"), music.get("artist_name")


def iter_saved_posts(
    loader: Optional[instaloader.Instaloader],
    download_dir: Path,
    delay_seconds: float = 3.0,
    posts_iterable=None,
) -> Iterator[SavedPost]:
    posts = posts_iterable if posts_iterable is not None else instaloader.Profile.own_profile(loader.context).get_saved_posts()

    for post in posts:
        audio_title, audio_artist = _music_attribution(post)
        video_path = None
        if post.is_video:
            if posts_iterable is None:
                loader.download_post(post, target=download_dir)
                video_path = Path(download_dir) / f"{post.shortcode}.mp4"

        yield SavedPost(
            shortcode=post.shortcode,
            caption=post.caption or "",
            hashtags=list(post.caption_hashtags),
            is_video=post.is_video,
            video_path=video_path,
            audio_title=audio_title,
            audio_artist=audio_artist,
        )

        if posts_iterable is None and delay_seconds:
            time.sleep(delay_seconds)
