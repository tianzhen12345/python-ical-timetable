# 一个重庆邮电大学的实现作为参考，代码不再包含任何其他注释

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
# 		{
# 			"judge": ("风华" in loc) or (loc == "运动场1"),
# 			"text": r"""LOCATION:风华运动场\n南山街道重庆邮电大学5栋
# X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=风华运动场\\n南山街道重庆邮电大学5栋:geo:29.532757,106.607510"""
# 		},
# 		{
# 			"judge": "太极" in loc,
# 			"text": r"""LOCATION:重庆邮电大学-太极体育场\n崇文路2号重庆邮电大学内
# X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学-太极体育场\\n崇文路2号重庆邮电大学内:geo:29.532940,106.609072"""
# 		},
# 		{
# 			"judge": "乒乓球" in loc,
# 			"text": r"""LOCATION:风雨操场(乒乓球馆)\n崇文路2号重庆邮电大学内
# X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=风雨操场(乒乓球馆)\\n崇文路2号重庆邮电大学内:geo:29.534230,106.608516"""
# 		},
# 		{
# 			"judge": ("篮球" in loc) or ("排球" in loc),
# 			"text": r"""LOCATION:重庆邮电学院篮球排球馆\n崇文路2号重庆邮电大学内
# X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电学院篮球排球馆\\n崇文路2号重庆邮电大学内:geo:29.534025,106.609148"""
# 		},
# 		{
# 			"judge": ("综合实验" in loc) or ("实验实训楼" in loc),
# 			"text": r"""LOCATION:重庆邮电大学综合实验大楼\n南山路新力村
# X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学综合实验大楼\\n南山路新力村:geo:29.524289,106.605595"""
# 		},
# 		{
# 			"judge": loc[0] == "1",
# 			"text": r"""LOCATION:重庆邮电大学-光电工程学院\n崇文路2号重庆邮电大学内
# X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学-光电工程学院\\n崇文路2号重庆邮电大学内:geo:29.531478,106.605921"""
# 		},
# 		{
# 			"judge": loc[0] == "2",
# 			"text": r"""LOCATION:重庆邮电大学二教学楼\n崇文路2号重庆邮电大学内
# X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学二教学楼\\n崇文路2号重庆邮电大学内:geo:29.532703,106.606747"""
# 		},
# 		{
# 			"judge": loc[0] == "3",
# 			"text": r"""LOCATION:重庆邮电大学第三教学楼\n崇文路2号
# X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学第三教学楼\\n崇文路2号:geo:29.535119,106.609114"""
# 		},
# 		{
# 			"judge": loc[0] == "4",
# 			"text": r"""LOCATION:重庆邮电大学第四教学楼\n崇文路2号
# X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学第四教学楼\\n崇文路2号:geo:29.536107,106.608759"""
# 		},
# 		{
# 			"judge": loc[0] == "5",
# 			"text": r"""LOCATION:重庆邮电大学-国际学院\n崇文路2号重庆邮电大学内
# X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学-国际学院\\n崇文路2号重庆邮电大学内:geo:29.536131,106.610090"""
# 		},
# 		{
# 			"judge": loc[0] == "8",
# 			"text": r"""LOCATION:重庆邮电大学八教学楼A栋\n崇文路2号重庆邮电大学内
# X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学八教学楼A栋\\n崇文路2号重庆邮电大学内:geo:29.535322,106.611020"""
# 		},
# 		{
# 			"judge": True,
# 			"text": r"""LOCATION:重庆邮电大学\n崇文路2号
# X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学\\n崇文路2号:geo:29.530807,106.607617"""
# 		}
	]

	def geo(classroom):
		loc = ""
		for place in school.AppleMaps(classroom):
			if place["judge"]:
				loc = place["text"]
				break
		return loc