import ctypes
import os

# Get the absolute path to the .so file
so_path = os.path.join(os.path.dirname(__file__), "AUTOREGFB.cpython-312.so")

# Load the shared object file
try:
    lib = ctypes.CDLL(so_path)
    print("Shared library loaded successfully!")

    # If there's a function inside the .so file (e.g., "main"), call it:
    if hasattr(lib, "main"):
        lib.main()
    else:
        print("No 'main' function found in AUTOREGFB.cpython-312.so")

except OSError as e:
    print("Error loading shared library:", e)
