#!/usr/bin/python
import os, sys

PARAM_FS = '|'

dic = {'key':1}
del dic['key']

fields = [
'twitter.user.statuses_count',
'twitter.user.screen_name',
'twitter.user.profile_image_url',
'twitter.user.lang',
'twitter.user.id_str',
'twitter.user.id',
'twitter.user.created_at',
'twitter.text',
'twitter.source',
'twitter.id',
'twitter.filter_level',
'twitter.created_at',
'interaction.type',
'interaction.source',
'interaction.schema.version',
'interaction.link',
'interaction.id',
'interaction.created_at',
'interaction.content',
'interaction.author.username',
'interaction.author.link',
'interaction.author.id',
'interaction.author.avatar',
'TweetRange',
'TweetID',
'language.tag',
'language.confidence',
'twitter.user.followers_count',
'twitter.user.name',
'interaction.author.name',
'klout.score',
'twitter.user.friends_count',
'twitter.links.0',
'twitter.domains.0',
'links.url.0',
'links.created_at.0',
'links.code.0',
'twitter.user.description',
'links.normalized_url.0',
'links.meta.lang.0',
'links.meta.content_type.0',
'links.meta.charset.0',
'links.title.0',
'links.hops.0.0',
'twitter.lang',
'links.hops.0.1',
'twitter.user.location',
'twitter.user.time_zone',
'twitter.user.utc_offset',
'links.meta.description.0',
'links.meta.opengraph.0.type',
'links.meta.opengraph.0.image',
'links.meta.opengraph.0.title',
'links.meta.keywords.0.0',
'links.meta.keywords.0.1',
'interaction.author.language',
'links.meta.opengraph.0.url',
'twitter.user.url',
'links.meta.opengraph.0.site_name',
'links.meta.opengraph.0.description',
'links.domain.0',
'twitter.user.listed_count',
'twitter.user.favourites_count',
'meta.audit_trail.factory.ts',
'twitter.user.geo_enabled',
'links.meta.keywords.0.2',
'demographic.gender',
'links.meta.keywords.0.3',
'meta.audit_trail.links.post_ts',
'links.meta.keywords.0.4',
'meta.audit_trail.links.pre_ts',
'twitter.hashtags.0'
]

head = '%s'%(PARAM_FS)
for f in fields:
    head = '%s%s%s' % (head, f, PARAM_FS)
print head

for line in open('a66c0c8e-94f6-42e9-95af-ee51e8dc1f9f_000000'):
    line = line.replace('\n','')
    es = line.split("\x02")
    for e in es:
        tmp = e.split('\x03')
        (k,v) = (tmp[0], tmp[1])
        if k in fields:
            dic[k] = v

    res = '%s'%(PARAM_FS) 
    for f in fields:
        if dic.has_key(f):
            res = '%s%s%s'%(res, dic[f], PARAM_FS)#.split(':\"')[1].replace('\"}',''))
            #print '%s \t %s' % (f, dic[f])
            del dic[f]
        else:
            res = '%sNA%s' % (res, PARAM_FS)
            #print '%s \t NA' % (f)
    print res
