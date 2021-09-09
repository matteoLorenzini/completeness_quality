from sickle import Sickle


sickle = Sickle('http://www.culturaitalia.it/oaiProviderCI/OAIHandler')

recs = sickle.ListRecords(metadataPrefix="pico", set="mura_fort")
for r in recs:
    print (r)

