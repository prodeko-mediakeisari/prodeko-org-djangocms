from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField


class Virka(models.Model):
    """ Position in the elections.
    """

    is_hallitus = models.BooleanField(default=False, verbose_name=_("Board"))
    name = models.CharField(max_length=50, unique=True, verbose_name=_("Position"))
    description = models.TextField(default="", verbose_name=_("Description"))
    read_by = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, verbose_name=_("Read by")
    )

    def __str__(self):
        return f"{self.name}"

    def natural_key(self):
        return self.name

    class Meta:
        # Correct spelling in Django admin
        verbose_name = _("position")
        verbose_name_plural = _("Positions")


class Ehdokas(models.Model):
    """ Applicant in the elections.
    """

    id = models.AutoField(primary_key=True)
    auth_prodeko_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    introduction = RichTextField()
    virka = models.ForeignKey(Virka, on_delete=models.CASCADE, related_name="ehdokkaat")
    pic = ThumbnailerImageField(
        blank=True,
        upload_to="app_vaalit/ehdokas_photos",
        default="images/toimari_photos/placeholder.jpg",
        verbose_name=_("Picture"),
    )

    def natural_key(self):
        """ String based representation of this object when accessed through
        foreign keys.

        In views.py get_ehdokkaat_json() method the serialize has
        use_natural_foreign_keys=True and as a result the foreign key virka
        field is example.user@prodeko.org as opposed to an integer value as
        it is in the database.
        """
        return self.auth_prodeko_user

    def __str__(self):
        v = self.virka
        nimi = self.name
        return f"{v}, {nimi}"

    class Meta:
        # Correct spelling in Django admin
        verbose_name = _("applicant")
        verbose_name_plural = _("Applicants")
        unique_together = ("auth_prodeko_user", "virka")


class Kysymys(models.Model):
    """ Question assigned to a specific candidate (Ehdokas).
    """

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )
    to_virka = models.ForeignKey(
        Virka, on_delete=models.CASCADE, related_name=_("questions")
    )
    question = models.TextField(blank=False, verbose_name=_("Question"))

    def __str__(self):
        return f"{self.to_virka}"

    class Meta:
        # Correct spelling in Django admin
        verbose_name = _("question")
        verbose_name_plural = _("Questions")
        # Order by most recently created first
        ordering = ["-created_at"]


class Vastaus(models.Model):
    """ Answer to a spesific question by a specific candidate.
    """

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    by_ehdokas = models.ForeignKey(
        Ehdokas, blank=True, on_delete=models.CASCADE, related_name=_("answered_by")
    )
    to_question = models.ForeignKey(
        Kysymys, blank=True, on_delete=models.CASCADE, related_name=_("answers")
    )
    answer = models.TextField(blank=False, verbose_name=_("Answer"))

    def __str__(self):
        return f"{self.by_ehdokas}"

    class Meta:
        # Correct spelling in Django admin
        verbose_name = _("answer")
        verbose_name_plural = _("Answers")
        # Order by most recently created first
        ordering = ["-created_at"]
