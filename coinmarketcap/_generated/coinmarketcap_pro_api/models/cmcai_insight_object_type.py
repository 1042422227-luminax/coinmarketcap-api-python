from typing import Literal, cast

CMCAIInsightObjectType = Literal["fixed_question", "top_news", "trending_question"]

CMCAI_INSIGHT_OBJECT_TYPE_VALUES: set[CMCAIInsightObjectType] = {
    "fixed_question",
    "top_news",
    "trending_question",
}


def check_cmcai_insight_object_type(value: str) -> CMCAIInsightObjectType:
    if value in CMCAI_INSIGHT_OBJECT_TYPE_VALUES:
        return cast(CMCAIInsightObjectType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CMCAI_INSIGHT_OBJECT_TYPE_VALUES!r}")
