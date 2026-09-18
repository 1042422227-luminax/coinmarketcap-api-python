from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cmcai_coins_latest_response_model import CMCAICoinsLatestResponseModel
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
    type_: str | Unset = UNSET,
    question_key: str | Unset = UNSET,
    sources_limit: int | Unset = 10,
    skip_invalid: bool | Unset = False,
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["crypto_id"] = crypto_id

    params["slug"] = slug

    params["symbol"] = symbol

    params["type"] = type_

    params["question_key"] = question_key

    params["sources_limit"] = sources_limit

    params["skip_invalid"] = skip_invalid

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v5/cmc-ai/coins/latest",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CMCAICoinsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = CMCAICoinsLatestResponseModel.from_dict(response.json())

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
    CMCAICoinsLatestResponseModel
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
    type_: str | Unset = UNSET,
    question_key: str | Unset = UNSET,
    sources_limit: int | Unset = 10,
    skip_invalid: bool | Unset = False,
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> Response[
    CMCAICoinsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Coin Insights Latest

     Returns the CMC AI questions and answers for a cryptocurrency. Use it to attach explainers to any
    asset you already display, including why the price moved today, what people are saying, what is on
    the roadmap, and the latest news. Exactly one of `crypto_id`, `slug`, or `symbol` is required; they
    are mutually exclusive.

    On a Coin Detail Page these insights appear as the blue question pills below the price chart, for
    example on [coinmarketcap.com/currencies/bitcoin/](https://coinmarketcap.com/currencies/bitcoin/).
    Some questions are a fixed template for that coin. Others are written for current market conditions
    and then go away.

    - `fixed_question` is a stable template. Examples include \"What is Bitcoin?\", \"What could affect
    BTC's future price?\", \"What is next on BTC's roadmap?\", and \"What is the latest update in BTC's
    codebase?\". Two templates depend on the day's move: \"Why is BTC's price up today?\" (`price_up`)
    or \"Why is BTC's price down today?\" (`price_down`). Only one of those is shown. A coin never
    returns both.
    - `trending_question` is a market-dependent question about that coin with no fixed template, for
    example a one-off prompt about a protocol incident or a catalyst unique to that asset.
    - `top_news` is a headline tied to the requested coin. These change as the news cycle changes.

    When a requested cryptocurrency is in the coverage set but has no content yet, it is still returned
    with an empty `insights[]` array rather than an error. Coins skipped by `skip_invalid`, and coins
    returned with an empty `insights[]`, are not charged. Pagination is over cryptocurrencies, not over
    individual insights. Coverage is the current top 100 by market cap and is not guaranteed per
    question. Use [/v5/cmc-ai/coins/map](/pro-api-reference/cmc-ai#cmc-ai-map) first if you need to know
    which coins currently have coverage. Market-wide homepage questions live on [/v5/cmc-
    ai/latest](/pro-api-reference/cmc-ai#market-feed-latest).

    Refresh cadence by question:

    - `price_up` and `price_down`: about every 1 hour.
    - `future_price`, `sentiment`, and `latest_news`: about every 8 hours.
    - `overview`, `roadmap`, and `codebase`: about every 24 hours.
    - `trending_question`: about every 24 hours.

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
    how often each question is regenerated.
    **Plan credit use:** 1 call credit per cryptocurrency returned. Skipped coins and empty-insight
    coins are free. Repeat calls that return the same content for a coin are not charged.
    **CMC equivalent page:** The blue question pills below the chart on Coin Detail Pages, e.g.
    [coinmarketcap.com/currencies/bitcoin/](https://coinmarketcap.com/currencies/bitcoin/).

    Args:
        crypto_id (str | Unset):  Example: 1,1027.
        slug (str | Unset):  Example: bitcoin,ethereum.
        symbol (str | Unset):  Example: BTC,ETH.
        type_ (str | Unset):  Example: fixed_question,top_news.
        question_key (str | Unset):  Example: price_up,overview.
        sources_limit (int | Unset):  Default: 10.
        skip_invalid (bool | Unset):  Default: False.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CMCAICoinsLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        crypto_id=crypto_id,
        slug=slug,
        symbol=symbol,
        type_=type_,
        question_key=question_key,
        sources_limit=sources_limit,
        skip_invalid=skip_invalid,
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
    type_: str | Unset = UNSET,
    question_key: str | Unset = UNSET,
    sources_limit: int | Unset = 10,
    skip_invalid: bool | Unset = False,
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> (
    CMCAICoinsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Coin Insights Latest

     Returns the CMC AI questions and answers for a cryptocurrency. Use it to attach explainers to any
    asset you already display, including why the price moved today, what people are saying, what is on
    the roadmap, and the latest news. Exactly one of `crypto_id`, `slug`, or `symbol` is required; they
    are mutually exclusive.

    On a Coin Detail Page these insights appear as the blue question pills below the price chart, for
    example on [coinmarketcap.com/currencies/bitcoin/](https://coinmarketcap.com/currencies/bitcoin/).
    Some questions are a fixed template for that coin. Others are written for current market conditions
    and then go away.

    - `fixed_question` is a stable template. Examples include \"What is Bitcoin?\", \"What could affect
    BTC's future price?\", \"What is next on BTC's roadmap?\", and \"What is the latest update in BTC's
    codebase?\". Two templates depend on the day's move: \"Why is BTC's price up today?\" (`price_up`)
    or \"Why is BTC's price down today?\" (`price_down`). Only one of those is shown. A coin never
    returns both.
    - `trending_question` is a market-dependent question about that coin with no fixed template, for
    example a one-off prompt about a protocol incident or a catalyst unique to that asset.
    - `top_news` is a headline tied to the requested coin. These change as the news cycle changes.

    When a requested cryptocurrency is in the coverage set but has no content yet, it is still returned
    with an empty `insights[]` array rather than an error. Coins skipped by `skip_invalid`, and coins
    returned with an empty `insights[]`, are not charged. Pagination is over cryptocurrencies, not over
    individual insights. Coverage is the current top 100 by market cap and is not guaranteed per
    question. Use [/v5/cmc-ai/coins/map](/pro-api-reference/cmc-ai#cmc-ai-map) first if you need to know
    which coins currently have coverage. Market-wide homepage questions live on [/v5/cmc-
    ai/latest](/pro-api-reference/cmc-ai#market-feed-latest).

    Refresh cadence by question:

    - `price_up` and `price_down`: about every 1 hour.
    - `future_price`, `sentiment`, and `latest_news`: about every 8 hours.
    - `overview`, `roadmap`, and `codebase`: about every 24 hours.
    - `trending_question`: about every 24 hours.

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
    how often each question is regenerated.
    **Plan credit use:** 1 call credit per cryptocurrency returned. Skipped coins and empty-insight
    coins are free. Repeat calls that return the same content for a coin are not charged.
    **CMC equivalent page:** The blue question pills below the chart on Coin Detail Pages, e.g.
    [coinmarketcap.com/currencies/bitcoin/](https://coinmarketcap.com/currencies/bitcoin/).

    Args:
        crypto_id (str | Unset):  Example: 1,1027.
        slug (str | Unset):  Example: bitcoin,ethereum.
        symbol (str | Unset):  Example: BTC,ETH.
        type_ (str | Unset):  Example: fixed_question,top_news.
        question_key (str | Unset):  Example: price_up,overview.
        sources_limit (int | Unset):  Default: 10.
        skip_invalid (bool | Unset):  Default: False.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CMCAICoinsLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        crypto_id=crypto_id,
        slug=slug,
        symbol=symbol,
        type_=type_,
        question_key=question_key,
        sources_limit=sources_limit,
        skip_invalid=skip_invalid,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    crypto_id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    question_key: str | Unset = UNSET,
    sources_limit: int | Unset = 10,
    skip_invalid: bool | Unset = False,
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> Response[
    CMCAICoinsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Coin Insights Latest

     Returns the CMC AI questions and answers for a cryptocurrency. Use it to attach explainers to any
    asset you already display, including why the price moved today, what people are saying, what is on
    the roadmap, and the latest news. Exactly one of `crypto_id`, `slug`, or `symbol` is required; they
    are mutually exclusive.

    On a Coin Detail Page these insights appear as the blue question pills below the price chart, for
    example on [coinmarketcap.com/currencies/bitcoin/](https://coinmarketcap.com/currencies/bitcoin/).
    Some questions are a fixed template for that coin. Others are written for current market conditions
    and then go away.

    - `fixed_question` is a stable template. Examples include \"What is Bitcoin?\", \"What could affect
    BTC's future price?\", \"What is next on BTC's roadmap?\", and \"What is the latest update in BTC's
    codebase?\". Two templates depend on the day's move: \"Why is BTC's price up today?\" (`price_up`)
    or \"Why is BTC's price down today?\" (`price_down`). Only one of those is shown. A coin never
    returns both.
    - `trending_question` is a market-dependent question about that coin with no fixed template, for
    example a one-off prompt about a protocol incident or a catalyst unique to that asset.
    - `top_news` is a headline tied to the requested coin. These change as the news cycle changes.

    When a requested cryptocurrency is in the coverage set but has no content yet, it is still returned
    with an empty `insights[]` array rather than an error. Coins skipped by `skip_invalid`, and coins
    returned with an empty `insights[]`, are not charged. Pagination is over cryptocurrencies, not over
    individual insights. Coverage is the current top 100 by market cap and is not guaranteed per
    question. Use [/v5/cmc-ai/coins/map](/pro-api-reference/cmc-ai#cmc-ai-map) first if you need to know
    which coins currently have coverage. Market-wide homepage questions live on [/v5/cmc-
    ai/latest](/pro-api-reference/cmc-ai#market-feed-latest).

    Refresh cadence by question:

    - `price_up` and `price_down`: about every 1 hour.
    - `future_price`, `sentiment`, and `latest_news`: about every 8 hours.
    - `overview`, `roadmap`, and `codebase`: about every 24 hours.
    - `trending_question`: about every 24 hours.

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
    how often each question is regenerated.
    **Plan credit use:** 1 call credit per cryptocurrency returned. Skipped coins and empty-insight
    coins are free. Repeat calls that return the same content for a coin are not charged.
    **CMC equivalent page:** The blue question pills below the chart on Coin Detail Pages, e.g.
    [coinmarketcap.com/currencies/bitcoin/](https://coinmarketcap.com/currencies/bitcoin/).

    Args:
        crypto_id (str | Unset):  Example: 1,1027.
        slug (str | Unset):  Example: bitcoin,ethereum.
        symbol (str | Unset):  Example: BTC,ETH.
        type_ (str | Unset):  Example: fixed_question,top_news.
        question_key (str | Unset):  Example: price_up,overview.
        sources_limit (int | Unset):  Default: 10.
        skip_invalid (bool | Unset):  Default: False.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CMCAICoinsLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        crypto_id=crypto_id,
        slug=slug,
        symbol=symbol,
        type_=type_,
        question_key=question_key,
        sources_limit=sources_limit,
        skip_invalid=skip_invalid,
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
    type_: str | Unset = UNSET,
    question_key: str | Unset = UNSET,
    sources_limit: int | Unset = 10,
    skip_invalid: bool | Unset = False,
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> (
    CMCAICoinsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Coin Insights Latest

     Returns the CMC AI questions and answers for a cryptocurrency. Use it to attach explainers to any
    asset you already display, including why the price moved today, what people are saying, what is on
    the roadmap, and the latest news. Exactly one of `crypto_id`, `slug`, or `symbol` is required; they
    are mutually exclusive.

    On a Coin Detail Page these insights appear as the blue question pills below the price chart, for
    example on [coinmarketcap.com/currencies/bitcoin/](https://coinmarketcap.com/currencies/bitcoin/).
    Some questions are a fixed template for that coin. Others are written for current market conditions
    and then go away.

    - `fixed_question` is a stable template. Examples include \"What is Bitcoin?\", \"What could affect
    BTC's future price?\", \"What is next on BTC's roadmap?\", and \"What is the latest update in BTC's
    codebase?\". Two templates depend on the day's move: \"Why is BTC's price up today?\" (`price_up`)
    or \"Why is BTC's price down today?\" (`price_down`). Only one of those is shown. A coin never
    returns both.
    - `trending_question` is a market-dependent question about that coin with no fixed template, for
    example a one-off prompt about a protocol incident or a catalyst unique to that asset.
    - `top_news` is a headline tied to the requested coin. These change as the news cycle changes.

    When a requested cryptocurrency is in the coverage set but has no content yet, it is still returned
    with an empty `insights[]` array rather than an error. Coins skipped by `skip_invalid`, and coins
    returned with an empty `insights[]`, are not charged. Pagination is over cryptocurrencies, not over
    individual insights. Coverage is the current top 100 by market cap and is not guaranteed per
    question. Use [/v5/cmc-ai/coins/map](/pro-api-reference/cmc-ai#cmc-ai-map) first if you need to know
    which coins currently have coverage. Market-wide homepage questions live on [/v5/cmc-
    ai/latest](/pro-api-reference/cmc-ai#market-feed-latest).

    Refresh cadence by question:

    - `price_up` and `price_down`: about every 1 hour.
    - `future_price`, `sentiment`, and `latest_news`: about every 8 hours.
    - `overview`, `roadmap`, and `codebase`: about every 24 hours.
    - `trending_question`: about every 24 hours.

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
    how often each question is regenerated.
    **Plan credit use:** 1 call credit per cryptocurrency returned. Skipped coins and empty-insight
    coins are free. Repeat calls that return the same content for a coin are not charged.
    **CMC equivalent page:** The blue question pills below the chart on Coin Detail Pages, e.g.
    [coinmarketcap.com/currencies/bitcoin/](https://coinmarketcap.com/currencies/bitcoin/).

    Args:
        crypto_id (str | Unset):  Example: 1,1027.
        slug (str | Unset):  Example: bitcoin,ethereum.
        symbol (str | Unset):  Example: BTC,ETH.
        type_ (str | Unset):  Example: fixed_question,top_news.
        question_key (str | Unset):  Example: price_up,overview.
        sources_limit (int | Unset):  Default: 10.
        skip_invalid (bool | Unset):  Default: False.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CMCAICoinsLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            crypto_id=crypto_id,
            slug=slug,
            symbol=symbol,
            type_=type_,
            question_key=question_key,
            sources_limit=sources_limit,
            skip_invalid=skip_invalid,
            start=start,
            limit=limit,
        )
    ).parsed
