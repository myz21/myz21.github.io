from pathlib import Path

from bs4 import BeautifulSoup

FILES = [
    "index.html",
    "about.html",
    "journey.html",
    "voluntary.html",
    "awards.html",
    "art.html",
    "captures.html",
    "projects.html",
]


def ensure_head(path: Path) -> None:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")

    if soup.html is None:
        return

    if soup.head is None:
        head = soup.new_tag("head")
        body = soup.body
        movable = []
        for child in list(soup.html.children):
            if child == head or child == body:
                continue
            movable.append(child)
        for child in movable:
            head.append(child.extract())
        soup.html.insert(0, head)

    for tag in list(soup.head.find_all("link", href="assets/styles/main.css")):
        tag.decompose()

    link = soup.new_tag("link", rel="stylesheet", href="assets/styles/main.css")
    soup.head.append(link)

    path.write_text(str(soup), encoding="utf-8")


for file_name in FILES:
    ensure_head(Path(file_name))
    print(f"updated: {file_name}")
