import os

import llm
from llm_anthropic import AsyncClaudeMessages, ClaudeMessages


DEFAULT_BASE_URLS = {
    "china": "https://api.moonshot.cn/anthropic",
    "cn": "https://api.moonshot.cn/anthropic",
    "global": "https://api.moonshot.ai/anthropic",
    "intl": "https://api.moonshot.ai/anthropic",
}


class Kimi(ClaudeMessages):
    needs_key = "kimi"
    key_env_var = "KIMI_API_KEY"

    def __init__(self, model_id, base_url=None):
        super().__init__(model_id, base_url=base_url or kimi_base_url())

    def __str__(self):
        return "Kimi: {}".format(self.model_id)


class AsyncKimi(AsyncClaudeMessages):
    needs_key = "kimi"
    key_env_var = "KIMI_API_KEY"

    def __init__(self, model_id, base_url=None):
        super().__init__(model_id, base_url=base_url or kimi_base_url())

    def __str__(self):
        return "Kimi: {}".format(self.model_id)


def kimi_base_url():
    region = os.environ.get("KIMI_REGION", "china").lower()
    return DEFAULT_BASE_URLS.get(region, DEFAULT_BASE_URLS["china"])


@llm.hookimpl
def register_models(register):
    models = [
        ("kimi-k2-0905-preview", ("k2-0905-preview",)),
        ("kimi-k2-0711-preview", ("k2-0711-preview",)),
        ("kimi-k2-turbo-preview", ("k2-turbo-preview",)),
        ("kimi-k2-thinking", ("k2-thinking",)),
        ("kimi-k2-thinking-turbo", ("k2-thinking-turbo",)),
    ]
    for model_id, aliases in models:
        register(
            Kimi(model_id),
            AsyncKimi(model_id),
            aliases=aliases,
        )
