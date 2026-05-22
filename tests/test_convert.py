import pytest

from src.convert import convert_markdown


def test_convert_simple_heading():
    md = "# Başlık\n\nParagraf"
    html = convert_markdown(md)
    assert "<h1>" in html and "Başlık" in html


def test_convert_code_block():
    md = "```
print('hello')
```"
    html = convert_markdown(md)
    assert "<code" in html or "<pre" in html
