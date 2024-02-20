"""
This type stub file was generated by pyright.
"""

from .base import library
from .linkcolumn import BaseLinkColumn

@library.register
class FileColumn(BaseLinkColumn):
    """
    Attempts to render `.FieldFile` (or other storage backend `.File`) as a
    hyperlink.

    When the file is accessible via a URL, the file is rendered as a
    hyperlink. The `.basename` is used as the text, wrapped in a span::

        <a href="/media/path/to/receipt.pdf" title="path/to/receipt.pdf">receipt.pdf</a>

    When unable to determine the URL, a ``span`` is used instead::

        <span title="path/to/receipt.pdf" class>receipt.pdf</span>

    `.Column.attrs` keys ``a`` and ``span`` can be used to add additional attributes.

    Arguments:
        verify_exists (bool): attempt to determine if the file exists
            If *verify_exists*, the HTML class ``exists`` or ``missing`` is
            added to the element to indicate the integrity of the storage.
        text (str or callable): Either static text, or a callable. If set, this
            will be used to render the text inside the link instead of
            the file's ``basename`` (default)
    """
    def __init__(self, verify_exists=..., **kwargs) -> None: ...
    def get_url(self, value, record):  # -> Any | None:
        ...
    def text_value(self, record, value): ...
    def render(self, record, value):  # -> SafeText:
        ...
    @classmethod
    def from_field(cls, field, **kwargs):  # -> Self@FileColumn | None:
        ...
