package pract_3

import java.util.Scanner
import kotlin.random.Random
import kotlin.text.iterator

val scan = Scanner(System.`in`)

fun game() {
    val number = Random.nextInt(0, 1001)
    println(number)
    println("Я загадал число от 0 до 1000. Вам нужно угадать его")
    var choice = scan.nextInt()

    while (choice >= 0) {
        if (choice == number) {
            println("Победа!")
            break
        }
        else if (choice < number) {
            println("Это число меньше загаданного")
            choice = scan.nextInt()
        }
        else {
            println("Это число больше загаданного")
            choice = scan.nextInt()
        }
    }
}


fun code_Morse(str: String): String {
    val new_str = StringBuilder()
    for (symbol in str) {
        when (symbol) {
            'А' -> new_str.append(".-")
            'Б' -> new_str.append("-...")
            'В' -> new_str.append(".--")
            'Г' -> new_str.append("--.")
            'Д' -> new_str.append("-..")
            'Е' -> new_str.append(".")
            'Ж' -> new_str.append("...-")
            'З' -> new_str.append("--..")
            'И' -> new_str.append("..")
            'Й' -> new_str.append(".---")
            'К' -> new_str.append("-.-")
            'Л' -> new_str.append(".-..")
            'М' -> new_str.append("--")
            'Н' -> new_str.append("-.")
            'О' -> new_str.append("---")
            'П' -> new_str.append(".--.")
            'Р' -> new_str.append(".-.")
            'С' -> new_str.append("...")
            'Т' -> new_str.append("-")
            'У' -> new_str.append("..-")
            'Ф' -> new_str.append("..-.")
            'Х' -> new_str.append("....")
            'Ц' -> new_str.append("-.-.")
            'Ч' -> new_str.append("---.")
            'Ш' -> new_str.append("----")
            'Щ' -> new_str.append("--.-")
            'Ъ' -> new_str.append("--.--")
            'Ы' -> new_str.append("-.--")
            'Ь' -> new_str.append("-..-")
            'Э' -> new_str.append("..-..")
            'Ю' -> new_str.append("..--")
            'Я' -> new_str.append(".-.-")
        }
        new_str.append(" ")
    }
    return new_str.toString().trim()
}


fun create_password() {
    print("\n\nВведите длину пароля (от 8 символов): ")
    var len = scan.nextInt()

    while (len < 8) {
        println("Пароль с $len количеством символов небезопасен")
        print("Введите длину пароля (от 8 символов): ")
        len = scan.nextInt()
    }

    print("Сгенерированный пароль: ")
    println(generate_password(len))
}


fun generate_password(len: Int): String {
    val uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    val lowercase = "abcdefghijklmnopqrstuvwxyz"
    val digits = "0123456789"
    val special = "!@#$%^&*()-_=+[]{}|;:,.<>?/"
    val allChars = uppercase + lowercase + digits + special

    val password = StringBuilder()

    password.append(uppercase[Random.nextInt(uppercase.length)])
    password.append(lowercase[Random.nextInt(lowercase.length)])
    password.append(digits[Random.nextInt(digits.length)])
    password.append(special[Random.nextInt(special.length)])

    for (i in 1..len - 4) {
        password.append(allChars[Random.nextInt(allChars.length)])
    }

    return password.toList().shuffled().joinToString("")
}


fun main() {
    game()

    println("\n\nВведите строку русских букв:")
    val str = readln()
    println(code_Morse(str))

    create_password()
}