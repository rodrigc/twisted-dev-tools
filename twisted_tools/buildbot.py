import os, sys
import urllib
import treq
import twisted

USER_AGENT = (
    "force-builds (%(name)s; %(platform)s) Twisted/%(twisted)s "
    "Python/%(python)s" % dict(
        name=os.name, platform=sys.platform,
        twisted=twisted.__version__, python=hex(sys.hexversion)))



def forceBuild(url, args, reactor=None):
    """
    Force a build of a given branch.

    @return: URL where build results can be found.
    """

    url = url + b"builders/_all/forceall"
    url = url + '?' + '&'.join([k + '=' + urllib.quote(v) for (k, v) in args])
    headers = {'user-agent': [USER_AGENT]}
    return treq.get(url, headers, reactor=reactor)
