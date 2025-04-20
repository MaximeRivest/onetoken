#!/bin/bash
set -e

# Clean build directories
rm -rf build/ dist/ *.egg-info/

# Install build dependencies
pip install --upgrade pip setuptools wheel build twine

# Build the package using PEP517
echo "Building package..."
python -m build

# Manually check the built distributions
echo "Checking distributions..."
twine check dist/*

# Prompt for upload
echo ""
read -p "Do you want to upload to PyPI? (y/n): " upload_choice

if [[ $upload_choice == "y" ]]; then
  echo "Uploading to PyPI..."
  twine upload dist/*
  echo "Package published to PyPI successfully!"
else
  echo "Upload skipped."
fi

echo "Generated files:"
ls -la dist/ 