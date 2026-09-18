from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cmcai_insight_object import CMCAIInsightObject


T = TypeVar("T", bound="CMCAILatestResultsObject")


@_attrs_define
class CMCAILatestResultsObject:
    r"""Results of your query returned as an object.

    Example:
        {'insights': [{'type': 'fixed_question', 'title': 'What are the trending narratives?', 'answer_id':
            '6a82d003e66d8e4bf5368dcf', 'question_key': 'trending_narratives', 'answer': {'tldr': '## TLDR\nAI, RWA, and
            ETF-flow narratives are leading attention this session, while meme-coin volume has cooled.', 'body': '## Deep
            Dive\nBitcoin dominance is steady and sector rotation is concentrated in a handful of large-cap themes.\n\n##
            Conclusion\nWatch BTC dominance and spot-ETF flows into the next session.'}, 'sources': [{'url':
            'https://coinmarketcap.com/trending-cryptocurrencies/'}, {'url': 'https://x.com/coinmarketcap'}],
            'sources_count': 91, 'sources_truncated': True, 'generated_at': '2026-08-17T09:11:37Z'}, {'type': 'top_news',
            'title': 'BTC stuck near $63K as US spot ETFs see $390M outflows', 'answer_id': '6a829ec8e210dd5a1b8f0570',
            'question_key': None, 'answer': {'tldr': '## TLDR\nUS spot Bitcoin ETFs posted another session of net outflows,
            keeping BTC range-bound.', 'body': '## Deep Dive\nSpot-ETF flow is the near-term driver. A return to net inflows
            would be the first sign the range is breaking.\n\n## Conclusion\nPrice is waiting on flow, not a new macro
            catalyst.'}, 'sources': [{'url': 'https://cryptopotato.com/btc-etf-outflows-august'}], 'sources_count': 27,
            'sources_truncated': True, 'generated_at': '2026-08-17T05:40:24Z'}], 'total_size': 26, 'has_more': True}

    Attributes:
        insights (list[CMCAIInsightObject] | Unset): Insight objects. Never a bare array at `data`.
        total_size (int | Unset): Total matching insights across all pages. Placed after the `insights[]` array.
            Example: 26.
        has_more (bool | Unset): `true` if more insights exist beyond this page, else `false`. Placed after the
            `insights[]` array. Example: True.
    """

    insights: list[CMCAIInsightObject] | Unset = UNSET
    total_size: int | Unset = UNSET
    has_more: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        insights: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.insights, Unset):
            insights = []
            for insights_item_data in self.insights:
                insights_item = insights_item_data.to_dict()
                insights.append(insights_item)

        total_size = self.total_size

        has_more = self.has_more

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if insights is not UNSET:
            field_dict["insights"] = insights
        if total_size is not UNSET:
            field_dict["total_size"] = total_size
        if has_more is not UNSET:
            field_dict["has_more"] = has_more

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cmcai_insight_object import CMCAIInsightObject

        d = dict(src_dict)
        _insights = d.pop("insights", UNSET)
        insights: list[CMCAIInsightObject] | Unset = UNSET
        if _insights is not UNSET:
            insights = []
            for insights_item_data in _insights:
                insights_item = CMCAIInsightObject.from_dict(insights_item_data)

                insights.append(insights_item)

        total_size = d.pop("total_size", UNSET)

        has_more = d.pop("has_more", UNSET)

        cmcai_latest_results_object = cls(
            insights=insights,
            total_size=total_size,
            has_more=has_more,
        )

        cmcai_latest_results_object.additional_properties = d
        return cmcai_latest_results_object

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
