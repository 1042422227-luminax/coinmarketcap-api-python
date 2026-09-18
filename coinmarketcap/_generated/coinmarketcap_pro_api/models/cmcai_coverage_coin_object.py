from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.cmcai_coverage_coin_object_available_question_keys_item import (
    CMCAICoverageCoinObjectAvailableQuestionKeysItem,
    check_cmcai_coverage_coin_object_available_question_keys_item,
)

T = TypeVar("T", bound="CMCAICoverageCoinObject")


@_attrs_define
class CMCAICoverageCoinObject:
    """A cryptocurrency currently in the CMC AI coverage set, without answer bodies.

    Attributes:
        crypto_id (int): CoinMarketCap cryptocurrency ID. Integer, not a string. Example: 1.
        name (str): Cryptocurrency name. Example: Bitcoin.
        symbol (str): Cryptocurrency symbol. Example: BTC.
        slug (str): URL-friendly lowercase slug. Example: bitcoin.
        url (str): Coin Detail Page URL. Example: https://coinmarketcap.com/currencies/bitcoin/.
        available_question_keys (list[CMCAICoverageCoinObjectAvailableQuestionKeysItem]): Fixed-question keys that
            currently have content for this cryptocurrency. May be empty. Example: ['price_up', 'future_price', 'overview'].
        num_insights (int): Insights currently available for this cryptocurrency, across all types. Example: 8.
        last_generated_at (datetime.datetime | None): ISO 8601 UTC time of the most recent generation. `null` if nothing
            has been generated yet. Example: 2026-08-17T09:14:14Z.
    """

    crypto_id: int
    name: str
    symbol: str
    slug: str
    url: str
    available_question_keys: list[CMCAICoverageCoinObjectAvailableQuestionKeysItem]
    num_insights: int
    last_generated_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        crypto_id = self.crypto_id

        name = self.name

        symbol = self.symbol

        slug = self.slug

        url = self.url

        available_question_keys = []
        for available_question_keys_item_data in self.available_question_keys:
            available_question_keys_item: str = available_question_keys_item_data
            available_question_keys.append(available_question_keys_item)

        num_insights = self.num_insights

        last_generated_at: None | str
        if isinstance(self.last_generated_at, datetime.datetime):
            last_generated_at = self.last_generated_at.isoformat()
        else:
            last_generated_at = self.last_generated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "crypto_id": crypto_id,
                "name": name,
                "symbol": symbol,
                "slug": slug,
                "url": url,
                "available_question_keys": available_question_keys,
                "num_insights": num_insights,
                "last_generated_at": last_generated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        crypto_id = d.pop("crypto_id")

        name = d.pop("name")

        symbol = d.pop("symbol")

        slug = d.pop("slug")

        url = d.pop("url")

        available_question_keys = []
        _available_question_keys = d.pop("available_question_keys")
        for available_question_keys_item_data in _available_question_keys:
            available_question_keys_item = check_cmcai_coverage_coin_object_available_question_keys_item(
                available_question_keys_item_data
            )

            available_question_keys.append(available_question_keys_item)

        num_insights = d.pop("num_insights")

        def _parse_last_generated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_generated_at_type_0 = isoparse(data)

                return last_generated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_generated_at = _parse_last_generated_at(d.pop("last_generated_at"))

        cmcai_coverage_coin_object = cls(
            crypto_id=crypto_id,
            name=name,
            symbol=symbol,
            slug=slug,
            url=url,
            available_question_keys=available_question_keys,
            num_insights=num_insights,
            last_generated_at=last_generated_at,
        )

        cmcai_coverage_coin_object.additional_properties = d
        return cmcai_coverage_coin_object

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
