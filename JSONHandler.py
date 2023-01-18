class JSONHandler:
    def __init__(self, data: dict):
        self.data = data

    ###--v Utility data v--###
    def getTableType(self):
        return self.data.get("table")

    def getEffectiveDate(self):
        return self.data.get("effectiveDate")

    def getNo(self):
        return self.data.get("no")
    ###--^ Currency data  ^--###

    ###--v Currency data v--###
    def getCurrencyData(self, code: str) -> dict:
        rates = self.data.get("rates")
        return next((x for x in rates if x.code == code), None)

    def getCurrencyName(self, code: str) -> str:
        return self.getCurrencyData(code).get("currency")

    def getCurrencyMid(self, code: str) -> float:
        return self.getCurrencyData(code).get("mid")
    ###--^ Currency data  ^--###
