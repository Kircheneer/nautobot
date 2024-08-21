"""
This type stub file was generated by pyright.
"""

from .base import library
from .linkcolumn import BaseLinkColumn

"""
This type stub file was generated by pyright.
"""
POSTGRES_AVAILABLE = ...
@library.register
class JSONColumn(BaseLinkColumn):
    """
    Render the contents of `~django.contrib.postgres.fields.JSONField` or
    `~django.contrib.postgres.fields.HStoreField` as an indented string.

    .. versionadded :: 1.5.0

    .. note::

        Automatic rendering of data to this column requires PostgreSQL support
        (psycopg2 installed) to import the fields, but this column can also be
        used manually without it.

    Arguments:
        json_dumps_kwargs: kwargs passed to `json.dumps`, defaults to `{'indent': 2}`
        attrs (dict): In addition to *attrs* keys supported by `~.Column`, the
            following are available:

             - ``pre`` -- ``<pre>`` around the rendered JSON string in ``<td>`` elements.

    """
    def __init__(self, json_dumps_kwargs=..., **kwargs) -> None:
        ...
    
    def render(self, record, value):
        ...
    
    @classmethod
    def from_field(cls, field, **kwargs):
        ...
    


