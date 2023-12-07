class DataValidator:
    
    def check_positive_int(list_of_strings):
        return [num for num in list_of_strings if num.isnumeric()]
    
print(DataValidator.check_positive_int(["123", "asd", "-12", "popo", "90", "1", "0"]))