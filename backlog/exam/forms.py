from django import forms
dept_choices = (
    ("dummy", "Select Department"),
    ("1st year", "1st year"),
    ("CSE", "CSE"),
    ("ECE", "ECE"),
    ("AS", "AS"),
    ("MECH", "MECH"),
    ("BCA", "BCA"),
)
exam_choices = (
    ("dummy", "Select Exam"),
    ("backlog", "Backlog Exam"),
    ("improvement", "Improvement Exam"),
    ("year_back", "Year back Exam"),
)
sem_choices = (
    ("dummy", "Select Sem"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
)

sub_cse = (
    ("dummy", "Select Subject"),
    ("DBMS", "Database Management System"),
    ("OS", "Operating System"),
)
code_cse = (("DBMS", "16CS302"), ("OS", "16CS303"))


class s_form(forms.Form):

    # dept = forms.CharField()
    dept = forms.ChoiceField(choices=dept_choices)
    exam_type = forms.ChoiceField(choices=exam_choices)
    sem = forms.ChoiceField(choices=sem_choices)
    subject = forms.ChoiceField(choices=sub_cse)
    subject_code = forms.ChoiceField(choices=code_cse)
