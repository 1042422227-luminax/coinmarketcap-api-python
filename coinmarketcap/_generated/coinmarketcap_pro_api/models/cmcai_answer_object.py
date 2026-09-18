from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CMCAIAnswerObject")


@_attrs_define
class CMCAIAnswerObject:
    """Two-section markdown answer, split from the stored blob using the same TLDR detection as the CoinMarketCap front
    end. No other edits are applied.

        Attributes:
            tldr (str): TLDR section as markdown, returned as the model produced it.
            body (str): Everything after the TLDR (Deep Dive, Conclusion) as markdown, as the model produced it.
    """

    tldr: str
    body: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tldr = self.tldr

        body = self.body

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tldr": tldr,
                "body": body,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tldr = d.pop("tldr")

        body = d.pop("body")

        cmcai_answer_object = cls(
            tldr=tldr,
            body=body,
        )

        cmcai_answer_object.additional_properties = d
        return cmcai_answer_object

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
