#### PART 1 ####
# final_grade: Calculates the final grade for each student, and writes the output (while eliminating illegal
# rows from the input file) into the file in `output_path`. Returns the average of the grades.
#   input_path: Path to the file that contains the input
#   output_path: Path to the file that will contain the output

def final_grade(input_path: str, output_path: str) -> int:
    input_file = open(input_path, "r")
    output_file = open(output_path, "w")
    output_records = {}
    grades = {}
    lines = input_file.readlines()
    for element in lines:
        line_elements = element.split(",")
        if not is_valid_record(line_elements):
            continue
        line_elements = clean(line_elements)
        numeric_id = int(line_elements[0])
        numeric_hw_grade = int(line_elements[1])
        total_grade = int((numeric_id % 100 + numeric_hw_grade) / 2)
        grades[numeric_id] = total_grade
        line_elements.append(str(total_grade) + "\n")
        line_elements[0] += ", "
        line_elements[1] += ", "
        current_record = ''.join(line_elements)
        output_records[line_elements[0]] = current_record

    for key in sorted(output_records.keys()):
        output_file.write(output_records[key])
    average = 0
    for grade in grades.values():
        average += grade
    input_file.close()
    output_file.close()
    return int(average / len(grades))


def clean(record: list) -> list:
    record[0] = record[0].strip()
    record.remove(record[1])
    record.remove(record[1])
    record[1] = record[1].split("\n")[0]
    record[1] = record[1].strip()
    return record


def is_valid_record(record: list) -> bool:
    id_trimmed = len((record[0]).split()[0])
    if record[0].startswith('0') or id_trimmed != 8:
        return False
    for c in record[1]:
        if not (c.isalpha() or c == " "):
            return False
    if int(record[2]) < 1:
        return False
    average = int(record[3].split("\n")[0])
    if not (50 < average <= 100):
        return False
    return True


#### PART 2 ####
# check_strings: Checks if `s1` can be constructed from `s2`'s characters.
#   s1: The string that we want to check if it can be constructed
#   s2: The string that we want to construct s1 from
def check_strings(s1: str, s2: str) -> bool:
    letters_hist = build_hist(s1)
    for c in s2:
        if c.lower() in letters_hist.keys():
            letters_hist[c.lower()] -= 1
    for i in letters_hist.values():
        if i > 0:
            return False
    return True


def build_hist(s1: str) -> dict:
    letters_hist = dict((c, 0) for c in s1.lower())
    for c in s1:
        if c.isalpha():
            letters_hist[c.lower()] += 1
    return letters_hist
