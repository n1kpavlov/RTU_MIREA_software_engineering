package pract_6.banking

class BankAccount(
    val accountNumber: String,
    initialBalance: Double,
    ownerName: String
) {
    var balance: Double
        get() = Math.round(field * 100.0) / 100.0
    var ownerName: String = ""
        set(value) {
            if (value.length < 2) {
                throw IllegalArgumentException("Имя владельца должно содержать не менее 2 символов")
            }
            field = value
        }
    private var transactionCount: Int = 0


    constructor(accountNumber: String, ownerName: String) : this(accountNumber, 0.0, ownerName)


    init {
        if (initialBalance < 0) {
            throw IllegalArgumentException("Начальный баланс не может быть отрицательным")
        }
        this.balance = initialBalance
        this.ownerName = ownerName
    }


    fun deposit(amount: Double) {
        if (amount <= 0) {
            throw IllegalArgumentException("Сумма пополнения должна быть положительной")
        }
        balance += amount
        logTransaction()
    }


    fun withdraw(amount: Double): Boolean {
        if (amount <= 0) {
            throw IllegalArgumentException("Сумма снятия должна быть положительной")
        }
        if (balance >= amount) {
            balance -= amount
            logTransaction()
            return true
        }
        return false
    }


    fun getAccountInfo(): String {
        return "Счет: $accountNumber\n" +
                "Владелец: $ownerName\n" +
                "Баланс: ${"%.2f".format(balance)} руб.\n" +
                "Количество операций: $transactionCount"
    }


    private fun logTransaction() {
        transactionCount++
    }
}