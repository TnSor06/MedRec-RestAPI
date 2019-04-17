username - ashutosh, pramod
password - bestrest
------------------------------
Custom id gen
urlhash = models.CharField(max_length=6, null=True, blank=True, unique=True)

# Sample of an ID generator - could be any string/number generator
# For a 6-char field, this one yields 2.1 billion unique IDs
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def save(self):
    if not self.urlhash:
        # Generate ID once, then check the db. If exists, keep trying.
        self.urlhash = id_generator()
        while MyModel.objects.filter(urlhash=self.urlhash).exists():
            self.urlhash = id_generator()
    super(MyModel, self).save()