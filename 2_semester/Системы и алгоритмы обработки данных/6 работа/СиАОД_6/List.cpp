#include "List.h"
#include <iostream>
#include <string>

using namespace std;

List::List() {
    first = nullptr;
    last = nullptr;
    count = 0;
}

void List::push_behind() {
    Node* ticket = new Node;
    ticket->prev = nullptr;
    cin >> ticket->bilet >> ticket->station >> ticket->train >> ticket->cart >> ticket->seat 
        >> ticket->cost >> ticket->date_sale >> ticket->date_leave >> ticket->time;
    ticket->next = first;
    if (first != nullptr)
        first->prev = ticket;
    if (count == 0) {
        first = ticket;
        last = ticket;
    }
    else
        first = ticket;
    count++;
}

void List::push_behind_node(Node* ticket) {
    ticket->next = first;
    if (first != nullptr)
        first->prev = ticket;
    if (count == 0) {
        first = ticket;
        last = ticket;
    }
    else
        first = ticket;
    count++;
}

void List::push_back() {
    Node* ticket = new Node;
    ticket->next = nullptr;
    cin >> ticket->bilet >> ticket->station >> ticket->train >> ticket->cart >> ticket->seat 
        >> ticket->cost >> ticket->date_sale >> ticket->date_leave >> ticket->time;
    ticket->prev = last;
    if (last != nullptr)
        last->next = ticket;
    if (count == 0) {
        first = ticket;
        last = ticket;
    }
    else
        last = ticket;
    count++;
}

void List::push_back_node(Node* ticket) {
    ticket->prev = last;
    if (last != nullptr)
        last->next = ticket;
    if (count == 0) {
        first = ticket;
        last = ticket;
    }
    else
        last = ticket;
    count++;
}

void List::add(int pos) {
    if (pos == 0) {
        cout << "Input position ";
        cin >> pos;
    }
    if (pos<1 || pos> count + 1) {
        cout << "Incorrect position!";
        return;
    }
    if (pos == count + 1) {
        push_back();
        return;
    }
    else if (pos == 1) {
        push_behind();
        return;
    }
    int i = 1;
    Node* p = first;
    while (i < pos) {
        p = p->next;
        i++;
    }
    Node* prev = p->prev;
    Node* ticket = new Node;

    cin >> ticket->bilet >> ticket->station >> ticket->train >> ticket->cart >> ticket->seat 
        >> ticket->cost >> ticket->date_sale >> ticket->date_leave >> ticket->time;

    if (prev != 0 && count != 1)
        prev->next = ticket;
    ticket->next = p;
    ticket->prev = prev;
    p->prev = ticket;

    count++;
}

void List::add_node(Node* ticket, int pos) {
    if (pos == count + 1) {
        push_back_node(ticket);
        return;
    }
    else if (pos == 1) {
        push_behind_node(ticket);
        return;
    }
    int i = 1;
    Node* p = first;
    while (i < pos) {
        p = p->next;
        i++;
    }
    Node* prev = p->prev;

    if (prev != 0 && count != 1)
        prev->next = ticket;
    ticket->next = p;
    ticket->prev = prev;
    p->prev = ticket;

    count++;
}

void List::del(int pos) {
    if (pos == 0) {
        cout << "Input position ";
        cin >> pos;
    }
    if (pos<1 || pos> count + 1) {
        cout << "Incorrect position!";
        return;
    }
    int i = 1;
    Node* p = first;
    while (i < pos) {
        p = p->next;
        i++;
    }
    Node* prev = p->prev;
    Node* next = p->next;
    if (prev != nullptr && count != 1)
        prev->next = next;
    if (next != nullptr && count != 1)
        next->prev = prev;
    if (pos == 1)
        first = next;
    if (pos == count)
        last = prev;
    delete p;
    count--;
}

void List::print() {
    Node* ticket = first;
    while (ticket) {
        cout << ticket->bilet << " " << ticket->station << " " << ticket->train 
            << " " << ticket->cart << " " << ticket->seat << " " << ticket->cost 
            << " " << ticket->date_sale << " " << ticket->date_leave << " " << ticket->time << endl;
        ticket = ticket->next;
    }
    cout << endl;
}

void List::printback() {
    Node* ticket = last;
    while (ticket) {
        cout << ticket->bilet << " " << ticket->station << " " << ticket->train << " " 
            << ticket->cart << " " << ticket->seat << " " << ticket->cost << " " 
            << ticket->date_sale << " " << ticket->date_leave << " " << ticket->time << endl;
        ticket = ticket->prev;
    }
    cout << endl;
}

void List::cartsorted() {
    Node* ticket = new Node;
    cin >> ticket->bilet >> ticket->station >> ticket->train >> ticket->cart >> ticket->seat 
        >> ticket->cost >> ticket->date_sale >> ticket->date_leave >> ticket->time;
    if (count == 0) {
        push_back_node(ticket);
        return;
    }
    if (ticket->cart > last->cart) {
        push_back_node(ticket);
        return;
    }
    if (ticket->cart <= first->cart) {
        push_behind_node(ticket);
        return;
    }
    Node* q = first;
    int Count = 1;
    while (q->next && ticket->cart > q->cart) {
        Count += 1;
        q = q->next;
    }
    add_node(ticket, Count);
    return;
}

void List::del_reach(string date) {
    int day1 = (date[0] - 48) * 10 + date[1] - 48;
    int mon1 = (date[3] - 48) * 10 + date[4] - 48;
    int year1 = (date[6] - 48) * 1000 + (date[7] - 48) * 100 + (date[8] - 48) * 10 + (date[9] - 48);
    int now = year1 * 365 + mon1 * 30 + day1;
    Node* q = first;
    int Count = 1;
    while (q->next) {
        int day = (q->date_leave[0] - 48) * 10 + q->date_leave[1] - 48;
        int mon = (q->date_leave[3] - 48) * 10 + q->date_leave[4] - 48;
        int year = (q->date_leave[6] - 48) * 1000 + (q->date_leave[7] - 48) * 100
            + (q->date_leave[8] - 48) * 10 + (q->date_leave[9] - 48);
        int leave = year * 365 + mon * 30 + day;
        if (leave < now) {
            Node* nextNode = q->next;
            del(Count);
            q = nextNode;
        }
        else {
            q = q->next;
            Count++;
        }
    }
    int day = (q->date_leave[0] - 48) * 10 + q->date_leave[1] - 48;
    int mon = (q->date_leave[3] - 48) * 10 + q->date_leave[4] - 48;
    int year = (q->date_leave[6] - 48) * 1000 + (q->date_leave[7] - 48) * 100
        + (q->date_leave[8] - 48) * 10 + (q->date_leave[9] - 48);
    int leave = year * 365 + mon * 30 + day;
    if (leave < now)
        del(Count);
}

List List::list_date(string date) {
    List ans;
    Node* q = first;
    while (q) {
        if (q->date_leave == date) {
            ans.push_back_node(clone_single(q));
        }
        q = q->next;
    }
    return ans;
}

Node* List::clone_single(Node* t)
{
    Node* temp = new Node();
    temp->bilet = t->bilet;
    temp->cart = t->cart;
    temp->cost = t->cost;
    temp->date_leave = t->date_leave;
    temp->date_sale = t->date_sale;
    temp->seat = t->seat;
    temp->station = t->station;
    temp->time = t->time;
    temp->train = t->train;

    temp->next = nullptr;
    temp->prev = nullptr;

    return temp;
}