import config
import subprocess
import shlex
import timeit
import MySQLdb
import collections
import matplotlib.pyplot as plt

Popen = subprocess.Popen
PIPE = subprocess.PIPE
sql = 'select * from table limit {n}'

def using_subprocess(n):
    p1 = Popen(
        shlex.split(
            'echo {s}'.format(s=sql.format(n=n))), stdout=PIPE, close_fds=True)

    p2 = Popen(
        shlex.split(
            'mysql --host={h} -u {u} --password={p} --database={d}'.format(
                h=config.HOST,
                u=config.USER,
                p=config.PASS,
                d=config.MYDB
                )),
        stdin=p1.stdout, stdout=PIPE, close_fds=True)

    p1.stdout.close()
    out, err = p2.communicate()
    return out

def using_mysqldb(n):
    connection = MySQLdb.connect(
        host = config.HOST, user = config.USER,
        passwd = config.PASS, db = config.MYDB)
    cursor = connection.cursor()

    cursor.execute(sql.format(n=n))
    rows = cursor.fetchall()
    return rows

times = collections.defaultdict(list)
ns = [10**i for i in range(5)]
for n in ns:
    times['using_mysqldb'].append(
        timeit.timeit('m.using_mysqldb({n})'.format(n=n),
                      'import __main__ as m',
                      number = 10))
    times['using_subprocess'].append(
        timeit.timeit('m.using_subprocess({n})'.format(n=n),
                      'import __main__ as m',
                      number = 10))

for name, time in times.iteritems():
    plt.plot(ns, time, label=name)
    # print('{n}: {t}'.format(n=name, t=time))
plt.legend(loc='best')
plt.show() 