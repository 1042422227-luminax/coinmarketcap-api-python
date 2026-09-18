from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.cmcai_insight_object_question_key_type_1 import (
    CMCAIInsightObjectQuestionKeyType1,
    check_cmcai_insight_object_question_key_type_1,
)
from ..models.cmcai_insight_object_question_key_type_2_type_1 import (
    CMCAIInsightObjectQuestionKeyType2Type1,
    check_cmcai_insight_object_question_key_type_2_type_1,
)
from ..models.cmcai_insight_object_question_key_type_3_type_1 import (
    CMCAIInsightObjectQuestionKeyType3Type1,
    check_cmcai_insight_object_question_key_type_3_type_1,
)
from ..models.cmcai_insight_object_type import CMCAIInsightObjectType, check_cmcai_insight_object_type

if TYPE_CHECKING:
    from ..models.cmcai_answer_object import CMCAIAnswerObject
    from ..models.cmcai_source_object import CMCAISourceObject


T = TypeVar("T", bound="CMCAIInsightObject")


@_attrs_define
class CMCAIInsightObject:
    """A single CMC AI insight: a fixed question, a trending question, or a top-news headline, plus its generated answer
    and sources.

        Attributes:
            type_ (CMCAIInsightObjectType): Insight type. One of `fixed_question`, `trending_question`, `top_news`. Never
                empty. Example: fixed_question.
            title (str): Display text: the question for `fixed_question`, the headline for `trending_question` and
                `top_news`. Never empty. Example: What are the trending narratives?.
            answer_id (str): 24-character hex id for this generated answer. Changes on regeneration, so a caller can detect
                content that needs re-translation. For `trending_question` and `top_news` it is also the item id. Never empty.
                Example: 6a82d003e66d8e4bf5368dcf.
            question_key (CMCAIInsightObjectQuestionKeyType1 | CMCAIInsightObjectQuestionKeyType2Type1 |
                CMCAIInsightObjectQuestionKeyType3Type1 | None): Stable semantic key for the question template. Set for
                `fixed_question`, `null` for `trending_question` and `top_news`. Market-level keys (on `/v5/cmc-ai/latest`):
                `altcoin_performance`, `trending_narratives`, `bullish_momentum`, `upcoming_events`, `market_sentiment`,
                `kol_discussion`. Coin-level keys (on `/v5/cmc-ai/coins/latest`): `price_up`, `price_down`, `future_price`,
                `sentiment`, `latest_news`, `overview`, `roadmap`, `codebase`. `price_up` and `price_down` are mutually
                exclusive. Example: trending_narratives.
            answer (CMCAIAnswerObject): Two-section markdown answer, split from the stored blob using the same TLDR
                detection as the CoinMarketCap front end. No other edits are applied.
            sources (list[CMCAISourceObject]): Source references, capped by `sources_limit`. May be empty.
            sources_count (int): True total sources for this insight, before `sources_limit` is applied. Example: 91.
            sources_truncated (bool): `true` if `sources[]` has fewer entries than `sources_count`. Example: True.
            generated_at (datetime.datetime): ISO 8601 UTC time the answer was generated. Never empty. Example:
                2026-08-17T09:11:37Z.
    """

    type_: CMCAIInsightObjectType
    title: str
    answer_id: str
    question_key: (
        CMCAIInsightObjectQuestionKeyType1
        | CMCAIInsightObjectQuestionKeyType2Type1
        | CMCAIInsightObjectQuestionKeyType3Type1
        | None
    )
    answer: CMCAIAnswerObject
    sources: list[CMCAISourceObject]
    sources_count: int
    sources_truncated: bool
    generated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        title = self.title

        answer_id = self.answer_id

        question_key: None | str
        if isinstance(self.question_key, str):
            question_key = self.question_key
        elif isinstance(self.question_key, str):
            question_key = self.question_key
        elif isinstance(self.question_key, str):
            question_key = self.question_key
        else:
            question_key = self.question_key

        answer = self.answer.to_dict()

        sources = []
        for sources_item_data in self.sources:
            sources_item = sources_item_data.to_dict()
            sources.append(sources_item)

        sources_count = self.sources_count

        sources_truncated = self.sources_truncated

        generated_at = self.generated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "title": title,
                "answer_id": answer_id,
                "question_key": question_key,
                "answer": answer,
                "sources": sources,
                "sources_count": sources_count,
                "sources_truncated": sources_truncated,
                "generated_at": generated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cmcai_answer_object import CMCAIAnswerObject
        from ..models.cmcai_source_object import CMCAISourceObject

        d = dict(src_dict)
        type_ = check_cmcai_insight_object_type(d.pop("type"))

        title = d.pop("title")

        answer_id = d.pop("answer_id")

        def _parse_question_key(
            data: object,
        ) -> (
            CMCAIInsightObjectQuestionKeyType1
            | CMCAIInsightObjectQuestionKeyType2Type1
            | CMCAIInsightObjectQuestionKeyType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                question_key_type_1 = check_cmcai_insight_object_question_key_type_1(data)

                return question_key_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                question_key_type_2_type_1 = check_cmcai_insight_object_question_key_type_2_type_1(data)

                return question_key_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                question_key_type_3_type_1 = check_cmcai_insight_object_question_key_type_3_type_1(data)

                return question_key_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CMCAIInsightObjectQuestionKeyType1
                | CMCAIInsightObjectQuestionKeyType2Type1
                | CMCAIInsightObjectQuestionKeyType3Type1
                | None,
                data,
            )

        question_key = _parse_question_key(d.pop("question_key"))

        answer = CMCAIAnswerObject.from_dict(d.pop("answer"))

        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = CMCAISourceObject.from_dict(sources_item_data)

            sources.append(sources_item)

        sources_count = d.pop("sources_count")

        sources_truncated = d.pop("sources_truncated")

        generated_at = isoparse(d.pop("generated_at"))

        cmcai_insight_object = cls(
            type_=type_,
            title=title,
            answer_id=answer_id,
            question_key=question_key,
            answer=answer,
            sources=sources,
            sources_count=sources_count,
            sources_truncated=sources_truncated,
            generated_at=generated_at,
        )

        cmcai_insight_object.additional_properties = d
        return cmcai_insight_object

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
