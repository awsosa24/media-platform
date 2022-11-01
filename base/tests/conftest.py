import pytest
from base.models import Channel, Content


@pytest.fixture()
def contents_shows(db):
    content_simpsons = Content.objects.create(name="The Simpsons", rating=8)
    content_futurama = Content.objects.create(name="Futurama", rating=9)
    return [content_simpsons, content_futurama]


@pytest.fixture()
def contents_news(db):
    content_news = Content.objects.create(name="News", rating=4)
    return content_news


@pytest.fixture()
def channel_fox(db, contents_shows):
    channel_fox = Channel.objects.create(
        title='Fox',
    )
    channel_fox.contents.set(contents_shows)
    return channel_fox


@pytest.fixture()
def channel_news(db, contents_news):
    channel_news = Channel.objects.create(
        title='News',
    )
    channel_news.contents.set([contents_news])
    return channel_news


@pytest.fixture()
def channel_network(db, contents_shows, channel_fox, channel_news):
    """
    channel_network has subchannels and content
    """
    channel_music = Channel.objects.create(
        title='Music',
    )
    channel_network = Channel.objects.create(
        title='Network',
    )
    channel_network.subchannels.set([channel_fox, channel_news, channel_music])
    channel_network.contents.set(contents_shows)
    return channel_network
