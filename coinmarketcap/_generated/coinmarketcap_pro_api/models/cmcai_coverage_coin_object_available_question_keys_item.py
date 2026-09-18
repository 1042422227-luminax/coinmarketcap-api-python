from typing import Literal, cast

CMCAICoverageCoinObjectAvailableQuestionKeysItem = Literal[
    "codebase", "future_price", "latest_news", "overview", "price_down", "price_up", "roadmap", "sentiment"
]

CMCAI_COVERAGE_COIN_OBJECT_AVAILABLE_QUESTION_KEYS_ITEM_VALUES: set[
    CMCAICoverageCoinObjectAvailableQuestionKeysItem
] = {
    "codebase",
    "future_price",
    "latest_news",
    "overview",
    "price_down",
    "price_up",
    "roadmap",
    "sentiment",
}


def check_cmcai_coverage_coin_object_available_question_keys_item(
    value: str,
) -> CMCAICoverageCoinObjectAvailableQuestionKeysItem:
    if value in CMCAI_COVERAGE_COIN_OBJECT_AVAILABLE_QUESTION_KEYS_ITEM_VALUES:
        return cast(CMCAICoverageCoinObjectAvailableQuestionKeysItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CMCAI_COVERAGE_COIN_OBJECT_AVAILABLE_QUESTION_KEYS_ITEM_VALUES!r}"
    )
