from langchain_core.tools import tool


@tool
def call_sanjay_tool() -> str:
    return "Sanjay is busy right now. Please try again later."

@tool
def call_subash_tool() -> str:
    return "Subash is Available"