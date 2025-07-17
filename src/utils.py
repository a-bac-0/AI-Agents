"""
Helper functions for the multi-agent system
"""

def get_platforms():
    return ["blog", "twitter", "linkedin", "instagram"]

def format_output(content: str, image: str = None) -> str:
    if image:
        return f"{content}\n\nImage: {image}"
    return content
