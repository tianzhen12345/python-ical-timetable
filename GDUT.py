
oeWeek = lambda startWeek, endWeek, mode: [i for i in range(startWeek, endWeek + 1) if (i + mode) % 2 == 0]
rgWeek = lambda startWeek, endWeek: [i for i in range(startWeek, endWeek + 1)]

classes = [
	["工程伦理", "张煜帆", "教2-419", rgWeek(4, 6)+[12], 2, [3, 4]],
	["弹塑性理论及有限元方法（双语）", "陈贡发", "实验2-520", rgWeek(4,19), 2, [10, 12]],
	["岩土塑性力学", "杨雪强", "教2-419", rgWeek(7,11)+rgWeek(13,19), 2, [3, 4]],
	["岩土塑性力学", "杨雪强", "教2-302", rgWeek(7,11)+rgWeek(13,19), 5, [3, 4]],
	["数值分析（公共）", "徐杰", "教2-419", rgWeek(4, 14) ,2, [5, 6, 7]],
	["工程硕士英语", "赖小玉", "教2-522", rgWeek(4, 15), 1, [1, 2]],
	["工程硕士英语", "赖小玉", "教2-522", rgWeek(4, 15), 5, [1, 2]],
	["自然辩证法概论", "王泽榔", "教2-419", rgWeek(4, 11) , 1, [5, 6]]
]

class school:

	name = "gdut"

	classTime = [
		(8, 30), 
		(9, 20), 
		(10, 25), 
		(11, 15), 
		(13, 50), 
		(14, 40), 
		(15, 30), 
		(16, 30), 
		(17, 20), 
		(18, 30), 
		(19, 20), 
		(20, 10)
	]

	classPeriod = 45

	starterDay = [2022, 8, 29]

	AppleMaps = lambda loc: [
		{
			"judge": "教2" in loc,
			"text": r"""LOCATION:广东工业大学大学城校区教学2号楼\n大学城外环西路100号广东工业大学(大学城校区)
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=广东工业大学大学城校区教学2号楼:geo:23.039990,113.398021"""
		},
		{
			"judge": "实验2" in loc,
			"text": r"""LOCATION:广东工业大学-实验2号楼\n大学城外环西路广东工业大学大学城校区
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=广东工业大学-实验2号楼:geo:23.036651,113.399994"""
		}
	]

	def geo(classroom):
		loc = ""
		for place in school.AppleMaps(classroom):
			if place["judge"]:
				loc = place["text"]
				break
		return loc
