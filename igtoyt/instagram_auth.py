from pathlib import Path

import instaloader
import yt_dlp.cookies


class CookieExtractionError(Exception):
    pass


def extract_instagram_cookies_from_chrome() -> dict[str, str]:
    try:
        jar = yt_dlp.cookies.extract_cookies_from_browser("chrome")
    except Exception as exc:  # yt-dlp raises its own DownloadError on failure
        raise CookieExtractionError(f"could not read Chrome cookies: {exc}") from exc

    cookies = {
        cookie.name: cookie.value
        for cookie in jar
        if cookie.domain and "instagram.com" in cookie.domain and cookie.name in ("sessionid", "csrftoken")
    }
    if "sessionid" not in cookies or "csrftoken" not in cookies:
        raise CookieExtractionError(
            "Instagram sessionid/csrftoken not found in Chrome cookies "
            "(are you logged into instagram.com in Chrome?)"
        )
    return cookies


def load_cookies_from_netscape_file(path: Path) -> dict[str, str]:
    cookies: dict[str, str] = {}
    with Path(path).open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            fields = line.split("\t")
            if len(fields) < 7:
                continue
            name, value = fields[5], fields[6]
            if name in ("sessionid", "csrftoken"):
                cookies[name] = value
    return cookies


def build_authenticated_loader(cookies: dict[str, str]) -> instaloader.Instaloader:
    loader = instaloader.Instaloader()
    loader.context.load_session(username="_cookie_session_", sessiondata=cookies)
    return loader


def get_authenticated_loader(
    cookies_txt_path: Path | None = None,
    chrome_extractor=extract_instagram_cookies_from_chrome,
) -> instaloader.Instaloader:
    try:
        cookies = chrome_extractor()
    except CookieExtractionError:
        if cookies_txt_path is None:
            raise CookieExtractionError(
                "Could not read the Instagram session from Chrome. "
                "Export a cookies.txt (e.g. with the 'Get cookies.txt LOCALLY' "
                "Chrome extension, as described in DESIGN.md) and pass its path."
            )
        cookies = load_cookies_from_netscape_file(cookies_txt_path)

    return build_authenticated_loader(cookies)
