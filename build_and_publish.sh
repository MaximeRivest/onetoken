#!/bin/bash
set -e

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Cleaning up previous builds...${NC}"
rm -rf dist/ build/ src/*.egg-info

echo -e "${YELLOW}Installing build dependencies...${NC}"
pip install --upgrade pip build twine

echo -e "${YELLOW}Building package...${NC}"
python -m build

echo -e "${GREEN}Build completed successfully!${NC}"
echo -e "Distribution files:"
ls -lh dist/

echo -e "\n${YELLOW}Do you want to publish to PyPI? (y/n)${NC}"
read publish_choice

if [ "$publish_choice" = "y" ]; then
    echo -e "${YELLOW}Do you want to upload to Test PyPI first? (y/n)${NC}"
    read test_pypi_choice
    
    if [ "$test_pypi_choice" = "y" ]; then
        echo -e "${YELLOW}Uploading to Test PyPI...${NC}"
        python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
        echo -e "${GREEN}Uploaded to Test PyPI successfully!${NC}"
        echo -e "You can install the test version with:"
        echo -e "pip install --index-url https://test.pypi.org/simple/ onetokenpy"
    fi

    echo -e "${YELLOW}Uploading to PyPI...${NC}"
    python -m twine upload dist/*
    echo -e "${GREEN}Upload completed successfully!${NC}"
else
    echo -e "${YELLOW}Skipping PyPI upload.${NC}"
fi 