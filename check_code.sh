#!/bin/bash
set -e

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Installing dev dependencies...${NC}"
pip install -e ".[dev]"

echo -e "\n${YELLOW}Running black (code formatting check)...${NC}"
black --check src tests

echo -e "\n${YELLOW}Running isort (import sorting check)...${NC}"
isort --check-only src tests

echo -e "\n${YELLOW}Running ruff (linting)...${NC}"
ruff check src tests

echo -e "\n${YELLOW}Running mypy (type checking)...${NC}"
mypy src

echo -e "\n${YELLOW}Running pytest (unit tests)...${NC}"
pytest tests -v

echo -e "\n${GREEN}All checks completed successfully!${NC}" 