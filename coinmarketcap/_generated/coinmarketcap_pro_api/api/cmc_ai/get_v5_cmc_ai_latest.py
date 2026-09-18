from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cmcai_latest_response_model import CMCAILatestResponseModel
from ...models.http_status_400_error_object import HTTPStatus400ErrorObject
from ...models.http_status_401_error_object import HTTPStatus401ErrorObject
from ...models.http_status_403_error_object import HTTPStatus403ErrorObject
from ...models.http_status_429_error_object import HTTPStatus429ErrorObject
from ...models.http_status_500_error_object import HTTPStatus500ErrorObject
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type_: str | Unset = UNSET,
    sources_limit: int | Unset = 10,
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["type"] = type_

    params["sources_limit"] = sources_limit

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v5/cmc-ai/latest",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CMCAILatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = CMCAILatestResponseModel.from_dict(response.json())

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
    CMCAILatestResponseModel
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
    type_: str | Unset = UNSET,
    sources_limit: int | Unset = 10,
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> Response[
    CMCAILatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Market Feed Latest

     Returns the CMC AI questions, answers, and top news from the CoinMarketCap homepage. Use it when you
    want a market briefing as structured data in a dashboard, terminal, or research product.

    On the homepage these insights appear as the blue question pills above the cryptocurrency list. Some
    questions are a fixed template. Others are written for current market conditions and then go away.

    - `fixed_question` is a stable template that stays in the rotation. Examples include \"What are the
    trending narratives?\", \"Are altcoins outperforming Bitcoin?\", and \"What is the market
    sentiment?\". The question text does not change. The answer is rewritten as the market moves.
    - `trending_question` is a market-dependent question with no fixed template. The question itself
    appears and disappears with current conditions, for example a one-off prompt about a sudden sector
    rotation or a catalyst dominating discussion that week.
    - `top_news` is a headline plus recap of a current story, for example \"BTC stuck near $63K as US
    spot ETFs see $390M outflows\". Headlines change as the news cycle changes.

    This endpoint is market-wide. Coin-specific questions appear as blue pills below the charts on a
    Coin Detail Page. Use [/v5/cmc-ai/coins/latest](/pro-api-reference/cmc-ai#coin-insights-latest) and
    [/v5/cmc-ai/coins/map](/pro-api-reference/cmc-ai#cmc-ai-map) for those.

    Refresh cadence:

    - `fixed_question`: about every 30 minutes.
    - `trending_question`: about every 30 minutes.
    - `top_news`: about every 30 minutes.

    Content is fetched from the database. This endpoint does not generate answers on request. Answers
    are English only.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - ~~Basic~~
    - ~~Builder~~
    - ~~Startup~~
    - ~~Growth~~
    - ~~Professional~~
    - Enterprise

    **Cache / Update frequency:** Responses may be up to 1 minute old. See the cadence list above for
    how often content is regenerated.
    **Plan credit use:** 1 call credit per request. Repeat calls that return the same content are not
    charged.
    **CMC equivalent page:** The blue question pills above the list on
    [coinmarketcap.com](https://coinmarketcap.com/).

    Args:
        type_ (str | Unset):  Example: fixed_question,top_news.
        sources_limit (int | Unset):  Default: 10.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CMCAILatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        type_=type_,
        sources_limit=sources_limit,
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
    type_: str | Unset = UNSET,
    sources_limit: int | Unset = 10,
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> (
    CMCAILatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Market Feed Latest

     Returns the CMC AI questions, answers, and top news from the CoinMarketCap homepage. Use it when you
    want a market briefing as structured data in a dashboard, terminal, or research product.

    On the homepage these insights appear as the blue question pills above the cryptocurrency list. Some
    questions are a fixed template. Others are written for current market conditions and then go away.

    - `fixed_question` is a stable template that stays in the rotation. Examples include \"What are the
    trending narratives?\", \"Are altcoins outperforming Bitcoin?\", and \"What is the market
    sentiment?\". The question text does not change. The answer is rewritten as the market moves.
    - `trending_question` is a market-dependent question with no fixed template. The question itself
    appears and disappears with current conditions, for example a one-off prompt about a sudden sector
    rotation or a catalyst dominating discussion that week.
    - `top_news` is a headline plus recap of a current story, for example \"BTC stuck near $63K as US
    spot ETFs see $390M outflows\". Headlines change as the news cycle changes.

    This endpoint is market-wide. Coin-specific questions appear as blue pills below the charts on a
    Coin Detail Page. Use [/v5/cmc-ai/coins/latest](/pro-api-reference/cmc-ai#coin-insights-latest) and
    [/v5/cmc-ai/coins/map](/pro-api-reference/cmc-ai#cmc-ai-map) for those.

    Refresh cadence:

    - `fixed_question`: about every 30 minutes.
    - `trending_question`: about every 30 minutes.
    - `top_news`: about every 30 minutes.

    Content is fetched from the database. This endpoint does not generate answers on request. Answers
    are English only.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - ~~Basic~~
    - ~~Builder~~
    - ~~Startup~~
    - ~~Growth~~
    - ~~Professional~~
    - Enterprise

    **Cache / Update frequency:** Responses may be up to 1 minute old. See the cadence list above for
    how often content is regenerated.
    **Plan credit use:** 1 call credit per request. Repeat calls that return the same content are not
    charged.
    **CMC equivalent page:** The blue question pills above the list on
    [coinmarketcap.com](https://coinmarketcap.com/).

    Args:
        type_ (str | Unset):  Example: fixed_question,top_news.
        sources_limit (int | Unset):  Default: 10.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CMCAILatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        type_=type_,
        sources_limit=sources_limit,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: str | Unset = UNSET,
    sources_limit: int | Unset = 10,
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> Response[
    CMCAILatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Market Feed Latest

     Returns the CMC AI questions, answers, and top news from the CoinMarketCap homepage. Use it when you
    want a market briefing as structured data in a dashboard, terminal, or research product.

    On the homepage these insights appear as the blue question pills above the cryptocurrency list. Some
    questions are a fixed template. Others are written for current market conditions and then go away.

    - `fixed_question` is a stable template that stays in the rotation. Examples include \"What are the
    trending narratives?\", \"Are altcoins outperforming Bitcoin?\", and \"What is the market
    sentiment?\". The question text does not change. The answer is rewritten as the market moves.
    - `trending_question` is a market-dependent question with no fixed template. The question itself
    appears and disappears with current conditions, for example a one-off prompt about a sudden sector
    rotation or a catalyst dominating discussion that week.
    - `top_news` is a headline plus recap of a current story, for example \"BTC stuck near $63K as US
    spot ETFs see $390M outflows\". Headlines change as the news cycle changes.

    This endpoint is market-wide. Coin-specific questions appear as blue pills below the charts on a
    Coin Detail Page. Use [/v5/cmc-ai/coins/latest](/pro-api-reference/cmc-ai#coin-insights-latest) and
    [/v5/cmc-ai/coins/map](/pro-api-reference/cmc-ai#cmc-ai-map) for those.

    Refresh cadence:

    - `fixed_question`: about every 30 minutes.
    - `trending_question`: about every 30 minutes.
    - `top_news`: about every 30 minutes.

    Content is fetched from the database. This endpoint does not generate answers on request. Answers
    are English only.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - ~~Basic~~
    - ~~Builder~~
    - ~~Startup~~
    - ~~Growth~~
    - ~~Professional~~
    - Enterprise

    **Cache / Update frequency:** Responses may be up to 1 minute old. See the cadence list above for
    how often content is regenerated.
    **Plan credit use:** 1 call credit per request. Repeat calls that return the same content are not
    charged.
    **CMC equivalent page:** The blue question pills above the list on
    [coinmarketcap.com](https://coinmarketcap.com/).

    Args:
        type_ (str | Unset):  Example: fixed_question,top_news.
        sources_limit (int | Unset):  Default: 10.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CMCAILatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        type_=type_,
        sources_limit=sources_limit,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    type_: str | Unset = UNSET,
    sources_limit: int | Unset = 10,
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> (
    CMCAILatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Market Feed Latest

     Returns the CMC AI questions, answers, and top news from the CoinMarketCap homepage. Use it when you
    want a market briefing as structured data in a dashboard, terminal, or research product.

    On the homepage these insights appear as the blue question pills above the cryptocurrency list. Some
    questions are a fixed template. Others are written for current market conditions and then go away.

    - `fixed_question` is a stable template that stays in the rotation. Examples include \"What are the
    trending narratives?\", \"Are altcoins outperforming Bitcoin?\", and \"What is the market
    sentiment?\". The question text does not change. The answer is rewritten as the market moves.
    - `trending_question` is a market-dependent question with no fixed template. The question itself
    appears and disappears with current conditions, for example a one-off prompt about a sudden sector
    rotation or a catalyst dominating discussion that week.
    - `top_news` is a headline plus recap of a current story, for example \"BTC stuck near $63K as US
    spot ETFs see $390M outflows\". Headlines change as the news cycle changes.

    This endpoint is market-wide. Coin-specific questions appear as blue pills below the charts on a
    Coin Detail Page. Use [/v5/cmc-ai/coins/latest](/pro-api-reference/cmc-ai#coin-insights-latest) and
    [/v5/cmc-ai/coins/map](/pro-api-reference/cmc-ai#cmc-ai-map) for those.

    Refresh cadence:

    - `fixed_question`: about every 30 minutes.
    - `trending_question`: about every 30 minutes.
    - `top_news`: about every 30 minutes.

    Content is fetched from the database. This endpoint does not generate answers on request. Answers
    are English only.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - ~~Basic~~
    - ~~Builder~~
    - ~~Startup~~
    - ~~Growth~~
    - ~~Professional~~
    - Enterprise

    **Cache / Update frequency:** Responses may be up to 1 minute old. See the cadence list above for
    how often content is regenerated.
    **Plan credit use:** 1 call credit per request. Repeat calls that return the same content are not
    charged.
    **CMC equivalent page:** The blue question pills above the list on
    [coinmarketcap.com](https://coinmarketcap.com/).

    Args:
        type_ (str | Unset):  Example: fixed_question,top_news.
        sources_limit (int | Unset):  Default: 10.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CMCAILatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
            sources_limit=sources_limit,
            start=start,
            limit=limit,
        )
    ).parsed
