package pract_2

import java.util.Scanner

fun main(){
    val scan = Scanner(System.`in`)

    //#1
    println("task #1")

    val N = scan.nextInt()
    val numbers = DoubleArray(N)

    for (i in 0..N-1) {
        numbers[i] = scan.nextDouble()
    }

    val average = numbers.average()
    print(average)


    //#2
    println("\n\ntask #2")

    val n = scan.nextInt()
    val arr = IntArray(n)

    for (i in 0..n-1) {
        arr[i] = scan.nextInt()
    }

    var i = 0
    while (i < n){
        val current = arr[i]
        var count = 0

        while (i < n && arr[i] == current){
            count++
            i++
        }

        println("$count $current")
    }

    //#3
    println("\n\ntask #3")

    val Nn = scan.nextInt()
    var strings = Array(Nn) { readLine() }

    for (i in 0..Nn - 1) {
        for (j in i + 1..Nn-1) {
            if (strings[i] == strings[j]) {
                println(strings[i])
                return
            }
        }
    }
}