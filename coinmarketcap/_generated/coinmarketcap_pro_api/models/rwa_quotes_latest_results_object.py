from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rwa_quotes_latest_results_object_rwa_assets_item import RWAQuotesLatestResultsObjectRwaAssetsItem


T = TypeVar("T", bound="RWAQuotesLatestResultsObject")


@_attrs_define
class RWAQuotesLatestResultsObject:
    """Results of your query returned as an object.

    Example:
        {'rwa_assets': [{'name': 'Nvidia Corp', 'symbol': 'NVDA', 'slug': 'nvidia', 'quotes': [{'symbol': 'USD',
            'crypto_id': 2781, 'average_tokenized_price': 226.4599992554912, 'tokenized_market_cap': 117414402.19394198,
            'tokenized_volume_24h': 79320399.19936948, 'last_updated': '2026-09-09T06:49:59.000Z'}], 'rwa_id': 2,
            'asset_type': 'stock', 'rwa_rank': 2, 'has_tokens': True, 'average_tokenized_price': 226.4599992554912,
            'tokenized_market_cap': 117414402.19394198, 'tokenized_volume_24h': 79320399.19936948, 'last_updated':
            '2026-09-09T06:50:33.594Z', 'tokens': [{'symbol': 'NVDAX', 'name': 'NVIDIA tokenized stock (xStock)', 'price':
            226.33422377299925, 'crypto_id': 36992, 'issuer_id': '6878977dcbbf471de3366e85', 'issuer_name': 'Backed Assets',
            'market_cap': 39526066.25, 'volume_24h': 12187859.2729597}, {'symbol': 'NVDAon', 'name': 'NVIDIA Tokenized Stock
            (Ondo)', 'price': 226.5005458510576, 'crypto_id': 38093, 'issuer_id': '688ca4ccabae9b5b9fb3167a', 'issuer_name':
            'Ondo Assets', 'market_cap': 38222994.66, 'volume_24h': 2634471.69806766}], 'tradfi_markets': [{'exchange':
            {'slug': 'binance', 'name': 'Binance', 'exchange_id': 270}, 'ticker': 'NVDA', 'market_url':
            'https://www.binance.com/en/stocks/EQ_NVDA'}]}, {'name': 'Gold', 'symbol': 'GOLD', 'slug': 'gold', 'quotes':
            [{'symbol': 'USD', 'crypto_id': 2781, 'average_tokenized_price': 4399.672364252196, 'tokenized_market_cap':
            4691165858.450071, 'tokenized_volume_24h': 386677568.7358118, 'last_updated': '2026-09-09T06:49:59.000Z'}],
            'rwa_id': 1, 'asset_type': 'commodity', 'rwa_rank': 1, 'has_tokens': True, 'average_tokenized_price':
            4399.672364252196, 'tokenized_market_cap': 4691165858.450071, 'tokenized_volume_24h': 386677568.7358118,
            'last_updated': '2026-09-09T06:50:32.066Z', 'tokens': [{'symbol': 'PAXG', 'name': 'PAX Gold', 'price':
            4404.158250158926, 'crypto_id': 4705, 'issuer_id': '68904c24abae9b5b9fb35815', 'issuer_name': 'Paxos',
            'market_cap': 1904813029.99, 'volume_24h': 183784699.06453583}, {'symbol': 'XAUt', 'name': 'Tether Gold',
            'price': 4399.163220342952, 'crypto_id': 5176, 'issuer_id': '68904e9cabae9b5b9fb358ac', 'issuer_name': 'Tether
            Holdings', 'market_cap': 2695911303.57, 'volume_24h': 201510910.10671782}], 'tradfi_markets': []}]}

    Attributes:
        rwa_assets (list[RWAQuotesLatestResultsObjectRwaAssetsItem] | Unset): Array of RWA asset objects (latest market
            data), one per requested asset.
    """

    rwa_assets: list[RWAQuotesLatestResultsObjectRwaAssetsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rwa_assets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rwa_assets, Unset):
            rwa_assets = []
            for rwa_assets_item_data in self.rwa_assets:
                rwa_assets_item = rwa_assets_item_data.to_dict()
                rwa_assets.append(rwa_assets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rwa_assets is not UNSET:
            field_dict["rwa_assets"] = rwa_assets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rwa_quotes_latest_results_object_rwa_assets_item import RWAQuotesLatestResultsObjectRwaAssetsItem

        d = dict(src_dict)
        _rwa_assets = d.pop("rwa_assets", UNSET)
        rwa_assets: list[RWAQuotesLatestResultsObjectRwaAssetsItem] | Unset = UNSET
        if _rwa_assets is not UNSET:
            rwa_assets = []
            for rwa_assets_item_data in _rwa_assets:
                rwa_assets_item = RWAQuotesLatestResultsObjectRwaAssetsItem.from_dict(rwa_assets_item_data)

                rwa_assets.append(rwa_assets_item)

        rwa_quotes_latest_results_object = cls(
            rwa_assets=rwa_assets,
        )

        rwa_quotes_latest_results_object.additional_properties = d
        return rwa_quotes_latest_results_object

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
