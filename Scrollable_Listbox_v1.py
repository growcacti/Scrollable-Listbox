import tkinter as tk
from tkinter import ttk

class ScrollableListbox(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        
        # Create the Listbox
        self.listbox = tk.Listbox(self, **kwargs)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Create the Scrollbar
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Connect the Scrollbar to the Listbox
        self.listbox.configure(yscrollcommand=self.scrollbar.set)
        
    def insert(self, index, *elements):
        """Insert elements into the Listbox."""
        self.listbox.insert(index, *elements)
    
    def delete(self, start, end=None):
        """Delete items from the Listbox."""
        self.listbox.delete(start, end)
    
    def get(self, start, end=None):
        """Get items from the Listbox."""
        return self.listbox.get(start, end)
    
    def bind(self, sequence, func, add=None):
        """Bind events to the Listbox."""
        self.listbox.bind(sequence, func, add)

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Custom Scrollable Listbox")
    
    scrollable_listbox = ScrollableListbox(root, height=10, width=40)
    scrollable_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    
    # Add some items to the Listbox
    for i in range(1, 101):
        scrollable_listbox.insert(tk.END, f"Item {i}")
    
    root.mainloop()

