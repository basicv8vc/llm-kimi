import llm


def test_plugin_is_installed():
    llm.get_model("m2")
