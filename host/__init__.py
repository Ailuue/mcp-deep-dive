"""The LLM-driven side of MCP: a host that lets a model call MCP tools.

Everything in here is needed ONLY for the LLM-in-the-loop sections (8 + the
capstone). The offline examples (the protocol, your first server, the client,
resources, prompts, the multi-tool server) never import this package.
"""
