package pract_4

fun topKFrequent(words: Array<String>, k: Int): List<String> {
    val frequency = mutableMapOf<String, Int>()
    for (word in words) {
        val currentCount = frequency[word] ?: 0
        frequency[word] = currentCount + 1
    }

    val wordFreqList = frequency.toList()

    val sorted = wordFreqList.sortedWith { a, b ->
        if (a.second == b.second) {
            b.first.compareTo(a.first)
        } else {
            b.second.compareTo(a.second)
        }
    }

    val result = mutableListOf<String>()
    for (i in 0 .. k) {
        if (i < sorted.size) {
            result.add(sorted[i].first)
        }
    }
    return result
}

fun main() {
    val words = arrayOf("the","day","is","sunny","the","the","the","sunny","is","is","day")
    println(topKFrequent(words, 4)) // [the, is, day, sunny]
}