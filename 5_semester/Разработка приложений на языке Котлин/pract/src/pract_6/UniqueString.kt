package pract_6

class UniqueString {
    private var charArray: CharArray


    constructor(chars: CharArray) {
        this.charArray = chars.copyOf()
    }


    constructor(str: String) {
        this.charArray = str.toCharArray()
    }


    fun getCharAt(index: Int): Char {
        if (index < 0 || index >= charArray.size) {
            throw IndexOutOfBoundsException("Индекс $index выходит за границы строки (0..${charArray.size - 1})")
        }
        return charArray[index]
    }


    fun length(): Int {
        return charArray.size
    }


    fun print() {
        println(String(charArray))
    }


    fun contains(substring: CharArray): Boolean {
        if (substring.isEmpty()) return true
        if (substring.size > charArray.size) return false
        for (i in 0..charArray.size - substring.size) {
            var found = true
            for (j in 0..substring.size - 1) {
                if (charArray[i + j] != substring[j]) {
                    found = false
                    break
                }
            }
            if (found) return true
        }
        return false
    }


    fun contains(substring: String): Boolean {
        return contains(substring.toCharArray())
    }


    fun trimStart(): UniqueString {
        var startIndex = 0
        while (startIndex < charArray.size && charArray[startIndex] == ' ') {
            startIndex++
        }
        return if (startIndex == 0) {
            this
        } else {
            UniqueString(charArray.copyOfRange(startIndex, charArray.size))
        }
    }


    fun reverse(): UniqueString {
        val reversed = CharArray(charArray.size)
        for (i in 0..charArray.size - 1) {
            reversed[i] = charArray[charArray.size - 1 - i]
        }
        return UniqueString(reversed)
    }
}