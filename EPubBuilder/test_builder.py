import os

from Builder import Builder

builder = Builder(os.path.join("..", "tests", "epubs"))


def test_make_container_folder():
    builder.make_container_folder("second_epub")
    epubs_list = os.listdir("../tests/epubs")
    assert "second_epub" in epubs_list


def test_make_meta_inf_folder():
    builder.make_container_folder("test_epub")
    builder.make_meta_inf_folder(builder.epub_container)
    meta_inf_path = builder.meta_inf_folder
    assert os.path.exists(meta_inf_path)


def test_make_opf_file():
    builder.make_opf_file()
    opf_file = os.path.join(builder.opf_container, builder.title+'.opf')
    assert os.path.exists(opf_file)


def test_create_template_html():
    builder.create_template_html()
    opf_folder = builder.opf_container
    book_path = os.path.join(opf_folder, "book.html")
    nav_path = os.path.join(opf_folder, "nav.html")
    assert os.path.exists(book_path) and os.path.exists(nav_path)


def test_make_epub():
    epub = builder.make_epub(builder.epub_container, builder.store_folder)
    assert os.path.exists(epub)
