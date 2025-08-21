import os

from Builder import Builder

builder = Builder("../tests/epubs")


def test_make_container_folder():
    builder.make_container_folder("second_epub")
    epubs_list = os.listdir("../tests/epubs")
    assert "second_epub" in epubs_list


def test_make_meta_inf_folder():
    builder.make_container_folder("third_epub")
    builder.make_meta_inf_folder(builder.epub_container)
    meta_inf_path = builder.meta_inf_folder
    assert os.path.exists(meta_inf_path)
