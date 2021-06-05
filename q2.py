class Hit(models.Model):

    PAGEVIEW = 'PV'
    DOWNLOAD = 'DL'
    ACTIONS = (
        (PAGEVIEW, 'Article web page view'),
        (DOWNLOAD, 'Article download'),
    )

    publication = models.ForeignKey('Publication', on_delete=models.CASCADE)
    date = models.DateTimeField(default=django.utils.timezone.now)
    ip_address = models.GenericIPAddressField()
    user_agent = models.ForeignKey('UserAgent', on_delete=models.SET_NULL,
                                   null=True, blank=True)
    action = models.CharField(max_length=2, choices=ACTIONS)

class Publication(models.Model):

    title = models.CharField(max_length=200)
    journal = models.ForeignKey('Journal', on_delete=models.CASCADE)
    # ... remaining fields omitted

    def get_all_hits(self): # this method will get all hits with views and downloads for a single publication
        all_hits = self.hit_set.all()
        return {"views":all_hits.filter(action=Hit.PAGEVIEW).count(),
                "downloads":all_hits.filter(action=Hit.DOWNLOAD).count()}


class Journal(models.Model):
    title = models.CharField(max_length=200)
    # ... remaining fields omitted

def get_journal_statistics(journal_id):
    # Construct summary dict in the form {journal_id -> (total_views, total_downloads)}
    journals = Journal.objects.all()
    summary = {}
    for journal in journals:
        publications = Publication.objects.filter(journal = journal)
        total_views=0 
        total_downloads=0
        for i in publications:
            publication_result = i.get_all_hits() # model method::please check in Publication model
            total_views+= publication_result['views']
            total_downloads+= publication_result['downloads']
            summary[journal.id]={"total_views":total_views , "total_downloads":total_downloads}
    return summary

