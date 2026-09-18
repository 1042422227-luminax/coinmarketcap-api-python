from typing import Literal, cast

GetV5CmcAiCoinsMapSort = Literal["cmc_rank", "crypto_id", "name"]

GET_V5_CMC_AI_COINS_MAP_SORT_VALUES: set[GetV5CmcAiCoinsMapSort] = {
    "cmc_rank",
    "crypto_id",
    "name",
}


def check_get_v5_cmc_ai_coins_map_sort(value: str) -> GetV5CmcAiCoinsMapSort:
    if value in GET_V5_CMC_AI_COINS_MAP_SORT_VALUES:
        return cast(GetV5CmcAiCoinsMapSort, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_V5_CMC_AI_COINS_MAP_SORT_VALUES!r}")
