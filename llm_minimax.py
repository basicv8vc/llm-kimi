import llm
from llm_anthropic import ClaudeMessages, AsyncClaudeMessages


class MiniMax(ClaudeMessages):
    needs_key = "minimax"
    key_env_var = "MINIMAX_API_KEY"

    def __str__(self):
        return "MiniMax: {}".format(self.model_id)


class AsyncMiniMax(AsyncClaudeMessages):
    needs_key = "minimax"
    key_env_var = "MINIMAX_API_KEY"

    def __str__(self):
        return "MiniMax: {}".format(self.model_id)


@llm.hookimpl
def register_models(register):
    register(
        MiniMax("MiniMax-M2", base_url="https://api.minimax.io/anthropic"),
        AsyncMiniMax("MiniMax-M2", base_url="https://api.minimax.io/anthropic"),
        aliases=("m2",),
    )
    register(
        MiniMax("MiniMax-M1", base_url="https://api.minimax.io/anthropic"),
        AsyncMiniMax("MiniMax-M1", base_url="https://api.minimax.io/anthropic"),
        aliases=("m1",),
    )
