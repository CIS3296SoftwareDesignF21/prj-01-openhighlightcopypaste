import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='openHighlightCopyPaste',
    version="1.0.0a1",
    description="Program to extract highlighted text from images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CIS3296SoftwareDesignF21/prj-01-openhighlightcopypaste",
    author="Bri McCaffrey, Cecily Devaney, Shivani Patel",
    license="Apache",
    py_modules=['ScannerWorker', 'main'],
    packages=setuptools.find_packages(),
    install_requires=['Pillow', 'pytesseract', 'opencv-python'],
    python_requires=">=3.6",
)
