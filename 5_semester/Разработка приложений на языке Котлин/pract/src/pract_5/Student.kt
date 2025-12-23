package pract_5

class Student {
    private var firstName: String = ""
        get() = field.replaceFirstChar { it.uppercase() }
        set(value) { field = value.trim() }
    private var lastName: String = ""
        get() = field.replaceFirstChar { it.uppercase() }
        set(value) { field = value.trim() }
    private var scores: IntArray = IntArray(10)

    fun setfirstName(value: String) {
        this.firstName = value
    }

    fun getfirstName(): String {
        return this.firstName
    }

    fun setlastName(value: String) {
        this.lastName = value
    }

    fun getlastName(): String {
        return this.lastName
    }

    fun getScores(): IntArray = scores.copyOf()

    fun setScores(newScores: IntArray) {
        scores = newScores.copyOf()
    }

    fun addScore(newScore: Int) {
        for (i in 0..scores.size - 2) {
            scores[i] = scores[i + 1]
        }
        scores[scores.size - 1] = newScore
    }

    fun getAverageScore(): Double {
        return if (scores.isEmpty()) 0.0
        else scores.average()
    }
}