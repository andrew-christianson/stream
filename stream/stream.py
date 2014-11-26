import csv
import pandas
import ast

def _norp(fp_or_fn, encoding="UTF-8"):
    if hasattr(fp_or_fn, "read"): # is a file-like
        def fp():
            fp_or_fn.seek(0)
            return fp_or_fn
        restartable = False
    else:
        fp = lambda : open(fp_or_fn, "r", encoding=encoding)
        restartable = True
    return fp,restartable

def _pytype(istr):
    try:
        return ast.literal_eval(istr)
    except:
        return istr

class Stream(object):

    def __init__(self, ffp, ffd, csize=100):
        self.ffd = ffd
        self.ffp = ffp
        self.csize = csize
    
    def data(self, raw=False):
        # with self.ffp() as fp:
        try:
            fp = self.ffp()
            diter = self.ffd(fp)
            data = []
            for datum in diter:
                if len(data) < self.csize:
                    data.append(datum)
                else:
                    if not raw:
                        yield pandas.DataFrame.from_records(data)
                    else:
                        yield data
                    data = [datum]
            if not raw:
                yield pandas.DataFrame.from_records(data)
            else:
                yield data
        finally:
            if self.restartable:
                fp.close()
            else:
                pass

    def map(self, fn):
        for i in self.data():
            yield fn(data)

    def __getitem__(self, item, raw=False):
        for i in self.data(raw=raw):
            yield i.ix[item]
    
    @classmethod
    def Lines(cls, fp_or_fn, encoding="UTF-8", **kwargs):
        fp, restartable = _norp(fp_or_fn, encoding=encoding)
        di = lambda f : f

        out = cls(fp, di, **kwargs)
        out.restartable = restartable
        return out

    @classmethod
    def CSV(cls, fp_or_fn, encoding="UTF-8", dialect=csv.excel, **kwargs):
        """Chunks data into pandas arrays, does descired computation on those
        arrays, then accumlates
        """
        fp, restartable = _norp(fp_or_fn, encoding)
        di = lambda f : map(lambda row: [_pytype(cell) for cell in row],
                            csv.reader(f, dialect = dialect))

        out = cls(fp, di, **kwargs)
        out.restartable = restartable
        return out

        
    
