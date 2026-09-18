from typing import Literal, cast

CMCAIInsightObjectQuestionKeyType2Type1 = Literal[
    "altcoin_performance",
    "bullish_momentum",
    "codebase",
    "future_price",
    "kol_discussion",
    "latest_news",
    "market_sentiment",
    "overview",
    "price_down",
    "price_up",
    "roadmap",
    "sentiment",
    "trending_narratives",
    "upcoming_events",
]

CMCAI_INSIGHT_OBJECT_QUESTION_KEY_TYPE_2_TYPE_1_VALUES: set[CMCAIInsightObjectQuestionKeyType2Type1] = {
    "altcoin_performance",
    "bullish_momentum",
    "codebase",
    "future_price",
    "kol_discussion",
    "latest_news",
    "market_sentiment",
    "overview",
    "price_down",
    "price_up",
    "roadmap",
    "sentiment",
    "trending_narratives",
    "upcoming_events",
}


def check_cmcai_insight_object_question_key_type_2_type_1(value: str) -> CMCAIInsightObjectQuestionKeyType2Type1:
    if value in CMCAI_INSIGHT_OBJECT_QUESTION_KEY_TYPE_2_TYPE_1_VALUES:
        return cast(CMCAIInsightObjectQuestionKeyType2Type1, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CMCAI_INSIGHT_OBJECT_QUESTION_KEY_TYPE_2_TYPE_1_VALUES!r}"
    )
