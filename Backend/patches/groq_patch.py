"""
Temporary compatibility patch.

Reason:
CrewAI 1.15.2 sends `cache_breakpoint`
which is not supported by the Groq API.

Remove this patch after CrewAI officially fixes the issue.
"""
import litellm
from copy import deepcopy

_original_completion = litellm.completion


def _patched_completion(*args, **kwargs):
    if "messages" in kwargs:
        messages = deepcopy(kwargs["messages"])

        for message in messages:
            if isinstance(message, dict):
                message.pop("cache_breakpoint", None)

        kwargs["messages"] = messages

    return _original_completion(*args, **kwargs)


def apply_patch():
    litellm.completion = _patched_completion