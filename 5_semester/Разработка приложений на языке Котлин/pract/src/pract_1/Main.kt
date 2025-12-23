package pract_1

import java.util.Scanner
import kotlin.text.iterator

fun main(){
    //#1
    println("task 1")

    val str = readln()
    var ATGC = Array(4, {0})

    for (x in str) {
        when(x){
            'A' -> ATGC[0]++
            'T' -> ATGC[1]++
            'G' -> ATGC[2]++
            'C' -> ATGC[3]++
        }
    }

    for (i in ATGC){
        print(" $i")
    }


    //#2
    println("\n\ntask 2")

    var count = Array(4, {0})
    val scan = Scanner(System.`in`)
    var x = scan.nextInt()

    count[0] = x / 8
    x %= 8
    count[1] = x / 4
    x %= 4
    count[2] = x / 2
    count[3] = x % 2

    for (i in count){
        print(" $i")
    }
}