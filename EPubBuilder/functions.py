import os


def make_mimetype_file(folder: str) -> str:
    """
    Creates a mimetype file in the specified folder.
    The mimetype file is required for EPUB files.
    """
    mimetype_path = os.path.join(folder, "mimetype")
    with open(mimetype_path, "w") as mimetype_file:
        mimetype_file.write("application/epub+zip")
    return mimetype_path
