from .constants import CURRENT_VERSION as __version
from .constants import ENVIRONMENT as __env

version = f'v{__version}'
num_version = __version
environment = __env.get('long_desc', 'Unknown')


def generate_version() -> str:
    """Generates an API version"""
    return f'v{__version} [{__env.get("short_desc", "?")}]'


def description_generator(title: str,
                          description: str | None = None,
                          responses: dict[str, dict[str, str]] | None = None) -> str:
    """
    Response struct:
        {
            "200": {
                "description": "ok",
                "reason": "all ok"
            }
        }
    """
    desc = f"""# {title}"""
    desc += "\n---"
    if description:
        desc += f"\n {description}"
        desc += "\n---"

    if responses:
        desc += "\n## The below table defines the HTTP Status codes that this API may return"
        desc += "\n| Status Code | Description | Reason |"
        desc += "\n| ----------- | ----------- | ------ |"
        for response_code in responses.keys():
            response = responses[response_code]
            code_col = f"| {response_code} "
            desc_col = f"| {response.get('description', 'None')} "
            reas_col = f"| {response.get('reason', 'None')} |"
            resp_str = f"\n{code_col}{desc_col}{reas_col}"
            desc += resp_str

    return desc