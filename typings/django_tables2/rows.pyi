"""
This type stub file was generated by pyright.
"""

class CellAccessor:
    """
    Allows accessing cell contents on a row object (see `BoundRow`)
    """
    def __init__(self, row) -> None: ...
    def __getitem__(self, key): ...
    def __getattr__(self, name): ...

class BoundRow:
    """
    Represents a *specific* row in a table.

    `.BoundRow` objects are a container that make it easy to access the
    final 'rendered' values for cells in a row. You can simply iterate over a
    `.BoundRow` object and it will take care to return values rendered
    using the correct method (e.g. :ref:`table.render_FOO`)

    To access the rendered value of each cell in a row, just iterate over it::

        >>> import django_tables2 as tables
        >>> class SimpleTable(tables.Table):
        ...     a = tables.Column()
        ...     b = tables.CheckBoxColumn(attrs={'name': 'my_chkbox'})
        ...
        >>> table = SimpleTable([{'a': 1, 'b': 2}])
        >>> row = table.rows[0]  # we only have one row, so let's use it
        >>> for cell in row:
        ...     print(cell)
        ...
        1
        <input type="checkbox" name="my_chkbox" value="2" />

    Alternatively you can use row.cells[0] to retrieve a specific cell::

        >>> row.cells[0]
        1
        >>> row.cells[1]
        '<input type="checkbox" name="my_chkbox" value="2" />'
        >>> row.cells[2]
        ...
        IndexError: list index out of range

    Finally you can also use the column names to retrieve a specific cell::

        >>> row.cells.a
        1
        >>> row.cells.b
        '<input type="checkbox" name="my_chkbox" value="2" />'
        >>> row.cells.c
        ...
        KeyError: "Column with name 'c' does not exist; choices are: ['a', 'b']"

    If you have the column name in a variable, you can also treat the `cells`
    property like a `dict`::

        >>> key = 'a'
        >>> row.cells[key]
        1

    Arguments:
        table: The `.Table` in which this row exists.
        record: a single record from the :term:`table data` that is used to
            populate the row. A record could be a `~django.db.Model` object, a
            `dict`, or something else.

    """
    def __init__(self, record, table) -> None: ...
    @property
    def table(self):  # -> Unknown:
        """The `.Table` this row is part of."""
        ...

    def get_even_odd_css_class(self):  # -> Literal['odd', 'even']:
        """
        Return css class, alternating for odd and even records.

        Return:
            string: `even` for even records, `odd` otherwise.
        """
        ...

    @property
    def attrs(self):  # -> AttributeDict:
        """Return the attributes for a certain row."""
        ...

    @property
    def record(self):  # -> Unknown:
        """The data record from the data source which is used to populate this row with data."""
        ...

    def __iter__(self):  # -> Generator[Unknown, Any, None]:
        """
        Iterate over the rendered values for cells in the row.

        Under the hood this method just makes a call to
        `.BoundRow.__getitem__` for each cell.
        """
        ...

    def get_cell(self, name):
        """
        Returns the final rendered html for a cell in the row, given the name
        of a column.
        """
        ...

    def get_cell_value(self, name):
        """
        Returns the final rendered value (excluding any html) for a cell in the
        row, given the name of a column.
        """
        ...

    def __contains__(self, item):  # -> bool:
        """
        Check by both row object and column name.
        """
        ...

    def items(self):  # -> Generator[tuple[Unknown, Unknown], Any, None]:
        """
        Returns iterator yielding ``(bound_column, cell)`` pairs.

        *cell* is ``row[name]`` -- the rendered unicode value that should be
        ``rendered within ``<td>``.
        """
        ...

class BoundPinnedRow(BoundRow):
    """
    Represents a *pinned* row in a table.
    """
    @property
    def attrs(self):  # -> AttributeDict:
        """
        Return the attributes for a certain pinned row.
        Add CSS classes `pinned-row` and `odd` or `even` to `class` attribute.

        Return:
            AttributeDict: Attributes for pinned rows.
        """
        ...

class BoundRows:
    """
    Container for spawning `.BoundRow` objects.

    Arguments:
        data: iterable of records
        table: the `~.Table` in which the rows exist
        pinned_data: dictionary with iterable of records for top and/or
         bottom pinned rows.

    Example:
        >>> pinned_data = {
        ...    'top': iterable,      # or None value
        ...    'bottom': iterable,   # or None value
        ... }

    This is used for `~.Table.rows`.
    """
    def __init__(self, data, table, pinned_data=...) -> None: ...
    def generator_pinned_row(self, data):  # -> Generator[BoundPinnedRow, Any, None]:
        """
        Top and bottom pinned rows generator.

        Arguments:
            data: Iterable data for all records for top or bottom pinned rows.

        Yields:
            BoundPinnedRow: Top or bottom `BoundPinnedRow` object for single pinned record.
        """
        ...

    def __iter__(self):  # -> Generator[BoundPinnedRow | BoundRow, Unknown, None]:
        ...
    def __len__(self):  # -> int:
        ...
    def __getitem__(self, key):  # -> BoundRows | BoundRow:
        """
        Slicing returns a new `~.BoundRows` instance, indexing returns a single
        `~.BoundRow` instance.
        """
        ...
