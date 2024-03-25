class BMI:
    def __init__(self, tinggi_kaki, berat_pound):
        self.tinggi_kaki = tinggi_kaki
        self.berat_pound = berat_pound

    def BMI_value(self):
        tinggi_meter = self.tinggi_kaki * 0.3048  # konversu kaki ke meter utk hitung bmi
        berat_kg = self.berat_pound * 0.453592  # konversi pound ke kg
        bmi = berat_kg / (tinggi_meter ** 2)  # Calculate BMI
        return bmi

    def __eq__(self, other):
        if isinstance(other, BMI):
            return (self.tinggi_kaki == other.tinggi_kaki) and (self.berat_pound == other.berat_pound)
        return False

bmi1 = BMI(6, 150)  
bmi2 = BMI(5.8, 140)  # tinggi dlm kaki, berat dalam pound
bmi3 = BMI(6, 150)  #dibuat sama sperti bmi1 untuk cek nanti

print("BMI pertama:", bmi1.BMI_value())
print("BMI kedua:", bmi2.BMI_value())

print("BMI pertama sama dengan kedua:", bmi1 == bmi2)
print("BMI pertama sama dengan ketiga:", bmi1 == bmi3)
