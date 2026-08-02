class Currency:
    def __init__(self,rupee=0,aed=0,riyal=0) -> None:
        self.rupee = rupee
        self.aed = aed
        self.riyal = riyal
        
    def __str__(self) -> str:
        return f"{self.rupee} Rupee,{self.aed} AED,{self.riyal} Riyal"
    
    def __add__(self, other):
        rupee = self.rupee + other.rupee
        aed = self.aed + other.aed
        riyal = self.riyal + other.riyal
        return Currency(rupee,aed,riyal)
    
def main():
    abdul = Currency(200,20,40)
    print(abdul)
       
    jabbar = Currency(100,10,20)
    print(jabbar)
    
    total = abdul + jabbar
    print(total)
       
if __name__ == "__main__":
    main()
        