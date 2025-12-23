import java.util.UUID


abstract class BankCard(val cardNumber: String, var pinCode: Int) {
    abstract fun getBalance(): Double
    abstract fun updateBalance(amount: Double)
}


class CreditCard(cardNumber: String, pinCode: Int, val creditLimit: Double) : BankCard(cardNumber, pinCode) {
    private var debt: Double = 0.0

    override fun getBalance(): Double {
        return creditLimit - debt // Баланс = кредитный лимит - долг
    }

    override fun updateBalance(amount: Double) {
        debt -= amount // При пополнении карты долг уменьшается
    }

    // Функционал метода такой же, как и у получения баланса
    /*fun getAvailableCredit(): Double { // Удален open, так как класс никем не наследуется и метод не переопределяется
        return creditLimit - debt
    }*/
}


class DebitCard(cardNumber: String, pinCode: Int) : BankCard(cardNumber, pinCode) {
    private var balance: Double = 0.0

    override fun getBalance(): Double {
        return balance
    }

    override fun updateBalance(amount: Double) {
        balance += amount // Увеличиваем\уменьшаем баланс, а не заменяем его
    }


    data class AdditionalInfo(val ownerName: String) // Не имеет смысл использовать data class с одним свойством
    // лучше просто добавить свойство ownerName в класс BankCard
}


enum class TransactionType {
    WITHDRAWAL,
    DEPOSIT // лишняя ;

    // Функция не имеет смысла внутри класса
    /*fun fromString(type: String): TransactionType {
        return valueOf(type.uppercase())
    }*/
}


data class Transaction(
    val cardNumber: String,
    val amount: Double,
    val date: String,
    val type: TransactionType
) {
    val transactionId: String = UUID.randomUUID().toString() // Генерация уникальных id
}


class ATM {

    private val transactions: MutableList<Transaction> = mutableListOf() // Удален метод и добавлена инициализация

    fun makeTransaction(card: BankCard, amount: Double, date: String, type: TransactionType): Boolean {

        when (type) {
            TransactionType.WITHDRAWAL -> {
                if (card.getBalance() >= amount) {
                    card.updateBalance(-amount)
                    transactions.add(Transaction(card.cardNumber, amount, date, type))
                    return true
                }
            }
            TransactionType.DEPOSIT -> {
                card.updateBalance(amount)
                transactions.add(Transaction(card.cardNumber, amount, date, type))
                return true
            }

        }
        return false
    }

    fun printTransactions(cardNumber: String) {

        val cardTransactions = transactions.filter { it.cardNumber == cardNumber }
        println("Транзакции по карте $cardNumber:")
        for (transaction in cardTransactions) {

            println("${transaction.date}: ${transaction.type} ${transaction.amount}")
        }
    }


    fun getAllTransactions(): List<Transaction> { // Метод возвращает неизменяемый список
        return transactions.toList()
    }
}


fun main() {
    val atm = ATM()

    val creditCard = CreditCard("1234-5678-9012-3456", 1234, 10000.0)
    val debitCard = DebitCard("9876-5432-1098-7654", 5678)

    debitCard.updateBalance(5000.0)

    atm.makeTransaction(creditCard, 2000.0, "2025-01-15", TransactionType.WITHDRAWAL)
    atm.makeTransaction(debitCard, 1000.0, "2025-01-15", TransactionType.DEPOSIT) // Передаем тип транзакции, а не строку с названием

    println("Баланс кредитной карты: ${creditCard.getBalance()}")
    println("Баланс дебетовой карты: ${debitCard.getBalance()}")

    atm.printTransactions("1234-5678-9012-3456")
}