import Mdutils

course_number = 'ENGE 511'
section = 'A'
title = 'Rhetorical Theory II—Contemporary Rhetoric'
prerequisite = 'N/A'
materials_1 = "text 1"
materials_2 = "text 2"
materials_3 = "text 3"
professor = 'Albus Dumbledore'
title = 'Associate Professor'
office = 'Tower Hall, S-306'
phone = '1234567899'
email = 'testing@joe_blow.com'


mdFile = MdUtils(file_name="python_script_to_markdown_testing", title="Testing, yo!")
mdFile.new_header(level=3, title='USF Mission Statement')
mdFile.new_paragraph("As a Catholic university rooted in the liberal arts, we are a welcoming community of learners challenged by Franciscan values and charism, engaged in a continuous pursuit of knowledge, faith, wisdom, and justice, and ever mindful of a tradition that emphasizes reverence for creation, compassion, and peacemaking. We strive for academic excellence in all programs, preparing women and men to contribute to the world through service and leadership.")
mdFile.new_header(level=3, title="College of Arts and Sciences Mission Statement available [here](https://www.stfrancis.edu/arts-sciences/)")
mdFile.new_header(level=3, title="Course Objectives/Outcomes:")
mdFile.new_paragraph("By the end of this course the student will be able to:", bold_italics_code='bi')
mdFile.new_header(level=3, title="Course Requirements":)
*By the end of this course the student will be able to:*

*Course Requirements:* 

*Students will be expected to:*

*Course Schedule/Outline:*

Provide detail on course schedule or outline, including modules, dates, or weeks for readings, due dates for assignments, etc.

*Methods of Evaluation:*

Explain evaluation methods

*Grading Scale:*

*Course Evaluations/Surveys:*

Information gleaned from course evaluations is an important part of maintaining quality and continuous improvement in courses. The University's expects students to thoughtfully participate in this anonymous evaluation process.













mdFile.create_md_file()










