"""School Module"""


from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Student:
    """Class Student"""
    name: str


@dataclass
class Subject:
    """Class Subject"""
    name: str


@dataclass
class GradeRecord:
    """class to save grade record"""
    student: Student
    subject: Subject
    grade: int


@dataclass
class StudentJournal:
    """Class Journal"""
    records: list[GradeRecord]

    def get_records_by_student(self, student_name: str) -> list[GradeRecord]:
        """Get records by Student"""
        records_by_student = []

        for record in self.records:
            if record.student.name == student_name:
                records_by_student.append(record)

        return records_by_student

    def get_records_by_subject(self, subject_name: str) -> list[GradeRecord]:
        """Get records by subject"""
        subject_records = []

        for record in self.records:
            if record.subject.name == subject_name:
                subject_records.append(record)

        return subject_records


class Statistics(ABC):
    """Class Statistik"""
    @abstractmethod
    def calculate(self, records: list[GradeRecord]) -> float:
        """_summary_

        Args:
            records (list[GradeRecord]): _description_
        """


class AverageStatistic(Statistics):
    """Class to get average"""

    def calculate(self, records: list[GradeRecord]) -> float:
        """Calculate average"""
        if not records:
            raise ValueError("Grade List is empty!")

        total_grades = 0

        for record in records:
            total_grades += record.grade

        return total_grades / len(records)


class Notifier(ABC):
    """Class Notifier"""
    @abstractmethod
    def notify(self, msg: str):
        """method notify"""


class ConsoleNotifier(Notifier):
    """Class Console Notifier"""

    def notify(self, msg: str):
        print(msg)


@dataclass
class Monitoring:
    """Class Monitoring"""
    statistics: Statistics
    notifier: Notifier

    threshold: float = 3.5

    def check_student_average(self, records: list[GradeRecord]) -> None:
        """_summary_"""
        average = self.statistics.calculate(records)

        if average < self.threshold:
            self.notifier.notify(f"Average is less than {self.threshold}")


student = Student(name="Daniel")
subject_math = Subject(name="Math")
subject_python = Subject(name="Python")

grade_records = [
    GradeRecord(student=student, subject=subject_math, grade=3),
    GradeRecord(student=student, subject=subject_python, grade=4),
    GradeRecord(student=student, subject=subject_math, grade=2),
]

journal = StudentJournal(records=grade_records)

student_records = journal.get_records_by_student("Daniel")

statistics = AverageStatistic()
notifier = ConsoleNotifier()

monitoring = Monitoring(
    statistics=statistics,
    notifier=notifier,
)

monitoring.check_student_average(student_records)

student2 = Student(name="Anna")

grade_records = [
    GradeRecord(student=student, subject=subject_math, grade=2),
    GradeRecord(student=student2, subject=subject_math, grade=5),
]

journal = StudentJournal(records=grade_records)

student2_records = journal.get_records_by_student("Daniel")

print(student2_records)
