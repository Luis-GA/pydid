"""Test DID URL class."""

import pytest

from pydid import DIDUrl, InvalidDIDUrlError

from .test_did import TEST_DID0, TEST_DID_URL_PARTS, TEST_DID_URLS


@pytest.mark.parametrize("inputs, output", zip(TEST_DID_URL_PARTS, TEST_DID_URLS))
def test_did_url(inputs, output):
    url = DIDUrl(**inputs)
    assert str(url) == output
    assert repr(url)


@pytest.mark.parametrize("url, parts", zip(TEST_DID_URLS, TEST_DID_URL_PARTS))
def test_did_url_parse(url, parts):
    assert DIDUrl.parse(url) == DIDUrl(**parts)


@pytest.mark.parametrize("lhs, rhs", zip(TEST_DID_URLS, TEST_DID_URLS[1:]))
def test_did_url_neq(lhs, rhs):
    lhs = DIDUrl.parse(lhs)
    assert lhs != rhs
    rhs = DIDUrl.parse(rhs)
    assert lhs != rhs
    assert lhs != {"not a": "DIDUrl"}


@pytest.mark.parametrize(
    "bad_url",
    [
        TEST_DID0,
        "not://a/did?url=value",
    ],
)
def test_did_url_parse_x(bad_url):
    with pytest.raises(InvalidDIDUrlError):
        DIDUrl.parse(bad_url)


@pytest.mark.parametrize("parts, url", zip(TEST_DID_URL_PARTS, TEST_DID_URLS))
def test_as_str(parts, url):
    assert DIDUrl.as_str(**parts) == url


@pytest.mark.parametrize("url", TEST_DID_URLS)
def test_is_valid(url):
    assert DIDUrl.is_valid(url)


@pytest.mark.parametrize("bad_url", [TEST_DID0, "not a did url"])
def test_is_valid_x(bad_url):
    assert not DIDUrl.is_valid(bad_url)
