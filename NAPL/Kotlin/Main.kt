package kotlincourse

data class Student(val name: String, val age: Int, val email: String?)
data class Course(val code: String, val title: String, val maxStudents: Int) {
    val students = mutableListOf<Student>()

    fun enroll(student: Student): Boolean {
        if (students.size >= maxStudents) return false
        students.add(student)
        return true
    }
}
data class Enrollment(val student: Student, val course: Course, val grade: Int?)

fun main() {
    val students = listOf(
        Student("Aarav", 20, "aarav@school.edu"),
        Student("Ananya", 21, null),
        Student("Rohan", 19, "rohan@school.edu"),
        Student("Isha", 22, null),
        Student("Meera", 18, "meera@school.edu"),
        Student("Arjun", 21, null),
        Student("Priya", 19, "priya@school.edu")
    )
    val math = Course("MATH101", "Calculus", 4)
    val physics = Course("PHYS101", "Physics", 3)
    students.take(4).forEach { math.enroll(it) }
    students.drop(4).forEach { physics.enroll(it) }

    val enrollments = listOf(
        Enrollment(students[0], math, 85), Enrollment(students[1], math, null),
        Enrollment(students[2], math, 78), Enrollment(students[3], math, 92),
        Enrollment(students[4], physics, 88), Enrollment(students[5], physics, null),
        Enrollment(students[6], physics, 75)
    )

    val email = students[1].email ?: "no email"
    val graded = enrollments.filter { it.grade != null }
    val grades = graded.map { it.grade ?: 0 }
    println("Ananya's email: $email")
    println("Students: ${enrollments.map { it.student.name }}")
    println("Total grades: ${grades.sum()}")
    println("Math students by age: ${math.students.groupBy { it.age }}")
    println("Average grade: ${graded.averageGrade()}")
    println(students[0].fullInfo())

    val report = ReportBuilder()
    report.title("Course Registration Report")
    report.line("Math students: ${math.students.size}")
    report.line("Physics students: ${physics.students.size}")
    report.print()
}

fun Student.fullInfo(): String = "$name, age $age, ${email ?: "no email"}"

fun List<Enrollment>.averageGrade(): Double {
    val grades = mapNotNull { it.grade }
    return if (grades.isEmpty()) 0.0 else grades.average()
}

class ReportBuilder {
    private var title = ""
    private val lines = mutableListOf<String>()

    fun title(value: String) { title = value }
    fun line(value: String) { lines.add(value) }

    fun print() {
        println("=== $title ===")
        lines.forEach { println(it) }
    }
}
