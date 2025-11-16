# llm-kimi

[![PyPI](https://img.shields.io/pypi/v/llm-kimi.svg)](https://pypi.org/project/llm-kimi/)
[![Changelog](https://img.shields.io/github/v/release/basicv8vc/llm-kimi?include_prereleases&label=changelog)](https://github.com/basicv8vc/llm-kimi/releases)
[![Tests](https://github.com/basicv8vc/llm-kimi/actions/workflows/test.yml/badge.svg)](https://github.com/basicv8vc/llm-kimi/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/basicv8vc/llm-kimi/blob/main/LICENSE)

LLM plugin for accessing the Kimi (Moonshot) models via their Anthropics-compatible API.

## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/).
```bash
git clone https://github.com/basicv8vc/llm-kimi
cd llm-kimi
llm install -e .
```
## Usage

Obtain an API key for Kimi from their [China developer platform](https://platform.moonshot.cn/) or [Global developer platform](https://platform.moonshot.ai/docs/overview).

Set the API key using:
```bash
llm keys set kimi
# Paste key here
```
Run the k2-thinking model like this:
```bash
llm -m k2-thinking "Solve 12 + 30"
```

Available model aliases:

- `k2-thinking`
- `k2-thinking-turbo`
- `k2-0905-preview`
- `k2-0711-preview`
- `k2-turbo-preview`


### Choosing the API endpoint

The plugin talks to the China endpoint (`https://api.moonshot.cn/anthropic`) by default.  
Set `KIMI_REGION=global` to automatically switch to `https://api.moonshot.us/anthropic`, or specify any custom URL with `KIMI_BASE_URL`.

```bash
# Use the global endpoint
export KIMI_REGION=global
```
## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd llm-kimi
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
python -m pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
