import os
from zipfile import ZipFile, ZIP_DEFLATED
import pathlib


TEMPLATE_FOLDER = "./templates"


def copy_template_html(folder: str) -> bool:
    book_file = os.path.join(TEMPLATE_FOLDER, 'book.html')
    nav_file = os.path.join(TEMPLATE_FOLDER, "nav.html")

    try:
        temp_var = {'book.html': book_file, 'nav.html': nav_file}
        for x in enumerate(temp_var):

            with open(temp_var[x[1]], 'r') as read_file:
                read_contents = read_file.read()
            with open(os.path.join(folder, x[1]), 'w') as write_f:
                write_f.write(read_contents)
        return True
    except Exception as e:
        print(e)
        return False


def make_mimetype_file(folder: str) -> str:
    """
    Creates a mimetype file in the specified folder.
    The mimetype file is required for EPUB files.
    """
    mimetype_path = os.path.join(folder, "mimetype")
    with open(mimetype_path, "w") as mimetype_file:
        mimetype_file.write("application/epub+zip")
    return mimetype_path


def make_container_xml(folder: str) -> bool:
    """
    Creates a container.xml file in the specified folder.
    This file is part of the EPUB structure.
    """

    try:
        xml_template_file = os.path.join(TEMPLATE_FOLDER, 'container.xml')
        with open(xml_template_file, 'r') as xml_file:
            xml_content = xml_file.read()

        container_file_path = os.path.join(folder, "container.xml")
        with open(container_file_path, "w") as container_file:
            container_file.write(xml_content.strip())

        return True
    except Exception as e:
        print(e)
        return False


def make_opf_file(folder: str, title: str) -> str:

    opf_template_file = os.path.join(TEMPLATE_FOLDER, 'title.opf')
    with open(opf_template_file, 'r') as opf_f:
        template_content = opf_f.read()

    opf_content = template_content.replace("{{title}}", title)

    opf_file = os.path.join(folder, title + ".opf")
    with open(opf_file, "w") as f:
        f.write(opf_content.strip())

    return opf_file


def make_zip(source_folder: str, store_path: str):
    directory = pathlib.Path(source_folder)

    try:
        with ZipFile(
            store_path, 'w', ZIP_DEFLATED, compresslevel=8) as zip_file:
            for filename in directory.rglob("*"):
                zip_file.write(
                    filename, arcname=filename.relative_to(directory))
        return store_path
    except Exception as e:
        print(e)
        return False
