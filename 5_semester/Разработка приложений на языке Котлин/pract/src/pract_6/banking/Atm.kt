package pract_6.banking

class Atm {
    private val accounts = mutableListOf<BankAccount>()


    fun createAccount(accountNumber: String, ownerName: String, initialBalance: Double = 0.0) {
        val account = BankAccount(accountNumber, initialBalance, ownerName)
        accounts.add(account)
    }


    fun findAccount(accountNumber: String): BankAccount? {
        return accounts.find { it.accountNumber == accountNumber }
    }


    fun depositToAccount(accountNumber: String, amount: Double): Boolean {
        val account = findAccount(accountNumber)
        return if (account != null) {
            try {
                account.deposit(amount)
                true
            } catch (e: IllegalArgumentException) {
                false
            }
        } else {
            false
        }
    }


    fun withdrawFromAccount(accountNumber: String, amount: Double): Boolean {
        val account = findAccount(accountNumber)
        return account?.withdraw(amount) ?: false
    }


    fun getAccountInfo(accountNumber: String): String? {
        val account = findAccount(accountNumber)
        return account?.getAccountInfo()
    }


    fun getAllAccountsInfo(): String {
        if (accounts.isEmpty()) {
            return "Нет зарегистрированных счетов"
        }
        return accounts.joinToString("\n\n") { it.getAccountInfo() }
    }
}