{
	'name' :"Student management",
	'summary':"manage student information like name and age",
	'author':"safa",
	'installable':True,
	'application':True,
	'depends':['base'],
        'data':[
		"views/student_views.xml",
		"views/student_inherit_views.xml",
		"views/course_views.xml",
		"reports/student_report.xml",
		"security/ir.model.access.csv"
	],
}