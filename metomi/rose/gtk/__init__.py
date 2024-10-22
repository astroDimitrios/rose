try:
    import gi

    gi.require_version("Gtk", "3.0")
    from gi.repository import Gtk
except (ImportError, RuntimeError, AssertionError):
    INTERACTIVE_ENABLED = False
else:
    INTERACTIVE_ENABLED = True
