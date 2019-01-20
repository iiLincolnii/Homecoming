import datetime
now=datetime.datetime.now()
delta=datetime.timedelta(days=1)
endnow=now+datetime.timedelta(days=6)
endnow=str(endnow.strftime('%Y-%m-%d'))
offset=now
while str(offset.strftime('%Y-%m-%d')) != endnow:
    offset += delta
    print(str(offset.strftime('%Y-%m-%d')))
