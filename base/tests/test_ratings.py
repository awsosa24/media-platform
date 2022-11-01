import pytest
import os.path
from django.core.management import call_command


@pytest.mark.str
def test_contents_news_str(contents_news):
    """
    Test channel_fox from fixtures
    """
    assert contents_news.__str__() == "News|4"


@pytest.mark.str
def test_channel_fox_str(channel_fox):
    """
    Test channel_fox from fixtures
    """
    assert channel_fox.__str__() == "Fox"


@pytest.mark.ratings
def test_channel_fox(channel_fox):
    """
    Test channel_fox from fixtures
    """
    assert channel_fox.avg_rating == 8.5


@pytest.mark.ratings
def test_channel_news(channel_news):
    """
    Test channel_news from fixtures
    """
    assert channel_news.avg_rating == 4


@pytest.mark.ratings
def test_channel_network(channel_network):
    """
    Test channel_network from fixtures
    """
    assert channel_network.avg_rating == 7


@pytest.mark.str
def test_command_rating(channel_fox):
    """
    Test channel_fox from fixtures
    """
    call_command('channels_ratings')
    assert os.path.isfile('base/tmp/ratings.csv') == True
