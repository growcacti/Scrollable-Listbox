# Scrollable-Listbox
Custom Widget
    ScrollableListbox Class:
        Inherits from tk.Frame, acting as a container for the Listbox and its vertical scrollbar.
        Designed to enhance a standard tk.Listbox with scrollability.

    Constructor (__init__):
        Initializes the ScrollableListbox by creating a tk.Listbox and an associated ttk.Scrollbar.
        Links the scrollbar to the listbox via the yscrollcommand property of the listbox and the command property of the scrollbar.

    Methods:
        insert(index, *elements): Inserts one or more elements into the listbox at the specified index.
        delete(start, end=None): Deletes one or more items from the listbox. If end is omitted, only the item at start is deleted.
        get(start, end=None): Retrieves one or more items from the listbox. If end is omitted, only the item at start is retrieved.
        bind(sequence, func, add=None): Binds an event sequence (e.g., <Double-Button-1>) to a callback function for the listbox.

    Example Usage:
        A simple GUI application is created in the if __name__ == "__main__": block.
        An instance of ScrollableListbox is created, added to the main application window (root), and populated with 100 items labeled "Item 1" through "Item 100".
        The listbox's size is defined by the height and width attributes passed during its creation.

    Scrollbar Behavior:
        The scrollbar enables vertical navigation through the items in the listbox when the number of items exceeds the visible area.


