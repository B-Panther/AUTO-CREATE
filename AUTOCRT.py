import importlib

try:
    # Import the compiled Cython module
    AUTOREGFB = importlib.import_module("AUTOREGFB")
    print("✅ Module 'AUTOREGFB' imported successfully!")

    # List available attributes (functions, classes, etc.)
    attributes = dir(AUTOREGFB)
    print("\n📌 Available attributes in AUTOREGFB:")
    for attr in attributes:
        print(f" - {attr}")

    # Try calling 'main' or another function if it exists
    function_name = "main"  # Change if needed
    if hasattr(AUTOREGFB, function_name):
        print(f"\n▶️ Running {function_name} function...")
        getattr(AUTOREGFB, function_name)()
    else:
        print(f"⚠️ No '{function_name}' function found in AUTOREGFB.")
        print("❗ Try using a different function from the list above.")

except ImportError as e:
    print("❌ Error importing AUTOREGFB:", e)
