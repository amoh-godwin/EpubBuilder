import os
import pytest

from Builder import Builder
import functions


def test_make_container_folder():
    builder = Builder("../tests/epubs")
    _ = builder.make_container_folder("second_epub")
    epubs_list = os.listdir("../tests/epubs")
    assert "second_epub" in epubs_list
