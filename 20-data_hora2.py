# -*- coding: utf-8 -*-
import datetime

t = datetime.time(1, 2, 3)
print t
print 'hora  :', t.hour
print 'minuto:', t.minute
print 'segundo:', t.second
print 'micro segundo:', t.microsecond

print 'Mais antigas  :', datetime.time.min
print 'Últimas    :', datetime.time.max
print 'Resolução:', datetime.time.resolution

for m in [ 1, 0, 0.1, 0.6 ]:
    try:
        print '%02.1f :' % m, datetime.time(0, 0, 0, microsecond=m)
    except TypeError, err:
        print 'ERROR:', err

today = datetime.date.today()
print today
print 'ctime:', today.ctime()
print 'tuple:', today.timetuple()
print 'ordinal:', today.toordinal()
print 'Ano:', today.year
print 'Mês :', today.month
print 'Dia :', today.day

d1 = datetime.date(2008, 3, 12)
print 'd1:', d1

d2 = d1.replace(year=2009)
print 'd2:', d2

print "microsegundos:", datetime.timedelta(microseconds=1)
print "millisegundos:", datetime.timedelta(milliseconds=1)
print "segundos     :", datetime.timedelta(seconds=1)
print "minutos     :", datetime.timedelta(minutes=1)
print "houras       :", datetime.timedelta(hours=1)
print "dias        :", datetime.timedelta(days=1)
print "semanas       :", datetime.timedelta(weeks=1)

today = datetime.date.today()
print 'Hoje    :', today

one_day = datetime.timedelta(days=1)
print 'Um Dia  :', one_day

yesterday = today - one_day
print 'Ontem:', yesterday

tomorrow = today + one_day
print 'Amanhã :', tomorrow

print 'amanhã - ontem:', tomorrow - yesterday
print 'ontem - amanhã:', yesterday - tomorrow

print 'Agora    :', datetime.datetime.now()
print 'Hoje  :', datetime.datetime.today()
print 'UTC Agora:', datetime.datetime.utcnow()

d = datetime.datetime.now()
for attr in [ 'year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
    print attr, ':', getattr(d, attr)

format = "%a %b %d %H:%M:%S %Y"

today = datetime.datetime.today()
print 'ISO     :', today

s = today.strftime(format)
print 'strftime:', s

d = datetime.datetime.strptime(s, format)
print 'strptime:', d.strftime(format)