package pract_6
import pract_6.banking.Atm

fun main() {
    println("task_1")

    val time1 = TimeMeasure(12, 34, 17)
    time1.display24HourFormat()
    time1.addTime(1, 1, 1)
    time1.display12HourFormat()
    println()

    val time2 = TimeMeasure(23, 17)
    time2.display24HourFormat()
    time2.display12HourFormat()
    println()

    val time3 = TimeMeasure(8)
    time3.display24HourFormat()
    time3.display12HourFormat()




    println("\n\ntask_2")

    val str1 = UniqueString(charArrayOf(' ', ' ', 'H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'))
    val str2 = UniqueString("  Hello world")

    println(str1.getCharAt(2))
    println(str2.getCharAt(2))

    println(str1.length())
    println(str2.length())

    str1.print()
    str2.print()

    println(str1.contains(charArrayOf('w', 'o', 'r', 'l', 'd')))
    println(str2.contains("world"))

    val str1clean = str1.trimStart()
    val str2clean = str2.trimStart()

    str1clean.reverse().print()
    str2clean.reverse().print()




    println("\n\ntask_bank")

    val atm = Atm()

    try {
        val account1 = atm.createAccount("1234567890", "Иван Иванов", 1000.0)
        val account2 = atm.createAccount("0987654321", "Петр Петров")

        println("1. Информация о счетах:")
        println(atm.getAccountInfo("1234567890"))
        println("\n" + atm.getAccountInfo("0987654321"))

        println("\n2. Пополнение счета:")
        atm.depositToAccount("0987654321", 500.75)
        println("После пополнения 500.75 руб:")
        println(atm.getAccountInfo("0987654321"))

        println("\n3. Снятие средств:")
        val success1 = atm.withdrawFromAccount("1234567890", 300.50)
        println("Снятие 300.50 руб со счета 1234567890: ${if (success1) "Успешно" else "Недостаточно средств"}")

        val success2 = atm.withdrawFromAccount("1234567890", 2000.0)
        println("Снятие 2000 руб со счета 1234567890: ${if (success2) "Успешно" else "Недостаточно средств"}")

        println("\n4. Информация после операций:")
        println(atm.getAccountInfo("1234567890"))

        println("\n5. Все счета в банкомате:")
        println(atm.getAllAccountsInfo())

    } catch (e: Exception) {
        println("Произошла ошибка: ${e.message}")
    }
}