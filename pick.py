def take_pick(root):
    from PIL import ImageGrab

    # Get the dimensions of the Tkinter window
    x = root.winfo_rootx()
    y = root.winfo_rooty()
    width = root.winfo_width()
    height = root.winfo_height()

    # Take a screenshot of the Tkinter window
    screenshot = ImageGrab.grab((x, y, x + width, y + height))

    # Specify the output image file name
    output_file = "tkinter_screenshot.png"

    # Save the screenshot as an image file
    screenshot.save(output_file)
    print(f"Screenshot saved as '{output_file}'")