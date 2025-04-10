import json
import os

class StudentManager:
    def __init__(self, filename='students.json'):
        self.filename = filename
        self.students = self.load_from_file()

    def load_from_file(self):
        """从文件加载学生数据"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []

    def save_to_file(self):
        """保存学生数据到文件"""
        with open(self.filename, 'w') as f:
            json.dump(self.students, f, indent=2)

    def add_student(self):
        """添加新学生"""
        student_id = input("请输入学号：")
        if any(s['id'] == student_id for s in self.students):
            print("该学号已存在！")
            return

        name = input("请输入姓名：")
        try:
            math = float(input("请输入数学成绩："))
            english = float(input("请输入英语成绩："))
            science = float(input("请输入科学成绩："))
        except ValueError:
            print("输入错误：成绩必须为数字！")
            return

        self.students.append({
            'id': student_id,
            'name': name,
            'scores': {
                'math': math,
                'english': english,
                'science': science
            }
        })
        self.save_to_file()
        print("学生添加成功！")

    def delete_student(self):
        """删除学生"""
        student_id = input("请输入要删除的学号：")
        for i, s in enumerate(self.students):
            if s['id'] == student_id:
                del self.students[i]
                self.save_to_file()
                print("学生删除成功！")
                return
        print("未找到该学号的学生！")

    def update_scores(self):
        """修改学生成绩"""
        student_id = input("请输入要修改的学号：")
        for s in self.students:
            if s['id'] == student_id:
                try:
                    s['scores']['math'] = float(input("新数学成绩："))
                    s['scores']['english'] = float(input("新英语成绩："))
                    s['scores']['science'] = float(input("新科学成绩："))
                    self.save_to_file()
                    print("成绩修改成功！")
                except ValueError:
                    print("输入错误：成绩必须为数字！")
                return
        print("未找到该学号的学生！")

    def query_student(self):
        """查询学生信息"""
        student_id = input("请输入要查询的学号：")
        for s in self.students:
            if s['id'] == student_id:
                print("\n学生信息：")
                print(f"学号：{s['id']}")
                print(f"姓名：{s['name']}")
                print("成绩：")
                for subject, score in s['scores'].items():
                    print(f"  {subject}: {score}")
                return
        print("未找到该学号的学生！")

    def show_all(self):
        """显示所有学生"""
        if not self.students:
            print("当前没有学生记录")
            return

        print("\n所有学生信息：")
        for s in self.students:
            avg_score = sum(s['scores'].values()) / 3
            print(f"{s['id']} {s['name']} 平均分：{avg_score:.1f}")

def main():
    manager = StudentManager()
    
    while True:
        print("\n学生成绩管理系统")
        print("1. 添加学生")
        print("2. 删除学生")
        print("3. 修改成绩")
        print("4. 查询学生")
        print("5. 显示所有")
        print("6. 退出系统")
        
        choice = input("请输入选项（1-6）：")
        
        if choice == '1':
            manager.add_student()
        elif choice == '2':
            manager.delete_student()
        elif choice == '3':
            manager.update_scores()
        elif choice == '4':
            manager.query_student()
        elif choice == '5':
            manager.show_all()
        elif choice == '6':
            print("感谢使用！")
            break
        else:
            print("无效的输入，请重新选择！")

if __name__ == "__main__":
    main()