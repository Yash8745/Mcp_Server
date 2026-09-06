# MCP Server Practice

A small Python project I built to **practice and understand the Model Context Protocol (MCP)** and how to create MCP tools using `FastMCP`.

## Features

This server currently provides two weather tools using the **National Weather Service (NWS) API**:

* `get_alerts` — Get active weather alerts for a US state.
* `get_forecast` — Get a weather forecast for a location using latitude and longitude.

## Tech Stack

* Python 3.11
* MCP / FastMCP
* `httpx`
* National Weather Service API
* `uv`

## Running Locally

Install dependencies:

```bash
uv sync
```

Run the MCP server:

```bash
uv run main.py
```

The server uses **stdio transport**, so it can be connected to an MCP-compatible client such as Claude Desktop or another MCP client.

## Project Structure

```text
Mcp_Server/
├── main.py
├── src/
├── experiments/
├── test.py
├── pyproject.toml
├── uv.lock
└── README.md
```

## Purpose

This project was created as a **learning/practice project for MCP**, experimenting with:

* Creating MCP servers
* Defining MCP tools with `FastMCP`
* Calling external APIs from MCP tools
* Async Python
* Connecting MCP servers to AI clients

More tools and experiments may be added as I continue learning MCP.
