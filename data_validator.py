class DataValidator:
    
    def check_positive_int(list_of_strings):
        valid_positive_ints = []
        for string in list_of_strings:
            if string.isnumeric():
                valid_positive_ints.append(string)
        return valid_positive_ints
    
    
print(DataValidator.check_positive_int(["123", "asd", "-12", "popo", "90", "1", "0"]))