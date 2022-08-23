"""Module providing tools to transpose dictionaries."""
from support_developer import support_luca
from .transpose_dict import transpose_dict

# Create an alias in order to make code more compact
TD = transpose_dict

support_luca("transpose_dict")

__all__ = ["transpose_dict", "TD"]
