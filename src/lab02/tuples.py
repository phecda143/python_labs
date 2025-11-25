def format_record(rec: tuple[str, str, float]) -> str:
    if len(rec[0]) == 0 or len(rec[1]) == 0:
        """пустое ФИО и пустая группа имеет аргумент правильного типа поэтому ValueError"""
        return "ValueError"
    if type(rec[2]) is not float:
        """неверный тип GPA имеет несоответствующий типа(например int вместо float поэтому TypeError"""
        return "TypeError"
    if isinstance(rec, tuple):
        if (
            isinstance(rec[0], str)
            and isinstance(rec[1], str)
            and isinstance(rec[2], float)
        ):
            name = rec[0].split()
            full_name = name[0][0].upper() + name[0][1:] + " "
            for initials in name[1:]:
                full_name += initials[0].upper() + "."
            return f'{full_name}, гр. {rec[1]}, GPA {"{:.2f}".format(rec[2])}'


print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
