from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.cmcai_latest_results_object import CMCAILatestResultsObject


T = TypeVar("T", bound="CMCAILatestResponseModel")


@_attrs_define
class CMCAILatestResponseModel:
    r"""
    Attributes:
        data (CMCAILatestResultsObject): Results of your query returned as an object. Example: {'insights': [{'type':
            'fixed_question', 'title': 'What are the trending narratives?', 'answer_id': '6a82d003e66d8e4bf5368dcf',
            'question_key': 'trending_narratives', 'answer': {'tldr': '## TLDR\nAI, RWA, and ETF-flow narratives are leading
            attention this session, while meme-coin volume has cooled.', 'body': '## Deep Dive\nBitcoin dominance is steady
            and sector rotation is concentrated in a handful of large-cap themes.\n\n## Conclusion\nWatch BTC dominance and
            spot-ETF flows into the next session.'}, 'sources': [{'url': 'https://coinmarketcap.com/trending-
            cryptocurrencies/'}, {'url': 'https://x.com/coinmarketcap'}], 'sources_count': 91, 'sources_truncated': True,
            'generated_at': '2026-08-17T09:11:37Z'}, {'type': 'top_news', 'title': 'BTC stuck near $63K as US spot ETFs see
            $390M outflows', 'answer_id': '6a829ec8e210dd5a1b8f0570', 'question_key': None, 'answer': {'tldr': '## TLDR\nUS
            spot Bitcoin ETFs posted another session of net outflows, keeping BTC range-bound.', 'body': '## Deep
            Dive\nSpot-ETF flow is the near-term driver. A return to net inflows would be the first sign the range is
            breaking.\n\n## Conclusion\nPrice is waiting on flow, not a new macro catalyst.'}, 'sources': [{'url':
            'https://cryptopotato.com/btc-etf-outflows-august'}], 'sources_count': 27, 'sources_truncated': True,
            'generated_at': '2026-08-17T05:40:24Z'}], 'total_size': 26, 'has_more': True}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: CMCAILatestResultsObject
    status: APIStatusObject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_status_object import APIStatusObject
        from ..models.cmcai_latest_results_object import CMCAILatestResultsObject

        d = dict(src_dict)
        data = CMCAILatestResultsObject.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        cmcai_latest_response_model = cls(
            data=data,
            status=status,
        )

        cmcai_latest_response_model.additional_properties = d
        return cmcai_latest_response_model

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
