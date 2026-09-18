from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cmcai_insight_object import CMCAIInsightObject


T = TypeVar("T", bound="CMCAICoinObject")


@_attrs_define
class CMCAICoinObject:
    """One requested cryptocurrency and its current CMC AI insights.

    Attributes:
        crypto_id (int): CoinMarketCap cryptocurrency ID. Example: 1.
        name (str): Cryptocurrency name. Example: Bitcoin.
        symbol (str): Cryptocurrency symbol. Example: BTC.
        slug (str): URL-friendly lowercase slug. Example: bitcoin.
        insights (list[CMCAIInsightObject]): Insight objects for this cryptocurrency. Empty when the coin is covered but
            no content has been generated yet.
    """

    crypto_id: int
    name: str
    symbol: str
    slug: str
    insights: list[CMCAIInsightObject]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        crypto_id = self.crypto_id

        name = self.name

        symbol = self.symbol

        slug = self.slug

        insights = []
        for insights_item_data in self.insights:
            insights_item = insights_item_data.to_dict()
            insights.append(insights_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "crypto_id": crypto_id,
                "name": name,
                "symbol": symbol,
                "slug": slug,
                "insights": insights,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cmcai_insight_object import CMCAIInsightObject

        d = dict(src_dict)
        crypto_id = d.pop("crypto_id")

        name = d.pop("name")

        symbol = d.pop("symbol")

        slug = d.pop("slug")

        insights = []
        _insights = d.pop("insights")
        for insights_item_data in _insights:
            insights_item = CMCAIInsightObject.from_dict(insights_item_data)

            insights.append(insights_item)

        cmcai_coin_object = cls(
            crypto_id=crypto_id,
            name=name,
            symbol=symbol,
            slug=slug,
            insights=insights,
        )

        cmcai_coin_object.additional_properties = d
        return cmcai_coin_object

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
