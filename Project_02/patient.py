class Patient:
    def __init__(self,name,age:int,disease) -> None:
        self.name = name
        self.age = age
        self.disease = disease
        
    def __str__(self) -> str:
        return f"Patient details: Name - {self.name},Age - {self.age},Disease - {self.disease}"
    
def main():
    patient_1 = Patient("John",23,"Blood Pressure")
    print(patient_1)
    
if __name__ == "__main__":
    main()