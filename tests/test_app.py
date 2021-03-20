import flask

from bunny3.bunny import DEFAULT_SEARCH_ENGINE


def test_core_commands_loaded(test_bunny):
    """ Test core commands are loaded """
    assert "Google" in test_bunny.commands
    assert "google" in test_bunny.aliasDict
    assert test_bunny.commands["Google"]["func"].name == "Google"
    assert "List" in test_bunny.commands
    assert "list" in test_bunny.aliasDict
    assert test_bunny.commands["List"]["func"].name == "List"


def test_default(test_client):
    """ Test Flask app redirects to the default search engine given an unknown command argument """
    query = "default"
    resp = test_client.get(query)
    print(resp.location)
    assert resp.location == DEFAULT_SEARCH_ENGINE


def test_google(test_client, test_bunny):
    """ Test Flask app redirects to google given the command argument 'google' """
    assert "Google" in test_bunny.commands
    resp = test_client.get("search?q=g+google")
    google_url = test_bunny.commands["Google"]["func"].url
    assert resp.location == f"{google_url}search?q=google"

    resp = test_client.get("search?q=google")
    google_url = test_bunny.commands["Google"]["func"].url
    assert resp.location == f"{google_url}"


def test_google_regex(test_client, test_bunny):
    """ Test Flask app redirects to google given the regex argument 'gsearch test' """
    resp = test_client.get("search?q=gsearch%20test")
    google_url = test_bunny.commands["Google"]["func"].url
    assert resp.location == f"{google_url}search?q=gsearch+test"


def test_help(test_client):
    test_list(test_client)


def test_list(test_client):
    """ Test Flask app redirects to /list given the command argument 'list' """
    resp = test_client.get("/search?q=list")
    assert resp.status_code == 302
    assert str(resp.location).endswith("/list")

    resp = test_client.get("/search?q=list", follow_redirects=True)
    assert "Bunny3 commands" in str(resp.data)


def test_noargs(test_client):
    """ Test Flask app redirects to default route given no args """
    query = "search?q="
    resp = test_client.get(query)
    assert resp.location.endswith(flask.url_for("default"))


def test_unknown_command(test_client, test_bunny):
    """ Test Flask app redirects to fallback given an unknown command """
    resp = test_client.get("/search?q=unknown")
    assert resp.status_code == 302
    # TODO: Update test once configurable fallback options is added
    google_url = test_bunny.commands["Google"]["func"].url
    assert resp.location == f"{google_url}search?q=unknown"
