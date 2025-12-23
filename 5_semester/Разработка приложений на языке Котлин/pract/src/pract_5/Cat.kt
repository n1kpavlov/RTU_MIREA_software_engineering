package pract_5
import kotlin.random.Random

class Cat {
    private fun rest() {
        println("Sleep")
    }

    private fun voice() {
        println("Meow")
    }

    private fun feed() {
        println("Eat")
    }

    public fun randomAction() {
        val action = Random.nextInt(0, 3)
        when (action) {
            0 -> this.rest()
            1 -> this.voice()
            2 -> this.feed()
        }
    }
}