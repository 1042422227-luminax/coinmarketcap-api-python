from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cmcai_coin_object import CMCAICoinObject


T = TypeVar("T", bound="CMCAICoinsLatestResultsObject")


@_attrs_define
class CMCAICoinsLatestResultsObject:
    r"""Results of your query returned as an object.

    Example:
        {'coins': [{'crypto_id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'slug': 'bitcoin', 'insights': [{'type':
            'fixed_question', 'title': "Why is BTC's price up today?", 'answer_id': '6a82d0abe24562528cd3f6ac',
            'question_key': 'price_up', 'answer': {'tldr': '## TLDR\nBitcoin bounced as US spot-ETF outflows slowed and
            funding rates reset closer to neutral.', 'body': '## Deep Dive\nThe move is a relief bounce inside a broader
            range, not a confirmed trend reversal.\n\n## Conclusion\nHold the range until ETF flows turn sustainably
            positive.'}, 'sources': [{'url': 'https://coinmarketcap.com/currencies/bitcoin/'}], 'sources_count': 57,
            'sources_truncated': True, 'generated_at': '2026-08-17T09:14:14Z'}, {'type': 'fixed_question', 'title': "What
            could affect BTC's future price?", 'answer_id': '6a82d11c9c0e4a1bb7e2c401', 'question_key': 'future_price',
            'answer': {'tldr': '## TLDR\nETF flows, dollar strength, and miner distribution remain the main forward-looking
            drivers for Bitcoin.', 'body': '## Deep Dive\nA sustained return of spot-ETF inflows would be the cleanest
            bullish tell. The opposite keeps BTC range-bound.\n\n## Conclusion\nPosition around flow, not a single print.'},
            'sources': [{'url': 'https://coinmarketcap.com/currencies/bitcoin/'}, {'url': 'https://cryptopotato.com/btc-etf-
            outflows-august'}], 'sources_count': 34, 'sources_truncated': True, 'generated_at': '2026-08-17T08:02:11Z'}]},
            {'crypto_id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'insights': [{'type':
            'fixed_question', 'title': "Why is ETH's price down today?", 'answer_id': '6a82d22f0ab14c33a91de802',
            'question_key': 'price_down', 'answer': {'tldr': '## TLDR\nEther lagged Bitcoin as ETH ETF flows stayed soft and
            L2 activity cooled.', 'body': '## Deep Dive\nRelative weakness versus BTC is the story more than a standalone
            ETH shock.\n\n## Conclusion\nETH/BTC is the pair to watch until ETF flow improves.'}, 'sources': [{'url':
            'https://coinmarketcap.com/currencies/ethereum/'}], 'sources_count': 22, 'sources_truncated': True,
            'generated_at': '2026-08-17T09:10:03Z'}]}], 'total_size': 2, 'has_more': False}

    Attributes:
        coins (list[CMCAICoinObject] | Unset): One object per requested cryptocurrency. Never a bare array at `data`.
        total_size (int | Unset): Total number of matching cryptocurrencies across all pages. Placed after the `coins[]`
            array. Example: 2.
        has_more (bool | Unset): `true` if more cryptocurrencies exist beyond this page, else `false`. Placed after the
            `coins[]` array.
    """

    coins: list[CMCAICoinObject] | Unset = UNSET
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
        from ..models.cmcai_coin_object import CMCAICoinObject

        d = dict(src_dict)
        _coins = d.pop("coins", UNSET)
        coins: list[CMCAICoinObject] | Unset = UNSET
        if _coins is not UNSET:
            coins = []
            for coins_item_data in _coins:
                coins_item = CMCAICoinObject.from_dict(coins_item_data)

                coins.append(coins_item)

        total_size = d.pop("total_size", UNSET)

        has_more = d.pop("has_more", UNSET)

        cmcai_coins_latest_results_object = cls(
            coins=coins,
            total_size=total_size,
            has_more=has_more,
        )

        cmcai_coins_latest_results_object.additional_properties = d
        return cmcai_coins_latest_results_object

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
