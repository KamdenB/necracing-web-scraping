class neca_filter:
    def filter(arr):
        res = []
        months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
        for x in arr:
            if any(month in x for months in month):
                res.append(x)
        return res