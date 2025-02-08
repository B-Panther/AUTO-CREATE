import ctypes
import os

# Get the absolute path to the shared library file
so_path = os.path.join(os.path.dirname(__file__), "AUTOREGFB.cpython-312.so")

# Load the shared object file
try:
    lib = ctypes.CDLL(so_path)
    print("✅ Shared library loaded successfully!")

    # List available functions in the .so file
    functions = [func for func in dir(lib) if not func.startswith("__")]
    
    if functions:
        print("\n📌 Available functions in AUTOREGFB.cpython-312.so:")
        for func in functions:
            print(f" - {func}")
    else:
        print("⚠️ No callable functions found in AUTOREGFB.cpython-312.so")

    # Attempt to call a function if it exists
    function_name = "main"  # Change this if the function name is different
    if hasattr(lib, function_name):
        print(f"\n▶️ Running {function_name} function...")
        getattr(lib, function_name)()
    else:
        print(f"⚠️ No '{function_name}' function found in AUTOREGFB.cpython-312.so")
        print("❗ Try using a different function name from the list above.")

except OSError as e:
    print("❌ Error loading shared library:", e)
