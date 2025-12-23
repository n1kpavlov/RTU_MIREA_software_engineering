package pract_5

class StudentService {
    fun findBestStudent(students: Array<Student>): Student? {
        if (students.isEmpty()) return null

        var bestStudent = students[0]
        var maxAverage = bestStudent.getAverageScore()

        for (i in 1..students.size - 1) {
            val currentAverage = students[i].getAverageScore()
            if (currentAverage > maxAverage) {
                maxAverage = currentAverage
                bestStudent = students[i]
            }
        }

        return bestStudent
    }

    fun sortStudentsByLastName(students: Array<Student>): Array<Student> {
        return students.sortedBy { it.getlastName() }.toTypedArray()
    }
}