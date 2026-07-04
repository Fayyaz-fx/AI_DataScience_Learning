from app import demo

# Validate that the Gradio Blocks interface constructs without error
try:
    assert demo is not None
    print("Gradio UI constructed successfully.")
except Exception as e:
    print(f"Error during construction: {e}")