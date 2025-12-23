package pract_5

fun main() {
    println("task_1")

    val cat = Cat()
    cat.randomAction()
    cat.randomAction()
    cat.randomAction()


    println("\n\ntask_2")

    val student = Student()

    student.setfirstName("  Nikita  ")
    student.setlastName(" pavlov")
    student.setScores(intArrayOf(5, 4, 3, 2, 2, 3, 4, 5, 5, 5))

    student.addScore(4)

    println(student.getfirstName())
    println(student.getlastName())
    println(student.getScores().contentToString())
    println(student.getAverageScore())


    println("\n\ntask_3")

    val student1 = Student().apply {
        setfirstName("иван")
        setlastName("петров")
        setScores(intArrayOf(5, 5, 5, 5, 5, 5, 5, 5, 5, 5)) // средний: 5.0
    }

    val student2 = Student().apply {
        setfirstName("анна")
        setlastName("сидорова")
        setScores(intArrayOf(4, 4, 4, 4, 4, 4, 4, 4, 4, 4)) // средний: 4.0
    }

    val student3 = Student().apply {
        setfirstName("петр")
        setlastName("иванов")
        setScores(intArrayOf(5, 4, 5, 4, 5, 4, 5, 4, 5, 4)) // средний: 4.5
    }

    val students = arrayOf(student1, student2, student3)
    val studentService = StudentService()

    val bestStudent = studentService.findBestStudent(students)
    println("Лучший студент: ${bestStudent?.getfirstName()} ${bestStudent?.getlastName()}")
    println("Средний балл: ${bestStudent?.getAverageScore()}")

    val sortedStudents = studentService.sortStudentsByLastName(students)
    println("\nСтуденты отсортированные по фамилии:")
    sortedStudents.forEach {
        println("${it.getlastName()} ${it.getfirstName()}")
    }
}