# ai-agent

A small CLI-based AI coding agent, built while working through Boot.dev's
["Build an AI Agent in Python"](https://www.boot.dev/courses/build-ai-agent-python)
course. It sends your prompt to an LLM (via [OpenRouter](https://openrouter.ai)),
and the model can call a set of sandboxed tools to explore and modify a target
codebase in order to answer questions or complete tasks.

## How it works

`main.py` runs an agent loop:

1. Your prompt is sent to the model along with the available tool schemas.
2. If the model requests a tool call (e.g. "list files in `pkg/`"), the agent
   executes it for real and feeds the result back to the model.
3. This repeats (up to 20 iterations) until the model responds with a final
   answer instead of another tool call.

All tool calls are restricted to a single working directory (currently
hardcoded to `./calculator` in [functions/call_function.py](functions/call_function.py))
so the agent can't read or write files outside of it.

## Setup

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

1. Install dependencies:
   ```bash
   uv sync
   ```
2. Create a `.env` file in the project root with your OpenRouter API key:
   ```
   OPENROUTER_API_KEY=your-key-here
   ```

## Usage

```bash
uv run main.py "your prompt here"
```

Add `--verbose` to also print the prompt, token usage, and each tool call's
raw result:

```bash
uv run main.py "how does the calculator render results to the console?" --verbose
```

## Available tools

The agent can call these functions against the working directory
(see [functions/](functions/)):

- `get_files_info` — list files/subdirectories, with size and type
- `get_file_content` — read a file's contents (truncated after `MAX_CHARS`, see [config.py](config.py))
- `write_file` — create or overwrite a file
- `run_python_file` — execute a Python file and capture its stdout/stderr

## Project structure

```
main.py                    CLI entrypoint and agent loop
prompts.py                 System prompt
config.py                  Shared config (e.g. MAX_CHARS)
functions/                 Tool implementations + schemas + dispatcher
calculator/                Sample project the agent operates on
```
