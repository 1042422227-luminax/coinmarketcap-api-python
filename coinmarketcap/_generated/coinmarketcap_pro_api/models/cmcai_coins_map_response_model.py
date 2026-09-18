from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.cmcai_coins_map_results_object import CMCAICoinsMapResultsObject


T = TypeVar("T", bound="CMCAICoinsMapResponseModel")


@_attrs_define
class CMCAICoinsMapResponseModel:
    """
    Attributes:
        data (CMCAICoinsMapResultsObject): Results of your query returned as an object. Example: {'coins':
            [{'crypto_id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'slug': 'bitcoin', 'url':
            'https://coinmarketcap.com/currencies/bitcoin/', 'available_question_keys': ['price_up', 'future_price',
            'latest_news', 'overview', 'roadmap', 'codebase'], 'num_insights': 8, 'last_generated_at':
            '2026-08-17T09:14:14Z'}, {'crypto_id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'url':
            'https://coinmarketcap.com/currencies/ethereum/', 'available_question_keys': ['price_down', 'future_price',
            'sentiment', 'overview', 'roadmap'], 'num_insights': 6, 'last_generated_at': '2026-08-17T09:10:03Z'},
            {'crypto_id': 825, 'name': 'Tether USDt', 'symbol': 'USDT', 'slug': 'tether', 'url':
            'https://coinmarketcap.com/currencies/tether/', 'available_question_keys': ['overview', 'latest_news'],
            'num_insights': 3, 'last_generated_at': '2026-08-16T21:04:00Z'}], 'total_size': 100, 'has_more': True}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: CMCAICoinsMapResultsObject
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
        from ..models.cmcai_coins_map_results_object import CMCAICoinsMapResultsObject

        d = dict(src_dict)
        data = CMCAICoinsMapResultsObject.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        cmcai_coins_map_response_model = cls(
            data=data,
            status=status,
        )

        cmcai_coins_map_response_model.additional_properties = d
        return cmcai_coins_map_response_model

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
