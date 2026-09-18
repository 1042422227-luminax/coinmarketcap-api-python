from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cmcai_coverage_coin_object import CMCAICoverageCoinObject


T = TypeVar("T", bound="CMCAICoinsMapResultsObject")


@_attrs_define
class CMCAICoinsMapResultsObject:
    """Results of your query returned as an object.

    Example:
        {'coins': [{'crypto_id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'slug': 'bitcoin', 'url':
            'https://coinmarketcap.com/currencies/bitcoin/', 'available_question_keys': ['price_up', 'future_price',
            'latest_news', 'overview', 'roadmap', 'codebase'], 'num_insights': 8, 'last_generated_at':
            '2026-08-17T09:14:14Z'}, {'crypto_id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'url':
            'https://coinmarketcap.com/currencies/ethereum/', 'available_question_keys': ['price_down', 'future_price',
            'sentiment', 'overview', 'roadmap'], 'num_insights': 6, 'last_generated_at': '2026-08-17T09:10:03Z'},
            {'crypto_id': 825, 'name': 'Tether USDt', 'symbol': 'USDT', 'slug': 'tether', 'url':
            'https://coinmarketcap.com/currencies/tether/', 'available_question_keys': ['overview', 'latest_news'],
            'num_insights': 3, 'last_generated_at': '2026-08-16T21:04:00Z'}], 'total_size': 100, 'has_more': True}

    Attributes:
        coins (list[CMCAICoverageCoinObject] | Unset): Supported cryptocurrencies. Never a bare array at `data`.
        total_size (int | Unset): Total supported cryptocurrencies across all pages. Placed after the `coins[]` array.
            Example: 100.
        has_more (bool | Unset): `true` if more records exist beyond this page, else `false`. Placed after the `coins[]`
            array. Example: True.
    """

    coins: list[CMCAICoverageCoinObject] | Unset = UNSET
    total_size: int | Unset = UNSET
    has_more: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        coins: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.coins, Unset):
            coins = []
            for coins_item_data in self.coins:
                coins_item = coins_item_data.to_dict()
                coins.append(coins_item)

        total_size = self.total_size

        has_more = self.has_more

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if coins is not UNSET:
            field_dict["coins"] = coins
        if total_size is not UNSET:
            field_dict["total_size"] = total_size
        if has_more is not UNSET:
            field_dict["has_more"] = has_more

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cmcai_coverage_coin_object import CMCAICoverageCoinObject

        d = dict(src_dict)
        _coins = d.pop("coins", UNSET)
        coins: list[CMCAICoverageCoinObject] | Unset = UNSET
        if _coins is not UNSET:
            coins = []
            for coins_item_data in _coins:
                coins_item = CMCAICoverageCoinObject.from_dict(coins_item_data)

                coins.append(coins_item)

        total_size = d.pop("total_size", UNSET)

        has_more = d.pop("has_more", UNSET)

        cmcai_coins_map_results_object = cls(
            coins=coins,
            total_size=total_size,
            has_more=has_more,
        )

        cmcai_coins_map_results_object.additional_properties = d
        return cmcai_coins_map_results_object

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
