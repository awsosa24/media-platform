from django.db import models
from django.db.models import Avg
from django.core.validators import MaxValueValidator, MinValueValidator
from .constants import OTHER, FILE_GENRE_CHOICES


class Content(models.Model):
    name = models.CharField(max_length=32)

    # metadata: a set of arbitrary metadata associated with the content
    description = models.CharField(max_length=32, blank=True, null=True)
    author = models.CharField(max_length=32, blank=True, null=True)
    genre = models.CharField(
        max_length=3,
        choices=FILE_GENRE_CHOICES,
        default=OTHER,
    )

    # rating: decimal number between 0 and 10
    rating = models.DecimalField(
        blank=True, null=True,
        max_digits=4, decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    def __str__(self):
        _return = self.name+'|'
        if self.rating:
            _return += str(self.rating)
        return _return


class ContentFile(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    file = models.FileField(upload_to='files')
    # file: can contain files (such as videos, pdfs, or text)
    content = models.ForeignKey(Content, blank=True, null=True, related_name="files", on_delete=models.CASCADE)

    def __str__(self):
        _return = str(self.name)
        return _return


class Channel(models.Model):
    """
    A Channel stores the hierarchical structure. It may have subchannels and contents.
    """
    # TODO: "In case a channel has no subchannels associated within it, it must contain a set of contents."
    # Id like more information about this. There are several paths we can do this, for example:
    # we can validate in a (post/put) serializer that we dont have empty subchannels and content at the same time
    # we can write a postSignal to populate content if case we have no subchannels
    # we can define a default content
    title = models.CharField(max_length=32)
    language = models.CharField(max_length=32, blank=True)
    picture = models.ImageField(upload_to='pics',  blank=True, null=True)
    subchannels = models.ManyToManyField("self", symmetrical=False, blank=True)
    contents = models.ManyToManyField(Content, blank=True)

    @property
    def avg_rating(self):
        channel = Channel.ratings(channel_id=self.id).first()
        rating = getattr(channel, 'average_rating')
        return rating

    def ratings(channel_id=None):
        """
        The rating of a channel is the average of the ratings of all the channels underneath, if
        the channel has no subchannels its rating is the average of the ratings of its contents. If
        a channel has no contents, it does not affect the ratings of its parent since its value is
        undefined.

        If the structure of subchannels has a depth greater than 2, this solution would need a refactor.
        For example, I'd most likely use a query with prefetch_related to subchannels (reduce db queries),
         in order to iterate and get ratings for each channel. I'd consider using Redis to temporarily  store ratings,
         in case we have too many channels.
        """
        channels = Channel.objects.all()

        if channel_id:
            channels = channels.filter(id=channel_id)

        # Channels with only content, no subchannels
        q_contents = channels.filter(subchannels__isnull=True) \
            .annotate(average_rating=Avg('contents__rating'))
        q_channels = q_contents

        # Channels with subchannels
        subchannels = channels.filter(subchannels__isnull=False)
        if subchannels.exists():
            q_subchannels_depth2 = subchannels.filter(
                subchannels__subchannels__isnull=False
            ).annotate(average_rating=Avg('subchannels__subchannels__contents__rating'))
            q_subchannels_depth1 = subchannels.filter(
                subchannels__subchannels__isnull=True
                ).annotate(average_rating=Avg('subchannels__contents__rating'))

            q_subchannels = q_subchannels_depth1.union(q_subchannels_depth2)
            q_channels = q_subchannels.union(q_contents)

        return q_channels.order_by('-average_rating')

    def __str__(self):
        return self.title


class ChannelGroup(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    channels = models.ManyToManyField(Channel, blank=True, related_name='groups')
