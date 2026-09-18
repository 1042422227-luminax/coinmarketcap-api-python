from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cmcai_coins_map_response_model import CMCAICoinsMapResponseModel
from ...models.get_v5_cmc_ai_coins_map_sort import GetV5CmcAiCoinsMapSort
from ...models.http_status_400_error_object import HTTPStatus400ErrorObject
from ...models.http_status_401_error_object import HTTPStatus401ErrorObject
from ...models.http_status_403_error_object import HTTPStatus403ErrorObject
from ...models.http_status_429_error_object import HTTPStatus429ErrorObject
from ...models.http_status_500_error_object import HTTPStatus500ErrorObject
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    crypto_id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    sort: GetV5CmcAiCoinsMapSort | Unset = "cmc_rank",
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["crypto_id"] = crypto_id

    params["slug"] = slug

    params["symbol"] = symbol

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v5/cmc-ai/coins/map",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CMCAICoinsMapResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = CMCAICoinsMapResponseModel.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = HTTPStatus400ErrorObject.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = HTTPStatus401ErrorObject.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = HTTPStatus403ErrorObject.from_dict(response.json())

        return response_403

    if response.status_code == 429:
        response_429 = HTTPStatus429ErrorObject.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = HTTPStatus500ErrorObject.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CMCAICoinsMapResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    crypto_id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    sort: GetV5CmcAiCoinsMapSort | Unset = "cmc_rank",
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> Response[
    CMCAICoinsMapResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    """CMC AI Map

     Returns the cryptocurrencies for which CMC AI currently writes Coin Detail Page content. Call this
    before [/v5/cmc-ai/coins/latest](/pro-api-reference/cmc-ai#coin-insights-latest) when you need to
    know which coins are covered, and which of those currently have an empty `insights[]`. No answer
    bodies are returned here.

    Current coverage is the top 100 cryptocurrencies by market cap. The set rotates as the ranking
    changes. All filters are optional. A filter that matches a coin we do not cover is not an error.
    That coin is simply absent from `data.coins[]`, and `total_size` reflects the matched count. A
    param-less call returns the full supported set.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - ~~Basic~~
    - ~~Builder~~
    - ~~Startup~~
    - ~~Growth~~
    - ~~Professional~~
    - Enterprise

    **Cache / Update frequency:** Responses may be up to 1 minute old.
    **Plan credit use:** 1 call credit per request. Repeat calls that return the same content are not
    charged.
    **CMC equivalent page:** No equivalent, API only.

    Args:
        crypto_id (str | Unset):  Example: 1,1027.
        slug (str | Unset):  Example: bitcoin,ethereum.
        symbol (str | Unset):  Example: BTC,ETH.
        sort (GetV5CmcAiCoinsMapSort | Unset):  Default: 'cmc_rank'.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CMCAICoinsMapResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        crypto_id=crypto_id,
        slug=slug,
        symbol=symbol,
        sort=sort,
        start=start,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    crypto_id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    sort: GetV5CmcAiCoinsMapSort | Unset = "cmc_rank",
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> (
    CMCAICoinsMapResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    """CMC AI Map

     Returns the cryptocurrencies for which CMC AI currently writes Coin Detail Page content. Call this
    before [/v5/cmc-ai/coins/latest](/pro-api-reference/cmc-ai#coin-insights-latest) when you need to
    know which coins are covered, and which of those currently have an empty `insights[]`. No answer
    bodies are returned here.

    Current coverage is the top 100 cryptocurrencies by market cap. The set rotates as the ranking
    changes. All filters are optional. A filter that matches a coin we do not cover is not an error.
    That coin is simply absent from `data.coins[]`, and `total_size` reflects the matched count. A
    param-less call returns the full supported set.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - ~~Basic~~
    - ~~Builder~~
    - ~~Startup~~
    - ~~Growth~~
    - ~~Professional~~
    - Enterprise

    **Cache / Update frequency:** Responses may be up to 1 minute old.
    **Plan credit use:** 1 call credit per request. Repeat calls that return the same content are not
    charged.
    **CMC equivalent page:** No equivalent, API only.

    Args:
        crypto_id (str | Unset):  Example: 1,1027.
        slug (str | Unset):  Example: bitcoin,ethereum.
        symbol (str | Unset):  Example: BTC,ETH.
        sort (GetV5CmcAiCoinsMapSort | Unset):  Default: 'cmc_rank'.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CMCAICoinsMapResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        crypto_id=crypto_id,
        slug=slug,
        symbol=symbol,
        sort=sort,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    crypto_id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    sort: GetV5CmcAiCoinsMapSort | Unset = "cmc_rank",
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> Response[
    CMCAICoinsMapResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    """CMC AI Map

     Returns the cryptocurrencies for which CMC AI currently writes Coin Detail Page content. Call this
    before [/v5/cmc-ai/coins/latest](/pro-api-reference/cmc-ai#coin-insights-latest) when you need to
    know which coins are covered, and which of those currently have an empty `insights[]`. No answer
    bodies are returned here.

    Current coverage is the top 100 cryptocurrencies by market cap. The set rotates as the ranking
    changes. All filters are optional. A filter that matches a coin we do not cover is not an error.
    That coin is simply absent from `data.coins[]`, and `total_size` reflects the matched count. A
    param-less call returns the full supported set.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - ~~Basic~~
    - ~~Builder~~
    - ~~Startup~~
    - ~~Growth~~
    - ~~Professional~~
    - Enterprise

    **Cache / Update frequency:** Responses may be up to 1 minute old.
    **Plan credit use:** 1 call credit per request. Repeat calls that return the same content are not
    charged.
    **CMC equivalent page:** No equivalent, API only.

    Args:
        crypto_id (str | Unset):  Example: 1,1027.
        slug (str | Unset):  Example: bitcoin,ethereum.
        symbol (str | Unset):  Example: BTC,ETH.
        sort (GetV5CmcAiCoinsMapSort | Unset):  Default: 'cmc_rank'.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CMCAICoinsMapResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        crypto_id=crypto_id,
        slug=slug,
        symbol=symbol,
        sort=sort,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    crypto_id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    sort: GetV5CmcAiCoinsMapSort | Unset = "cmc_rank",
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> (
    CMCAICoinsMapResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    """CMC AI Map

     Returns the cryptocurrencies for which CMC AI currently writes Coin Detail Page content. Call this
    before [/v5/cmc-ai/coins/latest](/pro-api-reference/cmc-ai#coin-insights-latest) when you need to
    know which coins are covered, and which of those currently have an empty `insights[]`. No answer
    bodies are returned here.

    Current coverage is the top 100 cryptocurrencies by market cap. The set rotates as the ranking
    changes. All filters are optional. A filter that matches a coin we do not cover is not an error.
    That coin is simply absent from `data.coins[]`, and `total_size` reflects the matched count. A
    param-less call returns the full supported set.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - ~~Basic~~
    - ~~Builder~~
    - ~~Startup~~
    - ~~Growth~~
    - ~~Professional~~
    - Enterprise

    **Cache / Update frequency:** Responses may be up to 1 minute old.
    **Plan credit use:** 1 call credit per request. Repeat calls that return the same content are not
    charged.
    **CMC equivalent page:** No equivalent, API only.

    Args:
        crypto_id (str | Unset):  Example: 1,1027.
        slug (str | Unset):  Example: bitcoin,ethereum.
        symbol (str | Unset):  Example: BTC,ETH.
        sort (GetV5CmcAiCoinsMapSort | Unset):  Default: 'cmc_rank'.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CMCAICoinsMapResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            crypto_id=crypto_id,
            slug=slug,
            symbol=symbol,
            sort=sort,
            start=start,
            limit=limit,
        )
    ).parsed
